import tensorflow as tf
import numpy as np

celcius= np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit= np.array([-40, 14, 32, 46.4, 59, 71.6, 100.4], dtype=float)     

capa= tf.keras.layers.Dense(units=1, input_shape=[1])
modelo= tf.keras.Sequential([capa])

modelo.compile(optimizer=tf.keras.optimizers.Adam(0.1), loss='mean_squared_error')
print("Entrenando el modelo...")
historial= modelo.fit(celcius, fahrenheit, epochs=1000, verbose=False)
print("Modelo entrenado!")

import matplotlib.pyplot as plt
plt.xlabel('Épocas')

plt.ylabel('Magnitud de pérdida')
plt.plot(historial.history['loss'])
plt.show()


print("Hagamos una predicción! ¿Cuántos grados Fahrenheit son 100 grados Celcius?")
resultado= modelo.predict([100.0])
print("El modelo predice que 100 grados Celcius son " + str(resultado) + " grados Fahrenheit.")

