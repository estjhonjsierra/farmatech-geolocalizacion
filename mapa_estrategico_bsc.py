import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 1. CONFIGURACIÓN HIGH-DEFINITION DE LA INTERFAZ DE USUARIO
st.set_page_config(
    page_title="FarmaTech - Balanced Scorecard Central",
    layout="wide",
    page_icon="🎯"
)

# Inyección de estilos CSS avanzados para personalización de botones premium
st.markdown("""
    <style>
    .main-title { font-family: 'Helvetica Neue', Arial, sans-serif; color: #1e3d59; font-weight: 800; font-size: 2.5rem; margin-bottom: 0.2rem; }
    .section-desc { color: #6c757d; font-size: 1.05rem; margin-bottom: 1.5rem; }
    .arrow-q { text-align: center; font-size: 1.8rem; color: #1e3d59; font-weight: bold; margin: 2px 0; }
    
    /* Forzar que los botones de Streamlit abarquen todo el ancho y simulen las tarjetas */
    div.stButton > button {
        width: 100%;
        font-size: 1.15rem !important;
        font-weight: bold !important;
        padding: 15px !important;
        border-radius: 12px !important;
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
st.markdown('<p class="section-desc">Modelado Dinámico de Causalidad e Impacto en Cascada — FarmaTech Ltda.</p>', unsafe_allow_html=True)
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

# Inicializar el estado de la aplicación para registrar los clics de los botones
if "fase_activa" not in st.session_state:
    st.session_state.fase_activa = "Neutro"

# 2. CONTROLES MAESTROS EN EL SIDEBAR (MODULADORES DE ENERGÍA)
st.sidebar.header("🎛️ Centro de Simulación Operativa")
st.sidebar.markdown("Modifique los inductores primarios para estresar las metas del negocio en tiempo real.")

transacciones_reales_dia = st.sidebar.slider("Transacciones Reales Diarias (POS)", min_value=30, max_value=120, value=65, step=5)
horas_cap = st.sidebar.slider("Horas de Capacitación Anual / Empleado", min_value=0, max_value=40, value=20, step=2)
eficiencia_logistica = st.sidebar.slider("Eficiencia Operativa del Canal Domicilios (%)", min_value=50, max_value=100, value=95, step=5)

meta_transacciones_dia = 84

# 3. DISTRIBUCIÓN DE PANTALLA EN DOS COLUMNAS MAESTRAS
col_mapa, col_analisis = st.columns([1, 1.2])

with col_mapa:
    st.subheader("🎯 Nodos del Mapa Estratégico")
    st.write("Presione directamente cualquiera de las tarjetas de colores para inyectar energía y abrir su simulación:")
    
    # BOTÓN 1: PERSPECTIVA FINANCIERA (Azul Corporativo)
    st.markdown("<style>div[key='btn_fin'] > button { background: linear-gradient(135deg, #1e3d59 0%, #112233 100%) !important; }</style>", unsafe_allow_html=True)
    if st.button("🔵 1. PERSPECTIVA FINANCIERA", key="btn_fin"):
        st.session_state.fase_activa = "Financiera"
        
    st.markdown('<div class="arrow-q">▲</div>', unsafe_allow_html=True)
    
    # BOTÓN 2: PERSPECTIVA DE CLIENTES (Naranja)
    st.markdown("<style>div[key='btn_cli'] > button { background: linear-gradient(135deg, #ff7f0e 0%, #b35900 100%) !important; }</style>", unsafe_allow_html=True)
    if st.button("🟠 2. PERSPECTIVA DE CLIENTES", key="btn_cli"):
        st.session_state.fase_activa = "Clientes"
        
    st.markdown('<div class="arrow-q">▲</div>', unsafe_allow_html=True)
    
    # BOTÓN 3: PERSPECTIVA DE PROCESOS INTERNOS (Verde)
    st.markdown("<style>div[key='btn_pro'] > button { background: linear-gradient(135deg, #2ca02c 0%, #175217 100%) !important; }</style>", unsafe_allow_html=True)
    if st.button("🟢 3. PERSPECTIVA DE PROCESOS INTERNOS", key="btn_pro"):
        st.session_state.fase_activa = "Procesos"
        
    st.markdown('<div class="arrow-q">▲</div>', unsafe_allow_html=True)
    
    # BOTÓN 4: PERSPECTIVA DE APRENDIZAJE Y CRECIMIENTO (Morado)
    st.markdown("<style>div[key='btn_cre'] > button { background: linear-gradient(135deg, #9467bd 0%, #52356b 100%) !important; }</style>", unsafe_allow_html=True)
    if st.button("🟣 4. PERSPECTIVA DE APRENDIZAJE Y CRECIMIENTO", key="btn_cre"):
        st.session_state.fase_activa = "Aprendizaje"

# =============================================================================
# BLOQUE DERECHO: DETECTA EL CLIC Y DESPLIEGA LA SIMULACIÓN AUTOMÁTICA
# =============================================================================
with col_analisis:
    st.subheader("🔮 Trazabilidad Dinámica de Causalidad")
    
    if st.session_state.fase_activa == "Neutro":
        st.info("💡 **Sistema Listo:** Haga clic directo en cualquiera de las 4 macro-tarjetas de color de la izquierda para disparar el flujo analítico y desplegar las gráficas con captura fotográfica.")
        
    elif st.session_state.fase_activa == "Financiera":
        st.markdown("### 💰 1. Impacto en Viabilidad Económica")
        st.write("La perspectiva financiera consolida el éxito de los inductores de base, calculando el margen mínimo de cobertura.")
        
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            eficiencia_fin = (transacciones_reales_dia / meta_transacciones_dia) * 100
            st.metric(label="Eficiencia Comercial (Meta: 84 Tx/Día)", value=f"{transacciones_reales_dia} Tx/Día", delta=f"{eficiencia_fin:.1f}% de la Meta")
        with col_f2:
            st.metric(label="Umbral Mínimo Mensual (P.E.)", value="\$138,600,000 COP", delta="OPEX \$41.5M Cubierto")
            
        fig_f = go.Figure(go.Indicator(
            mode = "gauge+number", value = transacciones_reales_dia,
            title = {'text': "Volumen de Operaciones Diarias en Canal POS"},
            gauge = {'axis': {'range': [0, 120]}, 'bar': {'color': "#1e3d59"}, 'threshold': {'line': {'color': "red", 'width': 4}, 'value': 84}}
        ))
        fig_f.update_layout(height=260, margin=dict(t=30, b=10, l=10, r=10))
        st.plotly_chart(fig_f, use_container_width=True, config=config_exportacion)

    elif st.session_state.fase_activa == "Clientes":
        st.markdown("### 👥 2. Impacto en Tracción de Demanda")
        st.write("La aceleración en el flujo de clientes crónicos altera la masa transaccional inyectada al Estado de Resultados.")
        
        ventas_fidelizadas = int(1200 + (transacciones_reales_dia * 15.5))
        ingresos_derived = ventas_fidelizadas * 55000
        
        st.success(f"📈 **Masa Transaccional Traccionada:** {ventas_fidelizadas:,} transacciones anuales acumuladas.")
        st.success(f"📈 **Facturación Estimada de Cierre:** \${ingresos_derived:,.0f} COP.")
        
        x_meses = [f"Mes {i}" for i in range(1, 13)]
        y_ventas = np.linspace(30, transacciones_reales_dia, 12) * 30
        fig_c = go.Figure()
        fig_c.add_trace(go.Scatter(x=x_meses, y=y_ventas, mode='lines+markers', name='Tendencia', line=dict(color='#ff7f0e', width=3)))
        fig_c.update_layout(title="Proyección de Crecimiento del Flujo de Clientes", height=230, margin=dict(t=30, b=10, l=10, r=10))
        st.plotly_chart(fig_c, use_container_width=True, config=config_exportacion)

    elif st.session_state.fase_activa == "Procesos":
        st.markdown("### 🏍️ 3. Impacto en Eficiencia de Procesos")
        st.write(f"Al operar con una eficiencia logística del {eficiencia_logistica}% en domicilios, se estabiliza la retención de la demanda:")
        
        nps_proyectado = 50 + (eficiencia_logistica * 0.35)
        st.warning(f"⭐ **Índice de Satisfacción Estimado:** Percepción fijada en **{nps_proyectado:.0f} puntos NPS**.")
        
        fig_p = go.Figure([go.Bar(x=['SLA Express 45 Min', 'Disponibilidad Stock', 'Norma INVIMA'], y=[eficiencia_logistica, 98, 100], marker_color='#2ca02c')])
        fig_p.update_layout(title="Cumplimiento de Estandares Internos (%)", height=230, margin=dict(t=30, b=10, l=10, r=10), yaxis=dict(range=[0, 110]))
        st.plotly_chart(fig_p, use_container_width=True, config=config_exportacion)

    elif st.session_state.fase_activa == "Aprendizaje":
        st.markdown("### 🧬 4. Impacto de Crecimiento y Aprendizaje")
        st.write(f"Al programar {horas_cap} horas de capacitación técnica en BPA, se mitiga el riesgo de pérdida operativa:")
        
        reduccion_errores = horas_cap * 2.2
        st.info(f"✔️ **Reducción del Error Operativo:** Disminución proyectada del **{reduccion_errores:.1f}%** en confusión de lotes.")
        
        horas_rango = np.arange(0, 41, 2)
        errores_rango = 100 - (horas_rango * 2.2)
        fig_cap = go.Figure()
        fig_cap.add_trace(go.Scatter(x=horas_rango, y=errores_rango, mode='lines', name='Curva de Error', line=dict(color='#9467bd', width=3)))
        fig_cap.add_trace(go.Scatter(x=[horas_cap], y=[100 - reduccion_errores], mode='markers', name='Tu Impacto', marker=dict(color='red', size=12, symbol='diamond')))
        fig_cap.update_layout(title="Curva de Reducción del Error Operativo", xaxis_title="Horas de Capacitación", yaxis_title="Error Residual (%)", height=230, margin=dict(t=30, b=10, l=10, r=10))
        st.plotly_chart(fig_cap, use_container_width=True, config=config_exportacion)

st.markdown("---")
st.markdown("""
