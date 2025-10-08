#Escribir un programa que pregunte por consola el precio de un producto en euros
#con dos decimales y muestre por pantalla el número de euros y el número de
#céntimos del precio introducido

precio = input("Introduce el precio en euros con 2 decimales: ")
d = precio.split(".")[1]
e = precio.split(".")[0]


print (f"El precio es: {e} euros y {d} céntimos") 

