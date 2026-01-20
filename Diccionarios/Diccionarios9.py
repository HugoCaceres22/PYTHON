facturas = {}

while True:
    print("1. Añadir factura")
    print("2. Pagar factura")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        numero = input("Número de factura: ")
        coste = float(input("Coste: "))
        facturas[numero] = coste

    elif opcion == "2":
        numero = input("Número de factura a pagar: ")

        if numero in facturas:
            del facturas[numero]
            print("Factura pagada")
        else:
            print("No existe esa factura")

    elif opcion == "3":
        break

print("Facturas pendientes:", facturas)
