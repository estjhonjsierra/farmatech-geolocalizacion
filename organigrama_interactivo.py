import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 1. CONFIGURACIÓN HIGH-DEFINITION DE LA INTERFAZ CORPORATIVA (UI/UX)
st.set_page_config(
    page_title="FarmaTech - Enterprise Talent Suite",
    layout="wide",
    page_icon="🏢"
)

# Inyección de estilos CSS avanzados y limpios para estilización de fuentes y contenedores
st.markdown("""
    <style>
    .main-title { font-family: 'Helvetica Neue', Arial, sans-serif; color: #1e3d59; font-weight: 800; font-size: 2.4rem; margin-bottom: 0.1rem; }
    .section-desc { color: #6c757d; font-size: 1.05rem; margin-bottom: 1.5rem; }
    .header-nivel { padding: 8px 15px; border-radius: 6px; font-weight: bold; font-size: 1.1rem; margin-top: 15px; margin-bottom: 10px; }
    .estrat-hdr { background-color: #1e3d59; color: white; }
    .tact-hdr { background-color: #ff7f0e; color: white; }
    .ope-hdr { background-color: #2ca02c; color: white; }
    .arrow-q { text-align: center; font-size: 1.8rem; color: #1e3d59; font-weight: bold; margin: 4px 0; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🏢 Componente 2: Estructura Orgánica, Nómina y Manual de Funciones</h1>', unsafe_allow_html=True)
st.markdown('<p class="section-desc">Tabla 26. Matriz Avanzada de Consulta de Perfiles, Requisitos Legales ReTHUS y Asignaciones Salariales — FarmaTech Ltda.</p>', unsafe_allow_html=True)
st.markdown("---")

# Configuración universal para descarga de reportes y capturas fotográficas (Cámara 📸 fija y activa)
config_exportacion = {
    'displayModeBar': True,
    'displaylogo': False,
    'modeBarButtonsToRemove': ['zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d'],
    'toImageButtonOptions': {
        'format': 'png',
        'filename': 'farmatech_reporte_talento_humano',
        'height': 550,
        'width': 1050,
        'scale': 2
    }
}

# Variables financieras y legales de referencia unificada (Año 2026)
smmlv_2026 = 1430000
factor_prestacional = 1.48

# 2. SECCIÓN DE INDUCTORES DE CONTROL EN LA BARRA LATERAL (SIDEBAR)
st.sidebar.header("🎛️ Centro de Simulación de Carga Operativa")
st.sidebar.markdown("Modifique los inductores en tiempo real para estresar las métricas de rendimiento del personal de primera línea.")

transacciones_reales_dia = st.sidebar.slider("Transacciones Reales Diarias (POS)", min_value=30, max_value=120, value=65, step=5)
horas_capacitacion = st.sidebar.slider("Horas de Capacitación Anual / Empleado", min_value=0, max_value=40, value=20, step=2)
eficiencia_logistica = st.sidebar.slider("Eficiencia de Entrega de Flota (%)", min_value=50, max_value=100, value=95, step=5)

meta_transacciones_dia = 84

st.subheader("🗺️ Tablero de Control y Mando del Organigrama")
st.write("Active el interruptor de cualquier cargo estructural para desplegar su manual de funciones, auditoría de nómina y KPI con captura de imagen.")
st.markdown("---")

# =============================================================================
# 1. BLOQUE DE NIVEL ESTRATÉGICO
# =============================================================================
st.markdown('<div class="header-nivel estrat-hdr">🏛️ NIVEL I: DIRECCIÓN ESTRATÉGICA Y GOBIERNO CORPORATIVO</div>', unsafe_allow_html=True)

col_e1, col_e2 = st.columns(2)

with col_e1:
    act_junta = st.toggle("👥 NODO 1: JUNTA DE SOCIOS (Composición del Capital Social)", value=False)
    if act_junta:
        st.markdown("### 👥 Manual de la Junta de Socios")
        st.markdown("**Naturaleza Societaria:** Sociedad de Responsabilidad Limitada (Ltda.) bajo el Artículo 353 del Código de Comercio.")
        st.markdown("**Matriz de Capital Social (\$280.000.000 COP - Consistencia con la Tabla 12):**")
        
        # Estructurar tabla de socios indexada
        socios_data = {
            "Socio / Inversionista": ["Fondo Emprender SENA", "Inversionista Ángel (IPS)", "Jhon Jaime Sierra", "Lucy Semanate", "Danna Delgado", "Mauricio Echeverry"],
            "Aporte Capital": ["\$112.000.000", "\$70.000.000", "\$56.000.000", "\$28.000.000", "\$7.000.000", "\$7.000.000"],
            "Participación (%)": ["40.0%", "25.0%", "20.0%", "10.0%", "2.5%", "2.5%"]
        }
        st.dataframe(pd.DataFrame(socios_data), use_container_width=True, hide_index=True)
        st.caption("Nota de Control Laboral: Los socios operan ad honorem dentro del órgano consultor externo, evitando sobrecargar la nómina pre-equilibrio.")

with col_e2:
    act_gerencia = st.toggle("👔 NODO 2: GERENCIA GENERAL (Jhon Jaime Sierra - Representación Legal)", value=False)
    if act_gerencia:
        st.markdown("### 👔 Manual de Funciones: Gerente General")
        st.write("**Misión:** Ejercer la representación legal y comercial de la compañía, salvaguardar las metas de empleo pactadas ante el SENA y auditar la rentabilidad del proyecto.")
        st.write("**Responsabilidades Críticas:**")
        st.markdown("1. Suscribir y firmar convenios de distribución mayorista de medicamentos con Coopidrogas.")
        st.markdown("2. Auditar de forma trimestral los flujos netos de caja generados por las operaciones presenciales y digitales.")
        st.markdown("3. Evaluar el Retorno de Inversión (ROI) y autorizar los planes de expansión hacia la segunda sede en el Año 3.")

st.markdown('<div class="arrow-q">▲</div>', unsafe_allow_html=True)

# =============================================================================
# 2. BLOQUE DE NIVEL TÁCTICO (DIRECCIONES EN TRES COLUMNAS EN PARALELO)
# =============================================================================
st.markdown('<div class="header-nivel tact-hdr">⚡ NIVEL II: DIRECCIÓN TÁCTICA Y CONTROL DE CALIDAD BIOSANITARIA</div>', unsafe_allow_html=True)

col_t1, col_t2, col_t3 = st.columns(3)

with col_t1:
    act_dt = st.toggle("⚙️ NODO 3: DIRECCIÓN TÉCNICA (Regente de Farmacia)", value=False)
with col_t2:
    act_dc = st.toggle("📢 NODO 4: DIRECCIÓN COMERCIAL (Socio Consultor)", value=False)
with col_t3:
    act_dterr = st.toggle("🗺️ NODO 5: DIRECCIÓN TERRITORIAL (Socio Consultor)", value=False)

if act_dt:
    st.markdown("---")
    st.markdown("### ⚙️ Manual Técnico de Cargo: Regente de Farmacia (Director Técnico)")
    
    col_dt1, col_dt2 = st.columns(2)
    with col_dt1:
        st.write("**Requisito Normativo:** Título como Tecnólogo en Regencia de Farmacia (Ley 485 de 1998), con registro activo en el ReTHUS y tarjeta profesional vigente.")
        st.write("**Asignación en OPEX (Tabla 11):** `$4.500.000 COP/mes` (Costo fijo empresarial con carga prestacional unificada).")
        st.markdown("**Desglose Contable de la Carga de Nómina:**")
        sueldo_base_dt = 3040000
        st.markdown(f"- Salario Base Contractual: `${sueldo_base_dt:,.0f} COP`")
        st.markdown(f"- Prestaciones Sociales & Seguridad Social (factor 1.48): `${sueldo_base_dt * 0.48:,.0f} COP`")
        st.markdown("- Total Costo Fijo Mensual FarmaTech: `$4.500.000 COP` (Consistencia Absoluta)")
    
    with col_dt2:
        cumplimiento_bpa = min(100.0, 75.0 + (horas_capacitacion * 0.65))
        st.markdown(f"📈 **Índice de Conformidad Sanitaria (BPA Estimado):** `{cumplimiento_bpa:.1f}%` (Umbral Seccional de Salud: 100%)")
        
        fig_dt = go.Figure(go.Indicator(
            mode = "gauge+number", value = cumplimiento_bpa,
            title = {'text': "Conformidad Estándar Sanitario e Inspección Seccional"},
            gauge = {'axis': {'range': [50, 100]}, 'bar': {'color': "#1e3d59"}, 'threshold': {'line': {'color': "red", 'width': 4}, 'value': 95}}
        ))
        fig_dt.update_layout(height=230, margin=dict(t=30, b=10, l=10, r=10))
        st.plotly_chart(fig_dt, use_container_width=True, config=config_exportacion)

if act_dc:
    st.markdown("---")
    st.markdown("### 📢 Manual de Cargo: Dirección Comercial (Órgano Consultor)")
    st.write("**Estatus Laboral:** Asesoría externa ad honorem asumida por el socio fundador (Asignación: \$0 COP en OPEX).")
    st.write("**Funciones Principales:**")
    st.markdown("1. Monitorear el embudo de conversión omnicanal de pedidos capturados desde la API de WhatsApp Business.")
    st.markdown("2. Controlar la ejecución del presupuesto de pauta publicitaria geo-segmentada de `$2.500.000 COP mensuales` fletado en la Tabla 11.")
    st.markdown("3. Diseñar las campañas de fidelización y el programa 'Puntos Salud' para los pacientes de patologías crónicas.")

if act_dterr:
    st.markdown("---")
    st.markdown("### 🗺️ Manual de Cargo: Dirección Territorial (Órgano Consultor)")
    st.write("**Estatus Laboral:** Gestión de operaciones externa ad honorem asumida por el socio fundador (Asignación: \$0 COP en OPEX).")
    st.write("**Funciones Principales:**")
    st.markdown("1. Coordinar y auditar la infraestructura física de los 80 m² localizada estratégicamente en el Mall La 33.")
    st.markdown("2. Supervisar los turnos de la fuerza de venta operativa y gestionar las relaciones institucionales con clínicas del sector.")

st.markdown('<div class="arrow-q">▲</div>', unsafe_allow_html=True)

# =============================================================================
# 3. BLOQUE DE NIVEL OPERATIVO (CUATRO COLUMNAS EN PARALELO)
# =============================================================================
st.markdown('<div class="header-nivel ope-hdr">🟩 NIVEL III: AREA OPERATIVA, ATENCIÓN OMNICANAL Y DISTRIBUCIÓN EXPRESS</div>', unsafe_allow_html=True)

col_o1, col_o2, col_o3, col_o4 = st.columns(4)

with col_o1:
    act_aux1 = st.toggle("📋 NODO 6: AUXILIAR 1 (Terminal POS 1)", value=False)
with col_o2:
    act_aux2 = st.toggle("💬 NODO 7: AUXILIAR 2 (WhatsApp)", value=False)
with col_o3:
    act_aux3 = st.toggle("📦 NODO 8: AUXILIAR 3 (Almacén / FEFO)", value=False)
with col_o4:
    act_dom = st.toggle("🏍️ NODO 9: MENSAJERO (Última Milla)", value=False)

if act_aux1 or act_aux2 or act_aux3:
    st.markdown("---")
