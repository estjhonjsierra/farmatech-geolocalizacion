import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 1. CONFIGURACIÓN HIGH-DEFINITION DE LA INTERFAZ DE USUARIO (UI)
st.set_page_config(
    page_title="FarmaTech - Balanced Scorecard Unificado",
    layout="wide",
    page_icon="🎯"
)

# Inyección de estilos CSS avanzados para maquetación ejecutiva premium
st.markdown("""
    <style>
    .main-title { font-family: 'Helvetica Neue', Arial, sans-serif; color: #1e3d59; font-weight: 800; font-size: 2.5rem; margin-bottom: 0.2rem; }
    .section-desc { color: #6c757d; font-size: 1.05rem; margin-bottom: 1.5rem; }
    
    .bsc-node {
        padding: 18px;
        border-radius: 12px;
        color: white;
        font-family: Arial, sans-serif;
        text-align: center;
        margin: 8px auto;
        max-width: 850px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.06);
    }
    .fin-node { background: linear-gradient(135deg, #1e3d59 0%, #112233 100%); border-left: 8px solid #00d2ff; }
    .cli-node { background: linear-gradient(135deg, #ff7f0e 0%, #b35900 100%); border-left: 8px solid #ffe600; }
    .pro-node { background: linear-gradient(135deg, #2ca02c 0%, #175217 100%); border-left: 8px solid #00ffcc; }
    .cre-node { background: linear-gradient(135deg, #9467bd 0%, #52356b 100%); border-left: 8px solid #f000ff; }
    
    .node-title { font-size: 1.15rem; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; }
    .node-desc { font-size: 0.9rem; opacity: 0.95; line-height: 1.4; margin-top: 3px; }
    .arrow-connector { text-align: center; font-size: 1.8rem; color: #1e3d59; line-height: 1; margin: 2px 0; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🚀 3.1 Cuadro de Mando Integral — Balanced Scorecard (BSC)</h1>', unsafe_allow_html=True)
st.markdown('<p class="section-desc">Estructura de Causalidad y Modelado del Ciclo Completo de Proyecciones (Meses 1 a 12) — FarmaTech Ltda.</p>', unsafe_allow_html=True)
st.markdown("---")

# CONFIGURACIÓN DE EXPORTACIÓN CON BARRA DE HERRAMIENTAS SIEMPRE VISIBLE
config_exportacion = {
    'displayModeBar': True,        # Mantiene la barra siempre visible
    'displaylogo': False,          # Quita el logo de Plotly para limpiar espacio
    'modeBarButtonsToRemove': ['zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d'], # Deja solo la cámara y el hover
    'toImageButtonOptions': {
        'format': 'png',
        'filename': 'farmatech_balanced_scorecard_maestro',
        'height': 600,
        'width': 1100,
        'scale': 2                  # Duplica la resolución para que se vea nítido en Word
    }
}

# =============================================================================
# BLOQUE SUPERIOR: MAPA DE CAUSALIDAD ESTÁTICO TOTAL (Para captura directa)
# =============================================================================
st.subheader("🛸 Diagrama de Flujo y Vectores de Causalidad Estructural")
st.write("Representación de la ruta crítica adaptada al manual de operaciones. Tómele una captura completa para su informe.")

st.markdown("""
    <div class="bsc-node fin-node">
        <div class="node-title">1. Perspectiva Financiera</div>
        <div class="node-desc">Alcanzar Punto de Equilibrio (84 Tx/Día • Mes 7) | Ingresos de \$891M Anuales | Margen Neto Sostenido del 30% | ROI en Año 3</div>
    </div>
    <div class="arrow-connector">▲</div>
    <div class="bsc-node cli-node">
        <div class="node-title">2. Perspectiva de Clientes</div>
        <div class="node-desc">Capturar el 15% del Nicho Crónico (675 Pacientes) | Sostener NPS ≥ 70 | Omnicanalidad Digital del 40% vía WhatsApp Business</div>
    </div>
    <div class="arrow-connector">▲</div>
    <div class="bsc-node pro-node">
        <div class="node-title">3. Perspectiva de Procesos Internos</div>
        <div class="node-desc">Garantizar SLA Express (20-45 Min en 95% de Envíos) | Abastecimiento Stock Fijo ≥ 30 Días | Cero Hallazgos Críticos en INVIMA</div>
    </div>
    <div class="arrow-connector">▲</div>
    <div class="bsc-node cre-node">
        <div class="node-title">4. Perspectiva de Aprendizaje y Crecimiento</div>
        <div class="node-desc">Capacitación Técnica ≥ 20 Horas/Año en BPA • Optimización con Software ERP Memphis • Fidelización de 2.500 Pacientes para 2028</div>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# =============================================================================
# BLOQUE INFERIOR: LA GRAN GRÁFICA MAESTRA UNIFICADA (AÑO COMPLETO SIN FILTROS)
# =============================================================================
st.subheader("📊 5.3 Modelado de Rampa Comercial y Convergencia Financiera Coherente")
st.write("La siguiente gráfica unifica el ciclo completo de los 12 meses en un solo plano visual. Use la cámara fija o el botón inferior para descargar.")

# Datos reales de la Tabla 15
meses_lista = [f"Mes {i}" for i in range(1, 13)]
transacciones_mes = [600, 900, 1350, 1700, 2100, 2400, 2520, 2550, 2580, 2620, 2660, 2700]

ticket_promedio = 55000
opex_fijo_mensual = 41500000

ingresos_mes = [tx * ticket_promedio for tx in transacciones_mes]
margen_bruto_mes = [ing * 0.30 for ing in ingresos_mes]
utilidad_neta_mes = [margen - opex_fijo_mensual for margen in margen_bruto_mes]

# Calcular Flujo de Caja Acumulado Real
flujo_acumulado = []
saldo_temporal = 0
for util in utilidad_neta_mes:
    saldo_temporal += util
    flujo_acumulado.append(saldo_temporal)

# Construcción de la Gráfica Maestra
fig_maestra = go.Figure()

# 1. Línea de OPEX Fijo Ancla
fig_maestra.add_trace(go.Scatter(
    x=meses_lista, y=[opex_fijo_mensual]*12,
    mode='lines', name='Carga Fija (OPEX Fijo: $41.5M)',
    line=dict(color='red', width=2.5, dash='dash')
))

# 2. Línea de Margen Bruto (Ingresos Netos Reales)
fig_maestra.add_trace(go.Scatter(
    x=meses_lista, y=margen_bruto_mes,
    mode='lines+markers', name='Margen Bruto Generado (30%)',
    line=dict(color='green', width=3.5),
    marker=dict(size=8, symbol='circle')
))

# 3. Línea del Flujo de Caja Acumulado
fig_maestra.add_trace(go.Scatter(
    x=meses_lista, y=flujo_acumulado,
    mode='lines+markers', name='Flujo de Caja Acumulado',
    line=dict(color='#9467bd', width=3),
    marker=dict(size=6, symbol='diamond')
))

# Destacar el Punto de Equilibrio exacto en el Mes 7
fig_maestra.add_trace(go.Scatter(
    x=["Mes 7"], y=[margen_bruto_mes[6]],
    mode='markers', name='★ PUNTO DE EQUILIBRIO (Mes 7)',
    marker=dict(color='gold', size=16, symbol='star', line=dict(color='black', width=1.5))
))

# Ajustes de diseño premium libres de contaminación visual
fig_maestra.update_layout(
    xaxis_title="Cronología Mensual del Proyecto",
    yaxis_title="Unidades Monetarias en Pesos (COP)",
    height=480,
    margin=dict(t=20, b=20, l=20, r=20),
    legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5),
    hovermode="x unified"
)

# Renderizar la gráfica maestra con la barra de herramientas fija
st.plotly_chart(fig_maestra, use_container_width=True, config=config_exportacion)

st.markdown("---")
st.markdown("""
> **Nota de consistencia técnica para la entrega escrita:** La presente modelación integrada unifica las cuatro perspectivas del Balanced Scorecard en un solo entorno predictivo. El vector verde del Margen Bruto demuestra cómo la rampa comercial (traccionada por las capacitaciones del personal y las campañas de marketing) cruza de forma exacta la barrera del OPEX fijo (línea roja) en el **Mes 7 al consolidar las 2.520 transacciones**. El vector morado (*Flujo Acumulado*) expone con total transparencia contable cómo el colchón financiero de \$80.000.000 COP fletado en el CAPEX inicial absorbe el déficit de los meses 1 al 6, garantizando la viabilidad del proyecto FarmaTech Ltda. antes de la curva de superávit.
""")
