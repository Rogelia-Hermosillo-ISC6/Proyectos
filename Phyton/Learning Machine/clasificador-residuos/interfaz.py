import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import tensorflow as tf
import cv2
import numpy as np

model = tf.keras.models.load_model("modelo_residuos.h5")
classes = ["metal", "organico", "papel_carton", "plastico"]

ventana = tk.Tk()
ventana.title("Clasificador de Residuos")
ventana.geometry("700x550")
ventana.config(bg="#2C3E50")  

titulo = tk.Label(
    ventana,
    text="CLASIFICADOR DE RESIDUOS",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#2C3E50"
)
titulo.pack(pady=10)

frame_principal = tk.Frame(ventana, bg="#2C3E50")
frame_principal.pack()

frame_video = tk.Frame(
    frame_principal,
    width=420,
    height=300,
    bg="#34495E",
    bd=2,
    relief="ridge"
)
frame_video.grid(row=0, column=0, padx=20, pady=10)

label_img = tk.Label(frame_video, bg="#34495E")
label_img.place(relwidth=1, relheight=1)

label_resultado = tk.Label(
    ventana,
    text="Resultado:",
    font=("Arial", 14, "bold"),
    fg="#ECF0F1",
    bg="#2C3E50"
)
label_resultado.pack(pady=10)

def predecir(frame):
    img = cv2.resize(frame, (224,224))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img, verbose=0)
    clase = classes[np.argmax(prediction)]
    confianza = np.max(prediction)

    return clase, confianza

def subir_imagen():
    ruta = filedialog.askopenfilename()
    if not ruta:
        return

    frame = cv2.imread(ruta)
    clase, confianza = predecir(frame)

    texto = f"{clase.upper()}  |  {confianza*100:.2f}%"
    label_resultado.config(text=texto)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (420,300))

    img = Image.fromarray(frame)
    img = ImageTk.PhotoImage(img)

    label_img.config(image=img)
    label_img.image = img

cap = None

def usar_camara():
    global cap
    cap = cv2.VideoCapture(0)
    actualizar_camara()

def actualizar_camara():
    global cap

    if cap is None:
        return

    ret, frame = cap.read()
    if not ret:
        return

    clase, confianza = predecir(frame)
    texto = f"{clase.upper()}  |  {confianza*100:.2f}%"
    label_resultado.config(text=texto)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (420,300))

    img = Image.fromarray(frame)
    img = ImageTk.PhotoImage(img)

    label_img.config(image=img)
    label_img.image = img

    ventana.after(10, actualizar_camara)

def detener_camara():
    global cap
    if cap:
        cap.release()
        cap = None

frame_botones = tk.Frame(ventana, bg="#2C3E50")
frame_botones.pack(pady=10)

btn_imagen = tk.Button(
    frame_botones,
    text="📁 Subir Imagen",
    command=subir_imagen,
    bg="#27AE60",
    fg="white",
    font=("Arial", 11, "bold"),
    width=18
)
btn_imagen.grid(row=0, column=0, padx=10)

btn_camara = tk.Button(
    frame_botones,
    text="📷 Usar Cámara",
    command=usar_camara,
    bg="#2980B9",
    fg="white",
    font=("Arial", 11, "bold"),
    width=18
)
btn_camara.grid(row=0, column=1, padx=10)

btn_detener = tk.Button(
    frame_botones,
    text="⛔ Detener",
    command=detener_camara,
    bg="#C0392B",
    fg="white",
    font=("Arial", 11, "bold"),
    width=18
)
btn_detener.grid(row=0, column=2, padx=10)
ventana.mainloop()