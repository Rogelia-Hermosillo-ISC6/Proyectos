#con funciones realizar un programa que calcule la serie fibonacci
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    serie = [0, 1]
    for i in range(2, n):
        next_value = serie[i-1] + serie[i-2]
        serie.append(next_value)
    
    return serie
num_terms = int(input("Cuantos numeros??: "))
fibonacci_series = fibonacci(num_terms)  
print(fibonacci_series)
