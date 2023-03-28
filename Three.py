# 3. Orden descendente de números pares hasta 2 que sean < ó = n y n > ó =2
n : int = 350 # para iniciar, ingresar un número n
while (n >= 2): # n debe ser > ó = a 2
    n -= 1  # actualizar con n - 1 para ir de mayor a menor
    if n % 2 != 0: # el modulo difernte de 0
        continue # la condición anterior indica números impares, si se cumple continúa con el siguiente 
    print(n) # si no se cumple lo anterior, imprimir el número, siendo éste par