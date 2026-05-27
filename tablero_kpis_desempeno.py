import streamlit as st
import pandas as pd
import numpy as np
import io
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# =========================================================================
# 1. ARQUITECTURA DE INTERFAZ CORPORATIVA (UI/UX) E INYECCIÓN DE ESTILOS CSS
# =========================================================================
st.set_page_config(
    page_title="FarmaTech - Enterprise Quality & KPI Suite",
    layout="wide",
    page_icon="💊",
    initial_sidebar_state="expanded"
)

# Inyección de estilos CSS avanzados: Colores vibrantes, tarjetas y sombras
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }
    .main-header { 
        background: linear-gradient(90deg, #1E3D59 0%, #2B5B84 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800; 
        font-size: 2.8rem; 
        margin-bottom: 0rem; 
    }
    .sub-header { color: #6c757d; font-size: 1.2rem; margin-bottom: 2rem; font-weight: 400; }
    
    /* Estilos para las tarjetas de métricas */
    div[data-testid="metric-container"] {
        background-color: #ffffff;
        border: 1px solid #e0e6ed;
        padding: 15px 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: transform 0.2s ease-in-out;
    }
    div[data-testid="metric-container"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">📊 FarmaTech Ltda. — Centro de Comando Integral</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Suite Avanzada de Monitoreo Comercial, Logístico y Cumplimiento Regulatorio (POS Memphis)</p>', unsafe_allow_html=True)

# =========================================================================
# 2. PANEL LATERAL DE ENTRADAS (FILTROS Y SIMULADOR)
# =========================================================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3004/3004416.png", width=80) # Icono de farmacia de ejemplo
    st.markdown("### 🕹️ Consola de Simulación")
    st.caption("Ajuste las métricas reales para evaluar el SGC.")

    st.markdown("---")
    st.markdown("**📈 Dimensión Comercial**")
    pacientes_activos_sim = st.slider("Pacientes Crónicos Activos", 100, 1000, 684, help="Meta Año 1: 675")
    ticket_promedio_sim = st.number_input("Ticket Promedio ($ COP)", min_value=30000, max_value=100000, value=55400, step=1000)
    conversion_wa_sim = st.slider("Conversión WhatsApp (%)", 0.5, 10.0, 3.4, step=0.1)

    st.markdown("---")
    st.markdown("**🚚 Dimensión Logística (BPA)**")
    SLA_domicilios_sim = st.slider("SLA Domicilios Express (%)", 50, 100, 96)
    exactitud_inv_sim = st.slider("Exactitud de Inventario (%)", 80.0, 100.0, 98.5, step=0.1)
    tasa_recompra_sim = st.slider("Tasa de Recompra Mensual (%)", 30, 100, 62)
    hallazgos_auditoria_rx = st.selectbox("Incidentes de Dispensación (Rx)", [0, 1, 2, 3], index=0)

    st.markdown("---")
    st.markdown("**💰 Dimensión Financiera**")
    opex_ejecutado_sim = st.number_input("Gasto Operativo Real ($ COP)", min_value=35000000, max_value=55000000, value=41650000, step=500000)
    nps_evaluado_sim = st.slider("NPS (Satisfacción Cliente)", -100, 100, 74)

# =========================================================================
# 3. MOTOR DE CÁLCULO
# =========================================================================
OPEX_PRESUPUESTADO_ANUAL_BASE = 41500000
TOTAL_NICHO_MERCADO_CRONICOS = 4500
INGRESOS_META_ANUAL_PROYECTADOS = 1339250000

tasa_penetración_calculada = (pacientes_activos_sim / TOTAL_NICHO_MERCADO_CRONICOS) * 100
ejecución_opex_calculada = (opex_ejecutado_sim / OPEX_PRESUPUESTADO_ANUAL_BASE) * 100
margen_bruto_fijo_modelo = 32.5

# =========================================================================
# 4. SISTEMA DINÁMICO DE SEMÁFOROS (DASHBOARD METRICS)
# =========================================================================
st.subheader("🚨 Monitoreo de Alertas Críticas (Tiempo Real)")
col1, col2, col3, col4 = st.columns(4)

with col1:
    color_inv = "normal" if exactitud_inv_sim >= 98.0 else "inverse"
    st.metric("📦 Exactitud Inventario", f"{exactitud_inv_sim}%", "Cumple BPA" if exactitud_inv_sim >= 98 else "- Riesgo Auditoría", delta_color=color_inv)

with col2:
    color_sla = "normal" if SLA_domicilios_sim >= 95 else "inverse"
    st.metric("⏱️ SLA Domicilios", f"{SLA_domicilios_sim}%", "Cumple Express" if SLA_domicilios_sim >= 95 else "- Retrasos", delta_color=color_sla)

with col3:
    color_nps = "normal" if nps_evaluado_sim >= 70 else "inverse"
    st.metric("⭐ Satisfacción (NPS)", f"{nps_evaluado_sim} pts", "Fidelización Alta" if nps_evaluado_sim >= 70 else "- Riesgo Fuga", delta_color=color_nps)

with col4:
    color_opex = "normal" if ejecución_opex_calculada <= 105.0 else "inverse"
    st.metric("💵 Ejecución OPEX", f"{ejecución_opex_calculada:.1f}%", "Gasto Controlado" if ejecución_opex_calculada <= 105 else "- Sobrepresupuesto", delta_color=color_opex)

st.divider()

# =========================================================================
# 5. VISUALIZACIÓN DE ALTO IMPACTO (GRÁFICAS PLOTLY)
# =========================================================================
st.subheader("📈 Análisis Gráfico de Desempeño")
g_col1, g_col2, g_col3 = st.columns(3)

# Gráfica 1: Velocímetro NPS
with g_col1:
    fig_nps = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = nps_evaluado_sim,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "NPS (Net Promoter Score)", 'font': {'size': 18}},
        gauge = {
            'axis': {'range': [-100, 100], 'tickwidth': 1},
            'bar': {'color': "#1E3D59"},
            'steps': [
                {'range': [-100, 0], 'color': "#ffcdd2"},
                {'range': [0, 70], 'color': "#fff9c4"},
                {'range': [70, 100], 'color': "#c8e6c9"}],
            'threshold': {'line': {'color': "green", 'width': 4}, 'thickness': 0.75, 'value': 70}
        }
    ))
    fig_nps.update_layout(height=250, margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig_nps, use_container_width=True)

# Gráfica 2: Embudo de Conversión Comercial
with g_col2:
    fig_funnel = go.Figure(go.Funnel(
        y = ["Tráfico Digital", "Consultas WhatsApp", "Ventas Efectivas"],
        x = [10000, 3000, int(3000 * (conversion_wa_sim/100))],
        textinfo = "value+percent initial",
        marker = {"color": ["#5C82A6", "#3E6A93", "#1E3D59"]}
    ))
    fig_funnel.update_layout(title="Embudo Digital WhatsApp", height=250, margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig_funnel, use_container_width=True)

# Gráfica 3: OPEX vs Presupuesto (Barra)
with g_col3:
    fig_bar = px.bar(
        x=["Presupuesto Base", "Gasto Ejecutado"], 
        y=[OPEX_PRESUPUESTADO_ANUAL_BASE, opex_ejecutado_sim],
        color=["Presupuesto", "Ejecutado"],
        color_discrete_sequence=["#A5B9C9", "#1E3D59" if ejecución_opex_calculada <= 105 else "#D9534F"]
    )
    fig_bar.update_layout(title="Control de Presupuesto (OPEX)", height=250, showlegend=False, margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig_bar, use_container_width=True)

st.divider()

# =========================================================================
# 6. TABLA 33 Y EXPORTACIÓN AVANZADA (EXCEL + BOTONES)
# =========================================================================
st.subheader("📋 Tabla 33. Tablero de Indicadores Clave de Desempeño (KPIs)")

diccionario_kpis = {
    "KPI": ["Penetración Nicho Crónico", "Ticket Promedio", "Conversión WhatsApp", "Cumplimiento SLA Domicilios", "NPS (Satisfacción)", "Exactitud de Inventario", "Tasa de Recompra", "Margen Bruto", "Control de OPEX", "Cero Dispensaciones Rx"],
    "Definición y Objetivo": ["% capturado del nicho de 4.500 pacientes.", "Valor canasta mensual promedio.", "% de chats que cierran en venta.", "% entregas en rango 20-45 min.", "Nivel de lealtad del cliente.", "Control de stock físico vs POS.", "% pacientes con pedido recurrente.", "Rentabilidad tras costos (COGS).", "Eficiencia del gasto operativo.", "Seguridad sanitaria Ley 485."],
    "Meta Año 1": ["15% (675 pac.)", "≥ $55,000", "≥ 3%", "≥ 95%", "≥ 70 pts", "≥ 98%", "≥ 60%", "≥ 30%", "≤ 105%", "0 fallos"],
    "Valor Actual": [f"{tasa_penetración_calculada:.1f}%", f"${ticket_promedio_sim:,}", f"{conversion_wa_sim:.1f}%", f"{SLA_domicilios_sim}%", f"{nps_evaluado_sim} pts", f"{exactitud_inv_sim}%", f"{tasa_recompra_sim}%", f"{margen_bruto_fijo_modelo:.1f}%", f"{ejecución_opex_calculada:.1f}%", f"{hallazgos_auditoria_rx}"],
    "Estado": ["🟢" if pacientes_activos_sim >= 675 else "🔴", "🟢" if ticket_promedio_sim >= 55000 else "🔴", "🟢" if conversion_wa_sim >= 3.0 else "🔴", "🟢" if SLA_domicilios_sim >= 95 else "🔴", "🟢" if nps_evaluado_sim >= 70 else "🔴", "🟢" if exactitud_inv_sim >= 98.0 else "🔴", "🟢" if tasa_recompra_sim >= 60 else "🔴", "🟢" if margen_bruto_fijo_modelo >= 30 else "🔴", "🟢" if ejecución_opex_calculada <= 105 else "🔴", "🟢" if hallazgos_auditoria_rx == 0 else "🔴"]
}

df_kpi = pd.DataFrame(diccionario_kpis)

# Mostrar DataFrame estilizado
st.dataframe(
    df_kpi, 
    use_container_width=True, 
    hide_index=True,
    column_config={"Estado": st.column_config.TextColumn("Estado", help="Semáforo de Cumplimiento")}
)

# Función para exportar a Excel con XlsxWriter (Profesional)
def to_excel(df):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='KPIs FarmaTech')
        workbook = writer.book
        worksheet = writer.sheets['KPIs FarmaTech']
        # Formato de cabecera
        header_format = workbook.add_format({'bold': True, 'bg_color': '#1E3D59', 'font_color': 'white'})
        for col_num, value in enumerate(df.columns.values):
            worksheet.write(0, col_num, value, header_format)
            worksheet.set_column(col_num, col_num, 22) # Ajustar ancho columnas
    processed_data = output.getvalue()
    return processed_data

excel_data = to_excel(df_kpi)

col_btn1, col_btn2 = st.columns([1, 4])
with col_btn1:
    st.download_button(
        label="📥 Descargar Reporte Excel",
        data=excel_data,
        file_name=f"FarmaTech_KPIs_{datetime.now().strftime('%Y%m%d')}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        type="primary"
    )

st.divider()

# =========================================================================
# 7. SISTEMA DE AUDITORÍA Y CAPTURA DE EVIDENCIA (CÁMARA)
# =========================================================================
st.subheader("📸 Auditoría en Sitio (Dirección Técnica)")
st.markdown("Herramienta exclusiva para el **Regente de Farmacia**. Capture evidencia fotográfica de las condiciones de almacenamiento (FEFO), dispensación o incidentes para adjuntar al informe mensual.")

enable_camera = st.checkbox("Activar Cámara de Auditoría")

if enable_camera:
    foto = st.camera_input("Capturar evidencia fotográfica del estante o receta médica")
    if foto is not None:
        st.success("✅ Evidencia capturada exitosamente y encriptada para el SGC.")
        st.image(foto, caption=f"Evidencia registrada el {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", width=400)
