import tensorflow as tf
import numpy as np

pulgadas = np.array([1, 2, 4, 6, 8, 10, 20], dtype=float)
metros = np.array([0.0254, 0.0508, 0.1016, 0.1524, 0.2032, 0.254, 0.508], dtype=float)

capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("Entrenando el modelo...")
historial = modelo.fit(pulgadas, metros, epochs=1000, verbose=False)
print("¡Modelo entrenado!")

import matplotlib.pyplot as plt
plt.xlabel('Épocas')
plt.ylabel('Magnitud de pérdida')
plt.plot(historial.history['loss'])
plt.show()
print("Hagamos una predicción...")
print("¿Cuántos metros son 4 pulgadas?")

resultado = modelo.predict([4.0])
print("El modelo predice que 4 pulgadas son " + str(resultado) + " metros.")