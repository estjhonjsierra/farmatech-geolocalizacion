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
    .kpi-card { background-color: #ffffff; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-left: 5px solid #17a2b8; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🚀 FarmaTech Ltda. — Centro de Control Analítico Avanzado</h1>', unsafe_allow_html=True)
st.caption("Simulación Cuántica de Sensibilidad y Modelado de Costos Fijos Estructurales (OPEX 2026)")
st.markdown("---")

# 1. BASE DE DATOS ESTRUCTURAL (Tabla 11 Oficial)
data_opex = {
    "Rubro Técnico": [
        "Arrendamiento Local", "Nómina: Regente de Farmacia", "Nómina: 3 Auxiliares", 
        "Nómina: 1 Mensajero", "Servicios Públicos", "Póliza de Responsabilidad", 
        "Licenciamiento ERP", "Combustible Flota", "Marketing Digital", 
        "Insumos Bioseguridad", "Margen Imprevistos", "Fondo Reserva Capital"
    ],
    "Monto Fijo": [, 4500000, 6300000, 2100000, 1200000, 600000, 400000, 1200000, 2500000, 500000, 2000000, 15200000],
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
col_visual1, col_visual2 = st.columns([4, 5])

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
    fig_donut.update_layout(margin=dict(t=10, b=10, l=10, r=10), showlegend=False, height=350)
    st.plotly_chart(fig_donut, use_container_width=True)

st.markdown("---")

# 5. EL NIVEL SUPERIOR: MODELADO MATEMÁTICO TRIDIMENSIONAL (SCATTER 3D REALISTA)
st.subheader("🛸 Simulación Espacial 3D de Viabilidad Financiera")
st.write("Esta gráfica modela 500 escenarios combinando dinámicamente variaciones de Ticket, Margen y Transacciones. La esfera roja representa el estado actual seleccionado en tus controles.")

# Generación aleatoria controlada de escenarios matemáticos para simulación Montecarlo básica
np.random.seed(42)
num_escenarios = 500
tickets_sim = np.random.uniform(35000, 120000, num_escenarios)
margenes_sim_pct = np.random.uniform(15, 50, num_escenarios)
margenes_sim_pesos = tickets_sim * (margenes_sim_pct / 100)
transacciones_sim = total_opex / margenes_sim_pesos

# Creación de DataFrame de simulación espacial
df_3d = pd.DataFrame({
    'Ticket': tickets_sim,
    'Margen_%': margenes_sim_pct,
    'Transacciones': transacciones_sim
})

# Graficar el espacio 3D
fig_3d = go.Figure()

# Agregar nube de puntos de fondo (Escenarios hipotéticos)
fig_3d.add_trace(go.Scatter3d(
    x=df_3d['Ticket'],
    y=df_3d['Margen_%'],
    z=df_3d['Transacciones'],
    mode='markers',
    marker=dict(
        size=4,
        color=df_3d['Transacciones'],
        colorscale='Viridis',
        opacity=0.6,
        colorbar=dict(title="Volumen de Tx", x=0)
    ),
    name="Escenarios Virtuales"
))

# Agregar el punto actual (Hito FarmaTech en base a los Sliders)
fig_3d.add_trace(go.Scatter3d(
    x=[ticket_simulado],
    y=[margen_simulado_pct],
    z=[tx_punto_equilibrio],
    mode='markers',
    marker=dict(size=12, color='red', symbol='diamond', line=dict(color='white', width=2)),
    name="Tu Configuración Real"
))

fig_3d.update_layout(
    scene=dict(
        xaxis_title='Ticket Promedio ($)',
        yaxis_title='Margen Bruto (%)',
        zaxis_title='Tx de Equilibrio (Cant.)'
    ),
    margin=dict(t=20, b=20, l=20, r=20),
    height=550,
    legend=dict(orientation="h", yanchor="bottom", y=0.9, xanchor="center", x=0.5)
)

st.plotly_chart(fig_3d, use_container_width=True)
