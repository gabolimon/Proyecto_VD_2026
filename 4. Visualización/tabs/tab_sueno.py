# ============================================================
# tabs/tab_sueno.py
# ============================================================

import streamlit as st
import pandas as pd
import plotly.express as px

def render(sl_f):

    st.subheader("Sueño y Fatiga")

    if sl_f.empty:
        st.warning("No hay datos para los filtros seleccionados.")
        return

    # --------------------------------------------------------
    # KPIs
    # --------------------------------------------------------
    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Horas de Sueño</div>
            <div class="kpi-value">{sl_f['promedio_horas_sueno'].mean():.1f}</div>
        </div>
        """, unsafe_allow_html=True)

    with k2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Calidad Sueño</div>
            <div class="kpi-value">{sl_f['puntaje_calidad_sueno'].mean():.1f}</div>
        </div>
        """, unsafe_allow_html=True)

    with k3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Uso Nocturno</div>
            <div class="kpi-value">{sl_f['horas_uso_nocturno'].mean():.1f}</div>
        </div>
        """, unsafe_allow_html=True)

    with k4:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Nivel Fatiga</div>
            <div class="kpi-value">{sl_f['nivel_fatiga'].mean():.1f}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # --------------------------------------------------------
    # TABLA DE DATOS
    # --------------------------------------------------------
    st.subheader("Tabla de datos")
    if st.checkbox("Mostrar datos", key="tabla_sueno"):
        data_load_state = st.text("Cargando datos...")
        data_load_state.success("Datos cargados correctamente")
        st.dataframe(sl_f, use_container_width=True)

    st.markdown("---")

    # --------------------------------------------------------
    # GRÁFICAS
    # --------------------------------------------------------
    col1, col2 = st.columns(2)

    with col1:
        clasificacion = (
            sl_f["clasificacion_sueno"]
            .value_counts()
            .reset_index()
        )
        clasificacion.columns = ["categoria", "cantidad"]

        fig = px.pie(
            clasificacion,
            names="categoria",
            values="cantidad",
            hole=0.55,
            title="Clasificación de la Calidad del Sueño",
            color_discrete_sequence=["#7FB77E", "#B8A1E3", "#4A90E2"]
        )
        fig.update_traces(
            textposition="inside",
            textinfo="percent+label"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fatiga_edad = (
            sl_f
            .groupby("grupo_edad")["nivel_fatiga"]
            .mean()
            .reset_index()
            .sort_values("nivel_fatiga", ascending=False)
        )

        fig = px.bar(
            fatiga_edad,
            x="grupo_edad",
            y="nivel_fatiga",
            color="nivel_fatiga",
            color_continuous_scale=["#B8A1E3", "#5BC0BE", "#4A90E2"],
            title="Nivel Promedio de Fatiga por Grupo Etario"
        )
        fig.update_layout(
            xaxis_title="Grupo Etario",
            yaxis_title="Nivel de Fatiga",
            coloraxis_showscale=False
        )
        st.plotly_chart(fig, use_container_width=True)