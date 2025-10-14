#Escribir un programa que almacene la cadena de caracteres contraseña en una
#variable, pregunte al usuario por la contraseña e imprima por pantalla si la
#contraseña introducida por el usuario coincide con la guardada en la variable sin
#tener en cuenta mayúsculas y minúsculas.


contraseña = "hola3"
contraseñaniput = input("Introduce tu contraseña: ")

if contraseña.lower() == contraseñaniput.lower()  :
    print ("La contraseña coincide con la de la variable")
else :
    print ("La contraseña NO coincide con la de la variable")    