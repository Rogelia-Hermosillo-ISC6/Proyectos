import tensorflow as tf
from tensorflow import keras
import numpy as np
from tensorflow.keras.preprocessing import image

# Cargar modelo entrenado
model = keras.models.load_model("modelo_perros_gatos.h5")

# Imagen de prueba
img_path = "imagen_prueba.jpg"  # Cambia por tu archivo
img = image.load_img(img_path, target_size=(150,150))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0) / 255.0

# Predecir
prediction = model.predict(img_array)

if prediction[0][0] > 0.5:
    print("Es un PERRO 🐶")
else:
    print("Es un GATO 🐱")