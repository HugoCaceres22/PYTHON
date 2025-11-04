#Escribir un programa que almacene la cadena de caracteres contraseña en una
#variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
#correcta.
  
contraseña = "hola"

pregunta = input("Escribe tu contraseña : ")


if pregunta == contraseña :
        print ("Contraseña correcta")

else : 
    print ("contraseña incorrecta, vuelve a introducirla")
    
    while pregunta != contraseña :
        pregunta = input("Escribe tu contraseña : ")
     

