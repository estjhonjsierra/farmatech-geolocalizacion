import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Configuración inicial forzando el diseño responsive y limpio
st.set_page_config(page_title="FarmaTech - Plano Arquitectónico", layout="wide")

# Control estricto de la geometría de la ventana para eliminar espacios vacíos laterales
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
st.sidebar.header("⚙️ Control de Infraestructura")
st.sidebar.write("Simulación de áreas funcionales para el cumplimiento normativo INVIMA y optimización de flujos.")

# Glosario de zonas en la barra lateral
st.sidebar.subheader("📐 Resumen de Áreas Técnicas")
st.sidebar.markdown("""
🎨 **Zonificación Comercial y Sanitaria:**
*   🛒 **Zona Dispensación (20 m²):** Área frontal de atención.
*   📦 **Bodega General (15 m²):** Custodia de stock común.
*   👨‍⚕️ **Consultoría QF (8 m²):** Módulo de atención privada.
*   🛵 **Nodo Logístico (8 m²):** Alistamiento de domicilios.
*   🏢 **Administración (6 m²):** Oficina de control central.
*   ❄️ **Cadena de Frío (6 m²):** Cuarto técnico de refrigeración.
*   📥 **Recepción/Cuarentena (5 m²):** Inspección técnica de lotes.
*   ⚠️ **Unidad Residuos (4 m²):** Gestión de desechos y Punto Azul.
*   🥼 **Servicios/Vestier (4 m²):** Zona de higiene del personal.
*   🚶 **Circulación (4 m²):** Pasillos y pasadizos técnicos.
""")

st.sidebar.markdown("---")
st.sidebar.subheader("📸 Herramientas de Reporte")
if st.sidebar.button("📷 Guardar Plano y Reporte (PDF)"):
    st.components.v1.html("<script>window.parent.print();</script>", height=0, width=0)

# --- CUERPO PRINCIPAL DEL DASHBOARD ---
st.markdown(f"""
    <div style="background-color: #f8f9fa; padding: 25px; border-radius: 8px; border-left: 6px solid #0056b3; margin-bottom: 25px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
        <h2 style="margin: 0; color: #1c2833; font-family: Arial, sans-serif;">📐 Plano Funcional Estructurado a Escala Comercial (80 m²)</h2>
        <p style="margin: 5px 0 0 0; color: #566573; font-size: 15px;">FarmaTech Ltda. &mdash; Distribución Espacial Homologada bajo el Decreto 2200 de 2005 y Resolución 1403 de 2007.</p>
    </div>
""", unsafe_allow_html=True)

# --- BASE DE DATOS GEOMÉTRICA (Coordenadas X, Y a escala métrica real para un local de 8m x 10m) ---
# Se definen los rectángulos [x0, y0, x1, y1] para simular las paredes reales de cada área
zonas = [
    {"name": "Zona de Dispensación y Atención", "x": [0, 0, 8, 8, 0], "y": [0, 2.5, 2.5, 0, 0], "area": 20, "color": "#2ca02c", "desc": "Frente comercial. 3 módulos POS simultáneos para atención presencial."},
    {"name": "Bodega de Almacenamiento General", "x": [0, 0, 4, 4, 0], "y": [2.5, 6.25, 6.25, 2.5, 2.5], "area": 15, "color": "#ff7f0e", "desc": "Custodia técnica de inventarios de alta rotación (30-45 días de stock)."},
    {"name": "Módulo de Consulta Farmacéutica (QF)", "x": [4, 4, 8, 8, 4], "y": [2.5, 4.5, 4.5, 2.5, 2.5], "area": 8, "color": "#1f77b4", "desc": "Orientación técnica personalizada al paciente crónico y captación de datos."},
    {"name": "Nodo Logístico de Alistamiento", "x": [4, 4, 8, 8, 4], "y": [4.5, 6.5, 6.5, 4.5, 4.5], "area": 8, "color": "#9467bd", "desc": "Embalaje, picking y despacho centralizado de pedidos de WhatsApp Business."},
    {"name": "Área Administrativa y Control", "x": [0, 0, 2.4, 2.4, 0], "y": [6.25, 8.75, 8.75, 6.25, 6.25], "area": 6, "color": "#7f7f7f", "desc": "Gestión contable, monitoreo del sistema ERP y tesorería."},
    {"name": "Cuarto de Cadena de Frío", "x": [2.4, 2.4, 4.8, 4.8, 2.4], "y": [6.25, 8.75, 8.75, 6.25, 6.25], "area": 6, "color": "#17becf", "desc": "Custodia controlada de biológicos e insulinas (Neveras de 2°C a 8°C)."},
    {"name": "Bahía de Recepción y Cuarentena", "x": [4.8, 4.8, 6.8, 6.8, 4.8], "y": [6.25, 8.75, 8.75, 6.25, 6.25], "area": 5, "color": "#bcbd22", "desc": "Inspección técnica de lotes, control de fechas de vencimiento y calidad."},
    {"name": "Unidad de Bioseguridad y Punto Azul", "x": [6.8, 6.8, 8, 8, 6.8], "y": [6.5, 9.83, 9.83, 6.5, 6.5], "area": 4, "color": "#d62728", "desc": "Segregación de residuos hospitalarios y contenedor de fármacos posconsumo."},
    {"name": "Servicios Sanitarios y Vestier", "x": [0, 0, 1.6, 1.6, 0], "y": [8.75, 11.25, 11.25, 8.75, 8.75], "area": 4, "color": "#e377c2", "desc": "Área de higiene, vestuario y bienestar para el personal operativo (BPA)."},
    {"name": "Corredores y Circulación Interna", "x": [1.6, 1.6, 6.8, 6.8, 1.6], "y": [8.75, 9.53, 9.53, 8.75, 8.75], "area": 4, "color": "#8c564b", "desc": "Pasadizos e interconexiones técnicas para movilidad de mercancías."},
]

# --- CONSTRUCCIÓN DEL GRÁFICO ARQUITECTÓNICO CON PLOTLY ---
fig = go.Figure()

for zona in zonas:
    # Dibujar la zona coloreada con bordes definidos que simulan paredes
    fig.add_trace(go.Scatter(
        x=zona["x"],
        y=zona["y"],
        fill="subsection" if "Circulación" in zona["name"] else "assignment" if "Dispensación" in zona["name"] else "toself",
        fillcolor=zona["color"],
        mode="lines",
        line=dict(color="#1c2833", width=2),
        name=zona["name"],
        text=f"<b>{zona['name']}</b><br>Área: {zona['area']} m²<br>{zona['desc']}",
        hoverinfo="text",
        opacity=0.85
    ))
    
    # Calcular el centro geométrico de cada zona para colocar el texto flotante de identificación
    center_x = sum(set(zona["x"])) / len(set(zona["x"]))
    center_y = sum(set(zona["y"])) / len(set(zona["y"]))
    
    # Añadir el nombre abreviado de la zona directamente en el mapa para realismo
    fig.add_annotation(
        x=center_x,
        y=center_y,
        text=f"<b>{zona['name'][:16]}...</b><br>{zona['area']} m²",
        showarrow=False,
        font=dict(size=11, color="black"),
        align="center"
    )

# Configuración de los ejes para simular un plano cuadriculado de ingeniería (Plano cartesiano métrico)
fig.update_layout(
    title=dict(text="📐 Distribución en Planta (Layout Técnico Industrial - Vista Superior)", font=dict(size=18)),
    xaxis=dict(title="Frente Comercial del Establecimiento (Metros)", range=[-0.5, 8.5], dtick=1, showgrid=True, gridcolor="#e5e7e9"),
    yaxis=dict(title="Fondo Comercial del Establecimiento (Metros)", range=[-0.5, 11.5], dtick=1, showgrid=True, gridcolor="#e5e7e9"),
    margin=dict(l=10, r=10, t=50, b=10),
    template="plotly_white",
    showlegend=False,
    height=600,
    hoverlabel=dict(bgcolor="white", font_size=13, font_family="Arial")
)

# Renderizar el plano a escala responsivo al 100% de la pantalla
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

