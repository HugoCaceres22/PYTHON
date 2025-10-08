#Escribir un programa que pregunte por consola por los productos de una cesta de la
#compra, separados por comas, y muestre por pantalla cada uno de los productos en
#una línea distinta.

#PARA EL EXAMEN MEJOR LA 10-1
p = input("Introduce los productos de la compra separados por una coma: ")

i = p.split(",")
x = "\n".join(i) #une todos los elementos de i, insertando "\n" entre cada elemento.

print(x)







