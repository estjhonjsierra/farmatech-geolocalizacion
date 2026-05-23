import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 1. CONFIGURACIÓN PREMIUM DE LA INTERFAZ DE USUARIO
st.set_page_config(
    page_title="FarmaTech - Quantum BSC Dashboard",
    layout="wide",
    page_icon="🛸"
)

# Inyección de CSS avanzado para interacciones realistas y diseño de vanguardia
st.markdown("""
    <style>
    .main-title { font-family: 'Helvetica Neue', Arial, sans-serif; color: #1e3d59; font-weight: 800; font-size: 2.5rem; margin-bottom: 0.2rem; }
    .section-desc { color: #6c757d; font-size: 1.05rem; margin-bottom: 1.5rem; }
    
    /* Efecto hover y diseño para los nodos interactivos */
    .quantum-card {
        padding: 22px;
        border-radius: 14px;
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
        margin: 12px auto;
        max-width: 750px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .quantum-card:hover {
        transform: scale(1.02);
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        cursor: pointer;
    }
    
    .f-node { background: linear-gradient(135deg, #1e3d59 0%, #112233 100%); border-left: 8px solid #00d2ff; }
    .c-node { background: linear-gradient(135deg, #ff7f0e 0%, #b35900 100%); border-left: 8px solid #ffe600; }
    .p-node { background: linear-gradient(135deg, #2ca02c 0%, #175217 100%); border-left: 8px solid #00ffcc; }
    .a-node { background: linear-gradient(135deg, #9467bd 0%, #52356b 100%); border-left: 8px solid #f000ff; }
    
    .q-title { font-size: 1.25rem; font-weight: bold; text-transform: uppercase; letter-spacing: 1.5px; }
    .q-desc { font-size: 0.95rem; opacity: 0.9; margin-top: 5px; }
    .q-indicator { font-size: 0.8rem; background: rgba(255,255,255,0.2); padding: 2px 8px; border-radius: 20px; display: inline-block; margin-top: 8px; }
    
    .arrow-q { text-align: center; font-size: 2.2rem; color: #1e3d59; animation: pulse 2s infinite; font-weight: bold; margin: -5px 0; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🛸 Módulo de Causalidad Cuántica — Balanced Scorecard (BSC)</h1>', unsafe_allow_html=True)
st.markdown('<p class="section-desc">Tabla 20. Sistema de Simulación de Impacto Transversal en Cascada de Metas — FarmaTech Ltda.</p>', unsafe_allow_html=True)
st.markdown("---")

# Configuración universal para descarga de reportes (Cámara 📸 activa)
config_exportacion = {
    'displayModeBar': True,
    'toImageButtonOptions': {
        'format': 'png',
        'filename': 'farmatech_quantum_causality',
        'height': 600,
        'width': 1100,
        'scale': 2
    }
}

# 2. CONTROLES MAESTROS EN EL SIDEBAR
st.sidebar.header("🎛️ Moduladores de Energía Operativa")
st.sidebar.markdown("Manipule los inductores primarios para proyectar el impacto en la red corporativa.")

horas_cap = st.sidebar.slider("Horas de Capacitación Anual / Empleado", min_value=0, max_value=40, value=20, step=2)
eficiencia_procesos = st.sidebar.slider("Eficiencia Operativa del Canal Domicilios (%)", min_value=50, max_value=100, value=95, step=5)

# 3. CONSTRUCCIÓN DE LA ARQUITECTURA INTERACTIVA (HTML NODES)
col_mapa, col_simulacion = st.columns()

with col_mapa:
    st.subheader("🎯 Mapa de Nodos Estratégicos")
    st.write("Haga clic en los selectores inferiores para activar la trazabilidad analítica de cada perspectiva.")
    
    # Renderizar las hermosas cajas degradadas premium
    st.markdown("""
        <div class="quantum-card f-node">
            <div class="q-title">1. Perspectiva Financiera</div>
            <div class="q-desc">Punto de Equilibrio (84 Tx/Día) • Ingresos de \$891M • Margen Neto Sostenido del 30%</div>
            <div class="q-indicator">Inductor Final de Éxito Corporativo</div>
        </div>
        <div class="arrow-q">▲</div>
        <div class="quantum-card c-node">
            <div class="q-title">2. Perspectiva de Clientes</div>
            <div class="q-desc">Capturar 15% del Nicho Crónico (675 Clientes) • NPS ≥ 70 • Omnicanalidad Digital del 40%</div>
            <div class="q-indicator">Fidelización y Atracción de Demanda</div>
        </div>
        <div class="arrow-q">▲</div>
        <div class="quantum-card p-node">
            <div class="q-title">3. Perspectiva de Procesos Internos</div>
            <div class="q-desc">SLA Express (20-45 Min en 95% de Envíos) • Stock Fijo ≥ 30 Días • Habilitación Sanitaria INVIMA</div>
            <div class="q-indicator">Estándar de Calidad y Logística de Última Milla</div>
        </div>
        <div class="arrow-q">▲</div>
        <div class="quantum-card a-node">
            <div class="q-title">4. Perspectiva de Aprendizaje y Crecimiento</div>
            <div class="q-desc">Capacitación Técnica Avanzada • Optimización del ERP Memphis • Meta de 2.500 Pacientes para 2028</div>
            <div class="q-indicator">Motor Sostenible e Inductor de Competitividad Inicial</div>
        </div>
    """, unsafe_allow_html=True)

# =============================================================================
# EL COMPONENTE INÉDITO: EL MOTOR DE IMPACTO CUÁNTICO EN TIEMPO REAL
# =============================================================================
with col_simulacion:
    st.subheader("🔮 Centro de Trazabilidad e Impacto en Cascada")
    
    # El selector interactivo que simula los clics en los bloques
    nodo_seleccionado = st.radio(
        "Seleccione un Nodo del Balanced Scorecard para disparar la simulación de impacto:",
        ["Ninguno - Estado Neutro", "4. Aprendizaje y Crecimiento", "3. Procesos Internos", "2. Clientes", "1. Financiera"],
        index=0
    )
    
    st.markdown("---")
    
    if nodo_seleccionado == "Ninguno - Estado Neutro":
        st.info("💡 **Sistema en Espera:** Seleccione una perspectiva para analizar cómo sus indicadores empujan, estresan y modifican de forma automática al resto de la organización en una cadena de causalidad real.")
        
    elif nodo_seleccionado == "4. Aprendizaje y Crecimiento":
        st.markdown("### 🧬 Simulación de Impacto: Aprendizaje → Procesos")
        st.write(f"Al programar `{horas_cap} horas` de capacitación en Buenas Prácticas de Almacenamiento (BPA), el sistema proyecta matemáticamente los siguientes efectos multiplicadores:")
        
        # Fórmulas predictivas basadas en las horas de capacitación de la barra lateral
        reduccion_errores = horas_cap * 2.2
        mejora_inventario = min(100.0, 70.0 + (horas_cap * 0.75))
        
        st.success(f"✔️ **Reducción de Errores de Dispensación:** Disminución proyectada del **{reduccion_errores:.1f}%** en confusiones de lotes.")
        st.success(f"✔️ **Eficiencia en Custodia de Stock:** Precisión del inventario físico contra el ERP Memphis estimada en un **{mejora_inventario:.1f}%**.")
        
        # Gráfica lineal interactiva instantánea que modela esta causalidad predictiva
        horas_rango = np.arange(0, 41, 2)
        errores_rango = 100 - (horas_rango * 2.2)
        fig_cap = go.Figure()
        fig_cap.add_trace(go.Scatter(x=horas_rango, y=errores_rango, mode='lines', name='Curva de Error', line=dict(color='#9467bd', width=3)))
        fig_cap.add_trace(go.Scatter(x=[horas_cap], y=[100 - reduccion_errores], mode='markers', name='Tu Impacto Actual', marker=dict(color='red', size=12, symbol='diamond')))
        fig_cap.update_layout(title="Impacto del Aprendizaje sobre la Tasa de Error Interno", xaxis_title="Horas de Capacitación", yaxis_title="Índice de Error Residual (%)", height=250, margin=dict(t=30,b=10,l=10,r=10))
        st.plotly_chart(fig_cap, use_container_width=True, config=config_exportacion)

    elif nodo_seleccionado == "3. Procesos Internos":
        st.markdown("### 🏍️ Simulación de Impacto: Procesos → Clientes")
        st.write(f"Con una eficiencia logística del `{eficiencia_procesos}%` en la flota de motocicletas, se altera directamente la percepción del usuario en Laureles-Estadio:")
        
        # Relación causal predictiva entre logística y satisfacción (NPS)
        nps_proyectado = 50 + (eficiencia_procesos * 0.35)
        st.warning(f"⭐ **Índice de Satisfacción Neto (NPS) Estimado:** El modelo predice un comportamiento de **{nps_proyectado:.0f} puntos NPS** gracias al cumplimiento del rango de 20-45 minutos.")
        st.warning(f"⭐ **Retención del Nicho Crónico:** Probabilidad de recompra mensual estabilizada en un **{eficiencia_procesos:.1f}%**.")

    elif nodo_seleccionado == "2. Clientes":
        st.markdown("### 👥 Simulación de Impacto: Clientes → Financiera")
        st.write(f"Bajo el escenario actual de fidelización de la base de datos de pacientes crónicos, se proyecta la masa crítica transaccional:")
        
        # Simular volumen de ventas en base al slider de satisfacción de la barra lateral
        ventas_fidelizadas = int(1200 + (nps_actual * 15.5))
        ingresos_derivados = ventas_fidelizadas * 55000
        
        st.info(f"📈 **Masa Transaccional Traccionada:** El flujo de clientes fidelizados arrastra **{ventas_fidelizadas:,} transacciones anuales**.")
        st.info(f"📈 **Inyección al Estado de Resultados:** Facturación complementaria estimada en **\${ingresos_derivados:,.0f} COP**.")

    elif nodo_seleccionado == "1. Financiera":
        st.markdown("### 💰 El Hito del Cierre: Viabilidad del Proyecto")
        st.write("La perspectiva financiera consolida el éxito total de los inductores anteriores. Si los nodos 4, 3 y 2 operan de forma óptima, el modelo económico responde de la siguiente manera:")
        
        # Tarjetas de estado financiero final
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            st.metric(label="OPEX Fijo Mensual Unificado", value="\$41,500,000 COP")
        with col_f2:
