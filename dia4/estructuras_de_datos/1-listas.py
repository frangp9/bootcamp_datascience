# LISTAS 
# una lista es una coleccion ordenada y mutable de elementos
# se definen utilizanso corchetes [] y los elementos están separados por comas. 
dias = ["lunes","martes","miercoles","jueves","viernes"]

#imprimir uno o mas datos
# print(dias) - imprime todo
# print(dias[0]) - imprime el primer dia
# print(dias[1;4]) - imprime un rango 
# print(dias[:]) - imprime todos
# print(dias[-1]) - el ultimo

print(dias)
print(dias[0])
print(dias[1:4])
print(dias[-1])
print(dias[:])

#agregar valores a la lista 
dias.append("sábado")
dias.append("domingo")
print(dias)

#eliminar valores de la lista
dias.pop() #elimina el último elemento de la lista 
dias.pop(3)
print(dias)

#modificar un elemento de la lista 
dias[3] = "jueves"
dias[4] = "viernes"
print(dias)

#recorrer una lista con bucle for
print(f"total de la lista de dias : {len(dias)}")
for contador in range(len(dias)):
    print(f"Hoy es {dias[contador]}")
    
#forma mejorada
for dia in dias:
    print(f"hoy es {dia}")
    