# ============================================================
# tabs/tab_dopamina.py
# ============================================================

import streamlit as st
import pandas as pd
import plotly.express as px

def render(dp_f):

    st.subheader("Gratificación Inmediata")

    if dp_f.empty:
        st.warning("No hay datos para los filtros seleccionados.")
        return

    # --------------------------------------------------------
    # KPIs
    # --------------------------------------------------------
    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Tasa de Interacción</div>
            <div class="kpi-value">{dp_f['tasa_interaccion'].mean():.1f}</div>
        </div>
        """, unsafe_allow_html=True)

    with k2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Activación Dopamina</div>
            <div class="kpi-value">{dp_f['puntaje_activacion_dopamina'].mean():.1f}</div>
        </div>
        """, unsafe_allow_html=True)

    with k3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Gratificación Inmediata</div>
            <div class="kpi-value">{dp_f['dependencia_gratificacion_inmediata'].mean():.1f}</div>
        </div>
        """, unsafe_allow_html=True)

    with k4:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Videos Cortos</div>
            <div class="kpi-value">{dp_f['horas_consumo_video_corto'].mean():.1f}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # --------------------------------------------------------
    # TABLA DE DATOS
    # --------------------------------------------------------
    st.subheader("Tabla de datos")
    if st.checkbox("Mostrar datos", key="tabla_dopamina"):
        data_load_state = st.text("Cargando datos...")
        data_load_state.success("Datos cargados correctamente")
        st.dataframe(dp_f, use_container_width=True)

    st.markdown("---")

    # --------------------------------------------------------
    # GRÁFICAS
    # --------------------------------------------------------
    col1, col2 = st.columns(2)

    with col1:
        consumo = (
            dp_f["consumo_video_categoria"]
            .value_counts()
            .reset_index()
        )
        consumo.columns = ["categoria", "cantidad"]

        fig = px.pie(
            consumo,
            names="categoria",
            values="cantidad",
            hole=0.55,
            title="Distribución del Consumo de Videos Cortos",
            color_discrete_sequence=["#4A90E2", "#5BC0BE", "#7FB77E", "#B8A1E3"]
        )
        fig.update_traces(
            textposition="inside",
            textinfo="percent+label"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        interaccion = (
            dp_f
            .groupby("plataforma")["tasa_interaccion"]
            .mean()
            .reset_index()
            .sort_values("tasa_interaccion", ascending=False)
        )

        fig = px.bar(
            interaccion,
            x="plataforma",
            y="tasa_interaccion",
            color="tasa_interaccion",
            color_continuous_scale=["#B8A1E3", "#5BC0BE", "#4A90E2"],
            title="Tasa de Interacción Promedio por Plataforma"
        )
        fig.update_layout(
            xaxis_title="Plataforma",
            yaxis_title="Tasa de Interacción",
            coloraxis_showscale=False
        )
        st.plotly_chart(fig, use_container_width=True)