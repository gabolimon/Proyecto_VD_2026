# ============================================================
# tabs/tab_uso_digital.py
# ============================================================

import streamlit as st
import pandas as pd
import plotly.express as px

def render(sm_f):

    st.subheader("Uso Digital")

    if sm_f.empty:
        st.warning("No hay datos para los filtros seleccionados.")
        return

    # --------------------------------------------------------
    # KPIs
    # --------------------------------------------------------
    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Horas Pantalla</div>
            <div class="kpi-value">{sm_f['horas_pantalla_diaria'].mean():.1f}</div>
        </div>
        """, unsafe_allow_html=True)

    with k2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Doomscrolling</div>
            <div class="kpi-value">{sm_f['frecuencia_doomscrolling'].mean():.1f}</div>
        </div>
        """, unsafe_allow_html=True)

    with k3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Exposición IA</div>
            <div class="kpi-value">{sm_f['exposicion_recomendacion_ia'].mean():.1f}</div>
        </div>
        """, unsafe_allow_html=True)

    with k4:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Pérdida Productividad</div>
            <div class="kpi-value">{sm_f['pct_perdida_productividad'].mean():.1f}%</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

# --------------------------------------------------------
    # TABLA DE DATOS
    # --------------------------------------------------------
    
    st.subheader("Tabla de datos")
    if st.checkbox("Mostrar datos", key="tabla_uso_digital"):
        data_load_state = st.text("Cargando datos...")
        data_load_state.success("Datos cargados correctamente")
        st.dataframe(sm_f, use_container_width=True)

    st.markdown("---")

    # --------------------------------------------------------
    # GRÁFICAS
    # --------------------------------------------------------
    col1, col2 = st.columns(2)

    with col1:
        horas_edad = (
            sm_f
            .groupby("grupo_edad")["horas_pantalla_diaria"]
            .mean()
            .reset_index()
            .sort_values("horas_pantalla_diaria")
        )

        fig = px.bar(
            horas_edad,
            x="grupo_edad",
            y="horas_pantalla_diaria",
            color="horas_pantalla_diaria",
            color_continuous_scale=["#B8A1E3", "#5BC0BE", "#4A90E2"],
            title="Horas de Pantalla Promedio por Grupo Etario"
        )
        fig.update_layout(
            xaxis_title="Grupo Etario",
            yaxis_title="Horas por Día",
            coloraxis_showscale=False
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        doom_platform = (
            sm_f
            .groupby("plataforma")["frecuencia_doomscrolling"]
            .mean()
            .reset_index()
            .sort_values("frecuencia_doomscrolling", ascending=False)
        )

        fig = px.bar(
            doom_platform,
            x="plataforma",
            y="frecuencia_doomscrolling",
            color="frecuencia_doomscrolling",
            color_continuous_scale=["#7FB77E", "#5BC0BE", "#4A90E2"],
            title="Frecuencia Promedio de Doomscrolling por Plataforma"
        )
        fig.update_layout(
            xaxis_title="Plataforma",
            yaxis_title="Frecuencia Promedio",
            coloraxis_showscale=False
        )
        st.plotly_chart(fig, use_container_width=True)