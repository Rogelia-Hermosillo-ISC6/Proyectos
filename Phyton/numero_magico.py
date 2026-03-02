#codigo que genere un numero aleatorio y el usuario tenga que adivinarlo
import random   
numero_aleatorio = random.randint(1, 100)
intentos = 0
adivinado = False   
while not adivinado:
    intento = int(input("Adivina el numero entre 1 y 100: "))
    intentos += 1
    if intento < numero_aleatorio:
        print("Bajo. Intenta de nuevo.")
    elif intento > numero_aleatorio:
        print("Alto. Intenta de nuevo.")
    else:
        adivinado = True
        print(f"¡Felicidades! Adivinaste el numero {numero_aleatorio} en {intentos} intentos.")

