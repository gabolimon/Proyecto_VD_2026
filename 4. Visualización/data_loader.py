# ============================================================
# data_loader.py
# ============================================================

import pandas as pd
import streamlit as st

@st.cache_data
def cargar_datos():

    # --- MENTAL HEALTH ---
    mh = pd.read_parquet("1. Datasets/2. Dataset Limpio/mental_health_trends.parquet")
    mh = mh[mh['anio'].between(2010, 2025)]
    mh['indice_bienestar_digital'] = (100 - ((mh['puntaje_ansiedad'] + mh['puntaje_depresion'] + mh['nivel_estres']) / 3)).round(2)
    mh['carga_psicologica_total'] = (mh['puntaje_ansiedad'] + mh['puntaje_depresion'] + mh['nivel_estres'] + mh['indice_soledad']).round(2)
    mh['brecha_autoestima_ansiedad'] = (mh['puntaje_autoestima'] - mh['puntaje_ansiedad']).round(2)

    # Atributo derivado — apoyo clínico
    # 0 = sin apoyo, 1 = apoyo parcial, 2 = apoyo completo
    mh['apoyo_clinico'] = (mh['acceso_terapia'].astype(int) + mh['uso_medicacion'].astype(int))

    # --- SOCIAL MEDIA ---
    sm = pd.read_parquet("1. Datasets/2. Dataset Limpio/social_media_usage.parquet")
    sm.drop(columns=['notification_checks_per_day', 'digital_detox_attempts'], errors='ignore', inplace=True)
    sm = sm[sm['anio'].between(2010, 2025)]
    sm['uso_pantalla_categoria'] = pd.cut(
        sm['horas_pantalla_diaria'],
        bins=[0, 3, 6, 9, 15],
        labels=['Bajo', 'Moderado', 'Alto', 'Severo']
    )
    sm['riesgo_orden'] = sm['nivel_riesgo_adiccion'].map({'Low': 1, 'Medium': 2, 'High': 3})

    # --- DOPAMINE ---
    dp = pd.read_parquet("1. Datasets/2. Dataset Limpio/dopamine_trigger_metrics.parquet")
    dp.drop(columns=['content_refresh_frequency'], errors='ignore', inplace=True)
    dp = dp[dp['anio'].between(2010, 2025)]
    dp['indice_adiccion_contenido'] = ((dp['puntaje_activacion_dopamina'] + dp['dependencia_gratificacion_inmediata']) / 2).round(2)
    dp['consumo_video_categoria'] = pd.cut(
        dp['horas_consumo_video_corto'],
        bins=[0, 2, 5, 8, 10],
        labels=['Bajo', 'Moderado', 'Alto', 'Severo'],
        include_lowest=True
    )

    # --- SLEEP ---
    sl = pd.read_parquet("1. Datasets/2. Dataset Limpio/sleep_disruption.parquet")
    sl.drop(columns=['night_notifications'], errors='ignore', inplace=True)
    sl = sl[sl['anio'].between(2010, 2025)]
    sl['clasificacion_sueno'] = pd.cut(
        sl['promedio_horas_sueno'],
        bins=[0, 5, 7, 9, 12],
        labels=['Insuficiente', 'Aceptable', 'Optimo', 'Excesivo'],
        include_lowest=True
    )
    sl['indice_disrupcion_sueno'] = (
        (sl['horas_uso_nocturno'] / 6) * 100 * 0.5 +
        (100 - sl['puntaje_calidad_sueno']) * 0.5
    ).round(2)

    return mh, sm, dp, sl