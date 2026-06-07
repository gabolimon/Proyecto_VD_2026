# ============================================================
# app.py — Dashboard principal
# Salud Mental y Redes Sociales (2010–2025)
# ============================================================

import streamlit as st
from data_loader import cargar_datos
from styles import load_styles
from tabs import tab_salud_mental, tab_uso_digital, tab_dopamina, tab_sueno

# ============================================================
# CONFIGURACIÓN
# ============================================================
st.set_page_config(
    page_title="Salud Mental y Redes Sociales",
    layout="wide"
)

# ============================================================
# ESTILOS
# ============================================================
st.markdown(load_styles(), unsafe_allow_html=True)

# ============================================================
# CARGA DE DATOS
# ============================================================
mh, sm, dp, sl = cargar_datos()

# ============================================================
# HEADER
# ============================================================
st.markdown("""
<div class="main-header">
    <div class="main-title">Salud Mental y Redes Sociales</div>
    <div class="main-subtitle">
        Análisis del impacto del uso de redes sociales en la salud mental global
    </div>
    <div class="authors">
        Periodo: 2010–2025
        <br>
        Gabriel Josué Limones Obando &nbsp;&nbsp;|&nbsp;&nbsp;
        María Fernanda Mora García
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================
st.sidebar.markdown("## FILTROS GLOBALES")
st.sidebar.info("Los filtros afectan todas las visualizaciones del dashboard.")

anios = st.sidebar.slider("Rango de años", 2010, 2025, (2010, 2025))

paises = st.sidebar.multiselect(
    "País",
    sorted(mh["pais"].unique()),
    default=[]
)

plataformas = st.sidebar.multiselect(
    "Plataforma",
    sorted(mh["plataforma"].unique()),
    default=[]
)

edades = st.sidebar.multiselect(
    "Grupo etario",
    sorted(mh["grupo_edad"].unique()),
    default=[]
)

generos = st.sidebar.multiselect(
    "Género",
    sorted(mh["genero"].unique()),
    default=[]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
## Objetivo
Explorar la relación entre:
- Salud mental
- Uso digital
- Gratificación inmediata
- Calidad del sueño
""")

# ============================================================
# FILTROS
# ============================================================
def aplicar_filtros(df):
    filtro = df["anio"].between(anios[0], anios[1])
    if paises:
        filtro &= df["pais"].isin(paises)
    if plataformas:
        filtro &= df["plataforma"].isin(plataformas)
    if edades:
        filtro &= df["grupo_edad"].isin(edades)
    if generos:
        filtro &= df["genero"].isin(generos)
    return df[filtro]

mh_f = aplicar_filtros(mh)
sm_f = aplicar_filtros(sm)
dp_f = aplicar_filtros(dp)
sl_f = aplicar_filtros(sl)

# ============================================================
# RESUMEN GENERAL
# ============================================================
st.markdown("""
<h2 style="color:#333333;font-size:28px;font-weight:700;margin-bottom:15px;">
    Resumen General
</h2>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="summary-card">
        <h3>Usuarios</h3>
        <h2>{len(mh_f):,}</h2>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="summary-card">
        <h3>Países</h3>
        <h2>{mh_f['pais'].nunique()}</h2>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="summary-card">
        <h3>Plataformas</h3>
        <h2>{mh_f['plataforma'].nunique()}</h2>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="summary-card">
        <h3>Grupos etarios</h3>
        <h2>{mh_f['grupo_edad'].nunique()}</h2>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ============================================================
# TABS
# ============================================================
tab1 = st.tabs([
    "Salud Mental"
    #"Uso Digital",
    #"Gratificación Inmediata",
    #"Sueño y Fatiga"
])

with tab1:
    tab_salud_mental.render(mh_f)
#
#with tab2:
#    tab_uso_digital.render(sm_f)
#
#with tab3:
#    tab_dopamina.render(dp_f)
#
#with tab4:
#    tab_sueno.render(sl_f)