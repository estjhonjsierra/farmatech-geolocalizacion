import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Configuración inicial forzando el diseño responsive de pantalla completa
st.set_page_config(page_title="FarmaTech - Maqueta 3D HD", layout="wide")

# Control geométrico para eliminar márgenes muertos laterales y optimizar la visualización
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
🛒 **Zona Dispensación (20 m²):** Mostradores, vitrinas y 3 terminales POS.
📦 **Bodega General (15 m²):** Estantería metálica con inventario clasificado.
👨‍⚕️ **Consultoría QF (8 m²):** Módulo privado para atención clínica.
🛵 **Nodo Logístico (8 m²):** Alistamiento y empaque de domicilios.
🏢 **Administración (6 m²):** Estación de control de sistemas ERP.
❄️ **Cadena de Frío (6 m²):** Neveras con stock térmico controlado.
📥 **Recepción/Cuarentena (5 m²):** Estibas de madera y mesa de inspección.
⚠️ **Unidad Residuos (4 m²):** Depósito y guardián de Punto Azul.
🥼 **Servicios/Vestier (4 m²):** Casilleros e higiene del personal.
🚶 **Circulación (4 m²):** Pasillos de interconexión técnica.
""")

st.sidebar.markdown("---")
st.sidebar.subheader("📸 Herramientas de Reporte")
if st.sidebar.button("📷 Guardar Maqueta de Ingeniería 3D (PDF)"):
    st.components.v1.html("<script>window.parent.print();</script>", height=0, width=0)

# --- CUERPO PRINCIPAL DEL DASHBOARD ---
st.markdown(f"""
    <div style="background-color: #f8f9fa; padding: 25px; border-radius: 8px; border-left: 6px solid #117a65; margin-bottom: 25px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
        <h2 style="margin: 0; color: #1c2833; font-family: Arial, sans-serif;">📐 Modelado Físico y Distribución Industrial de Detalle (80 m²)</h2>
        <p style="margin: 5px 0 0 0; color: #566573; font-size: 15px;">FarmaTech Ltda. &mdash; Simulación Realista de Estructuras, Mobiliario y Equipamiento de Planta (BPA Compliance).</p>
    </div>
""", unsafe_allow_html=True)

# --- BASE DE DATOS GEOMÉTRICA DE ÁREAS (80 m² Totales, Prismas Rectangulares Perfectos) ---
zonas_3d = [
    {"name": "Zona de Dispensación y Atención", "x_range": [0, 8], "y_range": [0, 2.5], "z_range": [0, 2.5], "area": 20, "color": "#a2d149", "desc": "Área comercial frontal orientada al usuario presencial."},
    {"name": "Bodega de Almacenamiento General", "x_range": [0, 4], "y_range": [2.5, 6.25], "z_range": [0, 2.5], "area": 15, "color": "#fcd12a", "desc": "Custodia técnica de stock mayorista (30-45 días de inventario)."},
    {"name": "Módulo de Consulta Farmacéutica (QF)", "x_range": [4, 8], "y_range": [2.5, 4.5], "z_range": [0, 2.5], "area": 8, "color": "#3498db", "desc": "Módulo privado para programas de lealtad y seguimiento a pacientes crónicos."},
    {"name": "Nodo Logístico de Alistamiento", "x_range": [4, 8], "y_range": [4.5, 6.5], "z_range": [0, 2.5], "area": 8, "color": "#bb8fce", "desc": "Centro de picking, empaque y despacho de pedidos omnicanal por WhatsApp."},
    {"name": "Área Administrativa y Control Central", "x_range": [0, 2.4], "y_range": [6.25, 8.75], "z_range": [0, 2.5], "area": 6, "color": "#b2babb", "desc": "Oficina administrativa y servidores de control central ERP."},
    {"name": "Cuarto de Cadena de Frío", "x_range": [2.4, 4.8], "y_range": [6.25, 8.75], "z_range": [0, 2.5], "area": 6, "color": "#5dedec", "desc": "Aislamiento térmico para la custodia de medicamentos termolábiles."},
    {"name": "Bahía de Recepción y Cuarentena", "x_range": [4.8, 6.8], "y_range": [6.25, 8.75], "z_range": [0, 2.5], "area": 5, "color": "#d4efdf", "desc": "Área técnica de descargue y muestreo organoléptico de lotes nuevos."},
    {"name": "Unidad de Bioseguridad y Punto Azul", "x_range": [6.8, 8], "y_range": [6.5, 9.83], "z_range": [0, 2.5], "area": 4, "color": "#ec7063", "desc": "Depósito de residuos hospitalarios peligrosos y punto ecológico posconsumo."},
    {"name": "Servicios Sanitarios y Vestier", "x_range": [0, 1.6], "y_range": [8.75, 11.25], "z_range": [0, 2.5], "area": 4, "color": "#f5cba7", "desc": "Higiene y bienestar físico para el personal operativo (BPA)."},
    {"name": "Corredores y Circulación Interna", "x_range": [1.6, 6.8], "y_range": [8.75, 9.53], "z_range": [0, 0.05], "area": 4, "color": "#d5f5e3", "desc": "Pasillos demarcados para tránsito seguro de personal y carros de carga."}
]

# --- 🚀 NUEVA BASE DE DATOS DE MOBILIARIO REALISTA EN 3D SÓLIDO (CUBOS INDEPENDIENTES REALES) ---
mobiliario_3d = [
    # Mostrador Comercial Frontal en Zona de Dispensación
    {"name": "🛋️ Mostrador Ergonómico POS Principal", "x": [1.0, 7.0], "y": [1.0, 1.6], "z": [0, 1.1], "color": "#ffffff", "desc": "Mesa de dispensación lineal que alberga las 3 cajas registradoras."},
    # Estanterías Industriales de la Bodega General
    {"name": "🛋️ Estantería Modular Pesada - Módulo A", "x": [0.2, 0.8], "y": [2.8, 5.8], "z": [0, 2.2], "color": "#34495e", "desc": "Góndola metálica industrial para almacenamiento de medicamentos OTC."},
    {"name": "🛋️ Estantería Modular Pesada - Módulo B", "x": [1.4, 2.0], "y": [2.8, 5.8], "z": [0, 2.2], "color": "#34495e", "desc": "Góndola metálica industrial para medicamentos de prescripción crónica (SOM)."},
    # Mobiliario del Consultorio del Químico Farmacéutico (QF)
    {"name": "🛋️ Escritorio de Consulta Clínica QF", "x": [5.0, 7.0], "y": [3.0, 4.0], "z": [0, 0.8], "color": "#eaecee", "desc": "Módulo administrativo del Regente para atención personalizada."},
    # Mobiliario del Nodo Logístico de Domicilios
    {"name": "🛋️ Mesa Técnica de Alistamiento y Despacho", "x": [5.0, 7.0], "y": [5.0, 6.0], "z": [0, 0.9], "color": "#ebf5fb", "desc": "Superficie de embalaje, etiquetado y picking omnicanal."},
    # Equipamiento del Cuarto de Cadena de Frío
    {"name": "🛋️ Refrigerador Clínico Horizontal No. 1", "x": [2.6, 3.4], "y": [6.6, 8.4], "z": [0, 1.2], "color": "#d1f2eb", "desc": "Nevera de alta precisión con termohigrómetro integrado para insulinas."},
    {"name": "🛋️ Refrigerador Clínico Horizontal No. 2", "x": [3.8, 4.6], "y": [6.6, 8.4], "z": [0, 1.2], "color": "#d1f2eb", "desc": "Nevera de alta precisión para custodia estable de biológicos y vacunas."},
    # Equipamiento de la Bahía de Recepción y Cuarentena
    {"name": "🛋️ Mesa de Inspección de Acero Inoxidable", "x": [5.0, 6.6], "y": [6.6, 7.6], "z": [0, 0.9], "color": "#bdc3c7", "desc": "Superficie aséptica para la validación y muestreo de lotes mayoristas."},
    {"name": "🛋️ Estiba de Madera Regulada (Cuarentena)", "x": [5.0, 6.6], "y": [7.8, 8.6], "z": [0, 0.15], "color": "#ba4a00", "desc": "Plataforma de aislamiento del suelo exigida por las Buenas Prácticas (BPA)."},
    # Contenedor Autorizado Punto Azul en Unidad de Residuos
    {"name": "🛋️ Módulo de Depósito y Contenedor Punto Azul", "x": [7.0, 7.8], "y": [7.0, 8.0], "z": [0, 1.4], "color": "#f1c40f", "desc": "Contenedor de recolección selectiva posconsumo autorizado por la Resolución 0371 de 2009."}
]

# --- FUNCIÓN GEOMÉTRICA DE PRISMAS SÓLIDOS PERFECTOS ---
def construir_solido_hd(fig, x_rng, y_rng, z_rng, color, name, hover_text, opacidad, grosor_borde):
    # Coordenadas ordenadas de los 8 vértices del prisma rectangular
    x = [x_rng[0], x_rng[1], x_rng[1], x_rng[0], x_rng[0], x_rng[1], x_rng[1], x_rng[0]]
    y = [y_rng[0], y_rng[0], y_rng[1], y_rng[1], y_rng[0], y_rng[0], y_rng[1], y_rng[1]]
    z = [z_rng[0], z_rng[0], z_rng[0], z_rng[0], z_rng[1], z_rng[1], z_rng[1], z_rng[1]]
    
    # Índices fijos de Plotly para renderizar las 6 caras del cubo sin errores de triangulación
    i = [0, 0, 0, 1, 1, 2, 4, 4, 4, 5, 5, 6]
    j = [1, 2, 3, 2, 5, 3, 5, 6, 7, 6, 1, 7]
    k = [2, 3, 7, 5, 6, 7, 6, 7, 3, 1, 2, 3]
    
    # Trace 1: Cuerpo sólido opaco del cuarto/mueble
    fig.add_trace(go.Mesh3d(
        x=x, y=y, z=z, i=i, j=j, k=k,
        color=color,
        opacity=opacidad,
        name=name,
        text=hover_text,
        hoverinfo="text",
        flatshading=True,
        lighting=dict(ambient=0.7, diffuse=0.6, roughness=0.2, specular=0.1)
    ))
    
    # Trace 2: Efecto Wireframe de Alta Definición (Líneas de contorno/paredes negras)
    # Conecta los vértices para dibujar las aristas y darle hiperrealismo de diseño industrial
    lineas_x = [x[0], x[1], x[2], x[3], x[0], x[4], x[5], x[1], x[5], x[6], x[2], x[6], x[7], x[3], x[7], x[4]]
    lineas_y = [y[0], y[1], y[2], y[3], y[0], y[4], y[5], y[1], y[5], y[6], y[2], y[6], y[7], y[3], y[7], y[4]]
    lineas_z = [z[0], z[1], z[2], z[3], z[0], z[4], z[5], z[1], z[5], z[6], z[2], z[6], z[7], z[3], z[7], z[4]]
    
    fig.add_trace(go.Scatter3d(
        x=lineas_x, y=lineas_y, z=lineas_z,
        mode="lines",
        line=dict(color="black", width=grosor_borde),
        hoverinfo="skip",
        showlegend=False
    ))

# Instanciación del mapa tridimensional
fig = go.Figure()

# 1. CAPA BASE: Renderizar las paredes de los cuartos técnicos (Opacidad media para ver el interior)
for zona in zonas_3d:
    html_zona = f"<b>{zona['name']}</b><br>Área: {zona['area']} m²<br>Infraestructura: Techo a 2.5m<br>{zona['desc']}"
    construir_solido_hd(fig, zona["x_range"], zona["y_range"], zona["z_range"], zona["color"], zona["name"], html_zona, opacidad=0.35, grosor_borde=1.5)

# 2. 🔥 CAPA SUPERIOR: Renderizar el Mobiliario y la Mercancía en 3D Sólido Real (Opacidad alta y bordes gruesos)
for mob in mobiliario_3d:
    html_mob = f"<b>{mob['name']}</b><br>{mob['desc']}<br>Dimensiones y ubicación métrica exacta."
    construir_solido_hd(fig, mob["x"], mob["y"], mob["z"], mob["color"], mob["name"], html_mob, opacidad=0.95, grosor_borde=3.0)

# Configuración técnica del entorno de visualización y cámara isométrica
fig.update_layout(
    title=dict(text="🏢 Distribución de Planta de Detalle e Ingeniería de Mobiliario (Layout Realista 3D HD)", font=dict(size=18)),
    scene=dict(
        xaxis=dict(title="Frente Comercial (Metros)", range=[-0.5, 8.5], dtick=1, backgroundcolor="rgb(245, 245, 245)", gridcolor="rgba(0,0,0,0.1)", showbackground=True),
        yaxis=dict(title="Fondo Comercial (Metros)", range=[-0.5, 11.5], dtick=1, backgroundcolor="rgb(235, 235, 235)", gridcolor="rgba(0,0,0,0.1)", showbackground=True),
        zaxis=dict(title="Altura Locativa (Metros)", range=[0, 3.5], dtick=1, backgroundcolor="rgb(225, 225, 225)", gridcolor="rgba(0,0,0,0.1)", showbackground=True),
        camera=dict(
            eye=dict(x=1.35, y=-1.35, z=1.55), # Ángulo isométrico perfecto que revela el interior
            up=dict(x=0, y=0, z=1)
        ),
        aspectmode="data"
    ),
    margin=dict(l=10, r=10, t=50, b=10),
    template="plotly_white",
    height=680,
    hoverlabel=dict(bgcolor="white", font_size=13, font_family="Arial")
)

# Proyectar el entorno de producción en Streamlit Cloud
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
