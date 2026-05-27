import streamlit as st
import pandas as pd
import numpy as np
import io
import plotly.graph_objects as go

# 1. CONFIGURACIÓN CORPORATIVA DE LA INTERFAZ (UI/UX)
st.set_page_config(page_title="FarmaTech - Tablero Control Calidad", layout="wide", page_icon="📊")

# Estilos CSS avanzados para la visualización web y regla de exportación limpia a PDF
st.markdown("""
<style>
    .main-title { font-family: 'Helvetica Neue', Arial, sans-serif; color: #1E3D59; font-weight: 800; font-size: 2.2rem; margin-bottom: 0.2rem; }
    .section-desc { color: #555555; font-size: 1.05rem; margin-bottom: 1.5rem; }
    .pdf-header { display: none; }
    @media print {
        .stSidebar, div[data-testid="stSidebarCollapseButton"], button, .stCheckbox { display: none !important; }
        .main { width: 100% !important; padding: 0 !important; }
        .main-title { color: #000000 !important; font-size: 1.9rem; }
        .pdf-header { display: block !important; font-family: sans-serif; font-size: 0.9rem; color: #444444; border-bottom: 2px solid #1E3D59; padding-bottom: 8px; margin-bottom: 25px; }
    }
</style>
""", unsafe_allow_html=True)

# Encabezado oficial visible únicamente en la exportación PDF
st.markdown("""
<div class="pdf-header">
    <strong>FARMATECH LTDA. — REPORTE OFICIAL SGC (SECCIÓN 7.3 TABLERO DE INDICADORES)</strong><br>
    Automatización Avanzada Python-Excel • Metodología PHVA • Vigencia Operativa 2026
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📊 FarmaTech Ltda. — Cuadro de Mando Operativo (SGC)</div>', unsafe_allow_html=True)
st.markdown('<div class="section-desc">Monitoreo de KPIs en Tiempo Real, Automatización de Reportes Excel Corporativos y Ciclo PHVA</div>', unsafe_allow_html=True)
st.divider()

# 2. PANEL LATERAL (FILTROS DINÁMICOS Y SIMULADOR DE SEMÁFOROS)
st.sidebar.header("🕹️ Simulador del POS Memphis")
st.sidebar.subheader("Filtros del Tablero")

filtro_proceso = st.sidebar.selectbox(
    "Filtrar Proceso Crítico", 
    ["Todos", "Gestión de Inventarios", "Atención y Domicilios", "Dispensación Técnica", "Marketing y Fidelización", "Gestión Financiera", "Talento Humano", "PQRS y Quejas"]
)

st.sidebar.subheader("Ingreso de Variables Reales")
exactitud_inv = st.sidebar.slider("Exactitud de Inventario Real (%)", 85.0, 100.0, 98.5, step=0.1)
tiempo_domicilios = st.sidebar.slider("Domicilios en < 45 min (%)", 70, 100, 96)
nps_actual = st.sidebar.slider("NPS Promedio Satisfecho (pts)", -100, 100, 74)
horas_capacitacion = st.sidebar.slider("Horas de Capacitación Ejecutadas", 0, 40, 22)
ingresos_reales_mes = st.sidebar.number_input("Ingresos Reales Mensuales ($ COP)", min_value=0, value=138600000)

# Parámetros fijos financieros
MARGEN_BRUTO_PCT = 0.30
OPEX_FIJO = 41500000
INGRESOS_META_ANUAL = 1339250000
absorcion_opex_pct = min(((ingresos_reales_mes * MARGEN_BRUTO_PCT) / OPEX_FIJO) * 100, 100.0)

# 3. SEMÁFOROS DIGITALES EN STREAMLIT
st.subheader("🚨 Semáforos Automáticos de Cumplimiento (Vista Celular/Web)")
col1, col2, col3, col4 = st.columns(4)

with col1:
    color_inv = "normal" if exactitud_inv >= 98.0 else "inverse"
    st.metric("Inventario (Meta: >98%)", f"{exactitud_inv}%", f"{'Óptimo — Confiable' if exactitud_inv >= 98.0 else 'Alerta — Desfase Físico'}", delta_color=color_inv)

with col2:
    color_dom = "normal" if tiempo_domicilios >= 95 else "inverse"
    st.metric("Domicilios Express (Meta: ≥95%)", f"{tiempo_domicilios}%", f"{'SLA Cumplido' if tiempo_domicilios >= 95 else 'Retrasos Detectados'}", delta_color=color_dom)

with col3:
    color_nps = "normal" if nps_actual >= 70 else "inverse"
    st.metric("Satisfacción (Meta NPS: ≥70)", f"{nps_actual} pts", f"{'Excelente Fidelización' if nps_actual >= 70 else 'Insatisfacción'}", delta_color=color_nps)

with col4:
    color_fin = "normal" if absorcion_opex_pct >= 100 else "inverse"
    st.metric("Absorción OPEX (Meta: 100%)", f"{absorcion_opex_pct:.1f}%", f"{'Punto Equilibrio Cubierto' if absorcion_opex_pct >= 100 else 'Alerta de Iliquidez'}", delta_color=color_fin)

st.divider()

# 4. CONSTRUCCIÓN DE LA DATA BASE PARA PANDAS Y EXCEL
datos_tabla_33 = {
    "KPI": ["Penetración Nicho Crónico", "Ticket Promedio", "Conversión WhatsApp", "Cumplimiento SLA Domicilios", "NPS (Net Promoter Score)", "Exactitud de Inventario", "Tasa de Recompra", "Margen Bruto", "Control de OPEX", "Cero Dispensaciones Rx"],
    "Meta Año 1": ["15.0%", "$55,000", "3.0%", "95.0%", "70", "98.0%", "60.0%", "30.0%", "105.0%", "0"],
    "Valor Actual": [15.2, ingresos_reales_mes/2520 if ingresos_reales_mes > 0 else 0, 3.4, tiempo_domicilios, nps_actual, exactitud_inv, 62.4, 30.0, absorcion_opex_pct, 0],
    "Unidad": ["%", "COP", "%", "%", "pts", "%", "%", "%", "%", "fallos"],
    "Responsable": ["Regente de Farmacia", "Gerente General", "Dir. Comercial", "Dir. Comercial", "Dir. Comercial", "Regente de Farmacia", "Dir. Comercial", "Gerente General", "Gerente General", "Regente de Farmacia"]
}
df_kpi = pd.DataFrame(datos_tabla_33)

# 5. BOTÓN DE AUTOMATIZACIÓN BRUTAL: GENERADOR DE EXCEL CON FORMATO EJECUTIVO
st.subheader("🐍 Módulo de Automatización Corporativa (Generación de Reportes Excel)")
st.write("Presiona el botón de abajo para compilar dinámicamente un archivo de Excel con fuentes ejecutivas, paleta de colores azul corporativo y formatos automáticos de semáforos.")

# Crear el buffer en memoria para descargar el archivo sin escribir en disco
buffer = io.BytesIO()
with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
    df_kpi.to_excel(writer, sheet_name='KPIs SGC', index=False, startrow=3)
    
    workbook  = writer.book
    worksheet = writer.sheets['KPIs SGC']
    
    # Estilos Ejecutivos Personalizados
    fmt_title = workbook.add_format({'bold': True, 'font_size': 16, 'font_color': '#1E3D59', 'font_name': 'Segoe UI'})
    fmt_header = workbook.add_format({'bold': True, 'bg_color': '#1E3D59', 'font_color': 'white', 'font_name': 'Segoe UI', 'border': 1, 'align': 'center'})
    fmt_cell = workbook.add_format({'font_name': 'Segoe UI', 'font_size': 11, 'border': 1})
    fmt_num = workbook.add_format({'font_name': 'Segoe UI', 'font_size': 11, 'border': 1, 'num_format': '#,##0.0'})
    
    # Escribir Encabezado de la Empresa
    worksheet.write('A1', 'FARMATECH LTDA. — REPORTE MENSUAL DE CALIDAD (SGC)', fmt_title)
    worksheet.write('A2', 'Generado automáticamente vía Python / POS Memphis / Vigencia 2026')
    
    # Aplicar Formato a las columnas
    worksheet.set_column('A:A', 25, fmt_cell)
    worksheet.set_column('B:D', 15, fmt_num)
    worksheet.set_column('E:E', 25, fmt_cell)
    
    # Volver a formatear las cabeceras de la tabla
    for col_num, header in enumerate(df_kpi.columns):
        worksheet.write(3, col_num, header, fmt_header)
        
    # Formato Condicional (Semáforos Inteligentes) directamente insertados en las celdas de Excel
    worksheet.conditional_format('C5:C14', {
        'type': 'cell', 'criteria': '>=', 'value': 70,
        'format': workbook.add_format({'bg_color': '#C6EFCE', 'font_color': '#006100'})
    })
    worksheet.conditional_format('C5:C14', {
        'type': 'cell', 'criteria': '<', 'value': 70,
        'format': workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})
    })

# Botón nativo de descarga
st.download_button(
    label="📥 Descargar Reporte Automatizado de KPIs de Calidad en Excel",
    data=buffer.getvalue(),
    file_name="Reporte_KPIs_FarmaTech_2026.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

st.divider()

# 6. EXPOSICIÓN DE LA TABLA COMPLETA EN PANTALLA
st.subheader("📋 Tabla 33. Tablero de indicadores clave de desempeño — FarmaTech Ltda.")
st.dataframe(df_kpi, use_container_width=True, hide_index=True)
st.caption("Fuente: Elaboración propia (2026). KPIs completamente integrados con la suite analítica digital de FarmaTech Ltda.")

st.divider()

# 7. MÓDULO FOTOGRÁFICO DE AUDITORÍA
st.subheader("📸 Captura de Evidencia Física — Auditoría de Calidad e Infraestructura")
habilitar_camara = st.checkbox("Activar Cámara / Dispositivo de Inspección")

if habilitar_camara:
    foto_evidencia = st.camera_input("Enfoque el termohigrómetro o estantería para indexar en la bitácora")
    if foto_evidencia:
        st.success("✅ Evidencia visual registrada con éxito en el SGC de FarmaTech Ltda.")
        st.image(foto_evidencia, caption="Registro de Evidencia de Campo — Control Sanitario", width=400)

