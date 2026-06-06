# ============================================================
# styles.py
# ============================================================

def load_styles():
    return """
<style>

/* ── FONDO GENERAL DE LA APP ── */
.stApp {
    background-color: #FAFBFC;
}

/* ── ESPACIADO SUPERIOR DEL CONTENIDO PRINCIPAL ── */
.main .block-container {
    padding-top: 1rem;
}

/* ══════════════════════════════════════════════
   HEADER PRINCIPAL
   Franja de gradiente con título, subtítulo
   y nombres de los integrantes
══════════════════════════════════════════════ */
.main-header {
    background: linear-gradient(
        90deg,
        #4A90E2,
        #5BC0BE,
        #B8A1E3
    );
    padding: 0.9rem 1.4rem;
    border-radius: 18px;
    margin-bottom: 20px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
}

/* Título del header */
.main-title {
    color: white;
    font-size: 34px;
    font-weight: 800;
    margin-bottom: 0px;
}

/* Subtítulo del header */
.main-subtitle {
    color: white;
    font-size: 15px;
    margin-top: 5px;
}

/* Nombres de integrantes y periodo */
.authors {
    color: rgba(255,255,255,0.95);
    font-size: 14px;
    margin-top: 10px;
}

/* ══════════════════════════════════════════════
   TARJETAS DE RESUMEN GENERAL
   Las 4 tarjetas debajo del header
   (Usuarios, Países, Plataformas, Grupos etarios)
══════════════════════════════════════════════ */
.summary-card {
    background-color: white;
    padding: 12px;
    min-height: 130px;
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    border-top: 5px solid #4A90E2;
    text-align: center;
}

/* Título de la tarjeta de resumen */
.summary-card h3 {
    font-size: 20px;
    margin-bottom: 8px;
    font-weight: 600;
    color: #333333;
    margin-top: 5px;
}

/* Valor de la tarjeta de resumen */
.summary-card h2 {
    font-size: 32px;
    font-weight: 700;
    color: #4A90E2;
    margin: 5px 0;
}

/* ══════════════════════════════════════════════
   TARJETAS KPI
   Las 4 tarjetas de indicadores dentro de cada tab
   (Ansiedad, Depresión, Estrés, etc.)
══════════════════════════════════════════════ */
.kpi-card {
    background: linear-gradient(135deg, #F3F8FF, #EAF3FF);
    border: 1px solid #D7E7FA;
    border-radius: 12px;
    padding: 10px;
    text-align: center;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    height: 90px;
}

/* Título del KPI */
.kpi-title {
    font-size: 14px;
    color: #666;
    font-weight: 600;
}

/* Valor del KPI */
.kpi-value {
    font-size: 28px;
    font-weight: 700;
    color: #4A90E2;
    margin-top: 4px;
}

/* ══════════════════════════════════════════════
   TABS
   Pestañas de navegación entre secciones
   (Salud Mental, Uso Digital, Dopamina, Sueño)
══════════════════════════════════════════════ */

/* Espaciado entre tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
}

/* Tab inactivo */
.stTabs [data-baseweb="tab"] {
    background-color: #F0F5FF;
    border: 1px solid #D6E4FF;
    border-radius: 10px 10px 0px 0px;
    padding: 10px 20px;
    font-weight: 600;
    color: #4A4A4A;
    height: 50px;
}

/* Tab activo (seleccionado) */
.stTabs [aria-selected="true"] {
    background-color: #4A90E2 !important;
    color: white !important;
    border-color: #4A90E2 !important;
}

/* ══════════════════════════════════════════════
   SIDEBAR — PANEL DE FILTROS
   Panel lateral izquierdo con los filtros globales
══════════════════════════════════════════════ */

/* Fondo del sidebar */
[data-testid="stSidebar"] {
    background-color: #125FAB;
}

/* Todo el texto dentro del sidebar en blanco */
[data-testid="stSidebar"] * {
    color: white !important;
}

/* Etiquetas del slider y multiselect */
[data-testid="stSidebar"] .stSlider label,
[data-testid="stSidebar"] .stMultiSelect label {
    color: white !important;
}

/* Caja de info del sidebar
   (st.sidebar.info - mensaje sobre los filtros) */
[data-testid="stSidebar"] [data-testid="stNotification"] {
    background-color: #3A0603;
    border: 1px solid white;
    color: white !important;
}

[data-testid="stSidebar"] [data-testid="stNotification"] p {
    color: white !important;
}

</style>
"""