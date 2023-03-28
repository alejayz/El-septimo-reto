# 2. imprimir lista de impares desde 3 hasta 999 y lista de pares desde 2 hasta 1000.
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