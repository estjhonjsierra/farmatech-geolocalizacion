import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="FarmaTech - Análisis OPEX", layout="wide")
st.title("📊 Estructura de Costos Fijos Mensuales (OPEX) — FarmaTech Ltda.")

data_opex = {
    "Rubro de Costo Fijo": [
        "Arrendamiento Local", "Nómina: Regente de Farmacia", "Nómina: 3 Auxiliares", 
        "Nómina: 1 Mensajero", "Servicios Públicos e Internet", "Póliza de Responsabilidad", 
        "Licenciamiento ERP (Memphis)", "Combustible y Rodamiento", "Pauta y Marketing Digital", 
        "Insumos Bioseguridad y MPGIRH", "Margen para Imprevistos", "Fondo de Reserva de Capital"
    ],
    "Monto Mensual (COP)": [
        5000000, 4500000, 6300000, 2100000, 1200000, 600000, 
        400000, 1200000, 2500000, 500000, 2000000, 15200000
    ]
}

df_opex = pd.DataFrame(data_opex)
opex_total = df_opex["Monto Mensual (COP)"].sum()

col_izq, col_der = st.columns(2)
with col_izq:
    st.subheader("📋 Matriz de Costos Fijos")
    df_mostrar = df_opex.copy()
    df_mostrar["Monto Mensual (COP)"] = df_mostrar["Monto Mensual (COP)"].map("${:,.0f}".format)
    st.dataframe(df_mostrar, use_container_width=True, hide_index=True)
    st.metric(label="TOTAL OPEX MENSUAL UNIFICADO", value=f"${opex_total:,.0f} COP")

with col_der:
    st.subheader("🍰 Distribución Porcentual del Gasto Fijo")
    fig_pie = go.Figure(data=[go.Pie(
        labels=df_opex["Rubro de Costo Fijo"], 
        values=df_opex["Monto Mensual (COP)"], 
        hole=.4
    )])
    st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("---")
st.subheader("🎛️ Simulador Dinámico de Sensibilidad Financiera")
col_sim1, col_sim2 = st.columns(2)
with col_sim1:
    ticket_promedio = st.slider("Ticket Promedio de Venta (COP)", min_value=30000, max_value=120000, value=55000, step=5000)
with col_sim2:
    margen_bruto_pct = st.slider("Margen de Contribución Unitario (%)", min_value=15, max_value=50, value=30, step=5)

margen_pesos = ticket_promedio * (margen_bruto_pct / 100)
transacciones_necesarias = opex_total / margen_pesos

st.markdown("### 🎯 Resultados de la Simulación")
col_res1, col_res2 = st.columns(2)
with col_res1:
    st.metric(label="Margen Bruto de Utilidad por Ticket", value=f"${margen_pesos:,.0f} COP")
with col_res2:
    st.metric(label="Transacciones Mensuales de Equilibrio", value=f"{transacciones_necesarias:,.0f} tx")

