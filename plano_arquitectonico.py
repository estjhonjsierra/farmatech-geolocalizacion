import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Configuración inicial forzando el diseño responsive de pantalla completa
st.set_page_config(page_title="FarmaTech - Plano Ingeniería 3D", layout="wide")

# Control geométrico para eliminar márgenes muertos laterales
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

# --- PANEL DE CONTROL SIDEBAR ---
st.sidebar.header("⚙️ Control de Infraestructura e Ingeniería 3D")
st.sidebar.write("Modelado de volumetrías físicas y equipamiento técnico bajo normativas INVIMA, Decreto 2200/2005 y Resolución 1403/2007.")

st.sidebar.subheader("📐 Desglose Técnico de Áreas (80 m²)")
st.sidebar.markdown("""
🛒 **Zona Dispensación (20 m²):** Frente comercial, mostrador ergonómico y terminales POS.
📦 **Bodega General (15 m²):** Estantería industrial clasificada.
👨‍⚕️ **Consultoría QF (8 m²):** Módulo privado para atención.
🛵 **Nodo Logístico (8 m²):** Alistamiento de domicilios.
🏢 **Administración (6 m²):** Estación de control contable.
❄️ **Cadena de Frío (6 m²):** Cuarto técnico aislado con refrigeradores.
📥 **Recepción/Cuarentena (5 m²):** Bahía de inspección de lotes.
⚠️ **Unidad Residuos (4 m²):** Depósito y contenedor Punto Azul.
🥼 **Servicios/Vestier (4 m²):** Zona de higiene interna.
🚶 **Circulación (4 m²):** Pasillos técnicos unidireccionales.
""")

st.sidebar.markdown("---")
st.sidebar.subheader("📸 Herramientas de Reporte")
if st.sidebar.button("📷 Guardar Maqueta Técnica 3D (PDF)"):
    st.components.v1.html("<script>window.parent.print();</script>", height=0, width=0)

# --- CUERPO PRINCIPAL DEL DASHBOARD ---
st.markdown(f"""
    <div style="background-color: #f8f9fa; padding: 25px; border-radius: 8px; border-left: 6px solid #0056b3; margin-bottom: 25px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
        <h2 style="margin: 0; color: #1c2833; font-family: Arial, sans-serif;">📐 Plano Técnico y Modelado Volumétrico de Planta (80 m²)</h2>
        <p style="margin: 5px 0 0 0; color: #566573; font-size: 15px;">FarmaTech Ltda. &mdash; Maqueta de Ingeniería con Equipamiento Técnico Integrado (INVIMA Compliance).</p>
    </div>
""", unsafe_allow_html=True)

# --- BASE DE DATOS GEOMÉTRICA DE ÁREAS (80 m² Totales) ---
zonas_3d = [
    {"name": "Zona de Dispensación y Atención", "x_range": [0, 8], "y_range": [0, 2.5], "z_range": [0, 2.5], "area": 20, "color": "#2ca02c", "desc": "Área comercial. Mostrador ergonómico y 3 terminales POS."},
    {"name": "Bodega de Almacenamiento General", "x_range": [0, 4], "y_range": [2.5, 6.25], "z_range": [0, 2.5], "area": 15, "color": "#ff7f0e", "desc": "Custodia de inventarios. Estantería modular metálica clasificada."},
    {"name": "Módulo de Consulta Farmacéutica (QF)", "x_range": [4, 8], "y_range": [2.5, 4.5], "z_range": [0, 2.5], "area": 8, "color": "#1f77b4", "desc": "Asesoría privada. Escritorio clínico y base de datos para pacientes crónicos."},
    {"name": "Nodo Logístico de Alistamiento", "x_range": [4, 8], "y_range": [4.5, 6.5], "z_range": [0, 2.5], "area": 8, "color": "#9467bd", "desc": "Mesa de picking y embalaje de despachos para WhatsApp Business."},
    {"name": "Área Administrativa y Control Central", "x_range": [0, 2.4], "y_range": [6.25, 8.75], "z_range": [0, 2.5], "area": 6, "color": "#7f7f7f", "desc": "Oficina administrativa. Gestión contable, archivo y control ERP."},
    {"name": "Cuarto de Cadena de Frío", "x_range": [2.4, 4.8], "y_range": [6.25, 8.75], "z_range": [0, 2.5], "area": 6, "color": "#17becf", "desc": "Refrigeración técnica. Neveras horizontales calibradas de 2°C a 8°C."},
    {"name": "Bahía de Recepción y Cuarentena", "x_range": [4.8, 6.8], "y_range": [6.25, 8.75], "z_range": [0, 2.5], "area": 5, "color": "#bcbd22", "desc": "Estación de muestreo. Mesa de inspección física y estibas de cuarentena."},
    {"name": "Unidad de Bioseguridad y Punto Azul", "x_range": [6.8, 8], "y_range": [6.5, 9.83], "z_range": [0, 2.5], "area": 4, "color": "#d62728", "desc": "Área de residuos peligrosos y contenedor de fármacos posconsumo."},
    {"name": "Servicios Sanitarios y Vestier", "x_range": [0, 1.6], "y_range": [8.75, 11.25], "z_range": [0, 2.5], "area": 4, "color": "#e377c2", "desc": "Higiene y vestuario del personal conforme a parámetros de BPA."},
    {"name": "Corredores y Circulación Interna", "x_range": [1.6, 6.8], "y_range": [8.75, 9.53], "z_range": [0, 0.2], "area": 4, "color": "#8c564b", "desc": "Pasillos demarcados para tránsito seguro de personal y carros de carga."}
]

# --- BASE DE DATOS DE EQUIPAMIENTO TÉCNICO INTERNO INTERACTIVO ---
equipamiento_tecnico = [
    {"name": "🛠️ Mostrador de Atención y Terminales POS", "x": 4.0, "y": 1.2, "z": 1.0, "color": "white", "size": 10, "desc": "Estación comercial con 3 cajas registradoras ergonómicas."},
    {"name": "🛠️ Estanterías Metálicas de Almacenamiento", "x": 2.0, "y": 4.5, "z": 1.2, "color": "black", "size": 8, "desc": "Góndolas industriales de almacenamiento organizadas por acción terapéutica."},
    {"name": "🛠️ Escritorio de Consultoría Médica", "x": 6.0, "y": 3.5, "z": 0.8, "color": "white", "size": 8, "desc": "Módulo de atención individualizada para pacientes crónicos."},
    {"name": "🛠️ Estación de Picking y Embalaje", "x": 6.0, "y": 5.5, "z": 0.9, "color": "white", "size": 8, "desc": "Mesa técnica para organización y despacho de pedidos omnicanal."},
    {"name": "🛠️ Escritorio de Gestión Administrativa", "x": 1.2, "y": 7.5, "z": 0.8, "color": "black", "size": 8, "desc": "Puesto de control de tesorería, contabilidad y sistemas ERP."},
    {"name": "🛠️ Refrigeradores Horizontales Clínicos", "x": 3.6, "y": 7.5, "z": 1.1, "color": "cyan", "size": 9, "desc": "Neveras horizontales certificadas INVIMA con rango estable de 2°C a 8°C."},
    {"name": "🛠️ Mesa de Muestreo e Inspección", "x": 5.8, "y": 7.5, "z": 0.9, "color": "black", "size": 8, "desc": "Superficie de acero inoxidable para validación organoléptica de lotes."},
    {"name": "🛠️ Contenedor Autorizado Punto Azul", "x": 7.4, "y": 8.1, "z": 1.3, "color": "yellow", "size": 10, "desc": "Depósito regulado por la Res. 0371/2009 para descarte de medicamentos vencidos."}
]

# --- FUNCION GEOMÉTRICA DE SÓLIDOS PERFECTOS ---
def construir_cubo_tecnico(fig, x_rng, y_rng, z_rng, color, name, hover_text):
    # Generación indexada de las 6 caras cuadradas de un prisma para evitar distorsiones visuales
    x = [x_rng[0], x_rng[1], x_rng[1], x_rng[0], x_rng[0], x_rng[1], x_rng[1], x_rng[0]]
    y = [y_rng[0], y_rng[0], y_rng[1], y_rng[1], y_rng[0], y_rng[0], y_rng[1], y_rng[1]]
    z = [z_rng[0], z_rng[0], z_rng[0], z_rng[0], z_rng[1], z_rng[1], z_rng[1], z_rng[1]]
    
    i = [0, 0, 0, 1, 1, 2, 2, 3, 3, 0, 0, 4]
    j = [1, 2, 3, 2, 5, 3, 6, 0, 7, 4, 5, 5]
    k = [2, 3, 7, 5, 6, 6, 7, 4, 4, 5, 1, 6]
    
    fig.add_trace(go.Mesh3d(
        x=x, y=y, z=z, i=i, j=j, k=k,
        color=color,
        opacity=0.70,
        name=name,
        text=hover_text,
        hoverinfo="text",
        flatshading=True,
        lighting=dict(ambient=0.6, diffuse=0.6, roughness=0.3, specular=0.2)
    ))

# Instanciación del entorno gráfico 3D
fig = go.Figure()

# 1. Dibujar los cuartos técnicos funcionales con paredes tridimensionales sólidas
for zona in zonas_3d:
    info_html = f"<b>{zona['name']}</b><br>Área: {zona['area']} m²<br>Estructura: Techo a 2.5 metros<br>{zona['desc']}"
    construir_cubo_tecnico(fig, zona["x_range"], zona["y_range"], zona["z_range"], zona["color"], zona["name"], info_html)

# 2. Inyectar los elementos y equipamiento interior de ingeniería de la droguería
for eq in equipamiento_tecnico:
    hover_eq = f"<b>{eq['name']}</b><br>{eq['desc']}<br>Ubicación técnica: X={eq['x']}, Y={eq['y']}, Z={eq['z']}"
    
    fig.add_trace(go.Scatter3d(
        x=[eq["x"]], y=[eq["y"]], z=[eq["z"]],
        mode="markers",
        marker=dict(
            size=eq["size"],
            color=eq["color"],
            symbol="diamond",
            line=dict(color="black", width=2)
        ),
        name=eq["name"],
        text=hover_eq,
        hoverinfo="text"
    ))

# Ajustes de renderizado de la cámara y grillas de ingeniería
fig.update_layout(
    title=dict(text="🏢 Distribución Arquitectónica e Ingeniería de Planta (Layout Industrial 3D)", font=dict(size=18)),
    scene=dict(
        xaxis=dict(title="Frente Comercial (Metros)", range=[-0.5, 8.5], dtick=1, backgroundcolor="rgb(245, 245, 245)", gridcolor="white", showbackground=True),
        yaxis=dict(title="Fondo Comercial (Metros)", range=[-0.5, 11.5], dtick=1, backgroundcolor="rgb(235, 235, 235)", gridcolor="white", showbackground=True),
        zaxis=dict(title="Altura Locativa (Metros)", range=[0, 3.5], dtick=1, backgroundcolor="rgb(225, 225, 225)", gridcolor="white", showbackground=True),
        camera=dict(
            eye=dict(x=1.5, y=-1.5, z=1.7), # Ángulo isométrico de control óptimo
            up=dict(x=0, y=0, z=1)
        ),
        aspectmode="data"
    ),
    margin=dict(l=10, r=10, t=50, b=10),
    template="plotly_white",
    height=650,
    hoverlabel=dict(bgcolor="white", font_size=13, font_family="Arial")
)

# Proyectar el entorno interactivo final
st.plotly_chart(fig, use_container_width=True)

# --- CUADRO DE VALIDACIÓN SANITARIA (POR FUERA DEL MAPA) ---
st.markdown("### 📋 Verificación de Parámetros de Infraestructura (INVIMA Compliance)")
c1, c2 = st.columns(2)

with c1:
    st.info("""
    🔒 **Garantía del Flujo Unidireccional de Mercancías:**
    La disposición física de las áreas (Recepción ➡️ Cuarentena ➡️ Almacenamiento Bodega / Cuarto Frío ➡️ Dispensación / Logística) impide los cruces de contaminación. La mercancía ingresa de forma técnica por la zona de carga trasera, se valida microbiológica y físicamente, y pasa a custodia, respetando las Buenas Prácticas de Almacenamiento (BPA) de la **Resolución 1403 de 2007**.
    """)

with c2:
    st.warning("""
    ⚠️ **Sustento del Presupuesto de Adecuación ($40M COP):**
    La habilitación física de estos 80 m² demanda intervenciones civiles específicas cubiertas por el CAPEX del proyecto: instalación de pisos epóxicos asépticos de media caña, sistemas de aire acondicionado con renovación de flujo para control térmico, termohigrómetros con calibración digital y la adecuación de la cabina aislada de Bioseguridad para el Punto Azul de residuos peligrosos.
    """)
