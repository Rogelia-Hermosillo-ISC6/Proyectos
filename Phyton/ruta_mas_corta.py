import math

def calcular_distancia(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def optimizar_ruta(ubicacion_inicial, lista_paquetes, tiempo_maximo):
    ruta_optima = []
    paquetes_pendientes = lista_paquetes.copy()
    posicion_actual = ubicacion_inicial
    tiempo_total = 0
    paquetes_no_entregados = []

    while paquetes_pendientes:
        paquete_cercano = min(
            paquetes_pendientes, 
            key=lambda p: calcular_distancia(posicion_actual, (p[1], p[2]))
        )
        
        distancia = calcular_distancia(posicion_actual, (paquete_cercano[1], paquete_cercano[2]))
        tiempo_viaje = distancia + paquete_cercano[3] 

        if tiempo_total + tiempo_viaje <= tiempo_maximo:
            tiempo_total += tiempo_viaje
            posicion_actual = (paquete_cercano[1], paquete_cercano[2])
            ruta_optima.append(paquete_cercano)
            paquetes_pendientes.remove(paquete_cercano)
        else:
            paquetes_no_entregados = paquetes_pendientes.copy()
            break

    return ruta_optima, tiempo_total, paquetes_no_entregados

inicio = (0, 0) 
max_tiempo = 50 
mis_paquetes = [
    (1, 10, 10, 5),
    (2, 2, 3, 2),
    (3, 20, 25, 10),
    (4, 5, 5, 3)
]

ruta, tiempo, fuera = optimizar_ruta(inicio, mis_paquetes, max_tiempo)

print("--- RESULTADOS DEL REPARTO ---")
print(f"Secuencia óptima de entrega: {[p[0] for p in ruta]}")
print(f"Tiempo total estimado: {tiempo:.2f} minutos")

if fuera:
    print("\nPaquetes que no se pudieron completar:")
    for p in fuera:
        print(f"- Paquete ID {p[0]}: Tiempo insuficiente.")