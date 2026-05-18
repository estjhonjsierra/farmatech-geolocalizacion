import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Configuración inicial forzando el diseño responsive de pantalla completa
st.set_page_config(page_title="FarmaTech - Infraestructura 3D Avanzada", layout="wide")

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
st.sidebar.write("Modelado volumétrico de alta fidelidad, inventarios y equipamiento técnico bajo normativas INVIMA.")

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
🚶 **Circulación (4 m²):** Pasillos demarcados unidireccionales.
""")

st.sidebar.markdown("---")
st.sidebar.subheader("📸 Herramientas de Reporte")
if st.sidebar.button("📷 Guardar Maqueta de Ingeniería 3D (PDF)"):
    st.components.v1.html("<script>window.parent.print();</script>", height=0, width=0)

# --- CUERPO PRINCIPAL DEL DASHBOARD ---
st.markdown(f"""
    <div style="background-color: #f8f9fa; padding: 25px; border-radius: 8px; border-left: 6px solid #117a65; margin-bottom: 25px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
        <h2 style="margin: 0; color: #1c2833; font-family: Arial, sans-serif;">📐 Modelado Físico y Distribución Industrial de Detalle (80 m²)</h2>
        <p style="margin: 5px 0 0 0; color: #566573; font-size: 15px;">FarmaTech Ltda. &mdash; Simulación de Activos Tangibles, Inventarios y Equipamiento de Planta (BPA Compliance).</p>
    </div>
""", unsafe_allow_html=True)

# --- BASE DE DATOS GEOMÉTRICA DE ÁREAS (80 m² Totales, Prismas Rectangulares Perfectos) ---
zonas_3d = [
    {"name": "Zona de Dispensación y Atención", "x_range":, "y_range": [0, 2.5], "z_range": [0, 2.5], "area": 20, "color": "#2ca02c", "desc": "Área comercial frontal orientada al usuario."},
    {"name": "Bodega de Almacenamiento General", "x_range":, "y_range": [2.5, 6.25], "z_range": [0, 2.5], "area": 15, "color": "#ff7f0e", "desc": "Custodia técnica de stock mayorista (30-45 días de inventario)."},
    {"name": "Módulo de Consulta Farmacéutica (QF)", "x_range":, "y_range": [2.5, 4.5], "z_range": [0, 2.5], "area": 8, "color": "#1f77b4", "desc": "Módulo privado para programas de lealtad y seguimiento a pacientes crónicos."},
    {"name": "Nodo Logístico de Alistamiento", "x_range":, "y_range": [4.5, 6.5], "z_range": [0, 2.5], "area": 8, "color": "#9467bd", "desc": "Centro de picking, empaque y despacho de pedidos omnicanal."},
    {"name": "Área Administrativa y Control Central", "x_range": [0, 2.4], "y_range": [6.25, 8.75], "z_range": [0, 2.5], "area": 6, "color": "#7f7f7f", "desc": "Oficina administrativa y servidores centralizados de sistemas ERP."},
    {"name": "Cuarto de Cadena de Frío", "x_range": [2.4, 4.8], "y_range": [6.25, 8.75], "z_range": [0, 2.5], "area": 6, "color": "#17becf", "desc": "Aislamiento térmico para la custodia de medicamentos termolábiles."},
    {"name": "Bahía de Recepción y Cuarentena", "x_range": [4.8, 6.8], "y_range": [6.25, 8.75], "z_range": [0, 2.5], "area": 5, "color": "#bcbd22", "desc": "Área técnica de descargue y muestreo organoléptico de lotes nuevos."},
    {"name": "Unidad de Bioseguridad y Punto Azul", "x_range": [6.8, 8], "y_range": [6.5, 9.83], "z_range": [0, 2.5], "area": 4, "color": "#d62728", "desc": "Depósito de residuos peligrosos y punto ecológico posconsumo."},
    {"name": "Servicios Sanitarios y Vestier", "x_range": [0, 1.6], "y_range": [8.75, 11.25], "z_range": [0, 2.5], "area": 4, "color": "#e377c2", "desc": "Higiene y bienestar físico para el personal operativo (BPA)."},
    {"name": "Corredores y Circulación Interna", "x_range": [1.6, 6.8], "y_range": [8.75, 9.53], "z_range": [0, 0.15], "area": 4, "color": "#8c564b", "desc": "Pasillos demarcados con pintura epóxica para tránsito continuo."}
]

# --- BASE DE DATOS DE EQUIPAMIENTO MOBILIARIO (Fijos Básicos) ---
equipamiento_fijo = [
    {"name": "🏢 Vitrinas y Mostrador Principal POS", "x": 4.0, "y": 1.2, "z": 1.0, "color": "#ffffff", "size": 11, "desc": "Estación comercial con 3 cajas ergonómicas."},
    {"name": "🏢 Escritorio Clínico QF", "x": 6.0, "y": 3.5, "z": 0.8, "color": "#ffffff", "size": 9, "desc": "Módulo privado del Regente Farmacéutico."},
    {"name": "🏢 Mesa de Empaque Logístico", "x": 6.0, "y": 5.5, "z": 0.9, "color": "#ffffff", "size": 9, "desc": "Superficie de alistamiento de domicilios de última milla."},
    {"name": "🏢 Escritorio Gerencial", "x": 1.2, "y": 7.5, "z": 0.8, "color": "#1c2833", "size": 9, "desc": "Puesto de control de tesorería y contabilidad."},
    {"name": "🏢 Refrigeradores Horizontales Clínicos", "x": 3.6, "y": 7.5, "z": 1.1, "color": "#00ffff", "size": 10, "desc": "Neveras certificadas con rango estable de 2°C a 8°C."},
    {"name": "🏢 Mesa de Recepción de Acero", "x": 5.8, "y": 7.5, "z": 0.9, "color": "#5d6d7e", "size": 9, "desc": "Superficie de muestreo y validación organoléptica de mercancías."},
    {"name": "🏢 Contenedor Autorizado Punto Azul", "x": 7.4, "y": 8.1, "z": 1.3, "color": "#f1c40f", "size": 12, "desc": "Depósito regulado (Res. 0371/2009) para medicamentos vencidos."}
]

# --- 🚀 NUEVA BASE DE DATOS DE ALTA DENSIDAD: INVENTARIOS Y DETALLES DE MERCANCÍA ---
inventario_detallado = [
    # Cajas de Mercancía en la Bodega General (Alta Densidad)
    {"name": "📦 Lote Medicamentos OTC: Analgésicos", "x": 1.0, "y": 3.5, "z": 0.6, "color": "#3498db", "desc": "Acetaminofén e Ibuprofeno (Alta Rotación). Stock: 45 días."},
    {"name": "📦 Lote Medicamentos OTC: Antigripales", "x": 1.0, "y": 4.5, "z": 0.6, "color": "#3498db", "desc": "Antigripales comunes en tabletas y jarabes. Stock en estantería."},
    {"name": "📦 Medicamentos Crónicos: Antihipertensivos", "x": 2.0, "y": 3.5, "z": 1.4, "color": "#58d68d", "desc": "Losartán y Enalapril (Portafolio especializado SOM)."},
    {"name": "📦 Medicamentos Crónicos: Diabetes", "x": 2.0, "y": 4.5, "z": 1.4, "color": "#58d68d", "desc": "Metformina y Glibenclamida para control de pacientes crónicos."},
    {"name": "📦 Elementos Complementarios: Cuidado Bebé", "x": 3.0, "y": 3.5, "z": 0.8, "color": "#f5b041", "desc": "Pañales y productos de higiene infantil de alta rotación."},
    {"name": "📦 Elementos Complementarios: Higiene Personal", "x": 3.0, "y": 4.5, "z": 0.8, "color": "#f5b041", "desc": "Champús, jabones y dermocosméticos básicos en góndola."},
    
    # Stock dentro del Cuarto de Cadena de Frío
    {"name": "🧊 Stock Clínico: Insulinas Glargina", "x": 3.2, "y": 7.2, "z": 1.5, "color": "#ffffff", "desc": "Custodia crítica en nevera 1. Rango térmico: 4.2°C verificado."},
    {"name": "🧊 Stock Clínico: Biológicos / Vacunas", "x": 4.0, "y": 7.2, "z": 1.5, "color": "#ffffff", "desc": "Custodia crítica en nevera 2. Monitoreo higrométrico permanente."},
    
    # Estibas y Mercancía en Recepción/Cuarentena
    {"name": "🪵 Estiba de Madera No. 1 (Ingreso)", "x": 5.2, "y": 8.2, "z": 0.2, "color": "#a04000", "desc": "Plataforma de aislamiento del suelo exigida por Buenas Prácticas."},
    {"name": "🪵 Estiba de Madera No. 2 (Muestreo)", "x": 6.4, "y": 8.2, "z": 0.2, "color": "#a04000", "desc": "Zona transitoria para inspección física por el auxiliar de turno."},
    {"name": "📦 Cajas de Despacho Mayorista Coopidrogas", "x": 5.2, "y": 8.2, "z": 0.6, "color": "#ebd8ab", "desc": "Cajas de inventario recién desembarcadas listas para codificación."},
    
    # Control e Instrumentación Médica (INVIMA Compliance)
    {"name": "🌡️ Termohigrómetro Digital Bodega", "x": 2.0, "y": 5.5, "z": 2.2, "color": "#e74c3c", "desc": "Sensor de control ambiental. Temperatura actual: 21.4°C | Humedad: 62%."},
    {"name": "🌡️ Termohigrómetro Digital Cuarto Frío", "x": 3.0, "y": 8.2, "z": 2.2, "color": "#e74c3c", "desc": "Sensor de control de cadena de frío. Temperatura actual: 4.5°C | Humedad: 58%."},
    {"name": "💨 Extractor y Renovador de Aire Flujo", "x": 7.5, "y": 9.0, "z": 2.4, "color": "#85929e", "desc": "Sistema mecánico de inyección de aire para renovación térmica ambiental (BPA)."}
]

# --- FUNCIÓN GEOMÉTRICA DE PRISMAS SÓLIDOS ---
def construir_prisma_industrial(fig, x_rng, y_rng, z_rng, color, name, hover_text):
    # Índices y coordenadas para construir cubos perfectos sin distorsión triangular en la web
    x = [x_rng, x_rng, x_rng, x_rng, x_rng, x_rng, x_rng, x_rng]
    y = [y_rng, y_rng, y_rng, y_rng, y_rng, y_rng, y_rng, y_rng]
    z = [z_rng, z_rng, z_rng, z_rng, z_rng, z_rng, z_rng, z_rng]
    
    i =
    j =
    k =
    
    fig.add_trace(go.Mesh3d(
        x=x, y=y, z=z, i=i, j=j, k=k,
        color=color,
        opacity=0.72,
        name=name,
        text=hover_text,
        hoverinfo="text",
        flatshading=True,
        lighting=dict(ambient=0.65, diffuse=0.65, roughness=0.25, specular=0.15)
    ))

# Instanciación del entorno de gráficos 3D
fig = go.Figure()

# 1. Dibujar las paredes físicas volumétricas de las áreas de la farmacia
for zona in zonas_3d:
    html_zona = f"<b>{zona['name']}</b><br>Área: {zona['area']} m²<br>Estructura: Altura libre 2.5m<br>{zona['desc']}"
    construir_prisma_industrial(fig, zona["x_range"], zona["y_range"], zona["z_range"], zona["color"], zona["name"], html_zona)

# 2. Dibujar la capa de Equipamiento Mobiliario Base (Marcadores Diamantes)
for eq in equipamiento_fijo:
    html_eq = f"<b>{eq['name']}</b><br>{eq['desc']}<br>Coordenadas de planta: X={eq['x']}, Y={eq['y']}, Z={eq['z']}"
    fig.add_trace(go.Scatter3d(
        x=[eq["x"]], y=[eq["y"]], z=[eq["z"]],
        mode="markers",
        marker=dict(size=eq["size"], color=eq["color"], symbol="diamond", line=dict(color="#1c2833", width=2)),
        name=eq["name"], text=html_eq, hoverinfo="text"
    ))

# 3. 🚀 DIBUJAR LA NUEVA CAPA DE ALTA DENSIDAD DE MERCANCÍA E INVENTARIO REPLETO (Marcadores Esferas de Control)
for inv in inventario_detallado:
    html_inv = f"<b>{inv['name']}</b><br>{inv['desc']}<br>Ubicación técnica: X={inv['x']}, Y={inv['y']}, Z={inv['z']}"
    fig.add_trace(go.Scatter3d(
        x=[inv["x"]], y=[inv["y"]], z=[inv["z"]],
        mode="markers",
        marker=dict(
            size=7,
            color=inv["color"],
            symbol="circle", # Círculos/Esferas perfectas para simular mercancía apilada
            line=dict(color="black", width=1)
        ),
        name=inv["name"],
        text=html_inv,
        hoverinfo="text"
    ))

# Configuración del espacio de renderizado, grillas métricas e iluminación de ingeniería
fig.update_layout(
    title=dict(text="🏢 Distribución de Detalle y Modelado Físico de Inventarios (Layout 3D Realista)", font=dict(size=18)),
    scene=dict(
        xaxis=dict(title="Frente Comercial (Metros)", range=[-0.5, 8.5], dtick=1, backgroundcolor="rgb(245, 245, 245)", gridcolor="white", showbackground=True),
        yaxis=dict(title="Fondo Comercial (Metros)", range=[-0.5, 11.5], dtick=1, backgroundcolor="rgb(235, 235, 235)", gridcolor="white", showbackground=True),
        zaxis=dict(title="Altura Locativa (Metros)", range=[0, 3.5], dtick=1, backgroundcolor="rgb(225, 225, 225)", gridcolor="white", showbackground=True),
        camera=dict(
            eye=dict(x=1.45, y=-1.45, z=1.65), # Ángulo isométrico optimizado
            up=dict(x=0, y=0, z=1)
        ),
        aspectmode="data"
    ),
    margin=dict(l=10, r=10, t=50, b=10),
    template="plotly_white",
    height=650,
    hoverlabel=dict(bgcolor="white", font_size=13, font_family="Arial")
)

# Proyectar el entorno interactivo final en Streamlit
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
