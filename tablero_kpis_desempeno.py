import streamlit as st
import pandas as pd
import numpy as np
import io
import plotly.graph_objects as go
from datetime import datetime

# ==========================================
# 1. ARQUITECTURA DE UI/UX Y ESTILOS DE INYECCIÓN CSS
# ==========================================
st.set_page_config(
    page_title="FarmaTech - Enterprise Quality & KPI Suite",
    layout="wide",
    page_icon="📊",
    initial_sidebar_state="expanded"
)

# Estilos CSS avanzados para maquetación web responsiva y optimización estricta de impresión PDF
st.markdown("""
<style>
    @import url('https://googleapis.com');
    
    html, body, [data-testid="stSidebar"] { font-family: 'Inter', sans-serif; }
    .main-header { color: #1E3D59; font-weight: 800; font-size: 2.4rem; margin-bottom: 0.1rem; letter-spacing: -0.5px; }
    .sub-header { color: #555555; font-size: 1.1rem; margin-bottom: 1.8rem; font-weight: 400; }
    .metric-container { background-color: #F8F9FA; border: 1px solid #E9ECEF; border-radius: 10px; padding: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02); }
    .pdf-only-header { display: none; }
    
    @media print {
        .stSidebar, div[data-testid="stSidebarCollapseButton"], button, .stCheckbox, [data-testid="stBorder"] { display: none !important; }
        .main { width: 100% !important; padding: 0 !important; }
        .main-header { color: #000000 !important; font-size: 2rem; }
        .pdf-only-header { display: block !important; font-family: 'Inter', sans-serif; font-size: 0.85rem; color: #333333; border-bottom: 2px solid #1E3D59; padding-bottom: 6px; margin-bottom: 30px; }
    }
</style>
""", unsafe_allow_html=True)

# Encabezado corporativo estructurado visible únicamente al exportar a PDF (Ctrl + P)
st.markdown(f"""
<div class="pdf-only-header">
    <table style="width:100%; border-collapse:collapse;">
        <tr>
            <td style="text-align:left; font-weight:bold; font-size:1.1rem; color:#1E3D59;">FARMATECH LTDA. — INFORME GERENCIAL ANALÍTICO</td>
            <td style="text-align:right; font-weight:600;">SGC — SECCIÓN 7.3</td>
        </tr>
        <tr>
            <td style="text-align:left; color:#666;">Sistema de Gestión de Calidad Automatizado (PHVA)</td>
            <td style="text-align:right; color:#666;">Fecha de Extracción: {datetime.now().strftime('%d/%m/%Y')}</td>
        </tr>
    </table>
</div>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">📊 FarmaTech Ltda. — Cuadro de Mando Integral (KPIs)</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Suite Avanzada de Monitoreo de Procesos Críticos e Integración de Datos del POS Memphis</p>', unsafe_allow_html=True)

# ==========================================
# 2. CAPA DE CONTROL LATERAL (FILTROS Y SIMULADOR PARAMÉTRICO)
# ==========================================
st.sidebar.markdown("### 🕹️ Centro de Control Analítico")
st.sidebar.caption("Modifique los valores operativos en tiempo real para evaluar la salud del proyecto.")

st.sidebar.markdown("---")
st.sidebar.markdown("**📈 Parámetros Comerciales**")
pacientes_activos = st.sidebar.slider("Pacientes Crónicos Activos en el Mes", 100, 1000, 684)
conversión_wa = st.sidebar.slider("Tasa de Conversión WhatsApp (%)", 0.5, 10.0, 3.4, step=0.1)
ticket_promedio_input = st.sidebar.number_input("Ticket Promedio por Transacción (\$ COP)", min_value=30000, max_value=100000, value=55400, step=100)

st.sidebar.markdown("---")
st.sidebar.markdown("**🚚 Operación y Logística (BPA)**")
SLA_domicilios_input = st.sidebar.slider("Cumplimiento SLA Domicilios (<45 min)", 60, 100, 96)
exactitud_inv_input = st.sidebar.slider("Exactitud de Inventario Físico vs POS", 85.0, 100.0, 98.5, step=0.1)
tasa_recompra_input = st.sidebar.slider("Tasa de Recompra Mensual Crónicos", 40, 100, 62)
hallazgos_rx = st.sidebar.selectbox("Hallazgos por Dispensación Irregular (Rx)", [0, 1, 2, 3], index=0)

st.sidebar.markdown("---")
st.sidebar.markdown("**💰 Control Presupuestal Financiero**")
opex_real_mensual = st.sidebar.number_input("Gasto Operativo Fijo Ejecutado (\$ COP)", min_value=30000000, max_value=50000000, value=41650000, step=50000)
nps_input = st.sidebar.slider("Nivel de Lealtad Evaluado (NPS)", -100, 100, 74)

# ==========================================
# 3. MOTOR DE CÁLCULO LOGÍSTICO Y FINANCIERO INTERNO
# ==========================================
OPEX_PRESUPUESTADO_BASE = 41500000
TOTAL_NICHO_CRONICOS = 4500
INGRESOS_TEÓRICOS_MES = 111604166 # Base para consolidar los \$1.339.250.000 anuales

# Cálculos dinámicos reales basados en inputs
tasa_penetracion = (pacientes_activos / TOTAL_NICHO_CRONICOS) * 100
ejecucion_opex_pct = (opex_real_mensual / OPEX_PRESUPUESTADO_BASE) * 100
margen_bruto_calculado = 30.0 # Margen base del modelo de negocio de FarmaTech

# ==========================================
# 4. DESPLIEGUE COMPLETO DE SEMÁFOROS INTELIGENTES (KPI CARDS)
# ==========================================
st.subheader("🚨 Estado de Alertas y Semáforos de Gestión")
c1, c2, c3, c4 = st.columns(4)

with c1:
    delta_color_inv = "normal" if exactitud_inv_input >= 98.0 else "inverse"
    st.metric("Exactitud Inventario (Meta: ≥98%)", f"{exactitud_inv_input}%", f"{'Conforme BPA' if exactitud_inv_input >= 98.0 else 'Fuera de Tolerancia'}", delta_color=delta_color_inv)

with c2:
    delta_color_dom = "normal" if SLA_domicilios_input >= 95 else "inverse"
    st.metric("SLA Domicilios (Meta: ≥95%)", f"{SLA_domicilios_input}%", f"{'Cumple SLA 45min' if SLA_domicilios_input >= 95 else 'Retrasos Críticos'}", delta_color=delta_color_dom)

with c3:
    delta_color_nps = "normal" if nps_input >= 70 else "inverse"
    st.metric("Lealtad NPS (Meta: ≥70)", f"{nps_input} pts", f"{'Zona Excelencia' if nps_input >= 70 else 'Riesgo Deserción'}", delta_color=delta_color_nps)

with c4:
    delta_color_opex = "normal" if ejecucion_opex_pct <= 105.0 else "inverse"
    st.metric("Gasto OPEX (Meta: ≤105%)", f"{ejecucion_opex_pct:.1f}%", f"{'Presupuesto Controlado' if ejecucion_opex_pct <= 105.0 else 'Déficit por Gasto Fijo'}", delta_color=delta_color_opex)

st.divider()

# ==========================================
# 5. MAQUETACIÓN ESTÁTICA Y ESTRUCTURACIÓN DE LA TABLA 33 (10 KPIs EXACTOS)
# ==========================================
st.subheader("📋 Tabla 33. Tablero de indicadores clave de desempeño — FarmaTech Ltda.")

diccionario_tabla_33 = {
    "KPI": [
        "Penetración Nicho Crónico", 
        "Ticket Promedio", 
        "Conversión WhatsApp", 
        "Cumplimiento SLA Domicilios", 
        "NPS (Net Promoter Score)", 
        "Exactitud de Inventario", 
        "Tasa de Recompra", 
        "Margen Bruto", 
        "Control de OPEX", 
        "Cero Dispensaciones Rx"
    ],
    "Definición y Objetivo": [
        "% capturado del nicho de 4.500 pacientes del sector.",
        "Valor de la canasta mensual con domicilio incluido.",
        "% de chats recibidos que cierran en venta efectiva.",
        "% de entregas en el rango garantizado de 20-45 minutos.",
        "Nivel de lealtad y satisfacción del cliente.",
        "Control de stock físico vs. sistema (BPA).",
        "% de pacientes crónicos con pedido recurrentes mensual.",
        "Rentabilidad después de costos mayoristas (COGS).",
        "Eficiencia del gasto frente al presupuesto operativo fijo.",
        "Seguridad sanitaria y cumplimiento de la Ley 485/1998."
    ],
    "Fórmula de Cálculo": [
        "(Pacientes activos / 4.500) × 100",
        "Ingresos totales / N.º transacciones",
        "(Pedidos / Mensajes) × 100",
        "(Dom. ≤ 45 min / Totales) × 100",
        "% Promotores − % Detractores",
        "(Ítems coincidentes / Total) × 100",
        "(Recompras / Clientes mes ant.) × 100",
        "((Ingresos − COGS) / Ingresos) × 100",
        "(OPEX real / \$41.500.000) × 100",
        "N.º de hallazgos en auditoría interna"
    ],
    "Meta Año 1": [
        "15% (675 pacientes)",
        "≥ \$55.000 COP",
        "≥ 3% mensual",
        "≥ 95%",
        "≥ 70 puntos",
        "≥ 98%",
        "≥ 60%",
        "≥ 30%",
        "≤ 105%",
        "0 fallos"
    ],
    "Valor Actual (Simulado)": [
        f"{tasa_penetracion:.1f}%",
        f"\${ticket_promedio_input:,} COP",
        f"{conversión_wa:.1f}%",
        f"{SLA_domicilios_input}%",
        f"{nps_input} pts",
        f"{exactitud_inv_input}%",
        f"{tasa_recompra_input}%",
        f"{margen_bruto_calculado:.1f}%",
        f"{ejecucion_opex_pct:.1f}%",
        f"{hallazgos_rx} fallos"
    ],
    "Fuente de Medición": [
        "Sistema POS",
        "Reporte POS",
        "WA Analytics",
        "App de rutas / Logística",
        "Encuesta WhatsApp",
        "Auditoría semanal",
        "Cohorte POS",
        "P&L Mensual",
        "Contabilidad / POS",
        "Regente de Farmacia"
    ]
}

df_final_kpi = pd.DataFrame(diccionario_tabla_33)

# Mostrar la tabla en pantalla completa con diseño interactivo nativo
st.dataframe(df_final_kpi, use_container_width=True, hide_index=True)
st.caption("Fuente: Elaboración propia (2026). KPIs alineados con la proyección de ingresos de \$1.339.250.000 COP para el Año 1 y los protocolos del Regente de Farmacia (DT).")

st.divider()

# ==========================================
# 6. ENTORNO DE AUTOMATIZACIÓN AVANZADA: GENERADOR EXCEL EXECUTIVO (.XLSX)
# ==========================================
st.subheader("🐍 Automatización de Reportabilidad Corporativa (Python Engineering)")
st.write("El siguiente módulo compila de forma nativa los datos dinámicos del SGC en un libro de cálculo de Microsoft Excel utilizando las directivas binarias de `xlsxwriter`.")

# Pipeline de construcción del buffer de descarga en memoria
excel_buffer = io.BytesIO()
with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as workbook_manager:
    df_final_kpi.to_excel(workbook_manager, sheet_name='Dashboard SGC', index=False, startrow=3)
    
