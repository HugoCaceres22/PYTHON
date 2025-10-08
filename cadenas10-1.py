#Escribir un programa que pregunte por consola por los productos de una cesta de la
#compra, separados por comas, y muestre por pantalla cada uno de los productos en
#una línea distinta.

p = input("Introduce los productos de la compra separados por una coma: ")


i = p.replace(", ", "\n")# Reemplaza , por salto de línea

print(i)







