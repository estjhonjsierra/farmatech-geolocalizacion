import streamlit as st
import pandas as pd
import numpy as np
import io
import plotly.graph_objects as go
from datetime import datetime

# =========================================================================
# 1. ARQUITECTURA DE INTERFAZ CORPORATIVA (UI/UX) E INYECCIÓN DE ESTILOS CSS
# =========================================================================
st.set_page_config(
    page_title="FarmaTech - Enterprise Quality & KPI Suite",
    layout="wide",
    page_icon="📊",
    initial_sidebar_state="expanded"
)

# Inyección de estilos CSS avanzados para maquetación web responsiva y optimización estricta de impresión PDF
st.markdown("""
<style>
    @import url('https://googleapis.com');
    
    html, body, [data-testid="stSidebar"] { font-family: 'Segoe UI', sans-serif; }
    .main-header { color: #1E3D59; font-weight: 800; font-size: 2.5rem; margin-bottom: 0.1rem; letter-spacing: -0.5px; }
    .sub-header { color: #555555; font-size: 1.15rem; margin-bottom: 2rem; font-weight: 400; }
    .status-panel { background-color: #F8F9FA; border-radius: 12px; padding: 25px; border: 1px solid #E9ECEF; margin-bottom: 25px; }
    .pdf-only-header { display: none; }
    
    @media print {
        .stSidebar, div[data-testid="stSidebarCollapseButton"], button, .stCheckbox, [data-testid="stBorder"] { display: none !important; }
        .main { width: 100% !important; padding: 0 !important; }
        .main-header { color: #000000 !important; font-size: 2.1rem; }
        .pdf-only-header { display: block !important; font-family: 'Segoe UI', sans-serif; font-size: 0.9rem; color: #222222; border-bottom: 3px solid #1E3D59; padding-bottom: 8px; margin-bottom: 35px; }
    }
</style>
""", unsafe_allow_html=True)

# Encabezado corporativo estructurado visible únicamente al exportar a PDF (Ctrl + P o Cmd + P)
st.markdown(f"""
<div class="pdf-only-header">
    <table style="width:100%; border-collapse:collapse;">
        <tr>
            <td style="text-align:left; font-weight:bold; font-size:1.2rem; color:#1E3D59;">FARMATECH LTDA. — INFORME CENTRAL DE CALIDAD E INDICADORES</td>
            <td style="text-align:right; font-weight:600; color:#1E3D59;">SGC — SECCIÓN 7.3</td>
        </tr>
        <tr>
            <td style="text-align:left; color:#555;">Cuadro de Mando Integral Automatizado (Metodología PHVA)</td>
            <td style="text-align:right; color:#555;">Fecha de Reporte: {datetime.now().strftime('%d/%m/%Y')}</td>
        </tr>
    </table>
</div>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">📊 FarmaTech Ltda. — Cuadro de Mando Integral (KPIs)</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Suite Avanzada de Automatización Comercial, Monitoreo de Procesos Críticos e Integración del POS Memphis</p>', unsafe_allow_html=True)
st.divider()

# =========================================================================
# 2. PANEL LATERAL DE ENTRADAS (FILTROS AVANZADOS Y SIMULADOR DE HARDWARE)
# =========================================================================
st.sidebar.markdown("### 🕹️ Consola de Control de Calidad")
st.sidebar.caption("Sincronice las métricas reales para evaluar las alertas del SGC frente a las metas del Año 1.")

st.sidebar.markdown("---")
st.sidebar.markdown("**📈 Dimensión Comercial y Ventas**")
pacientes_activos_sim = st.sidebar.slider("Pacientes Crónicos Activos en base", 100, 1000, 684, help="Meta Año 1: 675 pacientes")
ticket_promedio_sim = st.sidebar.number_input("Ticket Promedio de Transacción (\$ COP)", min_value=30000, max_value=100000, value=55400, step=200)
conversion_wa_sim = st.sidebar.slider("Tasa de Conversión de Canales Digitales (%)", 0.5, 10.0, 3.4, step=0.1)

st.sidebar.markdown("---")
st.sidebar.markdown("**🚚 Dimensión Logística y Operativa (BPA)**")
SLA_domicilios_sim = st.sidebar.slider("Eficiencia de SLA Express (<45 min)", 50, 100, 96)
exactitud_inv_sim = st.sidebar.slider("Exactitud de Inventario Físico vs POS", 80.0, 100.0, 98.5, step=0.1)
tasa_recompra_sim = st.sidebar.slider("Tasa de Recompra Mensual de Crónicos", 30, 100, 62)
hallazgos_auditoria_rx = st.sidebar.selectbox("Incidentes de Dispensación detectados (Rx)", [0, 1, 2, 3], index=0)

st.sidebar.markdown("---")
st.sidebar.markdown("**💰 Dimensión Presupuestal y Financiera**")
opex_ejecutado_sim = st.sidebar.number_input("Gasto Operativo Mensual Real (\$ COP)", min_value=35000000, max_value=55000000, value=41650000, step=50000)
nps_evaluado_sim = st.sidebar.slider("Indicador de Fidelidad del Cliente (NPS)", -100, 100, 74)

# =========================================================================
# 3. MOTOR DE CÁLCULO LOGÍSTICO Y FINANCIERO AVANZADO
# =========================================================================
OPEX_PRESUPUESTADO_ANUAL_BASE = 41500000
TOTAL_NICHO_MERCADO_CRONICOS = 4500
INGRESOS_META_ANUAL_PROYECTADOS = 1339250000

# Cálculos dinámicos con base en las entradas analíticas
tasa_penetración_calculada = (pacientes_activos_sim / TOTAL_NICHO_MERCADO_CRONICOS) * 100
ejecución_opex_calculada = (opex_ejecutado_sim / OPEX_PRESUPUESTADO_ANUAL_BASE) * 100
margen_bruto_fijo_modelo = 30.0

# =========================================================================
# 4. SISTEMA DINÁMICO DE SEMÁFOROS (DASHBOARD METRICS)
# =========================================================================
st.subheader("🚨 Monitoreo en Tiempo Real de Alertas y Semáforos Críticos")
col_card1, col_card2, col_card3, col_card4 = st.columns(4)

with col_card1:
    color_inventario = "normal" if exactitud_inv_sim >= 98.0 else "inverse"
    st.metric("Exactitud Inventario (Meta: ≥98%)", f"{exactitud_inv_sim}%", f"{'Conforme Estándar BPA' if exactitud_inv_sim >= 98.0 else 'Alerta: Desfase Crítico'}", delta_color=color_inventario)

with col_card2:
    color_domicilios = "normal" if SLA_domicilios_sim >= 95 else "inverse"
    st.metric("SLA de Domicilios (Meta: ≥95%)", f"{SLA_domicilios_sim}%", f"{'SLA Cumplido Express' if SLA_domicilios_sim >= 95 else 'Retrasos en Última Milla'}", delta_color=color_domicilios)

with col_card3:
    color_nps = "normal" if nps_evaluado_sim >= 70 else "inverse"
    st.metric("Satisfacción NPS (Meta: ≥70)", f"{nps_evaluado_sim} pts", f"{'Fidelización de Excelencia' if nps_evaluado_sim >= 70 else 'Riesgo de Deserción'}", delta_color=color_nps)

with col_card4:
    color_opex = "normal" if ejecución_opex_calculada <= 105.0 else "inverse"
    st.metric("Control Presupuestal OPEX (Meta: Ext. Max 105%)", f"{ejecución_opex_calculada:.1f}%", f"{'Gasto Ajustado Fijo' if ejecución_opex_calculada <= 105.0 else 'Sobrepresupuesto'}", delta_color=color_opex)

st.divider()

# =========================================================================
# 5. CONSTRUCCIÓN DE LA TABLA 33 CON SUS 10 KPIs FIDEDIGNOS (PANDAS)
# =========================================================================
st.subheader("📋 Tabla 33. Tablero de indicadores clave de desempeño — FarmaTech Ltda.")

diccionario_kpis_tabla_33 = {
    "KPI": [
        "Penetración Nicho Crónico", "Ticket Promedio", "Conversión WhatsApp", 
        "Cumplimiento SLA Domicilios", "NPS (Net Promoter Score)", "Exactitud de Inventario", 
        "Tasa de Recompra", "Margen Bruto", "Control de OPEX", "Cero Dispensaciones Rx"
    ],
    "Definición y Objetivo": [
        "% capturado del nicho de 4.500 pacientes del sector.",
        "Valor de la canasta mensual con domicilio incluido.",
        "% de chats recibidos que cierran en venta efectiva.",
        "% de entregas en el rango garantizado de 20-45 minutos.",
        "Nivel de lealtad y satisfacción del cliente.",
        "Control de stock físico vs. sistema (BPA).",
        "% de pacientes crónicos con pedido recurrente mensual.",
        "Rentabilidad después de costos mayoristas (COGS).",
        "Eficiencia del gasto frente al presupuesto operativo fijo.",
        "Seguridad sanitaria y cumplimiento de la Ley 485/1998."
    ],
    "Fórmula de Cálculo": [
        "(Pacientes activos / 4.500) × 100", "Ingresos totales / N.º transacciones",
        "(Pedidos / Mensajes) × 100", "(Dom. ≤ 45 min / Totales) × 100",
        "% Promotores − % Detractores", "(Ítems coincidentes / Total) × 100",
        "(Recompras / Clientes mes ant.) × 100", "((Ingresos − COGS) / Ingresos) × 100",
        "(OPEX real / \$41.500.000) × 100", "N.º de hallazgos en auditoría interna"
    ],
    "Meta Año 1": [
        "15% (675 pacientes)", "≥ \$55.000 COP", "≥ 3% mensual", 
        "≥ 95%", "≥ 70 puntos", "≥ 98%", 
        "≥ 60%", "≥ 30%", "≤ 105%", "0 fallos"
    ],
    "Valor Actual Actualizado": [
        f"{tasa_penetración_calculada:.1f}%", f"\${ticket_promedio_sim:,} COP", f"{conversion_wa_sim:.1f}%",
        f"{SLA_domicilios_sim}%", f"{nps_evaluado_sim} pts", f"{exactitud_inv_sim}%",
        f"{tasa_recompra_sim}%", f"{margen_bruto_fijo_modelo:.1f}%", f"{ejecución_opex_calculada:.1f}%",
        f"{hallazgos_auditoria_rx} fallos"
    ],
    "Fuente de Medición": [
        "Sistema POS", "Reporte POS", "WA Analytics", "App de rutas / Logística",
        "Encuesta WhatsApp", "Auditoría semanal", "Cohorte POS", "P&L Mensual",
        "Contabilidad / POS", "Regente de Farmacia"
    ]
}

df_kpi_completo_data = pd.DataFrame(diccionario_kpis_tabla_33)
st.dataframe(df_kpi_completo_data, use_container_width=True, hide_index=True)
st.caption("Fuente: Elaboración propia (2026). KPIs alineados de forma estricta con la proyección de ingresos de \$1.339.250.000 COP para el Año 1 y los protocolos de la Dirección Técnica.")

st.divider()

# =========================================================================
# 6. CENTRAL DE EXPORTACIÓN AVANZADA: GENERADOR EXCEL EJECUTIVO (XLSXWRITER)
# =========================================================================
st.subheader("⚙️ Central de Descargas de Reportes y Auditoría de Datos del SGC")
