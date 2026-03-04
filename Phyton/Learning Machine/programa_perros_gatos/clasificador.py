import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
img_size = (150, 150)
batch_size = 32

train_ds = keras.utils.image_dataset_from_directory(
    "train",
    image_size=img_size,
    batch_size=batch_size,
    label_mode="binary"
)

val_ds = keras.utils.image_dataset_from_directory(
    "test",
    image_size=img_size,
    batch_size=batch_size,
    label_mode="binary"
)
train_ds = train_ds.cache().prefetch(buffer_size=tf.data.AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=tf.data.AUTOTUNE)

model = keras.Sequential([
    layers.Rescaling(1./255, input_shape=(150, 150, 3)),
    
    layers.Conv2D(32, (3,3), activation='relu'),
    layers.MaxPooling2D(),
    
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(),
    
    layers.Flatten(),
    layers.Dense(12, activation='relu'), 
    layers.Dropout(0.5),
    layers.Dense(1, activation='sigmoid') 
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

print("\nIniciando entrenamiento rápido...")
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=3
)

model.save("modelo_perros_gatos.h5")
print("\nModelo guardado como 'modelo_perros_gatos.h5'")

plt.figure(figsize=(10, 4))
plt.plot(history.history['accuracy'], label='Precisión Entrenamiento')
plt.plot(history.history['val_accuracy'], label='Precisión Validación')
plt.legend()
plt.title("Progreso del Entrenamiento")
plt.xlabel("Épocas")
plt.ylabel("Precisión")
plt.show()