import math
# PROGRAMA CONVERSOR DE MONEDA SOLES A DOLARES (VICEVERSA) 
Salir = "no"
while(Salir == "no"):
    # ENTRADA
    print("================ CONVERTIDOR DE MONEDAS ============")

    print("=================== OPCIONES ====================")
    print("TC : 3.00 ")
    print("1. SOLES A DOLARES")
    print("2. DOLARES A SOLES")
    print("3. SALIR")
    print("=================================================")
    opcion = int(input("Ingrese la opcion deseada: "))
    
    #PROCESO
    TC = 3
    if(opcion == 1):
        operacion = "PEN - USD"
        PEN = int(input("Soles (PEN) : "))
        resultado = PEN / TC
        print(f"El total de {operacion} = {resultado:.2f} dólares")
    elif opcion == 2:
        operacion = "USD - PEN"
        USD = int(input("Dólares (USD) : "))
        resultado = USD * TC
        print(f"El total de {operacion} = {resultado:.2f} soles")
    elif opcion == 3:
        print("Gracias por usar el programa! Hasta la próxima!")
        break
               
    else:
        print("opción no valida...")
       
    Salir = input("Desea hacer otra operación ?(si,no) : ")
    if Salir == "si":
        break
