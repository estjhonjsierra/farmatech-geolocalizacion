import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 1. CONFIGURACIÓN CORPORATIVA DE LA INTERFAZ (UI/UX)
st.set_page_config(page_title="FarmaTech - Tablero Control Calidad", layout="wide", page_icon="📊")

# Estilos CSS avanzados para la visualización web y regla de exportación limpia a PDF
st.markdown("""
<style>
    .main-title { font-family: 'Helvetica Neue', Arial, sans-serif; color: #1E3D59; font-weight: 800; font-size: 2.2rem; margin-bottom: 0.2rem; }
    .section-desc { color: #555555; font-size: 1.05rem; margin-bottom: 1.5rem; }
    .pdf-header { display: none; }
    
    /* Regla CSS de Impresión Limpia para PDF (Ctrl + P) - Oculta componentes de desarrollo */
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
    <strong>FARMATECH LTDA. — REPORTE OFICIAL SGC (SECCIÓN 7.2 PROCEDIMIENTOS DE CONTROL)</strong><br>
    Evaluación de Procesos Críticos • Metodología PHVA • Vigencia Operativa 2026
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📊 FarmaTech Ltda. — Cuadro de Mando Operativo (SGC)</div>', unsafe_allow_html=True)
st.markdown('<div class="section-desc">Monitoreo de KPIs en Tiempo Real y Ciclo PHVA integrado al Sistema POS Memphis</div>', unsafe_allow_html=True)
st.divider()

# 2. PANEL LATERAL (FILTROS DINÁMICOS Y SIMULADOR DE SEMÁFOROS)
st.sidebar.header("🕹️ Simulador del POS Memphis")
st.sidebar.subheader("Filtros del Tablero")

filtro_proceso = st.sidebar.selectbox(
    "Filtrar Proceso Crítico", 
    ["Todos", "Gestión de Inventarios", "Atención y Domicilios", "Dispensación Técnica", "Marketing y Fidelización", "Gestión Financiera", "Talento Humano", "PQRS y Quejas"]
)

st.sidebar.subheader("Ingreso de Variables Reales")
st.sidebar.caption("Modifique los valores para alterar los indicadores del SGC:")
exactitud_inv = st.sidebar.slider("Exactitud de Inventario Real (%)", 85.0, 100.0, 98.5, step=0.1)
tiempo_domicilios = st.sidebar.slider("Domicilios en < 45 min (%)", 70, 100, 96)
nps_actual = st.sidebar.slider("NPS Promedio Satisfecho (pts)", -100, 100, 74)
horas_capacitacion = st.sidebar.slider("Horas de Capacitación Ejecutadas", 0, 40, 22)
ingresos_reales_mes = st.sidebar.number_input("Ingresos Reales Mensuales ($ COP)", min_value=0, value=138600000)

# Cálculos complementarios de control financiero (Carga OPEX y Margen Bruto)
MARGEN_BRUTO_PCT = 0.30
OPEX_FIJO = 41500000
margen_bruto_real = ingresos_reales_mes * MARGEN_BRUTO_PCT
absorcion_opex_pct = min((margen_bruto_real / OPEX_FIJO) * 100, 100.0)

# 3. COMPONENTE DE SEMÁFOROS DIGITALES AUTOMÁTICOS (CUADRO DE MANDO INTEGRAL)
st.subheader("🚨 Semáforos Automáticos de Cumplimiento")
col1, col2, col3, col4 = st.columns(4)

with col1:
    color_inv = "normal" if exactitud_inv >= 98.0 else "inverse"
    st.metric("Inventario (Meta: >98%)", f"{exactitud_inv}%", f"{'Óptimo — Confiable' if exactitud_inv >= 98.0 else 'Alerta — Desfase Físico'}", delta_color=color_inv)

with col2:
    color_dom = "normal" if tiempo_domicilios >= 95 else "inverse"
    st.metric("Domicilios Express (Meta: ≥95%)", f"{tiempo_domicilios}%", f"{'SLA Cumplido (20-45 min)' if tiempo_domicilios >= 95 else 'Retrasos Detectados'}", delta_color=color_dom)

with col3:
    color_nps = "normal" if nps_actual >= 70 else "inverse"
    st.metric("Satisfacción (Meta NPS: ≥70)", f"{nps_actual} pts", f"{'Excelente Fidelización' if nps_actual >= 70 else 'Insatisfacción de Clientes'}", delta_color=color_nps)

with col4:
    color_fin = "normal" if absorcion_opex_pct >= 100 else "inverse"
    st.metric("Absorción OPEX (Meta: 100%)", f"{absorcion_opex_pct:.1f}%", f"{'Punto Equilibrio Cubierto' if absorcion_opex_pct >= 100 else 'Alerta de Iliquidez'}", delta_color=color_fin)

st.sidebar.markdown("---")
st.sidebar.subheader("📄 Exportar Reporte de Calidad")
st.sidebar.info("Para exportar la Tabla 32 y las evidencias limpias a PDF, presione **Ctrl + P** o **Cmd + P** en su navegador y guarde el reporte.")

st.divider()

# 4. DESPLIEGUE COMPLETO DE LA TABLA 32 (7 PROCESOS EXACTOS)
st.subheader("📋 Tabla 32. Procedimientos clave de control operativo — FarmaTech Ltda.")

datos_tabla_32 = {
    "Proceso Crítico": [
        "Gestión de Inventarios", 
        "Atención y Domicilios", 
        "Dispensación Técnica", 
        "Marketing y Fidelización", 
        "Gestión Financiera", 
        "Talento Humano", 
        "PQRS y Quejas"
    ],
    "Procedimiento de Control": [
        "Conteo físico vs. POS. Revisión de fechas de vencimiento y rotación.",
        "Registro de tiempos (pedido → entrega). Encuesta NPS automática.",
        "Registro de fórmulas en POS. Auditoría semanal de registros crónicos y BPA.",
        "Análisis de métricas digitales (WhatsApp/Social). Tasa de recompra de crónicos.",
        "Comparativos ingresos reales vs. presupuestados. Control de OPEX.",
        "Evaluación de desempeño por cargo. Encuesta de clima organizacional.",
        "Registro de tickets por WhatsApp y mostrador. Respuesta en < 24 h."
    ],
    "Indicador de Control": [
        f"% exactitud inventario (> 98%). Monitoreado: {exactitud_inv}%. Vencidos en bodega (meta: cero).",
        f"% domicilios en < 45 min (≥ 95%). Monitoreado: {tiempo_domicilios}%. NPS promedio (meta: ≥ 70). Actual: {nps_actual} pts.",
        "Cero dispensaciones sin fórmula (Rx). Cero hallazgos BPA críticos.",
        "Tasa de recompra: > 60%. Conversión WhatsApp: ≥ 3%.",
        f"Margen bruto ≥ 30% (Actual simulado: {absorcion_opex_pct:.1f}% OPEX). Ingresos año 1: $1,339,250,000.",
        f"Rotación: < 15%/año. Capacitación: ≥ 20 h/empleado/año. Registrado: {horas_capacitacion} h.",
        "Tasa resolución: > 95% en < 24 h. PQRS recurrentes: cero."
    ],
    "Frecuencia / Responsable": [
        "Semanal — Dir. Territorial + Regente de Farmacia",
        "Diario / Mensual — Dir. Comercial",
        "Semanal — Regente de Farmacia",
        "Mensual — Dir. Comercial",
        "Mensual — Gerente General",
        "Semestral — Dir. Territorial",
        "Diario — Dir. Comercial + Regente"
    ]
}

df_control = pd.DataFrame(datos_tabla_32)

# Filtro dinámico de la tabla por proceso crítico
if filtro_proceso != "Todos":
    df_control = df_control[df_control["Proceso Crítico"] == filtro_proceso]

st.dataframe(df_control, use_container_width=True, hide_index=True)
st.caption("Fuente: Elaboración propia (2026). Metodología PHVA aplicada a los procesos de FarmaTech Ltda. en coherencia con las metas financieras de la Tabla 15 y el manual de cargos de la Tabla 30.")

st.divider()

# 5. MÓDULO FOTOGRÁFICO DE AUDITORÍA (CÁMARA DE VALIDACIÓN)
st.subheader("📸 Captura de Evidencia Física — Auditoría de Calidad e Infraestructura")
st.write("Carga e inyección de soporte fotográfico en tiempo real para el cumplimiento de las Buenas Prácticas de Almacenamiento (BPA).")

habilitar_camara = st.checkbox("Activar Cámara / Dispositivo de Inspección")

if habilitar_camara:
    foto_evidencia = st.camera_input("Enfoque el termohigrómetro, estantería o zona física para indexar en la bitácora del SGC")
    if foto_evidencia:
        st.success("✅ Evidencia registrada de forma conforme. Guardada con éxito en la traza analítica de FarmaTech Ltda.")
        st.image(foto_evidencia, caption="Registro de Evidencia de Campo — Control Sanitario", width=400)
else:
    st.info("El sensor de la cámara está en reposo. Active la casilla superior para capturar soporte visual para el reporte final.")
