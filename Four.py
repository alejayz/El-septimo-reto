# 4. Cuándo la población B superará a la de A.
A : float = 25 # se inicializa a A en millones
B : float = 18.9 # se inicializa a B en millones 
Año: int = 2022 # se inicializa en el año dado
while (A >= B): # A debe ser > ó = que B
    A = (A**0.02) + A  # calcular aumento con porcentaje
    B = (B**0.03) + B  # calcular aumento con porcentaje
    Año += 1 # actualizar con tiempo
print(" la población superará a la población de A en: " + str(Año)) # para indicar el dato final