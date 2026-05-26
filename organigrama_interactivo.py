import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# =============================================================================
# 1. CONFIGURACIÓN ESTRUCTURAL DE ALTA DEFINICIÓN (UI/UX)
# =============================================================================
st.set_page_config(
    page_title="FarmaTech - Enterprise Suite",
    layout="wide",
    page_icon="🏢"
)

# Inyección de CSS Avanzado para simular una Plataforma ERP/Estatutaria Corporativa
st.markdown("""
    <style>
    /* Estilos Generales de la Suite */
    .main-title { font-family: 'Helvetica Neue', Arial, sans-serif; color: #1e3d59; font-weight: 800; font-size: 2.6rem; margin-bottom: 0.1rem; }
    .section-desc { color: #6c757d; font-size: 1.05rem; margin-bottom: 1.5rem; }
    
    /* Diseño de Contenedores de Perspectiva Cuántica (Balanced Scorecard) */
    .quantum-card {
        padding: 22px;
        border-radius: 14px;
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
        margin: 12px auto;
        max-width: 750px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.08);
    }
    .f-node { background: linear-gradient(135deg, #1e3d59 0%, #112233 100%); border-left: 8px solid #00d2ff; }
    .c-node { background: linear-gradient(135deg, #ff7f0e 0%, #b35900 100%); border-left: 8px solid #ffe600; }
    .p-node { background: linear-gradient(135deg, #2ca02c 0%, #175217 100%); border-left: 8px solid #00ffcc; }
    .a-node { background: linear-gradient(135deg, #9467bd 0%, #52356b 100%); border-left: 8px solid #f000ff; }
    
    .q-title { font-size: 1.25rem; font-weight: bold; text-transform: uppercase; letter-spacing: 1.5px; }
    .q-desc { font-size: 0.95rem; opacity: 0.9; margin-top: 5px; }
    .q-indicator { font-size: 0.8rem; background: rgba(255,255,255,0.2); padding: 2px 8px; border-radius: 20px; display: inline-block; margin-top: 8px; }
    .arrow-q { text-align: center; font-size: 2.2rem; color: #1e3d59; font-weight: bold; margin: -5px 0; }

    /* Estilización de los Nodos del Organigrama Interactivo */
    div.stButton > button {
        width: 100%;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 1.1rem !important;
        font-weight: bold !important;
        padding: 14px !important;
        border-radius: 10px !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    div.stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 14px rgba(0,0,0,0.15);
    }
    </style>
""", unsafe_allow_html=True)

# Parámetros universales fijos de descarga (Cámara fotográfica activa en HD 📸)
config_exportacion = {
    'displayModeBar': True,
    'displaylogo': False,
    'modeBarButtonsToRemove': ['zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d'],
    'toImageButtonOptions': {
        'format': 'png',
        'filename': 'farmatech_suite_reporte',
        'height': 600,
        'width': 1100,
        'scale': 2
    }
}

# Inicialización obligatoria del control de estados del Organigrama Interactivo
if "cargo_activo" not in st.session_state:
    st.session_state.cargo_activo = "Ninguno"

# =============================================================================
# 2. ENTORNO LATERAL DE CONTROL E INDUCTORES (SIDEBAR SIMULATOR)
# =============================================================================
st.sidebar.header("🎛️ Centro de Simulación Cruzada")
st.sidebar.markdown("Modifique las variables operativas en tiempo real para estresar el Balanced Scorecard y las Métricas de Cargo.")

transacciones_reales_dia = st.sidebar.slider("Transacciones Reales Diarias (POS)", min_value=30, max_value=120, value=65, step=5)
horas_cap = st.sidebar.slider("Horas de Capacitación Anual / Empleado", min_value=0, max_value=40, value=20, step=2)
eficiencia_logistica = st.sidebar.slider("Eficiencia Operativa del Canal Domicilios (%)", min_value=50, max_value=100, value=95, step=5)

# Variables de referencia fijas (Consistencia con las Tablas 11, 12, 15 y 16)
ticket_promedio = 55000
opex_fijo_mensual = 41500000
meta_transacciones_dia = 84

# =============================================================================
# MÓDULO A: CUADRO DE MANDO INTEGRAL (BALANCED SCORECARD INTEGRADO)
# =============================================================================
st.markdown('<h1 class="main-title">🚀 Componente 1: Sistema del Balanced Scorecard e Impacto Unificado</h1>', unsafe_allow_html=True)
st.markdown('<p class="section-desc">Tabla 20. Simulación Cuántica de Relaciones de Causalidad Ascendente y Curvas de Caja (Meses 1 a 12)</p>', unsafe_allow_html=True)

col_nodes, col_curves = st.columns([1, 1.2])

with col_nodes:
    st.markdown("### 🎯 Mapa de Dependencia de Red")
    st.markdown("""
        <div class="quantum-card f-node">
            <div class="q-title">1. Perspectiva Financiera</div>
            <div class="q-desc">Punto de Equilibrio (84 Tx/Día • Mes 7) | Ingresos de \$1.339M Anuales | Margen Neto del 30%</div>
            <div class="q-indicator">Inductor Final de Éxito</div>
        </div>
        <div class="arrow-q">▲</div>
        <div class="quantum-card c-node">
            <div class="q-title">2. Perspectiva de Clientes</div>
            <div class="q-desc">Capturar el 15% del Nicho Crónico (675 Pacientes) | Sostener NPS ≥ 70 | Omnicanalidad del 40%</div>
            <div class="q-indicator">Fidelización y Atracción de Demanda</div>
        </div>
        <div class="arrow-q">▲</div>
        <div class="quantum-card p-node">
            <div class="q-title">3. Perspectiva de Procesos Internos</div>
            <div class="q-desc">SLA Express (20-45 Min en 95% de Envíos) | Stock Fijo ≥ 30 Días | Normatividad Seccional Salud</div>
            <div class="q-indicator">Estándar Operativo Logístico</div>
        </div>
        <div class="arrow-q">▲</div>
        <div class="quantum-card a-node">
            <div class="q-title">4. Perspectiva de Aprendizaje y Crecimiento</div>
            <div class="q-desc">Capacitación ≥ 20 Horas/Año en BPA | Optimización con Software ERP Memphis | Meta de 2.500 Pacientes para 2028</div>
            <div class="q-indicator">Motor Sostenible Inicial</div>
        </div>
    """, unsafe_allow_html=True)

with col_curves:
    st.markdown("### 📈 Figura 8. Curva Unificada de Rampa Comercial y Convergencia Contable")
    
    # Simulación dinámica del año completo parametrizada con los controles laterales
    meses_lista = [f"Mes {i}" for i in range(1, 13)]
    transacciones_mes = [600, 900, 1350, 1700, 2100, 2400, 2520, 2550, 2580, 2620, 2660, 2700]
    
    # Ajustar dinámicamente el comportamiento basándose en el slider del POS
    factor_ajuste = transacciones_reales_dia / 65.0
    transacciones_ajustadas = [int(tx * factor_ajuste) for tx in transacciones_mes]
    
    ingresos_mes = [tx * ticket_promedio for tx in transacciones_ajustadas]
    margen_bruto_mes = [ing * 0.30 for ing in ingresos_mes]
    utilidad_neta_mes = [margen - opex_fijo_mensual for margin, margen in zip(transacciones_ajustadas, margen_bruto_mes)]
    
    flujo_acumulado = []
    saldo_temporal = 0
    for util in utilidad_neta_mes:
        saldo_temporal += util
        flujo_acumulado.append(saldo_temporal)
        
    fig_maestra = go.Figure()
    # Línea de Costo OPEX Fijo Ancla
    fig_maestra.add_trace(go.Scatter(x=meses_lista, y=[opex_fijo_mensual]*12, mode='lines', name='OPEX Fijo Mensual (\$41.5M)', line=dict(color='red', width=2.5, dash='dash')))
    # Línea de Margen Bruto Generado
    fig_maestra.add_trace(go.Scatter(x=meses_lista, y=margen_bruto_mes, mode='lines+markers', name='Margen Bruto (30%)', line=dict(color='green', width=3.5)))
    # Línea del Flujo de Caja Acumulado
    fig_maestra.add_trace(go.Scatter(x=meses_lista, y=flujo_acumulado, mode='lines+markers', name='Flujo de Caja Acumulado', line=dict(color='#9467bd', width=3)))
    # Nodo de Equilibrio Mes 7
    fig_maestra.add_trace(go.Scatter(x=["Mes 7"], y=[margen_bruto_mes[6]], mode='markers', name='★ PUNTO DE EQUILIBRIO', marker=dict(color='gold', size=15, symbol='star', line=dict(color='black', width=1.5))))
    
    fig_maestra.update_layout(xaxis_title="Evolución Cronológica Mensual", yaxis_title="Pesos Colombianos (COP)", height=450, margin=dict(t=10, b=10, l=10, r=10), legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5), hovermode="x unified")
    st.plotly_chart(fig_maestra, use_container_width=True, config=config_exportacion)

st.markdown("---")

# =============================================================================
# MÓDULO B: SISTEMA DE ORGANIGRAMA FUNCIONAL INTERACTIVO
# =============================================================================
st.markdown('<h1 class="main-title">🏢 Componente 2: Estructura Orgánica y Manual de Funciones</h1>', unsafe_allow_html=True)
st.markdown('<p class="section-desc">Tabla 26. Panel de Consulta de Perfiles, Requisitos ReTHUS y Asignaciones Salariales — FarmaTech Ltda.</p>', unsafe_allow_html=True)

col_org, col_profile = st.columns([1.1, 1])

with col_org:
    st.markdown("### 🗺️ Tabla de Mandos y Organigrama")
    st.write("Haga clic directamente sobre cualquiera de los cargos estructurados de la empresa para desplegar su ficha de perfil.")
    
    # Fila de Gobierno Corporativo Superior
    st.markdown("<style>div[key='btn_junta'] > button { background: linear-gradient(135deg, #1e3d59 0%, #0f202e 100%) !important; border-bottom: 4px solid #00d2ff !important; }</style>", unsafe_allow_html=True)
    if st.button("👥 JUNTA DE SOCIOS — FarmaTech Ltda.\nJhon (20%) | Lucy (10%) | Danna (2.5%) | Mauricio (2.5%) | SENA (40%) | Ángel (25%)", key="btn_junta"):
        st.session_state.cargo_activo = "Junta"

