import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN HIGH-DEFINITION DE LA INTERFAZ DE USUARIO (UI)
st.set_page_config(
    page_title="FarmaTech - Balanced Scorecard",
    layout="wide",
    page_icon="🎯"
)

# Inyección de estilos CSS avanzados para crear tarjetas legibles y espaciadas
st.markdown("""
    <style>
    .main-title { font-family: 'Helvetica Neue', Arial, sans-serif; color: #1e3d59; font-weight: 800; font-size: 2.5rem; margin-bottom: 0.2rem; }
    .section-desc { color: #6c757d; font-size: 1.05rem; margin-bottom: 1.5rem; }
    
    /* Estilos para las tarjetas del Mapa Estratégico */
    .bsc-node {
        padding: 20px;
        border-radius: 12px;
        color: white;
        font-family: Arial, sans-serif;
        text-align: center;
        margin: 10px auto;
        max-width: 700px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .fin-node { background-color: #1e3d59; border-left: 8px solid #0f202e; }
    .cli-node { background-color: #ff7f0e; border-left: 8px solid #cc6600; }
    .pro-node { background-color: #2ca02c; border-left: 8px solid #1e6b1e; }
    .cre-node { background-color: #9467bd; border-left: 8px solid #6b438a; }
    
    .node-title { font-size: 1.2rem; font-weight: bold; margin-bottom: 5px; text-transform: uppercase; letter-spacing: 1px; }
    .node-desc { font-size: 0.95rem; opacity: 0.95; line-height: 1.4; }
    
    /* Estilo para las flechas de conexión */
    .arrow-connector {
        text-align: center;
        font-size: 2rem;
        color: #6c757d;
        line-height: 1;
        margin: 5px 0;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🚀 Tabla 20. Mapa estratégico — Objetivos por perspectiva BSC — FarmaTech Ltda.</h1>', unsafe_allow_html=True)
st.markdown('<p class="section-desc">Cuadro de Mando Integral, Causalidad Operativa y Modelado de Elasticidad de Metas (2026)</p>', unsafe_allow_html=True)
st.markdown("---")

# 2. SECCIÓN DE CONTROLES E INDUCTORES EN LA BARRA LATERAL (SIDEBAR)
st.sidebar.header("🎛️ Centro de Simulación de Metas")
st.sidebar.markdown("Estrese el cumplimiento de los objetivos estratégicos modificando el avance real del POS.")

transacciones_reales_dia = st.sidebar.slider("Transacciones Reales Diarias (POS)", min_value=30, max_value=120, value=65, step=5)
nps_actual = st.sidebar.slider("Índice de Satisfacción del Cliente (NPS)", min_value=40, max_value=100, value=74, step=2)
horas_capacitacion = st.sidebar.slider("Horas de Capacitación Anual / Empleado", min_value=5, max_value=40, value=22, step=1)

# Base fija estructural para cálculos comparativos
meta_transacciones_dia = 84

# 3. FILA DE TARJETAS METRICAS DINÁMICAS (KPI SCORING)
st.subheader("📊 Monitoreo de Inductores y Alertas de Desempeño")
col_kpi1, col_kpi2, col_kpi3 = st.columns(3)

with col_kpi1:
    eficiencia_financiera = (transacciones_reales_dia / meta_transacciones_dia) * 100
    st.metric(
        label="🎯 Eficiencia Financiera (Meta PE: 84 Tx/Día)", 
        value=f"{transacciones_reales_dia} Tx/Día", 
        delta=f"{eficiencia_financiera:.1f}% de la Meta de Caja"
    )
with col_kpi2:
    delta_nps = nps_actual - 70
    st.metric(
        label="⭐ Indicador de Fidelización (Meta NPS: ≥70)", 
        value=f"{nps_actual} NPS", 
        delta=f"{delta_nps} Puntos sobre el Umbral"
    )
with col_kpi3:
    delta_cap = horas_capacitacion - 20
    st.metric(
        label="📚 Desarrollo del Personal (Meta: ≥20 Hrs)", 
        value=f"{horas_capacitacion} Horas/Año", 
        delta=f"{delta_cap} Horas vs Estándar BPA"
    )

st.markdown("---")

# Layout de dos bloques: Tabla de datos a la izquierda y Mapa legible a la derecha
col_izq, col_der = st.columns([4, 5])

# =============================================================================
# BLOQUE IZQUIERDO: EXTRACCIÓN Y CONSULTA FILTRADA DE LA MATRIZ BSC
# =============================================================================
with col_izq:
    st.subheader("📋 Matriz de Planificación Estratégica")
    
    filtro_vista = st.selectbox(
        "Filtrar Cuadro de Mando por Enfoque de Gestión:",
        ["Todas las Perspectivas", "FINANCIERA", "CLIENTES", "PROCESOS", "CRECIMIENTO"]
    )
    
    bsc_raw_data = [
        {"Perspectiva": "FINANCIERA", "Objetivo": "Alcanzar el punto de equilibrio financiero", "Meta": "≥ 84 transacciones/día (OPEX cubierto)", "Horizonte": "Mes 7 operación"},
        {"Perspectiva": "FINANCIERA", "Objetivo": "Generar ingresos de $891 MM COP en el año 1", "Meta": "675 cl. × 2 compras × 12 meses × $55.000", "Horizonte": "Año 1"},
        {"Perspectiva": "FINANCIERA", "Objetivo": "Mantener margen bruto del 30% sobre ingresos", "Meta": "≥ $41.500.000 COP/mes en margen", "Horizonte": "Permanente"},
        {"Perspectiva": "FINANCIERA", "Objetivo": "Recuperar la inversión total de $280 MM", "Meta": "ROI positivo validado en flujo de caja", "Horizonte": "Año 3"},
        {"Perspectiva": "CLIENTES", "Objetivo": "Capturar el 15% del nicho de pacientes crónicos", "Meta": "675 pacientes crónicos activos", "Horizonte": "Año 1"},
        {"Perspectiva": "CLIENTES", "Objetivo": "Lograr NPS ≥ 70 en satisfacción de cliente", "Meta": "Encuesta WhatsApp post-entrega", "Horizonte": "Trimestral"},
        {"Perspectiva": "CLIENTES", "Objetivo": "Lograr omnicanalidad efectiva vía WhatsApp", "Meta": "≥ 40% de pedidos por canal digital", "Horizonte": "Año 1"},
        {"Perspectiva": "PROCESOS", "Objetivo": "Cumplir promesa de valor en domicilios express", "Meta": "95% de entregas en el rango 20-45 min", "Horizonte": "Mensual"},
        {"Perspectiva": "PROCESOS", "Objetivo": "Garantizar disponibilidad de stock estratégico", "Meta": "Stock seguridad ≥ 30 días (crónicos)", "Horizonte": "Permanente"},
        {"Perspectiva": "PROCESOS", "Objetivo": "Mantener habilitaciones sanitarias vigentes", "Meta": "Cero hallazgos críticos en visitas INVIMA", "Horizonte": "Permanente"},
        {"Perspectiva": "CRECIMIENTO", "Objetivo": "Capacitar al 100% del personal en BPA y HTA", "Meta": "Capacitación ≥ 20 horas/empleado/año", "Horizonte": "Semestral"},
        {"Perspectiva": "CRECIMIENTO", "Objetivo": "Liderazgo en el sector Laureles para 2028", "Meta": "≥ 2.500 pacientes fidelizados en el sistema", "Horizonte": "Año 2028"}
    ]
    df_bsc_all = pd.DataFrame(bsc_raw_data)
    
    if filtro_vista != "Todas las Perspectivas":
        df_bsc_all = df_bsc_all[df_bsc_all["Perspectiva"] == filtro_vista]
        
    st.dataframe(df_bsc_all, use_container_width=True, hide_index=True)

# =============================================================================
# BLOQUE DERECHO: MAPA DE VECTORES EN ALTA DEFINICIÓN (HTML CLEAN)
# =============================================================================
with col_der:
    st.subheader("🛸 Diagrama de Causalidad Estructural (Balanced Scorecard)")
    st.write("Modelado de vectores de dependencia ascendente. El desarrollo del personal impulsa la cadena de procesos, la retención de clientes y la rentabilidad.")
    
    # 1. Tarjeta Financiera
    st.markdown("""
        <div class="bsc-node fin-node">
            <div class="node-title">1. Perspectiva Financiera</div>
            <div class="node-desc">Alcanzar Punto de Equilibrio (≥84 Tx/Día) • Generar Ingresos de $891M Anuales • Margen del 30% • ROI en Año 3</div>
        </div>
        <div class="arrow-connector">▲</div>
    """, unsafe_allow_html=True)
    
    # 2. Tarjeta Clientes
    st.markdown("""
        <div class="bsc-node cli-node">
            <div class="node-title">2. Perspectiva de Clientes</div>
            <div class="node-desc">Capturar el 15% del Nicho Crónico (675 Pacientes) • Sostener NPS ≥ 70 • Omnicanalidad Digital del 40% vía WhatsApp</div>
        </div>
        <div class="arrow-connector">▲</div>
    """, unsafe_allow_html=True)
    
    # 3. Tarjeta Procesos Internos
    st.markdown("""
        <div class="bsc-node pro-node">
            <div class="node-title">3. Perspectiva de Procesos Internos</div>
            <div class="node-desc">Garantizar SLA Express (20-45 Min en 95% de Envíos) • Stock Fijo ≥ 30 Días • Cero Hallazgos Críticos ante INVIMA</div>
        </div>
        <div class="arrow-connector">▲</div>
    """, unsafe_allow_html=True)
    
    # 4. Tarjeta Aprendizaje y Crecimiento
    st.markdown("""
        <div class="bsc-node  cre-node">
            <div class="node-title">4. Perspectiva de Aprendizaje y Crecimiento</div>
            <div class="node-desc">Capacitación ≥ 20 Horas/Año en BPA • Optimización con Software ERP • Fidelización de 2.500 Usuarios para 2028</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
> **Nota analítica de control de mando integral:** La matriz del Balanced Scorecard unifica los inductores de crecimiento del talento humano con los resultados de rentabilidad exigidos por la junta de socios. Las metas de la perspectiva de Procesos (como la cobertura del 95% de entregas en menos de 45 minutos) justifican el uso de las tres motocicletas de la flota logística, mientras que el volumen de la perspectiva financiera conversa directamente con la capacidad de las tres terminales POS en el frente comercial.
""")
