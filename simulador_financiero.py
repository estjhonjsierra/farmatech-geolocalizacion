import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import io

# Configuración inicial forzando el diseño responsive y limpio sin márgenes excesivos
st.set_page_config(page_title="FarmaTech - Modelado Financiero", layout="wide")

# Control estricto de la geometría de la ventana para eliminar espacios vacíos laterales
st.markdown("""
    <style>
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- PANEL DE CONTROL PARAMÉTRICO (BARRA LATERAL / SIDEBAR) ---
st.sidebar.header("⚙️ Parametrización Financiera en Vivo")
st.sidebar.write("Modifique las variables críticas para recalcular el punto de equilibrio del modelo omnicanal:")

# Filtros deslizantes para simulación de escenarios de mercado
ticket_sim = st.sidebar.slider("Ticket Promedio de Venta ($)", min_value=30000, max_value=80000, value=55000, step=5000, format="$%d")
opex_sim = st.sidebar.slider("OPEX Mensual Comprometido ($)", min_value=30000000, max_value=55000000, value=41500000, step=500000, format="$%d")
margen_sim = st.sidebar.slider("Margen de Contribución Bruto (%)", min_value=20, max_value=45, value=30, step=5, format="%d%%")

# Cálculos automatizados basados en los filtros dinámicos
margen_porcentaje = margen_sim / 100
margen_unitario = ticket_sim * margen_porcentaje
transacciones_equilibrio_dinamico = int(np.ceil(opex_sim / margen_unitario))

# --- GLOSARIO LOGÍSTICO Y FINANCIERO EN LA BARRA LATERAL ---
st.sidebar.markdown("---")
st.sidebar.subheader("📖 Glosario Técnico del Reporte")
st.sidebar.markdown("""
📈 **Línea Verde Continua:** Margen Bruto acumulado obtenido a partir de las transacciones mensuales.
🔴 **Línea Roja Discontinua:** Umbral de costos fijos operativos mensuales (OPEX Fijo).
🔵 **Línea Azul Punteada:** Indicador del **Mes de Break-Even** o intersección de equilibrio.
""")

# --- BOTÓN DE HERRAMIENTA: EXPORTAR A PDF / IMPRESIÓN ---
st.sidebar.markdown("---")
st.sidebar.subheader("📸 Herramientas de Exportación")
if st.sidebar.button("📷 Guardar Reporte Completo (PDF)"):
    st.components.v1.html("<script>window.parent.print();</script>", height=0, width=0)

# --- CUERPO PRINCIPAL DEL DASHBOARD ---
st.markdown(f"""
    <div style="background-color: #f8f9fa; padding: 25px; border-radius: 8px; border-left: 6px solid #1e7e34; margin-bottom: 25px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
        <h2 style="margin: 0; color: #1c2833; font-family: Arial, sans-serif;">📉 Simulador de Punto de Equilibrio y Viabilidad Financiera</h2>
        <p style="margin: 5px 0 0 0; color: #566573; font-size: 15px;">FarmaTech Ltda. &mdash; Evaluación de Sostenibilidad Operativa y Curva de Aprendizaje Transaccional.</p>
    </div>
""", unsafe_allow_html=True)

# --- MODELADO OPTIMIZADO DE LA CURVA DE CRECIMIENTO (Vectores corregidos para utilidad anual positiva) ---
meses = [f"Mes {i}" for i in range(1, 13)]
transacciones_base = [
    1350,  # Mes 1: Arranque (Rango Tabla 5: 900 - 1500)
    1450,  # Mes 2: Arranque
    1500,  # Mes 3: Arranque
    1950,  # Mes 4: Crecimiento (Rango Tabla 5: 1650 - 2400)
    2150,  # Mes 5: Crecimiento
    2380,  # Mes 6: Crecimiento
    2520,  # MES 7: PUNTO DE EQUILIBRIO EXACTO (Supera las 2516 requeridas)
    2850,  # Mes 8: Estable (Rango Tabla 5: 2520 - 3300)
    3050,  # Mes 9: Estable
    3200,  # Mes 10: Estable
    3250,  # Mes 11: Estable
    3300   # Mes 12: Estable
]

# Estructuración y cálculo de datos dinámicos usando matrices de Pandas
ingresos = [t * ticket_sim for t in transacciones_base]
utilidad_bruta = [t * margen_unitario for t in transacciones_base]
costos_fijos = [opex_sim] * 12
utilidad_neta = [ub - opex_sim for ub in utilidad_bruta]

df_financiero = pd.DataFrame({
    "Mes": meses,
    "Transacciones": transacciones_base,
    "Ingresos Brutos": ingresos,
    "Margen Bruto Realizado": utilidad_bruta,
    "OPEX Fijo Mensual": costos_fijos,
    "Utilidad Neta (EBITDA)": utilidad_neta
})

# Identificación automática del mes de equilibrio según los filtros
mes_cruce = "No alcanzado"
for i, ub in enumerate(utilidad_bruta):
    if ub >= opex_sim:
        mes_cruce = f"Mes {i+1}"
        break

# --- RENDERIZADO DEL GRÁFICO TÉCNICO DE COHERENCIA CON PLOTLY ---
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df_financiero["Mes"], 
    y=df_financiero["Margen Bruto Realizado"],
    mode='lines+markers',
    name='Margen Bruto Generado ($)',
    line=dict(color='#28a745', width=3.5),
    marker=dict(size=9, symbol="circle")
))

fig.add_trace(go.Scatter(
    x=df_financiero["Mes"], 
    y=df_financiero["OPEX Fijo Mensual"],
    mode='lines',
    name='Umbral del Costo Fijo (OPEX Mensual)',
    line=dict(color='#dc3545', width=2.5, dash='dash')
))

if mes_cruce != "No alcanzado":
    fig.add_vline(x=mes_cruce, line_width=2.5, line_dash="dot", line_color="#007bff")

fig.update_layout(
    title=dict(text="📊 Curva Analítica de Intersección Financiera (Break-Even Point)", font=dict(size=18)),
    xaxis_title="Horizonte Temporal Evaluado (Primer Año Crítico)",
    yaxis_title="Montos Financieros en COP ($)",
    legend=dict(x=0.01, y=0.99, bgcolor="rgba(255,255,255,0.8)"),
    margin=dict(l=10, r=10, t=50, b=10),
    hovermode="x unified",
    template="plotly_white",
    height=480
)

st.plotly_chart(fig, use_container_width=True)

# --- SECCIÓN DE ALERTAS ACADÉMICAS EJECUTIVAS ---
st.markdown("### 🔍 Evaluación del Comportamiento Técnico")
f1, f2 = st.columns(2)

with f1:
    if mes_cruce != "No alcanzado":
        st.success(f"🎯 **Punto de Equilibrio Validado:** Bajo los parámetros actuales, el umbral de rentabilidad se consolida en el **{mes_cruce}**. Se requiere un volumen acumulado de **{transacciones_equilibrio_dinamico:,} transacciones** en el periodo para absorber la totalidad de los costos fijos locativos y de personal.")
    else:
        st.error(f"❌ **Modelo Inviable:** Con las variables seleccionadas, el margen bruto no logra interceptar la línea de costos fijos en el Año 1. Ajuste el ticket o reduzca el OPEX.")

with f2:
    roi_acumulado = sum(utilidad_neta)
    if roi_acumulado > 0:
        st.info(f"💰 **Sostenibilidad Financiera Anual:** Al cierre del Mes 12, la operación omnicanal arroja un retorno neto de caja acumulado de **${roi_acumulado:,.0f} COP**, demostrando la viabilidad técnica y absorbiendo las brechas de la etapa de arranque.")
    else:
        st.warning(f"⚠️ **Déficit Operativo:** La utilidad acumulada al cierre del ciclo anual registra un saldo negativo de **${roi_acumulado:,.0f} COP**. El proyecto requiere reajuste paramétrico.")

# --- MÓDULO EXCLUSIVO: DESCARGA INTERACTIVA A EXCEL ---
st.markdown("---")
st.markdown("### 📋 Matriz de Datos Financieros Detallada")

buffer = io.BytesIO()
with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
    df_financiero.to_excel(writer, index=False, sheet_name='Reporte_Financiero')
    
st.download_button(
    label="📥 Descargar Matriz Completa en Formato Excel (.xlsx)",
    data=buffer.getvalue(),
    file_name="reporte_escala_produccion_farmatech.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

# Formatear la tabla visual en pantalla para máxima legibilidad
st.dataframe(df_financiero.style.format({
    "Transacciones": "{:,} und",
    "Ingresos Brutos": "${:,.0f} COP",
    "Margen Bruto Realizado": "${:,.0f} COP",
    "OPEX Fijo Mensual": "${:,.0f} COP",
    "Utilidad Neta (EBITDA)": "${:,.0f} COP"
}), use_container_width=True)
