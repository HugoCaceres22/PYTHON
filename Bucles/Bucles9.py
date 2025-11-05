#Escribir un programa que almacene la cadena de caracteres contraseña en una
#variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
#correcta.
  
contraseña = "hola"
pregunta = input("Escribe tu contraseña : ")

if pregunta == contraseña :
        print ("Contraseña correcta")

else :     
    while pregunta != contraseña :
        print ("contraseña incorrecta, vuelve a introducirla")
        pregunta = input("Escribe tu contraseña : ")
     

