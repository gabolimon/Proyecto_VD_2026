# ============================================================
# tabs/tab_salud_mental.py
# ============================================================

import streamlit as st
import pandas as pd
import plotly.express as px

def render(mh_f):

    st.subheader("Salud Mental")

    if mh_f.empty:
        st.warning("No hay datos para los filtros seleccionados.")
        return

    # --------------------------------------------------------
    # KPIs
    # --------------------------------------------------------
    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Ansiedad </div>
            <div class="kpi-value">{mh_f['puntaje_ansiedad'].mean():.1f}</div>
        </div>
        """, unsafe_allow_html=True)

    with k2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Depresión</div>
            <div class="kpi-value">{mh_f['puntaje_depresion'].mean():.1f}</div>
        </div>
        """, unsafe_allow_html=True)

    with k3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Estrés</div>
            <div class="kpi-value">{mh_f['nivel_estres'].mean():.1f}</div>
        </div>
        """, unsafe_allow_html=True)

    with k4:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Soledad</div>
            <div class="kpi-value">{mh_f['indice_soledad'].mean():.1f}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

# --------------------------------------------------------
    # TABLA DE DATOS
    # --------------------------------------------------------
    st.subheader("Tabla de datos")
    if st.checkbox("Mostrar datos", key="tabla_salud_mental"):
        data_load_state = st.text("Cargando datos...")
        data_load_state.success("Datos cargados correctamente")
        st.dataframe(mh_f, use_container_width=True)

    st.markdown("---")


    # --------------------------------------------------------
    # GRÁFICAS
    # --------------------------------------------------------
    col1, col2 = st.columns(2)

    with col1:
        # Dropdown para seleccionar plataforma
        plataforma_seleccionada = st.selectbox(
            "Selecciona una plataforma",
            options=sorted(mh_f["plataforma"].unique()),
            key="dropdown_plataforma_salud"
        )

        df_plataforma = mh_f[mh_f["plataforma"] == plataforma_seleccionada]

        indicadores_plat = pd.DataFrame({
            "Indicador": ["Ansiedad", "Depresión", "Estrés", "Soledad"],
            "Promedio": [
                df_plataforma["puntaje_ansiedad"].mean(),
                df_plataforma["puntaje_depresion"].mean(),
                df_plataforma["nivel_estres"].mean(),
                df_plataforma["indice_soledad"].mean()
            ]
        })

        fig = px.bar(
            indicadores_plat,
            x="Indicador",
            y="Promedio",
            color="Indicador",
            title=f"Indicadores psicológicos — {plataforma_seleccionada}",
            labels={
                "Indicador": "Indicador",
                "Promedio" : "Promedio"
            },
            color_discrete_map={
                "Ansiedad" : "#1E3A8A",
                "Depresión": "#65A30D",
                "Estrés"   : "#9333EA",
                "Soledad"  : "#707070"
            }
        )

        fig.update_layout(
            showlegend=False,
            yaxis_range=[0, 100]
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Dropdown para seleccionar indicador
        indicador_seleccionado = st.selectbox(
            "Selecciona un indicador",
            options=[
                "puntaje_ansiedad",
                "puntaje_depresion",
                "nivel_estres",
                "indice_soledad"
            ],
            format_func=lambda x: {
                "puntaje_ansiedad" : "Ansiedad",
                "puntaje_depresion": "Depresión",
                "nivel_estres"     : "Estrés",
                "indice_soledad"   : "Soledad"
            }[x],
            key="dropdown_indicador_salud"
        )

        plat_indicador = (
            mh_f
            .groupby("plataforma")[indicador_seleccionado]
            .mean()
            .round(2)
            .reset_index()
            .sort_values(indicador_seleccionado, ascending=False)
        )

        plat_indicador.columns = ["plataforma", "promedio"]

        fig = px.bar(
            plat_indicador,
            x="plataforma",
            y="promedio",
            color="plataforma",
            title=f"{indicador_seleccionado.replace('_', ' ').title()} promedio por plataforma",
            labels={
                "plataforma": "Plataforma",
                "promedio"  : "Promedio"
            },
            color_discrete_sequence=[
                "#4F8EF7",  # Azul
                "#5AA9E6",  # Azul claro
                "#5EC2B7",  # Turquesa
                "#6BCB8B",  # Verde menta
                "#8CCF9B",  # Verde suave
                "#A3BFFA",  # Azul lavanda
                "#B39DDB",  # Lila
                "#9B7EDE",  # Morado suave
                "#7E57C2",  # Morado
                "#5E60CE"   
            ]
        )

        fig.update_layout(
            showlegend=False,
            xaxis_tickangle=-45
        )

        st.plotly_chart(fig, use_container_width=True)

    # --------------------------------------------------------
    # Dispersión — Bienestar Digital vs Brecha Autoestima-Ansiedad
    # --------------------------------------------------------
    st.markdown("---")

    fig_dispersion = px.scatter(
        mh_f,
        x="indice_bienestar_digital",
        y="brecha_autoestima_ansiedad",
        color="genero",
        symbol="genero",
        title="Bienestar Digital vs Brecha Autoestima-Ansiedad por Género",
        labels={
            "indice_bienestar_digital"  : "Índice de Bienestar Digital",
            "brecha_autoestima_ansiedad": "Brecha Autoestima-Ansiedad",
            "genero"                    : "Género"
        },
        color_discrete_map={
            "Male"  : "#1A6FBF",
            "Female": "#D63E6C",
            "Other" : "#2CA02C"
        },
        symbol_map={
            "Male"  : "circle",
            "Female": "triangle-up",
            "Other" : "square"
        },
        opacity=0.6
    )

    fig_dispersion.update_layout(
        height=500,
        legend=dict(
            title="Género",
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    fig_dispersion.update_traces(marker=dict(size=6))

    st.plotly_chart(fig_dispersion, use_container_width=True)

    # --------------------------------------------------------
    # Apoyo Clínico por Género y Grupo Etario
    # --------------------------------------------------------
    st.markdown("---")

    apoyo = (
        mh_f
        .groupby(["grupo_edad", "genero"])["apoyo_clinico"]
        .mean()
        .round(2)
        .reset_index()
    )

    apoyo["apoyo_clinico_label"] = apoyo["apoyo_clinico"].map({
        0: "Sin apoyo",
        1: "Apoyo parcial",
        2: "Apoyo completo"
    })

    fig_apoyo = px.bar(
        apoyo,
        x="grupo_edad",
        y="apoyo_clinico",
        color="genero",
        barmode="group",
        title="Nivel de Apoyo Clínico por Grupo Etario y Género",
        labels={
            "grupo_edad"   : "Grupo Etario",
            "apoyo_clinico": "Nivel de Apoyo Clínico (promedio)",
            "genero"       : "Género"
        },
        color_discrete_map={
            "Male"  : "#4A90E2",
            "Female": "#B8A1E3",
            "Other" : "#7FB77E"
        }
    )

    fig_apoyo.update_layout(
        height=450,
        xaxis_title="Grupo Etario",
        yaxis_title="Nivel de Apoyo Clínico (0-2)",
        legend=dict(
            title="Género",
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        yaxis=dict(
            tickvals=[0, 1, 2],
            ticktext=["Sin apoyo", "Apoyo parcial", "Apoyo completo"]
        )
    )

    st.plotly_chart(fig_apoyo, use_container_width=True)