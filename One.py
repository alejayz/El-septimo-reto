# 1. Programa que imprima listado de números del 1 al 100 con sus cuadrados.
i : int = 1 # se toma el 1 ya que es el inicio de la lista
while (i <= 100): # la lista debe ser hasta el 100
    cuadrado = i**2 # opración para hallar cuadrado
    print(str(i) + " - su cuadrado es " + str(cuadrado)) # imprimir el número y su cuadrado para finalizar el ciclo
    i += 1 # actualizar