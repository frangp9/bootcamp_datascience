# BUCLE FOR : PERMITE REPETIR SENTENCIAS DE CODIGO UNA DETERMINADA CANITDAD DE VECES 
for contador in range(1,11,3):
    print(contador)

# TABLA DE MULTIPICAR
# ENTRADA
tabla = int(input('Ingrese la tabla de multiplicar que desea ver : '))
# PROCESO
for contador in range(1,13,1):
    resultado = tabla * contador
    print(f'{tabla} x {contador} = {resultado}')
    