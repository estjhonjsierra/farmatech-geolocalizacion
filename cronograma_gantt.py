import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# 1. CONFIGURACIÓN PREMIUM DE LA INTERFAZ DE USUARIO (NIVEL INGENIERÍA)
st.set_page_config(
    page_title="FarmaTech - Sistema Central de Operaciones",
    layout="wide",
    page_icon="💊"
)

# Inyección de estilos CSS para personalización corporativa avanzada
st.markdown("""
    <style>
    .main-title { font-family: 'Helvetica Neue', Arial, sans-serif; color: #1e3d59; font-weight: 800; font-size: 2.5rem; margin-bottom: 0.2rem; }
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

st.markdown('<h1 class="main-title">🚀 Componente Técnico-Financiero FarmaTech Ltda.</h1>', unsafe_allow_html=True)
st.markdown('<p class="section-desc">Punto 5 y 6: Modelado del Presupuesto de Inversión, Análisis de Sensibilidad y Cronograma de Ruta Crítica (2026)</p>', unsafe_allow_html=True)

# 2. BASE DE DATOS ESTRUCTURAL (Tabla 11 Oficial Cuadrada)
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

# Configuración universal para descarga de reportes e imágenes en Plotly (Cámara 📸 activa)
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

ticket_simulado = st.sidebar.slider("Ticket Promedio de Venta (COP)", min_value=35000, max_value=120000, value=55000, step=5000)
margen_simulado_pct = st.sidebar.slider("Margen de Contribución Neto (%)", min_value=15, max_value=50, value=30, step=5)

# Fórmulas de ingeniería financiera automatizadas
margen_pesos = ticket_simulado * (margen_simulado_pct / 100)
tx_punto_equilibrio = total_opex / margen_pesos
ingresos_minimos = tx_punto_equilibrio * ticket_simulado

# 4. SISTEMA DE NAVEGACIÓN EN PESTAÑAS (TABS UNIFICADOS)
tab_costos, tab_sensibilidad, tab_sensibilidad_3d, tab_cronograma = st.tabs([
    "📊 5.1 Estructura de Costos (OPEX)", 
    "📈 5.3 Curva de Sensibilidad 2D",
    "🛸 Modelado Espacial 3D",
    "📅 6.1 Cronograma de Ruta Crítica (Gantt)"
])

# =============================================================================
# PESTAÑA 1: ANALÍTICA DE COSTOS FIJOS (TABLA Y DONUT)
# =============================================================================
with tab_costos:
    st.subheader("📋 Matriz Mensual de Carga Fija Estructural")
    st.write("Desglose detallado de los gastos operativos fijos requeridos para sostener la operación física y omnicanal.")
    
    col_k1, col_k2 = st.columns(2)
    with col_k1:
        st.metric(label="📉 COSTO FIJO REQUERIDO (OPEX)", value=f"${total_opex:,.0f} COP", delta="Fijo Mensual Unificado")
    with col_k2:
        st.metric(label="🛡️ RESPALDO ASIGNADO (CAPEX)", value="$80,000,000 COP", delta="Fondo de Reserva de Caja")
        
    st.markdown("---")
    col_vis1, col_vis2 = st.columns(2)
    
    with col_vis1:
        st.markdown("**Desglose de Costos de Nómina e Infraestructura**")
        df_ui = df_opex.copy()
        df_ui["Monto Fijo"] = df_ui["Monto Fijo"].map("${:,.0f}".format)
        st.dataframe(df_ui, use_container_width=True, hide_index=True)
        
    with col_vis2:
        st.markdown("**Distribución Porcentual Sectorizada (Gráfico de Dona)**")
        fig_donut = px.pie(
            df_opex, values="Monto Fijo", names="Rubro Técnico", hole=0.45,
            color_discrete_sequence=px.colors.qualitative.Prism
        )
        fig_donut.update_traces(textposition='inside', textinfo='percent')
        fig_donut.update_layout(margin=dict(t=10, b=10, l=10, r=10), showlegend=False, height=380)
        st.plotly_chart(fig_donut, use_container_width=True, config=config_exportacion)

# =============================================================================
# PESTAÑA 2: CURVA DE ELASTICIDAD OPERATIVA (2D RECOMENDADO)
# =============================================================================
with tab_sensibilidad:
    st.subheader("📈 Curva de Sensibilidad Operativa (Análisis de Elasticidad)")
    st.write("Evaluación de la elasticidad inversa entre el valor del Ticket Promedio y el número de transacciones mensuales.")
    
    col_k3, col_k4, col_k5 = st.columns(3)
    with col_k3:
        st.metric(label="💰 Utilidad Bruta por Ticket", value=f"${margen_pesos:,.0f} COP")
    with col_k4:
        st.metric(label="🎯 Volumen Crítico de Transacciones", value=f"{tx_punto_equilibrio:,.0f} tx/mes", delta="Punto de Equilibrio")
    with col_k5:
        st.metric(label="📊 Ingreso Mínimo de Cobertura", value=f"${ingresos_minimos:,.0f} COP")
        
    st.markdown("---")
    
    tickets_curva = np.arange(35000, 125000, 5000)
    margenes_curva_pesos = tickets_curva * (margen_simulado_pct / 100)
    transacciones_curva = total_opex / margenes_curva_pesos

    fig_linea = go.Figure()
    fig_linea.add_trace(go.Scatter(
        x=tickets_curva, y=transacciones_curva, mode='lines+markers', name='Umbral de Equilibrio',
        line=dict(color='#1e3d59', width=3), marker=dict(size=6)
    ))
    fig_linea.add_trace(go.Scatter(
        x=[ticket_simulado], y=[tx_punto_equilibrio], mode='markers', name='Configuración Seleccionada',
        marker=dict(color='red', size=14, symbol='diamond', line=dict(color='white', width=2))
    ))
    fig_linea.update_layout(
        xaxis_title='Ticket Promedio de Venta (COP)', yaxis_title='Transacciones Requeridas al Mes (Cant.)',
        height=420, margin=dict(t=20, b=20, l=20, r=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig_linea, use_container_width=True, config=config_exportacion)

# =============================================================================
# PESTAÑA 3: MODELADO MATEMÁTICO TRIDIMENSIONAL (SCATTER 3D PREMIUM QUE SE MUEVE)
# =============================================================================
with tab_sensibilidad_3d:
    st.subheader("🛸 Simulación Espacial 3D Dinámica de Viabilidad")
    st.write("Usa el ratón para rotar, arrastrar y ampliar el espacio matemático. Modifica los sliders de la barra lateral para mover el diamante rojo.")
    
    np.random.seed(42)
    num_escenarios = 400
    tickets_sim = np.random.uniform(35000, 120000, num_escenarios)
    margenes_sim_pct = np.random.uniform(15, 50, num_escenarios)
    margenes_sim_pesos = tickets_sim * (margenes_sim_pct / 100)
    transacciones_sim = total_opex / margenes_sim_pesos

    df_3d = pd.DataFrame({'Ticket': tickets_sim, 'Margen_%': margenes_sim_pct, 'Transacciones': transacciones_sim})

    fig_3d = go.Figure()
    fig_3d.add_trace(go.Scatter3d(
        x=df_3d['Ticket'], y=df_3d['Margen_%'], z=df_3d['Transacciones'], mode='markers',
        marker=dict(size=4, color=df_3d['Transacciones'], colorscale='Viridis', opacity=0.6, colorbar=dict(title="Volumen de Tx", x=0)),
        name="Escenarios de Simulación"
    ))
    fig_3d.add_trace(go.Scatter3d(
        x=[ticket_simulado], y=[margen_simulado_pct], z=[tx_punto_equilibrio], mode='markers',
        marker=dict(size=12, color='red', symbol='diamond', line=dict(color='white', width=2)),
        name="Tu Configuración Hito"
    ))
    fig_3d.update_layout(
        scene=dict(xaxis_title='Ticket ($)', yaxis_title='Margen (%)', zaxis_title='Tx Requeridas'),
        margin=dict(t=10, b=10, l=10, r=10), height=500,
        legend=dict(orientation="h", yanchor="bottom", y=0.9, xanchor="center", x=0.5)
    )
    st.plotly_chart(fig_3d, use_container_width=True, config=config_exportacion)

# =============================================================================
# PESTAÑA 4: CRONOGRAMA DE GANTT (CORREGIDO SIN ERRORES DE TYPE)
# =============================================================================
with tab_cronograma:
    st.subheader("📅 Ruta Crítica de la Fase Preoperativa")
    st.write("Planificación temporal de actividades (Semanas 1 a 12). Haz clic en la cámara de la esquina superior derecha para guardarlo en tu informe.")
    
    cronograma_data = [
        {"Actividad": "1. Registro Cámara Comercio", "Inicio": 1, "Duracion": 1, "Fase": "Legal"},
        {"Actividad": "2. Contratación Regente (DT)", "Inicio": 1, "Duracion": 12, "Fase": "Personal"},
        {"Actividad": "3. Trámites Seccional de Salud", "Inicio": 2, "Duracion": 11, "Fase": "Legal"},
        {"Actividad": "4. Convenio Coopidrogas", "Inicio": 1, "Duracion": 3, "Fase": "Legal"},
        {"Actividad": "5. Obra Civil Adecuación Local", "Inicio": 3, "Duracion": 6, "Fase": "Infraestructura"},
        {"Actividad": "6. Instalación Cadena de Frío", "Inicio": 5, "Duracion": 3, "Fase": "Infraestructura"},
        {"Actividad": "7. Montaje de Estanterías", "Inicio": 6, "Duracion": 3, "Fase": "Infraestructura"},
        {"Actividad": "8. Implementación Sistema POS", "Inicio": 8, "Duracion": 3, "Fase": "Tecnología"},
        {"Actividad": "9. Contratación de Auxiliares", "Inicio": 9, "Duracion": 2, "Fase": "Personal"},
        {"Actividad": "10. Adquisición Flota Motos", "Inicio": 10, "Duracion": 2, "Fase": "Logística"},
        {"Actividad": "11. Carga de Inventario Inicial", "Inicio": 11, "Duracion": 2, "Fase": "Logística"},
        {"Actividad": "12. Lanzamiento y Capacitación", "Inicio": 11, "Duracion": 2, "Fase": "Comercial"}
    ]
    df_gantt_clean = pd.DataFrame(cronograma_data)

    # Reconstrucción nativa del Gantt usando barras de Plotly estables
    fig_gantt_final = go.Figure()
    
    # Mapeo de colores estéticos por categoría
    colores_fase = {"Legal": "#1e3d59", "Personal": "#ff7f0e", "Infraestructura": "#2ca02c", "Tecnología": "#9467bd", "Logística": "#d62728", "Comercial": "#bcbd22"}
    
    for idx, row in df_gantt_clean.iterrows():
        fig_gantt_final.add_trace(go.Bar(
            name=row["Fase"],
            x=[row["Duracion"]],
            y=[row["Actividad"]],
            orientation='h',
            base=row["Inicio"],
            marker=dict(color=colores_fase[row["Fase"]]),
            showlegend=False
        ))

    # Forzar leyenda agrupada única para no duplicar por actividad
    for fase, color in colores_fase.items():
        fig_gantt_final.add_trace(go.Scatter(x=[None], y=[None], mode='markers', marker=dict(size=10, color=color), name=fase))

    fig_gantt_final.update_layout(
        xaxis=dict(title="Línea de Tiempo (Semanas)", tickvals=list(range(1, 14)), ticktext=[f"Semana {i}" for i in range(1, 14)], range=[0.5, 13.5]),
        yaxis=dict(autorange="reversed", title=""),
        height=480, margin=dict(t=20, b=20, l=20, r=20),
        barmode='stack', legend=dict(orientation="h", yanchor="bottom", y=-0.22, xanchor="center", x=0.5)
    )
    st.plotly_chart(fig_gantt_final, use_container_width=True, config=config_exportacion)
