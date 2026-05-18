import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Título de la sección financiera en Streamlit
st.markdown("---")
st.header("📉 Simulador Financiero Interactiva y Gráfico de Break-Even")
st.write("Visualización dinámica de la curva de aprendizaje transaccional y el umbral de rentabilidad mes a mes.")

# --- PARÁMETROS FIJOS DEL PROYECTO (COHERENCIA TOTAL) ---
opex_fijo = 41500000       # $41.5M COP mensuales
ticket_promedio = 55000    # $55.000 COP por venta
margen_porcentaje = 0.30   # 30% de Margen Bruto
margen_unitario = ticket_promedio * margen_porcentaje # $16.500 COP netos por transacción

# Punto de equilibrio teórico exacto: 2516 transacciones
transacciones_equilibrio = int(np.ceil(opex_fijo / margen_unitario))

# --- MODELADO DE CRECIMIENTO REALISTA POR MESES (Curva de Aprendizaje) ---
# Definimos las transacciones mensuales promedio basadas en los rangos de tu Tabla 5
meses = [f"Mes {i}" for i in range(1, 13)]
transacciones_proyectadas = [
    1100,  # Mes 1: Fase Arranque (Rango 900 - 1500)
    1300,  # Mes 2: Fase Arranque
    1500,  # Mes 3: Fase Arranque
    1750,  # Mes 4: Fase Crecimiento (Rango 1650 - 2400)
    2000,  # Mes 5: Fase Crecimiento
    2300,  # Mes 6: Fase Crecimiento
    2520,  # MES 7: CRUCE DEL PUNTO DE EQUILIBRIO (Supera las 2516 exactas)
    2700,  # Mes 8: Fase Estable (Rango 2520 - 3300)
    2900,  # Mes 9: Fase Estable
    3050,  # Mes 10: Fase Estable
    3200,  # Mes 11: Fase Estable
    3300   # Mes 12: Fase Estable
]

# --- CÁLCULO DE MATRICES FINANCIERAS CON PANDAS ---
ingresos = [t * ticket_promedio for t in transacciones_proyectadas]
utilidad_bruta = [t * margen_unitario for t in transacciones_proyectadas]
costos_fijos = [opex_fijo] * 12
utilidad_neta = [ub - opex_fijo for ub in utilidad_bruta]

# Creación del DataFrame de soporte
df_financiero = pd.DataFrame({
    "Mes": meses,
    "Transacciones": transacciones_proyectadas,
    "Ingresos Brutos": ingresos,
    "Margen Bruto (30%)": utilidad_bruta,
    "OPEX Fijo (Costos)": costos_fijos,
    "Utilidad Neta (EBITDA)": utilidad_neta
})

# --- CONSTRUCCIÓN DEL GRÁFICO DE INTERSECCIÓN CON PLOTLY ---
fig = go.Figure()

# Línea del Margen Bruto generado
fig.add_trace(go.Scatter(
    x=df_financiero["Mes"], 
    y=df_financiero["Margen Bruto (30%)"],
    mode='lines+markers',
    name='Margen Bruto Generado ($)',
    line=dict(color='#28a745', width=3),
    marker=dict(size=8)
))

# Línea base horizontal del OPEX fijo mensual
fig.add_trace(go.Scatter(
    x=df_financiero["Mes"], 
    y=df_financiero["OPEX Fijo (Costos)"],
    mode='lines',
    name='Umbral del Costo Fijo (OPEX Mensual)',
    line=dict(color='#dc3545', width=2, dash='dash')
))

# Sombreado de zonas operativas (Rojo para pérdidas, Verde para ganancias)
fig.add_vline(x="Mes 7", line_width=2, line_dash="dot", line_color="blue")

fig.update_layout(
    title="📈 Gráfico Técnico de Break-Even (Punto de Equilibrio al Mes 7)",
    xaxis_title="Evolución en el Horizonte de Tiempo (Primer Año de Operación)",
    yaxis_title="Montos Financieros en COP ($)",
    legend=dict(x=0.02, y=0.98),
    margin=dict(l=40, r=40, t=60, b=40),
    hovermode="x unified",
    height=500
)

# Renderizado del gráfico interactivo en Streamlit
st.plotly_chart(fig, use_container_width=True)

# --- PANEL DE ALERTAS EJECUTIVAS DIGITALES ---
st.markdown("### 🔍 Análisis Estadístico de la Proyección")
f1, f2 = st.columns(2)

with f1:
    st.success(f"🎯 **Punto de Equilibrio Alcanzado:** En el **Mes 7**, la droguería consolida **{transacciones_proyectadas[6]} transacciones**, superando la barrera técnica mínima de las **{transacciones_equilibrio} operaciones** requeridas para cubrir los gastos locativos y de nómina.")

with f2:
    roi_acumulado = sum(utilidad_neta)
    if roi_acumulado > 0:
        st.info(f"💰 **Retorno del Primer Año:** Al cierre del Mes 12, el modelo omnicanal genera una utilidad operativa acumulada neta de **${roi_acumulado:,.0f} COP**, absorbiendo las pérdidas de la etapa de arranque (Meses 1 a 6).")
    else:
        st.warning(f"⚠️ **Atención:** Revisar estructura de costos.")

# Mostrar la tabla de datos procesada por Pandas si el usuario lo desea
if st.checkbox("📋 Visualizar Matriz de Datos Financieros Detallada"):
    st.dataframe(df_financiero.style.format({
        "Ingresos Brutos": "${:,.0f} COP",
        "Margen Bruto (30%)": "${:,.0f} COP",
        "OPEX Fijo (Costos)": "${:,.0f} COP",
        "Utilidad Neta (EBITDA)": "${:,.0f} COP"
    }), use_container_width=True)

