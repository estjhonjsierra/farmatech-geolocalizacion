import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# 1. CONFIGURACIÓN PREMIUM DE LA INTERFAZ DE USUARIO
st.set_page_config(
    page_title="FarmaTech - Sistema Central de Operaciones",
    layout="wide",
    page_icon="💊"
)

# Inyección de estilos CSS para personalización corporativa avanzada
st.markdown("""
    <style>
    .main-title { font-family: 'Helvetica Neue', Arial, sans-serif; color: #1e3d59; font-weight: 800; font-size: 2.6rem; margin-bottom: 0.2rem; }
    .section-desc { color: #6c757d; font-size: 1.05rem; margin-bottom: 1.5rem; }
    stTabs [data-baseweb="tab-list"] { gap: 10px; }
    stTabs [data-baseweb="tab"] {
        background-color: #f1f3f5;
        border-radius: 8px 8px 0px 0px;
        padding: 10px 20px;
        font-weight: 600;
        color: #495057;
    }
    stTabs [data-baseweb="tab"]:hover { background-color: #e9ecef; }
    stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #1e3d59;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🚀 FarmaTech Ltda. — Sistema Central de Control Analítico</h1>', unsafe_allow_html=True)
st.markdown('<p class="section-desc">Arquitectura de Operaciones, Cronogramas y Simulación de Viabilidad Financiera (Fase 3 - 2026)</p>', unsafe_allow_html=True)

# 2. DEFINICIÓN DE LA BASE DE DATOS CENTRALIZADA (Tabla 11 Oficial)
data_opex = {
    "Rubro Técnico": [
        "Arrendamiento Local", "Nómina: Regente de Farmacia", "Nómina: 3 Auxiliares", 
        "Nómina: 1 Mensajero", "Servicios Públicos", "Póliza de Responsabilidad", 
        "Licenciamiento ERP", "Combustible Flota", "Marketing Digital", 
        "Insumos Bioseguridad", "Margen Imprevistos", "Fondo Reserva Capital"
    ],
    "Monto Fijo": [5000000, 4500000, 6300000, 2100000, 1200000, 600000, 400000, 1200000, 2500000, 500000, 2000000, 15200000],
    "Categoría": ["Infraestructura", "Personal", "Personal", "Personal", "Infraestructura", "Operación", "Tecnología", "Logística", "Comercial", "Operación", "Contingencia", "Liquidez"]
}
df_opex = pd.DataFrame(data_opex)
total_opex = df_opex["Monto Fijo"].sum()

# Configuración universal para descarga de reportes e imágenes en Plotly
config_exportacion = {
    'displayModeBar': True,
    'toImageButtonOptions': {
        'format': 'png',
        'filename': 'farmatech_reporte_grafico',
        'height': 600,
        'width': 1100,
        'scale': 2
    }
}

# 3. CONTROLES DEL MODELO FINANCIERO EN LA BARRA LATERAL (SIDEBAR)
st.sidebar.header("🎛️ Variables Macroeconómicas")
st.sidebar.markdown("Ajuste los parámetros para simular la sensibilidad del negocio en tiempo real.")

ticket_simulado = st.sidebar.slider("Ticket Promedio de Venta (COP)", min_value=35000, max_value=120000, value=55000, step=5000, format="$%d")
margen_simulado_pct = st.sidebar.slider("Margen de Contribución Neto (%)", min_value=15, max_value=50, value=30, step=5, format="%d%%")

# Fórmulas de ingeniería financiera automatizadas
margen_pesos = ticket_simulado * (margen_simulado_pct / 100)
tx_punto_equilibrio = total_opex / margen_pesos
ingresos_minimos = tx_punto_equilibrio * ticket_simulado

# 4. SISTEMA DE NAVEGACIÓN EN PESTAÑAS AVANZADAS (TABS)
tab_costos, tab_sensibilidad, tab_cronograma = st.tabs([
    "📊 Estructura de Costos (OPEX)", 
    "📈 Curva de Sensibilidad Operativa", 
    "📅 Cronograma de Ruta Crítica (Gantt)"
])

# =============================================================================
# PESTAÑA 1: ANALÍTICA DE COSTOS FIJOS (TABLA Y DONUT)
# =============================================================================
with tab_costos:
    st.subheader("📋 Matriz Mensual de Carga Fija Estructural")
    st.write("Desglose detallado de los gastos operativos fijos requeridos para sostener la operación física y omnicanal.")
    
    # Fila de métricas KPI superiores
    col_k1, col_k2 = st.columns(2)
    with col_k1:
        st.metric(label="📉 COSTO FIJO REQUERIDO (OPEX)", value=f"${total_opex:,.0f} COP", delta="Fijo Mensual")
    with col_k2:
        st.metric(label="🛡️ RESPALDO ASIGNADO (CAPEX TABLA 12)", value="$80,000,000 COP", delta="Fondo de Reserva de Caja")
        
    st.markdown("---")
    
    col_vis1, col_vis2 = st.columns([4, 5])
    
    with col_vis1:
        st.markdown("**Desglose Indexado al SMMLV 2026**")
        df_ui = df_opex.copy()
        df_ui["Monto Fijo"] = df_ui["Monto Fijo"].map("${:,.0f}".format)
        st.dataframe(df_ui, use_container_width=True, hide_index=True)
        
    with col_vis2:
        st.markdown("**Representación Porcentual Sectorizada del Gasto**")
        fig_donut = px.pie(
            df_opex, 
            values="Monto Fijo", 
            names="Rubro Técnico", 
            hole=0.45,
            color_discrete_sequence=px.colors.qualitative.Prism
        )
        fig_donut.update_traces(textposition='inside', textinfo='percent')
        fig_donut.update_layout(margin=dict(t=10, b=10, l=10, r=10), showlegend=True, height=380)
        st.plotly_chart(fig_donut, use_container_width=True, config=config_exportacion)

# =============================================================================
# PESTAÑA 2: CURVA DE ELASTICIDAD OPERATIVA (2D RECOMENDADO)
# =============================================================================
with tab_sensibilidad:
    st.subheader("📈 Análisis de Elasticidad y Simulación Dinámica")
    st.write("Evaluación interactiva del volumen transaccional requerido en el Mes 7 según la variación del Ticket Promedio y el Margen comercial.")
    
    col_k3, col_k4, col_k5 = st.columns(3)
    with col_k3:
        st.metric(label="💰 Utilidad Bruta por Ticket", value=f"${margen_pesos:,.0f} COP")
    with col_k4:
        st.metric(label="🎯 Volumen Crítico de Transacciones", value=f"{tx_punto_equilibrio:,.0f} tx/mes", delta="Punto de Equilibrio")
    with col_k5:
        st.metric(label="📊 Ingreso de Cobertura Requerido", value=f"${ingresos_minimos:,.0f} COP")
        
    st.markdown("---")
    
    # Generar matriz matemática lineal para renderizar la curva
    tickets_curva = np.arange(35000, 125000, 5000)
    margenes_curva_pesos = tickets_curva * (margen_simulado_pct / 100)
    transacciones_curva = total_opex / margenes_curva_pesos

    fig_linea = go.Figure()
    
    # Comportamiento elástico del mercado
    fig_linea.add_trace(go.Scatter(
        x=tickets_curva, y=transacciones_curva,
        mode='lines+markers', name='Umbral de Equilibrio',
        line=dict(color='#1e3d59', width=3), marker=dict(size=6)
    ))
    
    # Marcador de hito de simulación actual (Hito FarmaTech)
    fig_linea.add_trace(go.Scatter(
        x=[ticket_simulado], y=[tx_punto_equilibrio],
        mode='markers', name='Configuración Seleccionada',
        marker=dict(color='red', size=14, symbol='diamond', line=dict(color='white', width=2))
    ))
    
    fig_linea.update_layout(
        xaxis_title='Ticket Promedio de Venta (COP)',
        yaxis_title='Transacciones Requeridas al Mes (Unidades)',
        height=420, margin=dict(t=20, b=20, l=20, r=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig_linea, use_container_width=True, config=config_exportacion)

# =============================================================================
# PESTAÑA 3: CRONOGRAMA OPERATIVO DE GANTT
# =============================================================================
with tab_cronograma:
    st.subheader("📅 Ruta Crítica de la Fase Preoperativa")
    st.write("Planificación temporal estructurada para las 12 semanas de montaje institucional, legal, locativo y tecnológico.")
    
    cronograma_data = [
        dict(Task="1. Registro Cámara Comercio", Start="Week 1", Finish="Week 2", Fase="Legal/Institucional"),
        dict(Task="2. Contratación Regente (DT)", Start="Week 1", Finish="Week 12", Fase="Talento Humano"),
        dict(Task="3. Trámites Seccional de Salud", Start="Week 2", Finish="Week 12", Fase="Legal/Institucional"),
        dict(Task="4. Afiliación Coopidrogas", Start="Week 1", Finish="Week 4", Fase="Legal/Institucional"),
        dict(Task="5. Obra Civil Adecuación Local", Start="Week 3", Finish="Week 9", Fase="Infraestructura"),
        dict(Task="6. Instalación Cadena de Frío", Start="Week 5", Finish="Week 8", Fase="Infraestructura"),
        dict(Task="7. Montaje de Estanterías", Start="Week 6", Finish="Week 9", Fase="Infraestructura"),
        dict(Task="8. Implementación Tecnología POS", Start="Week 8", Finish="Week 11", Fase="Tecnológica"),
        dict(Task="9. Contratación Auxiliares", Start="Week 9", Finish="Week 11", Fase="Talento Humano"),
        dict(Task="10. Adquisición Flota Domicilios", Start="Week 10", Finish="Week 12", Fase="Logística"),
        dict(Task="11. Carga de Inventario Inicial", Start="Week 11", Finish="Week 13", Fase="Logística"),
        dict(Task="12. Lanzamiento y Capacitación", Start="Week 11", Finish="Week 13", Fase="Comercial")
    ]
    df_gantt = pd.DataFrame(cronograma_data)
    
    mapa_semanas = {f"Week {i}": i for i in range(1, 14)}
    df_gantt["Inicio_Num"] = df_gantt["Start"].map(mapa_semanas)
    df_gantt["Fin_Num"] = df_gantt["Finish"].map(mapa_semanas)

    fig_gantt = px.bar(
        df_gantt, x_start="Inicio_Num", x_end="Fin_Num", y="Task", color="Fase",
        labels={"Task": "Hito Crítico"},
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    fig_gantt.update_layout(
        xaxis=dict(
            title="Horizonte Temporal (Semanas)",
            tickvals=list(range(1, 13)),
            ticktext=[f"Semana {i}" for i in range(1, 13)]
        ),
        yaxis=dict(autorange="reversed", title=""),
        height=450, margin=dict(t=20, b=20, l=20, r=20),
        legend=dict(orientation="h", yanchor="bottom", y=-0.22, xanchor="center", x=0.5)
    )
    st.plotly_chart(fig_gantt, use_container_width=True, config=config_exportacion)

