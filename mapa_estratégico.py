import streamlit as st
import folium
from streamlit_folium import st_folium
import math

# Configuración avanzada de la interfaz de usuario
st.set_page_config(page_title="FarmaTech - Inteligencia Geográfica", layout="wide")

st.title("📍 Dashboard de Inteligencia Geográfica — FarmaTech Ltda.")
st.write("Herramienta analítica para el control de cobertura logística y segmentación comercial en tiempo real.")

# --- BASE DE DATOS ESTRATÉGICA COHERENTE CON CORTES 1 Y 2 ---
sede_lat, sede_lon = 6.2372, -75.5976

puntos_interes = [
    {
        "name": "Droguería Comercial Laureles", 
        "loc": [6.2374, -75.5968], 
        "cat": "Droguería de Barrio", 
        "dir": "Avenida 33 # 78-45",
        "desc": "Competidor tradicional más cercano sobre el corredor de la Avenida 33.",
        "img": "https://unsplash.com"
    },
    {
        "name": "Droguerías Galénica", 
        "loc": [6.2425, -75.5910], 
        "cat": "Droguería de Barrio", 
        "dir": "Calle 47D # 75-12",
        "desc": "Establecimiento tradicional con fuerte posicionamiento en el sector Laureles.",
        "img": "https://unsplash.com"
    },
    {
        "name": "Droguería Laureles", 
        "loc": [6.2405, -75.5935], 
        "cat": "Droguería de Barrio", 
        "dir": "Carrera 73 # 39B-20",
        "desc": "Competidor local enfocado en atención tradicional de mostrador.",
        "img": "https://unsplash.com"
    },
    {
        "name": "Droguería Farmasanarte La 72", 
        "loc": [6.2392, -75.5898], 
        "cat": "Droguería de Barrio", 
        "dir": "Calle 42 # 72-15",
        "desc": "Farmacia independiente de alta recordación en la zona residencial.",
        "img": "https://unsplash.com"
    },
    {
        "name": "Droguería Servifarma Los Colores", 
        "loc": [6.2490, -75.5915], 
        "cat": "Droguería de Barrio", 
        "dir": "Carrera 70 # 53-40",
        "desc": "Establecimiento limítrofe ubicado en el extremo norte del radio de acción.",
        "img": "https://unsplash.com"
    },
    {
        "name": "Droguería Cruz Verde Laureles", 
        "loc": [6.2415, -75.5955], 
        "cat": "Gran Cadena", 
        "dir": "Avenida Nutibara # 38-10",
        "desc": "Competidor corporativo con fuerte estrategia de precios y volumen de mercado.",
        "img": "https://unsplash.com"
    },
    {
        "name": "Droguería Audifarma Sector Estadio", 
        "loc": [6.2450, -75.5890], 
        "cat": "Gran Cadena", 
        "dir": "Carrera 70 # 44-85",
        "desc": "Dispensario de alto flujo enfocado principalmente en usuarios de EPS.",
        "img": "https://unsplash.com"
    },
    {
        "name": "Clínica del Amor", 
        "loc": [6.2398, -75.5862], 
        "cat": "Infraestructura de Salud", 
        "dir": "Diagonal 74B # 32D-21",
        "desc": "Centro asistencial cercano, catalogado como generador indirecto de fórmulas médicas.",
        "img": "https://unsplash.com"
    },
    {
        "name": "Centro de Especialistas Los Álamos", 
        "loc": [6.2368, -75.5932], 
        "cat": "Infraestructura de Salud", 
        "dir": "Carrera 78 # 32F-10",
        "desc": "Complejo de consultorios privados con alta concentración de pacientes crónicos.",
        "img": "https://unsplash.com"
    }
]

# --- FUNCIÓN MATEMÁTICA DE GEODESIA (Fórmula de Haversine para distancias reales) ---
def calcular_distancia(lat1, lon1, lat2, lon2):
    r_tierra = 6371000  # En metros
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    a = math.sin(d_lat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(d_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return r_tierra * c

# --- SECCIÓN DE FILTROS EN LA BARRA LATERAL (SIDEBAR) ---
st.sidebar.header("⚙️ Panel de Control y Filtros")

# 1. Filtro General por Categoría
categorias_disponibles = ["Droguería de Barrio", "Gran Cadena", "Infraestructura de Salud"]
categorias_seleccionadas = st.sidebar.multiselect(
    "1. Filtrar por Tipo de Entidad:",
    options=categorias_disponibles,
    default=categorias_disponibles
)

# 2. Filtro por Nombre Específico (Dinámico)
establecimientos_filtrados_cat = [p for p in puntos_interes if p["cat"] in categorias_seleccionadas]
nombres_disponibles = [p["name"] for p in establecimientos_filtrados_cat]

nombres_seleccionados = st.sidebar.multiselect(
    "2. Filtrar por Nombre Específico:",
    options=nombres_disponibles,
    default=nombres_disponibles
)

# Filtro final cruzado de datos
puntos_finales = [p for p in establecimientos_filtrados_cat if p["name"] in nombres_seleccionados]

# 3. Simulador de Pedidos Express
st.sidebar.markdown("---")
st.sidebar.subheader("🚀 Simulador de Pedidos Express")
sim_lat = st.sidebar.slider("Latitud del Cliente", min_value=6.2300, max_value=6.2500, value=6.2395, step=0.0005, format="%.4f")
sim_lon = st.sidebar.slider("Longitud del Cliente", min_value=-75.6100, max_value=-75.5800, value=-75.6015, step=0.0005, format="%.4f")

distancia_cliente = calcular_distancia(sede_lat, sede_lon, sim_lat, sim_lon)

if distancia_cliente <= 1500:
    st.sidebar.success(f"✅ **PEDIDO VIABLE**\n\nDistancia: {distancia_cliente:.0f} metros.\nTiempo estimado: 15-30 min.\nCosto de envío: $0 COP")
else:
    st.sidebar.error(f"❌ **FUERA DE COBERTURA STANDARD**\n\nDistancia: {distancia_cliente:.0f} metros.\nRequiere recargo o despacho ampliado.")

# 4. NUEVO GLOSARIO DE ICONOS PARA LA BARRA LATERAL
st.sidebar.markdown("---")
st.sidebar.subheader("📖 Glosario de Iconos del Mapa")
st.sidebar.markdown("""
🟢 **Icono Verde (Cruz):** Sede central de **FarmaTech Ltda.** en Mall La 33.
🔴 **Icono Rojo (Canasta):** Competidores directos (**Droguerías de Barrio**).
🟠 **Icono Naranja (Dólar):** Grandes cadenas de farmacias corporativas.
🔵 **Icono Azul (Usuario):** Ubicación simulada en tiempo real del cliente.
🌐 **Icono Turquesa (Médico):** Clínicas e IPS (Nodos generadores de demanda).
🔴 **Línea de Perímetro Roja:** Límite operativo estricto de **1.5 Kilómetros**.
""")

# 5. Botón de Captura / Reporte Técnico
st.sidebar.markdown("---")
st.sidebar.subheader("📸 Herramientas de Reporte")
if st.sidebar.button("📷 Capturar Pantallazo / Guardar Reporte"):
    st.components.v1.html("<script>window.parent.print();</script>", height=0, width=0)
    st.sidebar.caption("💡 Tip: Selecciona 'Guardar como PDF' para archivar.")

# --- CONSTRUCCIÓN DINÁMICA DEL MAPA ---
m = folium.Map(location=[sede_lat, sede_lon], zoom_start=15, control_scale=True)

# Círculo Base Operativo de 1.5 km (Fijo de fondo)
folium.Circle(
    radius=1500,
    location=[sede_lat, sede_lon],
    color="crimson",
    weight=2,
    fill=True,
    fill_color="#3186cc",
    fill_opacity=0.08,
    tooltip="Área de Influencia Logística: 1.5 Kilómetros"
).add_to(m)

# INYECCIÓN HTML PARA LA SEDE PRINCIPAL (FarmaTech)
html_popup_sede = """
<div style="font-family: Arial, sans-serif; width: 260px; line-height: 1.4;">
    <h4 style="margin:0 0 5px 0; color:#1e7e34;">FarmaTech Ltda.</h4>
    <b>Sede Principal Mall La 33</b><br>
    <span style="color:#555;">Dirección: Av. 33 # 80-07</span><br>
    <small style="color:#007bff; font-weight:bold;">Centro Operativo Omnicanal</small><br><br>
    <img src="https://unsplash.com" width="100%" style="border-radius:6px; box-shadow: 2px 2px 5px rgba(0,0,0,0.2);">
</div>
"""

folium.Marker(
    [sede_lat, sede_lon],
    popup=folium.Popup(html_popup_sede, max_width=290),
    tooltip="FarmaTech Sede Principal (Click para ver foto)",
    icon=folium.Icon(color="green", icon="medkit", prefix="fa")
).add_to(m)

# Marcador del Cliente Simulado
folium.Marker(
    [sim_lat, sim_lon],
    popup=f"<b>Dirección Cliente Simulado</b><br>Distancia radial: {distancia_cliente:.0f} metros.",
    tooltip="📍 Posición del Cliente",
    icon=folium.Icon(color="blue", icon="user", prefix="fa")
).add_to(m)

# Línea visual entre la farmacia y el cliente
folium.PolyLine([[sede_lat, sede_lon], [sim_lat, sim_lon]], color="gray", weight=2, dash_array="5, 5").add_to(m)

# Renderizado de Marcadores Filtrados con su FOTO INDIVIDUAL (CORRECCIÓN DE EXTRACCIÓN DE COORDENADAS)
for punto in puntos_finales:
    lat_dest, lon_dest = punto["loc"][0], punto["loc"][1]
    dist_comp = calcular_distancia(sede_lat, sede_lon, lat_dest, lon_dest)
    estado_cobertura = "DENTRO DEL RADIO" if dist_comp <= 1500 else "FUERA DE COBERTURA"
    
    if punto["cat"] == "Droguería de Barrio":
        color_icono, tipo_icono = "red", "shopping-basket"
        color_titulo = "#dc3545"
    elif punto["cat"] == "Gran Cadena":
        color_icono, tipo_icono = "orange", "usd"
        color_titulo = "#fd7e14"
    else:
        color_icono, tipo_icono = "cadetblue", "user-md"
        color_titulo = "#17a2b8"
        
    html_popup_comp = f"""
    <div style="font-family: Arial, sans-serif; width: 250px; line-height: 1.4;">
        <h4 style="margin:0 0 5px 0; color:{color_titulo};">{punto['name']}</h4>
        <i>{punto['cat']}</i><br>
        <b>Dirección:</b> {punto['dir']}<br>
        {punto['desc']}<br>
        <b>Distancia real:</b> {dist_comp:.0f} metros ({estado_cobertura})<br><br>
        <img src="{punto['img']}" width="100%" style="border-radius:6px; box-shadow: 2px 2px 4px rgba(0,0,0,0.15);">
    </div>
    """
        
    folium.Marker(
        location=punto["loc"],
        popup=folium.Popup(html_popup_comp, max_width=280),
        tooltip=punto["name"],
        icon=folium.Icon(color=color_icono, icon=tipo_icono, prefix="fa")
    ).add_to(m)

# Renderizar mapa principal
st_folium(m, width=1200, height=600)

# --- PANEL DE INDICADORES EN TIEMPO REAL ---
st.markdown("### 📊 Indicadores de Entorno de Mercado en Pantalla")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Droguerías de Barrio Visibles", value=sum(1 for p in puntos_finales if p["cat"] == "Droguería de Barrio"))
with col2:
    st.metric(label="Grandes Cadenas en Pantalla", value=sum(1 for p in puntos_finales if p["cat"] == "Gran Cadena"))
with col3:
    st.metric(label="Nodos de Salud Activos", value=sum(1 for p in puntos_finales if p["cat"] == "Infraestructura de Salud"))

# --- NUEVA SECCIÓN DE NOTAS DE CAMPO Y ANÁLISIS ESTRATÉGICO POR AFUERA DEL MAPA ---
st.markdown("---")
st.markdown("### 📝 Notas Analíticas de Localización y Red de Distribución")
nota_col1, nota_col2 = st.columns(2)

with nota_col1:
    st.info("""
    💡 **Sustento del Radio de Influencia Logística (1.5 km):**
    El perímetro delimitado por la circunferencia roja representa el área de cobertura crítica para nuestro modelo de farmacia omnicanal de alta rotación. Este rango garantiza que las tres motocicletas de nuestra flota propia efectúen entregas express en un intervalo controlado de 20 a 45 minutos sin incurrir en sobrecostos operativos, blindando el flujo de caja del proyecto.
    """)

with nota_col2:
    st.warning("""
    ⚠️ **Análisis de Densidad Competitiva Recurrente:**
    La visualización cartográfica evidencia que el eje comercial de la Avenida 33 concentra el mayor foco de saturación por parte de droguerías tradicionales de barrio. Para mitigar este riesgo comercial, FarmaTech Ltda. basa su propuesta de valor en la rapidez del servicio digital (WhatsApp Business) y la fidelización del paciente crónico, evitando la guerra directa de precios en el mostrador físico.
    """)
