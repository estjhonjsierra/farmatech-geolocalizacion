import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 1. CONFIGURACIÓN HIGH-DEFINITION DE LA INTERFAZ DE USUARIO (UI)
st.set_page_config(
    page_title="FarmaTech - Balanced Scorecard",
    layout="wide",
    page_icon="🎯"
)

# Inyección de estilos de cascada CSS para simular entorno de software empresarial
st.markdown("""
    <style>
    .main-title { font-family: 'Helvetica Neue', Arial, sans-serif; color: #1e3d59; font-weight: 800; font-size: 2.5rem; margin-bottom: 0.2rem; }
    .section-desc { color: #6c757d; font-size: 1.05rem; margin-bottom: 1.5rem; }
    .card-kpi { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-top: 4px solid #1e3d59; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🚀 Tabla 20. Mapa estratégico — Objetivos por perspectiva BSC — FarmaTech Ltda.</h1>', unsafe_allow_html=True)
st.markdown('<p class="section-desc">Cuadro de Mando Integral, Causalidad Operativa y Modelado de Elasticidad de Metas (2026)</p>', unsafe_allow_html=True)
st.markdown("---")

# Configuración universal para descarga de reportes y capturas (Cámara 📸 activa)
config_exportacion = {
    'displayModeBar': True,
    'toImageButtonOptions': {
        'format': 'png',
        'filename': 'farmatech_mapa_estrategico_bsc',
        'height': 650,
        'width': 1100,
        'scale': 2
    }
}

# 2. SECCIÓN DE CONTROLES E INDUCTORES EN LA BARRA LATERAL (SIDEBAR)
st.sidebar.header("🎛️ Centro de Simulación de Metas")
st.sidebar.markdown("Estrese el cumplimiento de los objetivos estratégicos modificando el avance real del POS.")

transacciones_reales_dia = st.sidebar.slider("Transacciones Reales Diarias (POS)", min_value=30, max_value=120, value=65, step=5)
nps_actual = st.sidebar.slider("Índice de Satisfacción del Cliente (NPS)", min_value=40, max_value=100, value=74, step=2)
horas_capacitacion = st.sidebar.slider("Horas de Capacitación Anual / Empleado", min_value=5, max_value=40, value=22, step=1)

# Base fija estructural para cálculos comparativos
opex_ancla = 41500000
meta_transacciones_dia = 84

# 3. FILA DE TARJETAS METRICAS DINÁMICAS (KPI SCORING)
st.subheader("📊 Monitoreo de Inductores y Alertas de Desempeño")
col_k1, col_k2, col_k3 = st.columns(3)

with col_k1:
    eficiencia_financiera = (transacciones_reales_dia / meta_transacciones_dia) * 100
    st.metric(
        label="🎯 Eficiencia Financiera (Meta PE: 84 Tx/Día)", 
        value=f"{transacciones_reales_dia} Tx/Día", 
        delta=f"{eficiencia_financiera:.1f}% de la Meta de Caja"
    )
with col_k2:
    delta_nps = nps_actual - 70
    st.metric(
        label="⭐ Indicador de Fidelización (Meta NPS: ≥70)", 
        value=f"{nps_actual} NPS", 
        delta=f"{delta_nps} Puntos sobre el Umbral"
    )
with col_k3:
    delta_cap = horas_capacitacion - 20
    st.metric(
        label="📚 Desarrollo del Personal (Meta: ≥20 Hrs)", 
        value=f"{horas_capacitacion} Horas/Año", 
        delta=f"{delta_cap} Horas vs Estándar BPA"
    )

st.markdown("---")

# Layout de dos bloques para desglose visual y mapa de causalidad
col_izq, col_der = st.columns([4, 6])

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
    
    st.markdown("""
    > **Nota analítica de control del mapa integral:** La matriz del Balanced Scorecard unifica los inductores de crecimiento del talento humano con los resultados de rentabilidad exigidos por la junta de socios. Las metas de la perspectiva de Procesos (como la cobertura del 95% de entregas en menos de 45 minutos) justifican el uso de las tres motocicletas de la flota logística, mientras que el volumen de la perspectiva financiera conversa directamente con la capacidad de las tres terminales POS en el frente comercial.
    """)

# =============================================================================
# BLOQUE DERECHO: DIAGRAMA DE CAUSALIDAD INTERCONECTADO (MAPA EN 2D PREMIUM)
# =============================================================================
with col_der:
    st.subheader("🛸 Diagrama de Flujo y Vectores de Causalidad Estructural")
    st.write("El mapa modela de forma visual cómo el aprendizaje indexado empuja el éxito de los procesos, la fidelización de clientes y la rentabilidad.")
    
    # Definición manual de las cajas de texto de las perspectivas en ejes X e Y
    nodos_x = [2, 2, 2, 2]
    nodos_y = [4, 3, 2, 1]
    textos_nodos = [
        "<b>1. PERSPECTIVA FINANCIERA</b><br>Punto de Equilibrio (84 Tx/Día) | ROI Año 3 | Margen 30%",
        "<b>2. PERSPECTIVA DE CLIENTES</b><br>Niche Crónicos 15% | NPS ≥ 70 | Omnicanalidad WA 40%",
        "<b>3. PERSPECTIVA DE PROCESOS INTERNOS</b><br>SLA Express 20-45 Min | Stock Fijo ≥ 30 Días | Normas INVIMA",
        "<b>4. PERSPECTIVA DE APRENDIZAJE Y CRECIMIENTO</b><br>Capacitación ≥ 20 Hrs/Año | Automatización ERP | Fidelización 2.500 Pacientes"
    ]
    colores_nodos = ["#1e3d59", "#ff7f0e", "#2ca02c", "#9467bd"]

    fig_mapa = go.Figure()

    # Dibujar las líneas conectores con flechas de causalidad ascendente
    for i in range(len(nodos_y) - 1):
        fig_mapa.add_trace(go.Scatter(
            x=[2, 2], y=[nodos_y[i+1]+0.35, nodos_y[i]-0.35],
            mode="lines",
            line=dict(color="#6c757d", width=3),
            hoverinfo="none", showlegend=False
        ))
        # Agregar cabeza de la flecha
        fig_mapa.add_trace(go.Scatter(
            x=[2], y=[nodos_y[i]-0.35],
            mode="markers",
            marker=dict(symbol="arrow-up", size=14, color="#6c757d"),
            hoverinfo="none", showlegend=False
        ))

    # Dibujar los bloques de texto rectangulares (Cajas del BSC)
    fig_mapa.add_trace(go.Scatter(
        x=nodos_x, y=nodos_y,
        mode="markers+text",
        marker=dict(
            shape="square",
            size=75,
            color=colores_nodos,
            line=dict(color="white", width=2)
        ),
        text=textos_nodos,
        textposition="center",
        textfont=dict(color="white", size=11, family="Arial"),
        showlegend=False
    ))

    # Ajustes métricos y estéticos del contenedor del diagrama de flujo
    fig_mapa.update_layout(
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[1, 3]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0.3, 4.7]),
        margin=dict(t=10, b=10, l=10, r=10),
        height=480,
        plot_bgcolor="rgba(0,0,0,0)"
    )
    
    # Renderizado final del gráfico con la barra de exportación PNG activa
    st.plotly_chart(fig_mapa, use_container_width=True, config=config_exportacion)

