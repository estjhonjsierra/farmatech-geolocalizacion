import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 1. CONFIGURACIÓN HIGH-DEFINITION DE LA INTERFAZ
st.set_page_config(
    page_title="FarmaTech - Enterprise Suite",
    layout="wide",
    page_icon="🏢"
)

# Inyección de CSS avanzado para simular los bloques exactos de la imagen y controlar los clics
st.markdown("""
    <style>
    .main-title { font-family: 'Helvetica Neue', Arial, sans-serif; color: #1e3d59; font-weight: 800; font-size: 2.4rem; margin-bottom: 0.2rem; }
    .section-desc { color: #6c757d; font-size: 1.05rem; margin-bottom: 1.5rem; }
    
    /* Forzar diseño de botones tipo bloques de organigrama */
    div.stButton > button {
        width: 100%;
        font-family: 'Arial', sans-serif !important;
        font-size: 1.1rem !important;
        font-weight: bold !important;
        padding: 15px !important;
        border-radius: 8px !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    div.stButton > button:hover {
        transform: scale(1.01);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    
    /* Clases de información corporativa */
    .profile-box { padding: 20px; border-radius: 10px; background-color: #f8f9fa; border-left: 6px solid #1e3d59; margin-top: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .profile-title { font-size: 1.3rem; font-weight: bold; color: #1e3d59; margin-bottom: 10px; text-transform: uppercase; }
    .metric-inline { font-weight: bold; color: #2ca02c; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🏢 Componente 2: Estructura Orgánica y Manual de Funciones</h1>', unsafe_allow_html=True)
st.markdown('<p class="section-desc">Tabla 26. Panel de Consulta de Perfiles, Requisitos ReTHUS y Asignaciones Salariales — FarmaTech Ltda.</p>', unsafe_allow_html=True)
st.markdown("---")

# Configuración universal para descarga de reportes (Cámara 📸 activa)
config_exportacion = {
    'displayModeBar': True,
    'toImageButtonOptions': {
        'format': 'png',
        'filename': 'farmatech_kpi_talento_humano',
        'height': 500,
        'width': 1000,
        'scale': 2
    }
}

# Inicializar la variable de control de clics en la sesión
if "cargo_activo" not in st.session_state:
    st.session_state.cargo_activo = "Ninguno"

# 2. CONTROLES DE SIMULACIÓN EN LA BARRA LATERAL (SIDEBAR)
st.sidebar.header("🎛️ Centro de Simulación Cruzada")
st.sidebar.markdown("Modifique las variables operativas en tiempo real para estresar los indicadores de cargo.")
transacciones_dia = st.sidebar.slider("Transacciones Reales Diarias (POS)", min_value=30, max_value=120, value=65, step=5)
horas_capacitacion = st.sidebar.slider("Horas de Capacitación Anual / Empleado", min_value=0, max_value=40, value=20, step=2)

# Valores base de nómina (Tabla 11) y salario mínimo 2026
smmlv_2026 = 1430000

# 3. CONSTRUCCIÓN DE LA ARQUITECTURA DEL ORGANIGRAMA VISUAL
st.subheader("🗺️ Tabla de Mandos y Organigrama")
st.write("Haga clic directamente sobre cualquiera de los bloques de color para desplegar su ficha de perfil y simulación técnica.")

# BLOQUE 1: JUNTA DE SOCIOS (Azul Corporativo Oscuro)
st.markdown("<style>div[key='btn_junta'] > button { background: linear-gradient(135deg, #1e3d59 0%, #102233 100%) !important; }</style>", unsafe_allow_html=True)
if st.button("👥 1. JUNTA DE SOCIOS & ESTRUCTURA DE CAPITAL", key="btn_junta"):
    st.session_state.cargo_activo = "Junta"

st.markdown("<div style='text-align:center; font-size:1.2rem; color:#1e3d59; margin:2px 0;'>▼</div>", unsafe_allow_html=True)

# BLOQUE 2: GERENCIA GENERAL (Azul Rey)
st.markdown("<style>div[key='btn_gerencia'] > button { background: linear-gradient(135deg, #2b5c8f 0%, #1e3d59 100%) !important; }</style>", unsafe_allow_html=True)
if st.button("👔 2. GERENCIA GENERAL (Representación Legal)", key="btn_gerencia"):
    st.session_state.cargo_activo = "Gerencia"

st.markdown("<div style='text-align:center; font-size:1.2rem; color:#1e3d59; margin:2px 0;'>▼</div>", unsafe_allow_html=True)

# NIVEL TÁCTICO: TRES COLUMNAS EN PARALELO (Mismo orden de tu imagen)
col_tact1, col_tact2, col_tact3 = st.columns(3)

with col_tact1:
    st.markdown("<style>div[key='btn_dt'] > button { background: linear-gradient(135deg, #2ca02c 0%, #195219 100%) !important; }</style>", unsafe_allow_html=True)
    if st.button("⚙️ DIRECCIÓN TÉCNICA\n(Regente de Farmacia)", key="btn_dt"):
        st.session_state.cargo_activo = "Direccion_Tecnica"

with col_tact2:
    st.markdown("<style>div[key='btn_dc'] > button { background: linear-gradient(135deg, #e65c00 0%, #993d00 100%) !important; }</style>", unsafe_allow_html=True)
    if st.button("📢 DIRECCIÓN COMERCIAL\n(Órgano Consultor)", key="btn_dc"):
        st.session_state.cargo_activo = "Direccion_Comercial"

with col_tact3:
    st.markdown("<style>div[key='btn_dterr'] > button { background: linear-gradient(135deg, #1f77b4 0%, #114466 100%) !important; }</style>", unsafe_allow_html=True)
    if st.button("🗺️ DIRECCIÓN TERRITORIAL\n(Órgano Consultor)", key="btn_dterr"):
        st.session_state.cargo_activo = "Direccion_Territorial"

st.markdown("<div style='text-align:center; font-size:1.2rem; color:#1e3d59; margin:4px 0;'>▼</div>", unsafe_allow_html=True)

# NIVEL OPERATIVO: TRES AUXILIARES + UN DOMICILIARIO
col_ope1, col_ope2, col_ope3, col_ope4 = st.columns(4)

with col_ope1:
    st.markdown("<style>div[key='btn_aux1'] > button { background: #5a9bd5 !important; }</style>", unsafe_allow_html=True)
    if st.button("📋 AUXILIAR 1\n(Terminal POS 1)", key="btn_aux1"):
        st.session_state.cargo_activo = "Auxiliar1"

with col_ope2:
    st.markdown("<style>div[key='btn_aux2'] > button { background: #5a9bd5 !important; }</style>", unsafe_allow_html=True)
    if st.button("💬 AUXILIAR 2\n(WhatsApp Business)", key="btn_aux2"):
        st.session_state.cargo_activo = "Auxiliar2"

with col_ope3:
    st.markdown("<style>div[key='btn_aux3'] > button { background: #5a9bd5 !important; }</style>", unsafe_allow_html=True)
    if st.button("📦 AUXILIAR 3\n(Bodega / FEFO)", key="btn_aux3"):
        st.session_state.cargo_activo = "Auxiliar3"

with col_ope4:
    st.markdown("<style>div[key='btn_dom'] > button { background: linear-gradient(135deg, #ffc000 0%, #b38600 100%) !important; color:black !important; }</style>", unsafe_allow_html=True)
    if st.button("🏍️ MENSAJERO\n(Última Milla)", key="btn_dom"):
        st.session_state.cargo_activo = "Mensajero"

st.markdown("---")

# =============================================================================
# DETECCIÓN DE EVENTOS Y DESPLIEGUE DE FICHA DE CARGO E IMPACTO
# =============================================================================
st.subheader("🔍 Ficha de Perfil Técnico y Análisis de Desempeño")

if st.session_state.cargo_activo == "Ninguno":
    st.info("💡 **Sistema Activo:** Haga clic sobre cualquier bloque del organigrama superior para abrir su manual de funciones y simular sus métricas.")

elif st.session_state.cargo_activo == "Junta":
    st.markdown('<div class="profile-box">', unsafe_allow_html=True)
    st.markdown('<div class="profile-title">👥 Junta de Socios — Composición del Capital Social</div>', unsafe_allow_html=True)
    st.write("**Estructura Jurídica:** Sociedad de Responsabilidad Limitada (Ltda.) - Artículo 353 del Código de Comercio.")
    st.write("**Distribución del Capital (\$280.000.000 COP):**")
    st.markdown("- **Fondo Emprender SENA:** 40% (\$112.000.000 COP) • Inversionista Institucional")
    st.markdown("- **Inversionista Ángel (IPS Local):** 25% (\$70.000.000 COP) • Aliado de Red de Pacientes")
    st.markdown("- **Jhon Jaime Sierra:** 20% (\$56.000.000 COP) • Área Financiera/Tecnológica")
    st.markdown("- **Lucy Semanate:** 10% (\$28.000.000 COP) • Operación de Territorio")
    st.markdown("- **Danna Delgado (2,5%) & Mauricio Echeverry (2,5%):** (\$14.000.000 COP) • Estrategia Comercial y Legal")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.cargo_activo == "Gerencia":
    st.markdown('<div class="profile-box">', unsafe_allow_html=True)
    st.markdown('<div class="profile-title">👔 Gerencia General — Jhon Jaime Sierra Marín</div>', unsafe_allow_html=True)
    st.write("**Misión:** Ejercer la representación legal, salvaguardar el cumplimiento de indicadores ante el SENA y liderar la estrategia de expansión corporativa.")
    st.write("**Funciones:** Firmar contratos mayoristas, auditar estados financieros y evaluar el ROI al cierre del Año 3.")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.cargo_activo == "Direccion_Tecnica":
    st.markdown('<div class="profile-box">', unsafe_allow_html=True)
    st.markdown('<div class="profile-title">⚙️ Dirección Técnica — Regente de Farmacia (Planta)</div>', unsafe_allow_html=True)
    st.write("**Requisito Legal:** Tecnólogo en Regencia de Farmacia (Ley 485 de 1998), inscrito en el ReTHUS.")
    st.write("**Asignación en OPEX:** `$4.500.000 COP/mes` (Costo unificado con carga prestacional completa).")
    
    cumplimiento_bpa = min(100.0, 75.0 + (horas_capacitacion * 0.65))
    st.markdown(f"📈 **Índice de Conformidad Sanitaria (BPA):** <span class='metric-inline'>{cumplimiento_bpa:.1f}%</span> (Meta Seccional de Salud: 100%)", unsafe_allow_html=True)
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number", value = cumplimiento_bpa,
        title = {'text': "Conformidad Estándar Sanitario Seccional de Salud"},
        gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "#2ca02c"}, 'threshold': {'line': {'color': "red", 'width': 4}, 'value': 95}}
    ))
    fig.update_layout(height=220, margin=dict(t=30,b=10,l=10,r=10))
    st.plotly_chart(fig, use_container_width=True, config=config_exportacion)
    st.markdown('</div>', unsafe_allow_html=True)

