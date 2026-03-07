# ordenar_lista.py
"""
Ejercicio: lista de números

1. Solicite al usuario ingresar 5 números enteros
2. Guarde cada número en una lista 
3. Una vez ingresados todos los números, el programa debe:
    - Mostrar la lista de numeros ingresados
    - Mostrar cuál es el número mayor
    - Mostrar cuál es el número menor
    - Mostrar la lista ordenada de mayor a menor.
"""
numeros = []
for i in range(5):
    num = int(input(f"Ingrese nro {i + 1} : "))
    numeros.append(num) 
    
# mostrar la lista de números ingresados
print(f"Lista ingresada : {numeros}")

# mostrar cual es el número mayor
mayor = max(numeros)
print(f"El mayor es {mayor}")

# mostrar cual es el número menor
menor = min(numeros)
print(f"El menor es {menor}")

# ordenar de mayor a menor
lista_ordenada = sorted(numeros,reverse=True)
print(f"Lista ordenada : {lista_ordenada}")



