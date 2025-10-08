#Escribir un programa que pregunte el nombre el un producto, su precio y un número
#de unidades y muestre por pantalla una cadena con el nombre del producto seguido
#de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con
#tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

no = input("Introduce el NOMBRE del producto: ")
pr = float(input("Introduce el PRECIO del producto: "))
nu = float(input("Introduce el numero de UNIDADES  del producto: "))
pt = pr*nu

print(f"El producto {no} tiene un precio de {pr:08.2f} , el numero de unidades es {nu:03.0f} y un coste de {pt:010.2f} ")

#pr es de donde se obtiene el valor, 08 son las cifras totales, con enteros y decimales
# a partir del . son los numeros decimales ya que f es float (decimal)







