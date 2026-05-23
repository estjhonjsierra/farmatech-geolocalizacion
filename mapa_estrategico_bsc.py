import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 1. CONFIGURACIÓN HIGH-DEFINITION DE LA INTERFAZ DE USUARIO (UI)
st.set_page_config(
    page_title="FarmaTech - Balanced Scorecard Central",
    layout="wide",
    page_icon="🎯"
)

# Inyección de estilos CSS avanzados para personalización de botones e interfaz
st.markdown("""
    <style>
    .main-title { font-family: 'Helvetica Neue', Arial, sans-serif; color: #1e3d59; font-weight: 800; font-size: 2.5rem; margin-bottom: 0.2rem; }
    .section-desc { color: #6c757d; font-size: 1.05rem; margin-bottom: 1.5rem; }
    .arrow-q { text-align: center; font-size: 1.8rem; color: #1e3d59; font-weight: bold; margin: 4px 0; }
    
    /* Forzar que los botones de Streamlit simulen las macro-tarjetas */
    div.stButton > button {
        width: 100%;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        padding: 18px !important;
        border-radius: 14px !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: transform 0.2s ease;
    }
    div.stButton > button:hover {
        transform: scale(1.01);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🚀 3.1 Cuadro de Mando Integral — Balanced Scorecard (BSC)</h1>', unsafe_allow_html=True)
st.markdown('<p class="section-desc">Módulo de Visualización de Objetivos Estratégicos y Causalidad Dinámica — FarmaTech Ltda.</p>', unsafe_allow_html=True)
st.markdown("---")

# Configuración universal para descarga de reportes y capturas (Cámara 📸 activa)
config_exportacion = {
    'displayModeBar': True,
    'toImageButtonOptions': {
        'format': 'png',
        'filename': 'farmatech_balanced_scorecard_reporte',
        'height': 600,
        'width': 1100,
        'scale': 2
    }
}

# Inicializar los estados de despliegue dinámico (Estados de acordeón independientes)
if "show_fin" not in st.session_state: st.session_state.show_fin = False
if "show_cli" not in st.session_state: st.session_state.show_cli = False
if "show_pro" not in st.session_state: st.session_state.show_pro = False
if "show_cre" not in st.session_state: st.session_state.show_cre = False

# 2. CONTROLES MAESTROS EN EL SIDEBAR (MODULADORES DE ENERGÍA)
st.sidebar.header("🎛️ Centro de Simulación Operativa")
st.sidebar.markdown("Modifique los inductores primarios para estresar las metas del negocio en tiempo real.")

transacciones_reales_dia = st.sidebar.slider("Transacciones Reales Diarias (POS)", min_value=30, max_value=120, value=65, step=5)
horas_cap = st.sidebar.slider("Horas de Capacitación Anual / Empleado", min_value=0, max_value=40, value=20, step=2)
eficiencia_logistica = st.sidebar.slider("Eficiencia Operativa del Canal Domicilios (%)", min_value=50, max_value=100, value=95, step=5)

meta_transacciones_dia = 84

st.subheader("🎯 Mapa Estratégico Interactivo")
st.write("Presione directamente cualquiera de las tarjetas de colores para abrir o cerrar su análisis de impacto dinámico.")
st.markdown("---")

# =============================================================================
# BLOQUE 1: PERSPECTIVA FINANCIERA (Azul Corporativo Deep)
# =============================================================================
st.markdown("<style>div[key='btn_fin'] > button { background: linear-gradient(135deg, #1e3d59 0%, #112233 100%) !important; }</style>", unsafe_allow_html=True)
if st.button("🔵 1. PERSPECTIVA FINANCIERA (Punto de Equilibrio • Ingresos Anuales • Margen)", key="btn_fin"):
    st.session_state.show_fin = not st.session_state.show_fin

if st.session_state.show_fin:
    st.markdown("#### 💰 Hito del Cierre: Viabilidad Económica del Proyecto")
    st.markdown("La perspectiva financiera consolida el éxito total de los inductores de los niveles inferiores. Si las operaciones en la base de datos se ejecutan correctamente, el modelo responde de la siguiente manera:")
    
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        eficiencia_financiera = (transacciones_reales_dia / meta_transacciones_dia) * 100
        st.metric(label="Eficiencia Comercial (Meta: 84 Tx/Día)", value=f"{transacciones_reales_dia} Tx/Día", delta=f"{eficiencia_financiera:.1f}% del Equilibrio")
    with col_f2:
        st.metric(label="OPEX Fijo Mensual Unificado", value="\$41.500.000 COP", delta="Cifra Ancla Estructurada")
    with col_f3:
        st.metric(label="Umbral de Facturación Requerido (PE)", value="\$138.600.000 COP", delta="Mes 7 Validado")
        
    fig_f = go.Figure(go.Indicator(
        mode = "gauge+number", value = transacciones_reales_dia,
        title = {'text': "Volumen de Operaciones Diarias en Canal POS"},
        gauge = {'axis': {'range': [0, 140]}, 'bar': {'color': "#1e3d59"}, 'threshold': {'line': {'color': "red", 'width': 4}, 'value': 84}}
    ))
    fig_f.update_layout(height=240, margin=dict(t=30, b=10, l=10, r=10))
    st.plotly_chart(fig_f, use_container_width=True, config=config_exportacion)

st.markdown('<div class="arrow-q">▲</div>', unsafe_allow_html=True)

# =============================================================================
# BLOQUE 2: PERSPECTIVA DE CLIENTES (Naranja Premium)
# =============================================================================
st.markdown("<style>div[key='btn_cli'] > button { background: linear-gradient(135deg, #ff7f0e 0%, #b35900 100%) !important; }</style>", unsafe_allow_html=True)
if st.button("🟠 2. PERSPECTIVA DE CLIENTES (Nicho Crónico • Satisfacción NPS • Omnicanalidad)", key="btn_cli"):
    st.session_state.show_cli = not st.session_state.show_cli

if st.session_state.show_cli:
    st.markdown("#### 👥 Simulación de Impacto: Clientes → Financiera")
    st.markdown("El volumen de clientes fidelizados altera la tracción comercial y la masa transaccional anual inyectada al Estado de Resultados.")
    
    ventas_fidelizadas = int(1200 + (transacciones_reales_dia * 15.5))
    ingresos_derived = ventas_fidelizadas * 55000
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.info(f"📈 Masa Transaccional Traccionada: El flujo de clientes crónicos arrastra {ventas_fidelizadas:,} transacciones anuales.")
    with col_c2:
        st.info(f"📈 Impacto en Facturación: Ingresos complementarios estimados en \${ingresos_derived:,.0f} COP.")
        
    x_meses = [f"Mes {i}" for i in range(1, 13)]
    y_ventas = np.linspace(30, transacciones_reales_dia, 12) * 30
    fig_c = go.Figure()
    fig_c.add_trace(go.Scatter(x=x_meses, y=y_ventas, mode='lines+markers', name='Tendencia', line=dict(color='#ff7f0e', width=3)))
    fig_c.update_layout(title="Proyección de Crecimiento del Flujo de Clientes", height=240, margin=dict(t=30, b=10, l=10, r=10))
    st.plotly_chart(fig_c, use_container_width=True, config=config_exportacion)

st.markdown('<div class="arrow-q">▲</div>', unsafe_allow_html=True)

# =============================================================================
# BLOQUE 3: PERSPECTIVA DE PROCESOS INTERNOS (Verde Botánico)
# =============================================================================
st.markdown("<style>div[key='btn_pro'] > button { background: linear-gradient(135deg, #2ca02c 0%, #175217 100%) !important; }</style>", unsafe_allow_html=True)
if st.button("🟢 3. PERSPECTIVA DE PROCESOS INTERNOS (SLA Envíos • Stock Bodega • INVIMA)", key="btn_pro"):
    st.session_state.show_pro = not st.session_state.show_pro

if st.session_state.show_pro:
    st.markdown("#### 🏍️ Simulación de Impacto: Procesos → Clientes")
    st.markdown(f"Al operar con una eficiencia logística del {eficiencia_logistica}% en la flota de motocicletas, se estabiliza la retención de la demanda:")
    
    nps_proyectado = 50 + (eficiencia_logistica * 0.35)
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.warning(f"⭐ Índice de Satisfacción Estimado: El modelo predice un comportamiento de {nps_proyectado:.0f} puntos NPS.")
    with col_p2:
        st.warning(f"⭐ Retención del Canal WhatsApp: Probabilidad de recompra mensual del {eficiencia_logistica:.1f}%.")
        
    fig_p = go.Figure([go.Bar(x=['SLA Express 45 Min', 'Disponibilidad Stock', 'Conformidad INVIMA'], y=[eficiencia_logistica, 98, 100], marker_color='#2ca02c')])
    fig_p.update_layout(title="Cumplimiento de Estándares de Operación Interna (%)", height=240, margin=dict(t=30, b=10, l=10, r=10), yaxis=dict(range=[0, 110]))
    st.plotly_chart(fig_p, use_container_width=True, config=config_exportacion)

st.markdown('<div class="arrow-q">▲</div>', unsafe_allow_html=True)

# =============================================================================
# BLOQUE 4: PERSPECTIVA DE APRENDIZAJE Y CRECIMIENTO (Morado Violeta)
# =============================================================================
st.markdown("<style>div[key='btn_cre'] > button { background: linear-gradient(135deg, #9467bd 0%, #52356b 100%) !important; }</style>", unsafe_allow_html=True)
if st.button("🟣 4. PERSPECTIVA DE APRENDIZAJE Y CRECIMIENTO (Capacitación BPA • ERP Memphis)", key="btn_cre"):
    st.session_state.show_cre = not st.session_state.show_cre

if st.session_state.show_cre:
    st.markdown("#### 🧬 Simulación de Impacto: Aprendizaje → Procesos")
    st.markdown(f"Al programar {horas_cap} horas de capacitación técnica en Buenas Prácticas de Almacenamiento, se proyectan los siguientes efectos en cascada:")
    
    reduccion_errores = horas_cap * 2.2
    mejora_inventario = min(100.0, 70.0 + (horas_cap * 0.75))
    
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        st.success(f"✔️ Reducción de Errores de Dispensación: Disminución proyectada del {reduccion_errores:.1f}% en confusión de lotes.")
    with col_a2:
        st.success(f"✔️ Precisión en Custodia de Stock: Sincronización del inventario estimado en un {mejora_inventario:.1f}%.")
        
    horas_rango = np.arange(0, 41, 2)
