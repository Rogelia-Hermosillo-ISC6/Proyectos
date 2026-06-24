import tensorflow as tf 
import cv2
import numpy as np

model = tf.keras.models.load_model("modelo_residuos.h5")

classes = ["metal", "organico", "papel_carton", "plastico"]

ruta_imagen = "prueba.jpg"
img = cv2.imread(ruta_imagen)

img_resized = cv2.resize(img, (224,224))
img_resized = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
img_resized = img_resized / 255.0
img_resized = np.expand_dims(img_resized, axis=0)

prediction = model.predict(img_resized)

clase = classes[np.argmax(prediction)]
confianza = np.max(prediction)

print("Predicción:", clase)
print("Confianza:", confianza*100, "%")

texto = f"{clase}: {confianza*100:.2f}%"

cv2.rectangle(img, (10,10), (400,70), (0,0,0), -1)

cv2.putText(
    img,
    texto,
    (20,50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255,255,0), 
    2,
    cv2.LINE_AA
)

cv2.imshow("Resultado", img)
cv2.waitKey(0)
cv2.destroyAllWindows()