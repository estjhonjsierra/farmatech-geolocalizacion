import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Configuración inicial forzando el diseño responsive y limpio sin márgenes excesivos
st.set_page_config(page_title="FarmaTech - Plano 3D", layout="wide")

# Control de la geometría de la ventana para eliminar espacios vacíos laterales
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

# --- PANEL DE CONTROL (BARRA LATERAL / SIDEBAR) ---
st.sidebar.header("⚙️ Control de Infraestructura 3D")
st.sidebar.write("Modelado tridimensional volumétrico de áreas funcionales para el cumplimiento normativo INVIMA.")

# Glosario de zonas en la barra lateral
st.sidebar.subheader("📐 Resumen de Áreas Técnicas")
st.sidebar.markdown("""
🎨 **Zonificación en Maqueta Virtual:**
*   🛒 **Zona Dispensación (20 m²):** Altura comercial 2.5m.
*   📦 **Bodega General (15 m²):** Altura comercial 2.5m.
*   👨‍⚕️ **Consultoría QF (8 m²):** Privado de atención médica.
*   🛵 **Nodo Logístico (8 m²):** Alistamiento omnicanal.
*   🏢 **Administración (6 m²):** Oficina de control central.
*   ❄️ **Cadena de Frío (6 m²):** Cuarto técnico aislado.
*   📥 **Recepción/Cuarentena (5 m²):** Validación técnica.
*   ⚠️ **Unidad Residuos (4 m²):** Punto Azul regulado.
*   🥼 **Servicios/Vestier (4 m²):** Zona de higiene personal.
*   🚶 **Circulación (4 m²):** Pasillos de interconexión.
""")

st.sidebar.markdown("---")
st.sidebar.subheader("📸 Herramientas de Reporte")
if st.sidebar.button("📷 Guardar Maqueta 3D y Reporte (PDF)"):
    st.components.v1.html("<script>window.parent.print();</script>", height=0, width=0)

# --- CUERPO PRINCIPAL DEL DASHBOARD ---
st.markdown(f"""
    <div style="background-color: #f8f9fa; padding: 25px; border-radius: 8px; border-left: 6px solid #e74c3c; margin-bottom: 25px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
        <h2 style="margin: 0; color: #1c2833; font-family: Arial, sans-serif;">📐 Modelado Arquitectónico Tridimensional Realista (80 m²)</h2>
        <p style="margin: 5px 0 0 0; color: #566573; font-size: 15px;">FarmaTech Ltda. &mdash; Maqueta Virtual Rotable Estructurada bajo el Decreto 2200 de 2005 y Resolución 1403 de 2007.</p>
    </div>
""", unsafe_allow_html=True)

# --- BASE DE DATOS GEOMÉTRICA (Coordenadas X, Y, Z a escala métrica real para un local de 8m x 10m x 2.5m de alto) ---
zonas_3d = [
    {"name": "Zona de Dispensación y Atención", "x": [0, 8, 8, 0, 0, 8, 8, 0], "y": [0, 0, 2.5, 2.5, 0, 0, 2.5, 2.5], "z": [0, 0, 0, 0, 2.5, 2.5, 2.5, 2.5], "area": 20, "color": "#2ca02c", "desc": "Frente comercial. 3 módulos POS simultáneos para atención presencial."},
    {"name": "Bodega de Almacenamiento General", "x": [0, 4, 4, 0, 0, 4, 4, 0], "y": [2.5, 2.5, 6.25, 6.25, 2.5, 2.5, 6.25, 6.25], "z": [0, 0, 0, 0, 2.5, 2.5, 2.5, 2.5], "area": 15, "color": "#ff7f0e", "desc": "Custodia técnica de inventarios de alta rotación (30-45 días de stock)."},
    {"name": "Módulo de Consulta Farmacéutica (QF)", "x": [4, 8, 8, 4, 4, 8, 8, 4], "y": [2.5, 2.5, 4.5, 4.5, 2.5, 2.5, 4.5, 4.5], "z": [0, 0, 0, 0, 2.5, 2.5, 2.5, 2.5], "area": 8, "color": "#1f77b4", "desc": "Orientación técnica personalizada al paciente crónico y captación de datos."},
    {"name": "Nodo Logístico de Alistamiento", "x": [4, 8, 8, 4, 4, 8, 8, 4], "y": [4.5, 4.5, 6.5, 6.5, 4.5, 4.5, 6.5, 6.5], "z": [0, 0, 0, 0, 2.5, 2.5, 2.5, 2.5], "area": 8, "color": "#9467bd", "desc": "Embalaje, picking y despacho centralizado de pedidos de WhatsApp Business."},
    {"name": "Área Administrativa y Control", "x": [0, 2.4, 2.4, 0, 0, 2.4, 2.4, 0], "y": [6.25, 6.25, 8.75, 8.75, 6.25, 6.25, 8.75, 8.75], "z": [0, 0, 0, 0, 2.5, 2.5, 2.5, 2.5], "area": 6, "color": "#7f7f7f", "desc": "Gestión contable, monitoreo del sistema ERP y tesorería."},
    {"name": "Cuarto de Cadena de Frío", "x": [2.4, 4.8, 4.8, 2.4, 2.4, 4.8, 4.8, 2.4], "y": [6.25, 6.25, 8.75, 8.75, 6.25, 6.25, 8.75, 8.75], "z": [0, 0, 0, 0, 2.5, 2.5, 2.5, 2.5], "area": 6, "color": "#17becf", "desc": "Custodia controlada de biológicos e insulinas (Neveras de 2°C a 8°C)."},
    {"name": "Bahía de Recepción y Cuarentena", "x": [4.8, 6.8, 6.8, 4.8, 4.8, 6.8, 6.8, 4.8], "y": [6.25, 6.25, 8.75, 8.75, 6.25, 6.25, 8.75, 8.75], "z": [0, 0, 0, 0, 2.5, 2.5, 2.5, 2.5], "area": 5, "color": "#bcbd22", "desc": "Inspección técnica de lotes, control de fechas de vencimiento y calidad."},
    {"name": "Unidad de Bioseguridad y Punto Azul", "x": [6.8, 8, 8, 6.8, 6.8, 8, 8, 6.8], "y": [6.5, 6.5, 9.83, 9.83, 6.5, 6.5, 9.83, 9.83], "z": [0, 0, 0, 0, 2.5, 2.5, 2.5, 2.5], "area": 4, "color": "#d62728", "desc": "Segregación de residuos hospitalarios y contenedor de fármacos posconsumo."},
    {"name": "Servicios Sanitarios y Vestier", "x": [0, 1.6, 1.6, 0, 0, 1.6, 1.6, 0], "y": [8.75, 8.75, 11.25, 11.25, 8.75, 8.75, 11.25, 11.25], "z": [0, 0, 0, 0, 2.5, 2.5, 2.5, 2.5], "area": 4, "color": "#e377c2", "desc": "Área de higiene, vestuario y bienestar para el personal operativo (BPA)."},
    {"name": "Corredores y Circulación Interna", "x": [1.6, 6.8, 6.8, 1.6, 1.6, 6.8, 6.8, 1.6], "y": [8.75, 8.75, 9.53, 9.53, 8.75, 8.75, 9.53, 9.53], "z": [0, 0, 0, 0, 0.2, 0.2, 0.2, 0.2], "area": 4, "color": "#8c564b", "desc": "Pasadizos e interconexiones técnicas para movilidad de mercancías."},
]

# --- CONSTRUCCIÓN DEL ENTORNO TRIDIMENSIONAL (PLOTLY 3D MESH) ---
fig = go.Figure()

# Índices fijos para construir los 12 triángulos de las 6 caras del prisma rectangular
i_indices = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
j_indices = [1, 2, 3, 0, 4, 5, 6, 7, 4, 5, 7, 6]
k_indices = [4, 5, 6, 7, 5, 6, 7, 4, 1, 2, 6, 5]

# Dibujar cada zona funcional como un bloque volumétrico 3D real sin elementos de texto fijos conflictivos
for zona in zonas_3d:
    html_hover = f"<b>{zona['name']}</b><br>Área: {zona['area']} m²<br>Altura: 2.5 metros<br>{zona['desc']}"
    
    fig.add_trace(go.Mesh3d(
        x=zona["x"], y=zona["y"], z=zona["z"],
        i=i_indices, j=j_indices, k=k_indices,
        color=zona["color"],
        opacity=0.80,
        name=zona["name"],
        text=html_hover,
        hoverinfo="text",
        flatshading=True,
        lighting=dict(ambient=0.6, diffuse=0.6, roughness=0.3, specular=0.2)
    ))

# Configuración de los ejes y el ángulo inicial de la cámara isométrica
fig.update_layout(
    title=dict(text="🏢 Maqueta Virtual de Distribución de Planta (Layout Especializado 3D Real)", font=dict(size=18)),
    scene=dict(
        xaxis=dict(title="Frente (Metros)", range=[-0.5, 8.5], dtick=1, backgroundcolor="rgb(240, 240, 240)", gridcolor="white", showbackground=True),
        yaxis=dict(title="Fondo (Metros)", range=[-0.5, 11.5], dtick=1, backgroundcolor="rgb(230, 230, 230)", gridcolor="white", showbackground=True),
        zaxis=dict(title="Altura (Metros)", range=[0, 3.5], dtick=1, backgroundcolor="rgb(220, 220, 220)", gridcolor="white", showbackground=True),
        camera=dict(
            eye=dict(x=1.6, y=-1.6, z=1.8),
            up=dict(x=0, y=0, z=1)
        ),
        aspectmode="data"
    ),
    margin=dict(l=10, r=10, t=50, b=10),
    template="plotly_white",
    height=650,
    hoverlabel=dict(bgcolor="white", font_size=13, font_family="Arial")
)

# Renderizar el gráfico interactivo 3D
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
