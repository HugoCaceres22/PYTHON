#Escribir un programa que pregunte por consola el precio de un producto en euros
#con dos decimales y muestre por pantalla el número de euros y el número de
#céntimos del precio introducido

precio = round(float(input("Introduce el precio en euros: ")), 2)

print (f"El precio en euros es: {precio} y el precio en céntimos es: {precio*100}") 

