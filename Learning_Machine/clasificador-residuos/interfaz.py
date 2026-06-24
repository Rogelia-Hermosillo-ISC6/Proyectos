import tkinter as tk
from tkinter import filedialog, scrolledtext
from PIL import Image, ImageTk, ImageDraw, ImageOps
import tensorflow as tf
import cv2
import numpy as np
import os
from datetime import datetime

# Base de datos completa con información sobre residuos
info_residuos = {
    "metal": {
        "nombre": "🔩 METAL",
        "color": "#E74C3C",
        "emoji_grande": "⛰️",
        "degradacion": "100-200 años",
        "descripcion": "Aluminio, acero, cobre, hierro, latas, alambre, tuberías, clavos, tornillos, etc.",
        
        "impacto_ambiental": "• Extracción minera genera contaminación\n• Requiere gran cantidad de energía para producir\n• Reciclaje ahorra 95% de energía vs. producción nueva\n• Contaminación del aire y agua en minas",
        
        "beneficios_reciclaje": "• Ahorra 95% de energía eléctrica\n• Reduce emisiones de CO2 en 97%\n• Una lata reciclada = energía para TV 3 horas\n• Infinitamente reciclable sin perder calidad",
        
        "como_reciclar": "• Limpiar y secar antes de reciclar\n• Separar metales ferrosos de no ferrosos\n• Aplastar latas para economizar espacio\n• Llevar a puntos de acopio especializados\n• Vender como chatarra por dinero",
        
        "donde_tirar": "🗑️ Contenedor gris/plateado de reciclaje\n📍 Centros de acopio de metales\n🏢 Empresas de reciclaje\n💰 Puntos de compra de chatarra",
        
        "reutilizacion": "🎨 Macetas y jardineras con latas\n🖼️ Esculturas y arte metálico\n🪑 Muebles decorativos\n💍 Joyería artesanal\n🎁 Objetos de decoración\n📦 Contenedores reutilizables",
        
        "ejemplos_productos": "Latas de bebidas, envases de conserva, cables, tuberías, herrajes, piezas de automóviles, aparatos viejos, herramientas",
        
        "estadisticas": "• 75 billones de latas se producen anualmente\n• Solo 50% se recicla a nivel mundial\n• Una lata tarda 200 años en degradarse\n• 24 latas = 1 kg de aluminio"
    },
    
    "organico": {
        "nombre": "🌱 ORGÁNICO",
        "color": "#27AE60",
        "emoji_grande": "🌿",
        "degradacion": "1-6 meses",
        "descripcion": "Restos de comida, frutas, verduras, hojas, ramas, poda, plantas, estiércol, servilletas sucias, cartón mojado, etc.",
        
        "impacto_ambiental": "• En vertederos produce metano (gas invernadero)\n• Contamina aguas subterráneas\n• Ocupa 50% del espacio en basureros\n• Genera mal olor y atrae plagas\n• El compostaje reduce emisiones 50%",
        
        "beneficios_reciclaje": "• Produce abono natural sin químicos\n• Mejora fertilidad del suelo\n• Reduce metano en vertederos\n• Retiene agua en el suelo\n• Económico y sustentable",
        
        "como_reciclar": "• Separar de plástico y papel\n• No incluir carne/hueso (atrae plagas)\n• Mezclar restos húmedos con materia seca\n• Hacer compost casero o municipal\n• Entregar a plantas de compostaje",
        
        "donde_tirar": "🗑️ Contenedor marrón de compostaje\n🌾 Plantas de compostaje municipal\n♻️ Huertos urbanos comunitarios\n🏡 Sistemas de compostaje casero",
        
        "reutilizacion": "🌻 Compost casero en 3-6 meses\n🌱 Abono para plantas y huertos\n🥕 Cultivo de alimentos propios\n🪴 Huertos urbanos en balcones\n🌳 Donar a áreas verdes\n🐝 Biodigestores anaeróbicos",
        
        "ejemplos_productos": "Cáscaras de frutas/verduras, restos de comida, posos de café, cáscaras de huevo, hojas, ramitas, césped, paja, papel mojado",
        
        "estadisticas": "• 30% de basura es orgánica\n• 1 kg = 250g de compost final\n• Huerto con compost casero: -50% gastos\n• Compost listo en 60-90 días"
    },
    
    "papel_carton": {
        "nombre": "📄 PAPEL Y CARTÓN",
        "color": "#F39C12",
        "emoji_grande": "📦",
        "degradacion": "2-6 meses",
        "descripcion": "Periódicos, revistas, cartón ondulado, cajas, papel de oficina, papel de regalo, envoltorios, tetra pack, etc.",
        
        "impacto_ambiental": "• Producción requiere 10 litros agua por hoja A4\n• Tala de árboles para papel virgen\n• Blanqueamiento químico contamina ríos\n• Reciclaje usa 50% menos energía\n• Genera mucha basura en hogares/oficinas",
        
        "beneficios_reciclaje": "• 1 árbol = 8,000 hojas recicladas\n• Ahorra 50% de energía vs. papel nuevo\n• Protege bosques nativos\n• Reduce contaminación del agua\n• Crea empleos en reciclaje",
        
        "como_reciclar": "• Separar cartón de papel fino\n• Romper cajas grandes para compactar\n• No mezclar con papel sucio/mojado\n• Quitar elementos adhesivos\n• Llevar a contenedores azules\n• Vender cartón pesado a recicladores",
        
        "donde_tirar": "🗑️ Contenedor azul de reciclaje\n📍 Puntos de acopio de papel\n🏢 Empresas de reciclaje\n📚 Centros de distribución\n💰 Recicladores informales",
        
        "reutilizacion": "🎨 Papier-mâché y proyectos artísticos\n📦 Empaque reutilizable para envíos\n🪴 Mulch para plantas y huertos\n🎁 Papel de regalo reciclado\n🗂️ Organizadores caseros\n🐕 Lecho para mascotas\n🎭 Proyectos escolares y manualidades",
        
        "ejemplos_productos": "Cajas de cartón, periódicos, revistas, papel de oficina, papel de regalo, envoltorios, servilletas limpias, cartulinas, folders",
        
        "estadisticas": "• 17 árboles se salvan por tonelada reciclada\n• Papel reciclado = 10% más débil que virgen\n• Se puede reciclar 5-7 veces máximo\n• 70% del papel que usamos se recicla"
    },
    
    "plastico": {
        "nombre": "♻️ PLÁSTICO",
        "color": "#3498DB",
        "emoji_grande": "🛢️",
        "degradacion": "400-1000 años",
        "descripcion": "Botellas, bolsas, envases, juguetes, tuberías de PVC, film plástico, espuma, contenedores de alimentos, etc.",
        
        "impacto_ambiental": "• 400+ años degradarse (algunos nunca)\n• 8 millones toneladas/año en océanos\n• Mata 1 millón de aves marinas/año\n• Microplásticos en cadena alimenticia\n• Producción libera dioxinas tóxicas\n• Quemarlo emite gases venenosos",
        
        "beneficios_reciclaje": "• Reduce 65% de energía vs. plástico nuevo\n• Evita contaminación marina\n• Retarda degradación de ecosistemas\n• 2 botellas recic. = 1 playera\n• Crea 10x más empleos que incineración",
        
        "como_reciclar": "• Limpiar y secar botellas\n• Separar por tipo (PET, HDPE, PVC, etc.)\n• Aplastar para economizar espacio\n• No mezclar con otros materiales\n• Retirar etiquetas si es posible\n• Llevar a contenedores amarillos\n• Evitar plásticos laminados",
        
        "donde_tirar": "🗑️ Contenedor amarillo de reciclaje\n🏪 Programas de devolución en supermercados\n📍 Centros de acopio especializados\n🏢 Empresas de reciclaje\n🎪 Ferias de reciclaje comunitarias",
        
        "reutilizacion": "🪴 Macetas y jardineras\n👜 Bolsos y mochilas hechas con botellas\n🪑 Muebles de plástico reciclado\n🎒 Mochilas escolares ecológicas\n🧴 Organizadores y contenedores\n🎨 Proyectos de arte y manualidades\n♨️ Fibra textil para ropa (poliéster)\n🏗️ Material de construcción",
        
        "ejemplos_productos": "Botellas de agua/bebidas, bolsas de plástico, envases de comida, juguetes, tuberías, películas plásticas, contenedores, vasos desechables",
        
        "estadisticas": "• 380 millones toneladas/año se producen\n• Solo 9% se recicla a nivel mundial\n• 1 botella recic. = 10 bolsas de basura\n• Contamina 5 océanos del planeta\n• Cifra aumenta 4% anualmente"
    }
}

model = tf.keras.models.load_model("modelo_residuos.h5")
classes = ["metal", "organico", "papel_carton", "plastico"]

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("🌍 Clasificador Inteligente de Residuos - Sistema Educativo")
ventana.geometry("1150x800")
ventana.config(bg="#1A1A2E")
ventana.resizable(True, True)

# ==================== ESTILOS ====================
COLOR_BG = "#1A1A2E"
COLOR_PANEL = "#16213E"
COLOR_ACCENT = "#0F3460"
COLOR_TEXT = "#EAEAEA"
COLOR_HIGHLIGHT = "#E94560"

# ==================== HEADER ====================
frame_header = tk.Frame(ventana, bg=COLOR_ACCENT, height=70)
frame_header.pack(fill=tk.X, padx=0, pady=0)
frame_header.pack_propagate(False)

titulo_principal = tk.Label(
    frame_header,
    text="🌍 CLASIFICADOR DE RESIDUOS",
    font=("Arial", 18, "bold"),
    fg=COLOR_TEXT,
    bg=COLOR_ACCENT
)
titulo_principal.pack(pady=8)

subtitulo = tk.Label(
    frame_header,
    text="Aprende a clasificar y reciclar • Impacto ambiental",
    font=("Arial", 9),
    fg="#B0B0B0",
    bg=COLOR_ACCENT
)
subtitulo.pack()

# ==================== CONTENIDO PRINCIPAL ====================
frame_contenido = tk.Frame(ventana, bg=COLOR_BG)
frame_contenido.pack(fill=tk.BOTH, expand=True, padx=8, pady=5)

# ---- PANEL IZQUIERDO: CÁMARA Y BOTONES (CON SCROLL) ----
frame_izquierdo_contenedor = tk.Frame(frame_contenido, bg=COLOR_BG, width=420)
frame_izquierdo_contenedor.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=5)
frame_izquierdo_contenedor.pack_propagate(False)

# Canvas y scrollbar
canvas_left = tk.Canvas(frame_izquierdo_contenedor, bg=COLOR_BG, highlightthickness=0, width=400)
scrollbar_left = tk.Scrollbar(frame_izquierdo_contenedor, orient=tk.VERTICAL, command=canvas_left.yview)
frame_izquierdo = tk.Frame(canvas_left, bg=COLOR_BG, width=400)

frame_izquierdo.bind(
    "<Configure>",
    lambda e: canvas_left.configure(scrollregion=canvas_left.bbox("all"))
)

canvas_left.create_window((0, 0), window=frame_izquierdo, anchor="nw")
canvas_left.configure(yscrollcommand=scrollbar_left.set)

canvas_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar_left.pack(side=tk.RIGHT, fill=tk.Y)

# Permitir scroll con rueda del mouse
def on_mousewheel(event):
    canvas_left.yview_scroll(int(-1*(event.delta/120)), "units")

canvas_left.bind_all("<MouseWheel>", on_mousewheel)

# Sección de cámara
frame_camara_section = tk.LabelFrame(
    frame_izquierdo,
    text="📷 CAPTURA",
    font=("Arial", 12, "bold"),
    fg=COLOR_HIGHLIGHT,
    bg=COLOR_PANEL,
    bd=2
)
frame_camara_section.pack(padx=8, pady=5, fill=tk.BOTH)

frame_video = tk.Frame(
    frame_camara_section,
    width=380,
    height=280,
    bg="#000000",
    bd=2,
    relief="solid"
)
frame_video.pack(padx=10, pady=10)
frame_video.pack_propagate(False)

label_img = tk.Label(frame_video, bg="#1a1a1a", text="📷 Ninguna imagen", font=("Arial", 14), anchor="center", justify=tk.CENTER)
label_img.place(relwidth=1, relheight=1)

# Resultado
label_resultado = tk.Label(
    frame_camara_section,
    text="Resultado: Esperando clasificación...",
    font=("Arial", 10, "bold"),
    fg=COLOR_HIGHLIGHT,
    bg=COLOR_PANEL
)
label_resultado.pack(pady=3)

# Confianza (barra de progreso)
frame_confianza = tk.Frame(frame_camara_section, bg=COLOR_PANEL)
frame_confianza.pack(padx=10, pady=3, fill=tk.X)

tk.Label(frame_confianza, text="Confianza:", font=("Arial", 9), fg=COLOR_TEXT, bg=COLOR_PANEL).pack(side=tk.LEFT)
label_confianza = tk.Label(frame_confianza, text="0%", font=("Arial", 9, "bold"), fg=COLOR_HIGHLIGHT, bg=COLOR_PANEL)
label_confianza.pack(side=tk.RIGHT)

# ---- BOTONES ----
frame_botones = tk.LabelFrame(
    frame_izquierdo,
    text="🎮 CONTROLES",
    font=("Arial", 12, "bold"),
    fg=COLOR_HIGHLIGHT,
    bg=COLOR_PANEL,
    bd=2
)
frame_botones.pack(padx=8, pady=5, fill=tk.BOTH)

botones_config = [
    ("📁 Subir Imagen", "#27AE60"),
    ("📷 Usar Cámara", "#2980B9"),
    ("📸 Capturar Foto", "#9B59B6"),
    ("⛔ Detener Cámara", "#C0392B"),
]

botones_dict = {}
for texto, color in botones_config:
    btn = tk.Button(
        frame_botones,
        text=texto,
        bg=color,
        fg="white",
        font=("Arial", 9, "bold"),
        width=22,
        relief=tk.RAISED,
        bd=1,
        activebackground=color,
        activeforeground="white"
    )
    btn.pack(pady=3, padx=5)
    botones_dict[texto.split()[0]] = btn

# ---- ESTADÍSTICAS DE SESIÓN ----
frame_stats = tk.LabelFrame(
    frame_izquierdo,
    text="📊 ESTADÍSTICAS",
    font=("Arial", 11, "bold"),
    fg=COLOR_HIGHLIGHT,
    bg=COLOR_PANEL,
    bd=2
)
frame_stats.pack(padx=8, pady=5, fill=tk.BOTH, expand=True)

# Total de predicciones
label_total = tk.Label(
    frame_stats,
    text="Total: 0",
    font=("Arial", 10, "bold"),
    fg=COLOR_HIGHLIGHT,
    bg=COLOR_PANEL
)
label_total.pack(anchor=tk.W, padx=10, pady=5)

# Metal
tk.Label(frame_stats, text="🔩 Metal", font=("Arial", 9), fg="#E74C3C", bg=COLOR_PANEL).pack(anchor=tk.W, padx=10)
frame_metal = tk.Frame(frame_stats, bg=COLOR_PANEL, height=15)
frame_metal.pack(fill=tk.X, padx=15, pady=2)
progress_metal = tk.Canvas(frame_metal, bg="#000000", height=12, bd=0, highlightthickness=0)
progress_metal.pack(fill=tk.X, side=tk.LEFT, expand=True)
label_metal_count = tk.Label(frame_stats, text="0", font=("Arial", 8), fg="#E74C3C", bg=COLOR_PANEL)
label_metal_count.pack(anchor=tk.E, padx=10)

# Orgánico
tk.Label(frame_stats, text="🌱 Orgánico", font=("Arial", 9), fg="#27AE60", bg=COLOR_PANEL).pack(anchor=tk.W, padx=10, pady=(10, 0))
frame_organico = tk.Frame(frame_stats, bg=COLOR_PANEL, height=15)
frame_organico.pack(fill=tk.X, padx=15, pady=2)
progress_organico = tk.Canvas(frame_organico, bg="#000000", height=12, bd=0, highlightthickness=0)
progress_organico.pack(fill=tk.X, side=tk.LEFT, expand=True)
label_organico_count = tk.Label(frame_stats, text="0", font=("Arial", 8), fg="#27AE60", bg=COLOR_PANEL)
label_organico_count.pack(anchor=tk.E, padx=10)

# Papel
tk.Label(frame_stats, text="📄 Papel", font=("Arial", 9), fg="#F39C12", bg=COLOR_PANEL).pack(anchor=tk.W, padx=10, pady=(10, 0))
frame_papel = tk.Frame(frame_stats, bg=COLOR_PANEL, height=15)
frame_papel.pack(fill=tk.X, padx=15, pady=2)
progress_papel = tk.Canvas(frame_papel, bg="#000000", height=12, bd=0, highlightthickness=0)
progress_papel.pack(fill=tk.X, side=tk.LEFT, expand=True)
label_papel_count = tk.Label(frame_stats, text="0", font=("Arial", 8), fg="#F39C12", bg=COLOR_PANEL)
label_papel_count.pack(anchor=tk.E, padx=10)

# Plástico
tk.Label(frame_stats, text="♻️ Plástico", font=("Arial", 9), fg="#3498DB", bg=COLOR_PANEL).pack(anchor=tk.W, padx=10, pady=(10, 0))
frame_plastico = tk.Frame(frame_stats, bg=COLOR_PANEL, height=15)
frame_plastico.pack(fill=tk.X, padx=15, pady=2)
progress_plastico = tk.Canvas(frame_plastico, bg="#000000", height=12, bd=0, highlightthickness=0)
progress_plastico.pack(fill=tk.X, side=tk.LEFT, expand=True)
label_plastico_count = tk.Label(frame_stats, text="0", font=("Arial", 8), fg="#3498DB", bg=COLOR_PANEL)
label_plastico_count.pack(anchor=tk.E, padx=10)

# ==================== PANEL CENTRAL Y DERECHO ====================
frame_centro_derecha = tk.Frame(frame_contenido, bg=COLOR_BG)
frame_centro_derecha.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)

# ---- INFORMACIÓN DEL RESIDUO ----
frame_info = tk.LabelFrame(
    frame_centro_derecha,
    text="ℹ️ INFORMACIÓN DETALLADA",
    font=("Arial", 13, "bold"),
    fg=COLOR_HIGHLIGHT,
    bg=COLOR_PANEL,
    bd=2
)
frame_info.pack(fill=tk.BOTH, expand=True, padx=8, pady=5)

# Área de texto principal y panel de imagen de la idea
frame_info_inner = tk.Frame(frame_info, bg=COLOR_PANEL)
frame_info_inner.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

text_info = scrolledtext.ScrolledText(
    frame_info_inner,
    width=70,
    height=28,
    bg="#0F3460",
    fg=COLOR_TEXT,
    font=("Courier", 9),
    bd=2,
    relief="solid",
    wrap=tk.WORD
)
text_info.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
text_info.config(state=tk.DISABLED)

# Panel derecho para mostrar la imagen de la idea de reutilización
frame_idea = tk.Frame(frame_info_inner, width=300, bg=COLOR_PANEL)
frame_idea.pack(side=tk.RIGHT, fill=tk.Y, padx=(10,0))
frame_idea.pack_propagate(False)

# Contenedor interno para centrar la imagen y la leyenda
frame_idea_inner = tk.Frame(frame_idea, bg=COLOR_PANEL)
frame_idea_inner.pack(expand=True, fill=tk.BOTH, padx=8, pady=8)

label_idea_img = tk.Label(frame_idea_inner, bg="#0F3460", text="🖼️ Idea", fg=COLOR_TEXT, bd=1, relief="solid")
label_idea_img.pack(fill=tk.BOTH, expand=True, padx=4, pady=(4,6))

label_idea_caption = tk.Label(frame_idea_inner, text="", bg=COLOR_PANEL, fg=COLOR_TEXT, font=("Arial", 10), wraplength=260, justify=tk.LEFT)
label_idea_caption.pack(pady=2, padx=4)

# Configurar tags para colores en el texto
text_info.tag_configure("titulo", font=("Arial", 14, "bold"), foreground=COLOR_HIGHLIGHT)
text_info.tag_configure("seccion", font=("Arial", 11, "bold"), foreground="#FFD700")
text_info.tag_configure("contenido", font=("Courier", 10), foreground=COLOR_TEXT)
text_info.tag_configure("stat", font=("Arial", 9), foreground="#00FF00")
text_info.tag_configure("warning", font=("Arial", 9, "bold"), foreground="#FF6B6B")

# ==================== FOOTER ====================
frame_footer = tk.Frame(ventana, bg=COLOR_ACCENT, height=30)
frame_footer.pack(fill=tk.X, padx=0, pady=0)
frame_footer.pack_propagate(False)

footer_text = tk.Label(
    frame_footer,
    text="💡 Tip: Aprende sobre cada residuo y cómo reciclarlo correctamente",
    font=("Arial", 8),
    fg="#B0B0B0",
    bg=COLOR_ACCENT
)
footer_text.pack(pady=5)

# ==================== VARIABLES GLOBALES ====================
cap = None
frame_actual = None
ultima_clase_preview = None
ultima_confianza_preview = 0.0
preview_activo = False
historial_predicciones = {"metal": 0, "organico": 0, "papel_carton": 0, "plastico": 0}
total_predicciones = 0

# Rutas de imágenes de ideas (colocar archivos en la carpeta 'ideas' junto al script)
BASE_DIR = os.path.dirname(__file__)
IDEAS_DIR = os.path.join(BASE_DIR, "ideas")
idea_image_paths = {
    "metal": os.path.join(IDEAS_DIR, "metal.jpg"),
    "organico": os.path.join(IDEAS_DIR, "organico.jpg"),
    "papel_carton": os.path.join(IDEAS_DIR, "papel_carton.jpg"),
    "plastico": os.path.join(IDEAS_DIR, "plastico.jpg"),
}

def cargar_imagen_idea(ruta, size=(260,260)):
    """Carga la imagen de la idea; si no existe, genera un placeholder centrado.
    Usa ImageOps.fit para mantener la proporción y rellenar el área sin distorsión.
    Muestra información del error por consola para depuración.
    """
    import traceback
    try:
        # Compatibilidad con versiones de Pillow para el parámetro de remuestreo
        try:
            resample = Image.Resampling.LANCZOS
        except AttributeError:
            resample = Image.ANTIALIAS

        if ruta and os.path.exists(ruta):
            img = Image.open(ruta).convert("RGB")
            img = ImageOps.fit(img, size, method=resample)
        else:
            # Generar placeholder centrado
            img = Image.new("RGB", size, (30, 30, 30))
            draw = ImageDraw.Draw(img)
            texto = "Imagen no disponible"
            # Usar textbbox si está disponible para medir mejor el texto
            try:
                bbox = draw.textbbox((0, 0), texto)
                w = bbox[2] - bbox[0]
                h = bbox[3] - bbox[1]
            except Exception:
                w, h = draw.textsize(texto)
            draw.text(((size[0]-w)/2, (size[1]-h)/2), texto, fill=(200,200,200))

        return ImageTk.PhotoImage(img)
    except Exception as e:
        # Imprime el error en consola para diagnóstico
        print("Error cargando imagen de idea:", e)
        traceback.print_exc()
        # Devolver un placeholder claro en pantalla en lugar del mensaje 'Error'
        img = Image.new("RGB", size, (40, 40, 40))
        draw = ImageDraw.Draw(img)
        texto = "Imagen no disponible"
        try:
            bbox = draw.textbbox((0, 0), texto)
            w = bbox[2] - bbox[0]
            h = bbox[3] - bbox[1]
        except Exception:
            w, h = draw.textsize(texto)
        draw.text(((size[0]-w)/2, (size[1]-h)/2), texto, fill=(200,200,200))
        return ImageTk.PhotoImage(img)

# ==================== FUNCIONES ====================

def actualizar_estadisticas():
    """Actualiza las estadísticas en pantalla con barras de progreso"""
    global total_predicciones
    
    label_total.config(text=f"Total: {total_predicciones}")
    
    # Calcular porcentajes
    if total_predicciones > 0:
        pct_metal = (historial_predicciones['metal'] / total_predicciones) * 100
        pct_organico = (historial_predicciones['organico'] / total_predicciones) * 100
        pct_papel = (historial_predicciones['papel_carton'] / total_predicciones) * 100
        pct_plastico = (historial_predicciones['plastico'] / total_predicciones) * 100
    else:
        pct_metal = pct_organico = pct_papel = pct_plastico = 0
    
    # Actualizar Metal
    progress_metal.delete("all")
    ancho_metal = int((pct_metal / 100) * 200)
    progress_metal.create_rectangle(0, 0, ancho_metal, 12, fill="#E74C3C", outline="")
    label_metal_count.config(text=f"{historial_predicciones['metal']} ({pct_metal:.0f}%)")
    
    # Actualizar Orgánico
    progress_organico.delete("all")
    ancho_organico = int((pct_organico / 100) * 200)
    progress_organico.create_rectangle(0, 0, ancho_organico, 12, fill="#27AE60", outline="")
    label_organico_count.config(text=f"{historial_predicciones['organico']} ({pct_organico:.0f}%)")
    
    # Actualizar Papel
    progress_papel.delete("all")
    ancho_papel = int((pct_papel / 100) * 200)
    progress_papel.create_rectangle(0, 0, ancho_papel, 12, fill="#F39C12", outline="")
    label_papel_count.config(text=f"{historial_predicciones['papel_carton']} ({pct_papel:.0f}%)")
    
    # Actualizar Plástico
    progress_plastico.delete("all")
    ancho_plastico = int((pct_plastico / 100) * 200)
    progress_plastico.create_rectangle(0, 0, ancho_plastico, 12, fill="#3498DB", outline="")
    label_plastico_count.config(text=f"{historial_predicciones['plastico']} ({pct_plastico:.0f}%)")

def predecir(frame):
    """Clasifica el residuo en la imagen"""
    img = cv2.resize(frame, (224, 224))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img, verbose=0)
    clase = classes[np.argmax(prediction)]
    confianza = np.max(prediction)

    return clase, confianza

def mostrar_previsualizacion_camara(clase, confianza):
    """Muestra una vista previa en vivo sin registrar estadísticas."""
    text_info.config(state=tk.NORMAL)
    text_info.delete(1.0, tk.END)
    text_info.insert(tk.END, f"👁️ Vista previa en vivo\n\nClasificación detectada: {clase.upper()}\nConfianza: {confianza*100:.1f}%\n\nPresiona 'Capturar Foto' para registrar este producto en las estadísticas y ver la información completa.")
    text_info.config(state=tk.DISABLED)

    label_idea_img.config(image="", text="🖼️ Idea")
    label_idea_caption.config(text="")


def mostrar_informacion(clase, confianza):
    """Muestra la información detallada del residuo"""
    global total_predicciones, historial_predicciones
    
    info = info_residuos.get(clase, {})
    
    # Actualizar estadísticas
    total_predicciones += 1
    historial_predicciones[clase] += 1
    actualizar_estadisticas()
    
    text_info.config(state=tk.NORMAL)
    text_info.delete(1.0, tk.END)
    
    # Contenido formateado
    contenido = f"""
{info.get('emoji_grande', '❓')} {info.get('nombre', 'DESCONOCIDO')}
{'='*95}

DESCRIPCIÓN:
{info.get('descripcion', 'N/A')}

TIEMPO DE DEGRADACIÓN EN NATURALEZA:
⏱️  {info.get('degradacion', 'N/A')}

IMPACTO AMBIENTAL:
{info.get('impacto_ambiental', 'N/A')}

BENEFICIOS DEL RECICLAJE:
✅ {info.get('beneficios_reciclaje', 'N/A')}

CÓMO RECICLAR CORRECTAMENTE:
🔄 {info.get('como_reciclar', 'N/A')}

DÓNDE TIRARLO:
📍 {info.get('donde_tirar', 'N/A')}

IDEAS DE REUTILIZACIÓN CREATIVA:
♻️  {info.get('reutilizacion', 'N/A')}

EJEMPLOS DE PRODUCTOS:
📦 {info.get('ejemplos_productos', 'N/A')}

ESTADÍSTICAS GLOBALES:
📊 {info.get('estadisticas', 'N/A')}

{'='*95}
Confianza de clasificación: {confianza*100:.1f}% | Hora: {datetime.now().strftime('%H:%M:%S')}
"""
    
    text_info.insert(tk.END, contenido)
    text_info.config(state=tk.DISABLED)

    # Mostrar imagen de la idea de reutilización (si existe)
    ruta_idea = idea_image_paths.get(clase)
    idea_img = cargar_imagen_idea(ruta_idea, size=(260,260))
    try:
        label_idea_img.config(image=idea_img, text="")
        label_idea_img.image = idea_img
    except Exception:
        label_idea_img.config(text="🖼️ Idea")

    # Mostrar una leyenda corta con la primera línea de 'reutilizacion'
    reutil_text = info.get('reutilizacion', '')
    primera_linea = reutil_text.split("\n")[0] if reutil_text else ''
    label_idea_caption.config(text=primera_linea)

def subir_imagen():
    global frame_actual
    ruta = filedialog.askopenfilename(filetypes=[("Imágenes", "*.jpg *.jpeg *.png *.bmp")])
    if not ruta:
        return

    frame = cv2.imread(ruta)
    if frame is None:
        label_resultado.config(text="Error: No se pudo cargar la imagen")
        return
    
    clase, confianza = predecir(frame)

    label_resultado.config(text=f"Resultado: {clase.upper()}")
    label_confianza.config(text=f"{confianza*100:.1f}%")

    frame_actual = frame.copy()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (380, 280))

    img = Image.fromarray(frame)
    img = ImageTk.PhotoImage(img)

    label_img.config(image=img)
    label_img.image = img

    mostrar_informacion(clase, confianza)
    botones_dict["📸"].config(state=tk.DISABLED)

def usar_camara():
    global cap, frame_actual, preview_activo
    cap = cv2.VideoCapture(0)
    preview_activo = True
    botones_dict["📸"].config(state=tk.NORMAL)
    botones_dict["📁"].config(state=tk.DISABLED)
    botones_dict["📷"].config(state=tk.DISABLED)
    actualizar_camara()

def actualizar_camara():
    global cap, frame_actual, ultima_clase_preview, ultima_confianza_preview, preview_activo

    if cap is None:
        return

    ret, frame = cap.read()
    if not ret:
        ventana.after(10, actualizar_camara)
        return

    frame_actual = frame.copy()
    clase, confianza = predecir(frame)
    ultima_clase_preview = clase
    ultima_confianza_preview = confianza
    
    label_resultado.config(text=f"En vivo: {clase.upper()}")
    label_confianza.config(text=f"{confianza*100:.1f}%")

    if preview_activo:
        mostrar_previsualizacion_camara(clase, confianza)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (380, 280))

    img = Image.fromarray(frame)
    img = ImageTk.PhotoImage(img)

    label_img.config(image=img)
    label_img.image = img

    ventana.after(10, actualizar_camara)

def capturar_foto():
    """Captura foto desde la cámara sin detenerla"""
    global frame_actual, ultima_clase_preview, ultima_confianza_preview, preview_activo

    if frame_actual is None:
        label_resultado.config(text="Error: No hay imagen de cámara disponible")
        label_confianza.config(text="0%")
        return

    label_resultado.config(text="Capturando...")
    ventana.update_idletasks()

    frame = frame_actual.copy()
    clase, confianza = predecir(frame)
    if clase is None:
        clase = ultima_clase_preview or "desconocido"
        confianza = ultima_confianza_preview

    preview_activo = False

    label_resultado.config(text=f"Capturada: {clase.upper()}")
    label_confianza.config(text=f"{confianza*100:.1f}%")

    mostrar_informacion(clase, confianza)

def detener_camara():
    global cap, preview_activo
    if cap:
        cap.release()
        cap = None
    preview_activo = False
    botones_dict["📸"].config(state=tk.DISABLED)
    botones_dict["📁"].config(state=tk.NORMAL)
    botones_dict["📷"].config(state=tk.NORMAL)
    label_resultado.config(text="Cámara detenida")
    text_info.config(state=tk.NORMAL)
    text_info.delete(1.0, tk.END)
    text_info.insert(tk.END, "Selecciona una opción para comenzar...")
    text_info.config(state=tk.DISABLED)

# ==================== CONEXIÓN DE BOTONES ====================
botones_dict["📁"].config(command=subir_imagen)
botones_dict["📷"].config(command=usar_camara)
botones_dict["📸"].config(command=capturar_foto)
botones_dict["⛔"].config(command=detener_camara)

# Mensaje inicial
text_info.config(state=tk.NORMAL)
text_info.insert(tk.END, "👋 Bienvenido al Clasificador de Residuos\n\n"
                         "📸 Pasos:\n"
                         "1. Haz clic en 'Subir Imagen' para cargar una foto\n"
                         "2. O selecciona 'Usar Cámara' para clasificación en vivo\n"
                         "3. Presiona 'Capturar Foto' para tomar fotos sin detener la cámara\n"
                         "4. Aprende sobre cada residuo y cómo reciclarlo\n\n"
                         "🌍 Juntos podemos hacer una diferencia ambiental")
text_info.config(state=tk.DISABLED)

ventana.mainloop()