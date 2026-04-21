import tensorflow as tf
import numpy as np
import cv2

model = tf.keras.models.load_model("modelo_residuos.h5")
clases = ["metal","organico","papel","plastico"]

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    img = cv2.resize(frame, (224,224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img, verbose=0)
    resultado = clases[np.argmax(pred)]

    cv2.putText(
        frame,
        resultado,
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )
    cv2.imshow("Clasificador de residuos", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()