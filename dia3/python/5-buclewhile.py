# BUCLE WHILE A DIFERENCIA DE FOR EJECUTA UNA ACCION MIENTRAS SE CUMPLA UNA CONDICIÓN
contador = 1
while(contador < 10):
    print(contador)
    contador += 1
    
numero_adivinar = 5
print('Adivina que nro estoy pensando')
while(contador != numero_adivinar):
    contador = int(input())
    if contador == numero_adivinar:
        print('GANASTE')
    else:
        print('intenta otra vez : ')
        