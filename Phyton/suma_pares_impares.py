#suma de numeros pares e impares de 1 a 100, una funcion para sumar pares y otra para impares
def sumar_pares(n):
    suma = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            suma += i
    return suma

def sumar_impares(n):
    suma = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            suma += i
    return suma
suma_pares = sumar_pares(100)        
suma_impares = sumar_impares(100)
print(f"Suma de números pares de 1 a 100: {suma_pares}")
print(f"Suma de números impares de 1 a 100: {suma_impares}") 
  

  
