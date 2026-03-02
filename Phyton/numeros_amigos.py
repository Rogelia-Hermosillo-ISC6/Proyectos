#programa que pida dos numeros y diga si son amigos o no 
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
def son_amigos(num1, num2):
    def suma_divisores(n):
        suma = 0
        for i in range(1, n):
            if n % i == 0:
                suma += i
        return suma
    return suma_divisores(num1) == num2 and suma_divisores(num2) == num1

if son_amigos(numero1, numero2):
    print(f"Son amigos.")
else:
    print(f"No son amigos.")
