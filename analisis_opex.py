import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# Configuración de página de alta definición (Premium UI)
st.set_page_config(page_title="FarmaTech Advanced Dashboard", layout="wide", page_icon="💊")

# Estilos CSS inyectados para simular una plataforma de software real
st.markdown("""
    <style>
    .reportview-container { background: #f8f9fa; }
    .main-title { font-family: 'Helvetica Neue', Arial, sans-serif; color: #1e3d59; font-weight: 800; font-size: 2.8rem; margin-bottom: 0.5rem; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🚀 FarmaTech Ltda. — Centro de Control Analítico Avanzado</h1>', unsafe_allow_html=True)
st.caption("Simulación de Sensibilidad y Modelado de Costos Fijos Estructurales (OPEX 2026)")
st.markdown("---")

# 1. BASE DE DATOS ESTRUCTURAL (Tabla 11 Oficial)
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

# 2. SECCIÓN DE CONTROLES FLOTANTES EN LA BARRA LATERAL (SIDEBAR)
st.sidebar.header("🎛️ Variables Macroeconómicas")
st.sidebar.markdown("Modifica los parámetros para estresar el modelo financiero en tiempo real.")

ticket_simulado = st.sidebar.slider("Ticket Promedio de Venta (COP)", min_value=35000, max_value=120000, value=55000, step=5000)
margen_simulado_pct = st.sidebar.slider("Margen de Contribución Neto (%)", min_value=15, max_value=50, value=30, step=5)

# Cálculos financieros inmediatos
margen_pesos = ticket_simulado * (margen_simulado_pct / 100)
tx_punto_equilibrio = total_opex / margen_pesos
ingresos_minimos = tx_punto_equilibrio * ticket_simulado

# 3. FILA DE INDICADORES EN TIEMPO REAL (KPIs)
col_kpi1, col_kpi2, col_kpi3, col_kpi4 = st.columns(4)

with col_kpi1:
    st.metric(label="📉 Costo Fijo (OPEX)", value=f"${total_opex:,.0f} COP", delta="Fijo Mensual")
with col_kpi2:
    st.metric(label="💰 Margen por Transacción", value=f"${margen_pesos:,.0f} COP", delta=f"{margen_simulado_pct}% Pactado")
with col_kpi3:
    st.metric(label="🎯 Meta transaccional Mes 7", value=f"{tx_punto_equilibrio:,.0f} Tx", delta="Punto de Equilibrio", delta_color="inverse")
with col_kpi4:
    st.metric(label="📊 Ingreso Mínimo de Cobertura", value=f"${ingresos_minimos:,.0f} COP", delta="Para Sostenibilidad")

st.markdown("---")

# 4. DISTRIBUCIÓN AVANZADA EN DOS COLUMNAS (TABLA VS GRÁFICO DONUT PREMIUM)
col_visual1, col_visual2 = st.columns(2)

with col_visual1:
    st.subheader("📋 Desglose de la Carga Fija")
    df_ui = df_opex.copy()
    df_ui["Monto Fijo"] = df_ui["Monto Fijo"].map("${:,.0f}".format)
    st.dataframe(df_ui, use_container_width=True, hide_index=True)

with col_visual2:
    st.subheader("🍩 Análisis Sectorial del Gasto")
    fig_donut = px.pie(
        df_opex, 
        values="Monto Fijo", 
        names="Rubro Técnico", 
        hole=0.45,
        color_discrete_sequence=px.colors.qualitative.Prism
    )
    fig_donut.update_traces(textposition='inside', textinfo='percent')
    fig_donut.update_layout(
        margin=dict(t=10, b=10, l=10, r=10), 
        showlegend=False, 
        height=350
    )
    # Habilitar barra de herramientas para descarga de imagen
    st.plotly_chart(fig_donut, use_container_width=True, config={'displayModeBar': True})

st.markdown("---")

# 5. NUEVO GRÁFICO RECOMENDADO: CURVA DE SENSIBILIDAD 2D TRADICIONAL ACADÉMICA
st.subheader("📈 Curva de Sensibilidad Operativa (Análisis de Elasticidad)")
st.write("El siguiente gráfico de dos dimensiones modela cuántas transacciones requiere el negocio según se mueva el Ticket Promedio. Usa la cámara de la esquina superior derecha del gráfico para exportar la captura de pantalla directa a tu informe.")

# Generar datos secuenciales para la curva lineal
tickets_curva = np.arange(35000, 125000, 5000)
margenes_curva_pesos = tickets_curva * (margen_simulado_pct / 100)
transacciones_curva = total_opex / margenes_curva_pesos

# Construir el gráfico de líneas premium
fig_linea = go.Figure()

# Línea general de comportamiento del mercado
fig_linea.add_trace(go.Scatter(
    x=tickets_curva,
    y=transacciones_curva,
    mode='lines+markers',
    name='Umbral de Equilibrio',
    line=dict(color='#1e3d59', width=3),
    marker=dict(size=6)
))

# Punto exacto seleccionado por el usuario en la barra lateral
fig_linea.add_trace(go.Scatter(
    x=[ticket_simulado],
    y=[tx_punto_equilibrio],
    mode='markers',
    name='Tu Configuración Actual',
    marker=dict(color='red', size=14, symbol='diamond', line=dict(color='white', width=2))
))

# Ajustes de etiquetas y diseño del gráfico lineal
fig_linea.update_layout(
    xaxis_title='Ticket Promedio de Venta (COP)',
    yaxis_title='Transacciones Requeridas al Mes (Cant.)',
    height=450,
    margin=dict(t=20, b=20, l=20, r=20),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

# Renderizar el gráfico con la barra de herramientas forzada para captura de imagen
st.plotly_chart(fig_linea, use_container_width=True, config={
    'displayModeBar': True,
    'toImageButtonOptions': {
        'format': 'png',
        'filename': 'farmatech_sensibilidad_equilibrio',
        'height': 600,
        'width': 1000,
        'scale': 2
    }
})
