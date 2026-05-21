import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# 1. CONFIGURACIÓN PREMIUM DE LA INTERFAZ DE USUARIO
st.set_page_config(
    page_title="FarmaTech - Proyección de Ingresos",
    layout="wide",
    page_icon="💰"
)

# Inyección de estilos CSS Corporativos
st.markdown("""
    <style>
    .main-title { font-family: 'Helvetica Neue', Arial, sans-serif; color: #1e3d59; font-weight: 800; font-size: 2.4rem; margin-bottom: 0.2rem; }
    .section-desc { color: #6c757d; font-size: 1.05rem; margin-bottom: 1.5rem; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🚀 Tabla 15. Proyección de ingresos y punto de equilibrio — FarmaTech Ltda. (Meses 1 a 12)</h1>', unsafe_allow_html=True)
st.markdown('<p class="section-desc">Módulo de Analítica Financiera y Modelado Estructural de Sostenibilidad</p>', unsafe_allow_html=True)
st.markdown("---")

# 2. DEFINICIÓN DE LA BASE DE DATOS DEL OPEX FIJO (Tabla 11)
data_opex = {
    "Rubro": ["Arrendamiento", "Nómina Regente", "Nómina Auxiliares", "Nómina Mensajero", "Servicios", "Seguros", "ERP", "Combustible", "Marketing", "Bioseguridad", "Imprevistos", "Fondo Reserva"],
    "Monto": [5000000, 4500000, 6300000, 2100000, 1200000, 600000, 400000, 1200000, 2500000, 500000, 2000000, 15200000]
}
opex_fijo = sum(data_opex["Monto"])

# Configuración universal para descarga de reportes (Cámara 📸 activa)
config_exportacion = {
    'displayModeBar': True,
    'toImageButtonOptions': {
        'format': 'png',
        'filename': 'farmatech_grafico_financiero',
        'height': 600,
        'width': 1100,
        'scale': 2
    }
}

# 3. BARRA LATERAL DE CONTROLES (SIDEBAR)
st.sidebar.header("🎛️ Parámetros Base del Negocio")
ticket_std = st.sidebar.slider("Ticket Promedio de Venta (COP)", min_value=35000, max_value=120000, value=55000, step=5000)
margen_std_pct = st.sidebar.slider("Margen Bruto Compartido (%)", min_value=15, max_value=50, value=30, step=5)

# 4. CONSTRUCCIÓN DE LA MATRIZ DINÁMICA DE LA TABLA 15 REAL
meses = ["Mes 1", "Mes 2", "Mes 3", "Mes 4", "Mes 5", "Mes 6", "Mes 7 ★ EQUILIBRIO", "Mes 12"]
clientes = [300, 450, 675, 850, 1050, 1200, 1260, 1350]
transacciones = [600, 900, 1350, 1700, 2100, 2400, 2520, 2700]

ingresos_calculados = [tx * ticket_std for tx in transacciones]
margen_bruto_calculado = [ing * (margen_std_pct / 100) for ing in ingresos_calculados]
opex_fijo_lista = [opex_fijo] * len(meses)
utilidad_mensual = [margen - opex for margen, opex in zip(margen_bruto_calculado, opex_fijo_lista)]

# Crear DataFrame oficial
df_tabla15 = pd.DataFrame({
    "Mes": meses,
    "Clientes Activos": clientes,
    "Transacc./mes": transacciones,
    "Ingresos (COP)": ingresos_calculados,
    "OPEX Fijo (COP)": opex_fijo_lista,
    "Margen Bruto (COP)": margen_bruto_calculado,
    "Utilidad Mensual (COP)": utilidad_mensual
})

# 5. DESPLIEGUE DE INDICADORES EN TIEMPO REAL
col_t1, col_t2, col_t3 = st.columns(3)
with col_t1:
    st.metric(label="📉 Carga OPEX Fijo Ancla", value=f"${opex_fijo:,.0f} COP")
with col_t2:
    st.metric(label="🎯 Ingreso Requerido Mes 7", value=f"${df_tabla15.iloc[6]['Ingresos (COP)']:,.0f} COP")
with col_t3:
    st.metric(label="🟩 Margen Operativo Mes 7", value=f"${df_tabla15.iloc[6]['Margen Bruto (COP)']:,.0f} COP")

st.markdown("---")

# 6. RENDERIZACIÓN DE LA TABLA 15 REVISADA
st.subheader("📋 Matriz de Planificación de Caja e Ingresos (Año 1)")
df_format = df_tabla15.copy()
for col in ["Ingresos (COP)", "OPEX Fijo (COP)", "Margen Bruto (COP)", "Utilidad Mensual (COP)"]:
    df_format[col] = df_format[col].map("${:,.0f}".format)

st.dataframe(df_format, use_container_width=True, hide_index=True)

st.markdown("""
> **Nota técnica de viabilidad operativa:** El cumplimiento del punto de equilibrio en el Mes 7 requiere procesar 2.520 transacciones mensuales. 
Esta meta es coherente con la capacidad técnica instalada de 3 módulos de despacho simultáneo en el mostrador principal y el soporte de 3 motocicletas para la flota de última milla. 
Asimismo, el volumen de ventas proyectado para el equilibrio representa solo una fracción de la brecha de mercado de $5.895 millones anuales identificada en el sector Laureles-Estadio.
""")

st.markdown("---")

# 7. GENERACIÓN DEL GRÁFICO 2D DE CURVA DE COMPORTAMIENTO FINANCIERO
st.subheader("📈 Visualización Comercial del Ciclo de Rampa")

fig_break = go.Figure()
# Línea de Costo Fijo
fig_break.add_trace(go.Scatter(
    x=df_tabla15["Mes"], y=df_tabla15["OPEX Fijo (COP)"],
    mode='lines', name='OPEX Fijo Mensual ($41.5M)',
    line=dict(color='red', width=2, dash='dash')
))
# Línea de Margen Bruto Real
fig_break.add_trace(go.Scatter(
    x=df_tabla15["Mes"], y=df_tabla15["Margen Bruto (COP)"],
    mode='lines+markers', name='Margen Bruto Generado (30%)',
    line=dict(color='green', width=3), marker=dict(size=8)
))

fig_break.update_layout(
    xaxis_title='Evolución Cronológica del Proyecto',
    yaxis_title='Flujo de Caja Mensual (COP)',
    height=450, margin=dict(t=20, b=20, l=20, r=20),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)
)

st.plotly_chart(fig_break, use_container_width=True, config=config_exportacion)

