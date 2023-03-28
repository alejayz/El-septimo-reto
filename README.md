# El-septimo-reto

El reto número 7 de la clase de programación y el cual resolveré en este repo consiste en:

*1.* Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

```python
i : int = 1 # se toma el 1 ya que es el inicio de la lista
while (i <= 100): # la lista debe ser hasta el 100
    cuadrado = i**2 # opración para hallar cuadrado
    print(str(i) + " - su cuadrado es " + str(cuadrado)) # imprimir el número y su cuadrado para finalizar el ciclo
    i += 1 # actualizar
```

*2.* Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

```python
a : int = 3 # se toma a 3 como inicio 
print("impares") # para indicar tipo de números
while (a <= 999): # los números deber llegar hasta 999
    if a % 2 != 0: # modulo debe ser diferente de 0
        print(a) # para finalizar, dada la condición anterior imprimir el número
    a += 1 # actualizar
print("fin") # para indicar fin de la lista

b : int = 2 # se toma el 2 como inicio
print("pares")
while (b <= 1000): # los números deben llegar hasta 1000
    if b % 2 == 0: # modulo deber ser iguaal a 0
        print(b) # imprimir el número de acuerdo a la condición dada para finalizar el ciclo
    b += 1
print("fin")
```

*3.* Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

```python
n : int # para iniciar, ingresar un número n
while (n >= 2): # n debe ser > ó = a 2
    n -= 1  # actualizar con n - 1 para ir de mayor a menor
    if n % 2 != 0: # el modulo difernte de 0
        continue # la condición anterior indica números impares, si se cumple continúa con el siguiente 
    print(n) # si no se cumple lo anterior, imprimir el número, siendo éste par
```

*4.* En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18:9 millones. Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.

```python
A : float = 25 # se inicializa a A en millones
B : float = 18.9 # se inicializa a B en millones 
Año: int = 2022 # se inicializa en el año dado
while (A >= B): # A debe ser > ó = que B
    A = (A**0.02) + A  # calcular aumento con porcentaje
    B = (B**0.03) + B  # calcular aumento con porcentaje
    Año += 1 # actualizar con tiempo
print(" la población superará a la población de A en: " + str(Año)) # para indicar el dato final
```

*5.* Imprimir el factorial de un número natural n dado.

*6.* Implementar un algoritmo que permita adivinar un número dado de 1 a 100, preguntando en cada caso si el número es mayor, menor o igual.

*7.* Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.

*8.* Implementar el algoritmo que muestre los números primos del 1 al 100. nota: use funciones
