def factura(precio, iva=21):
    return precio + precio * iva / 100


precio = int(input("Introduce el precio sin IVA: "))

iva = input("Introduce el porcentaje de IVA (enter para 21): ")

if iva == "":
    print("Total factura:", factura(precio))
else:
    print("Total factura:", factura(precio, int(iva)))
