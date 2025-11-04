#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla
#una a una las letras de la palabra introducida empezando por la última.
     
palabra = str(input("Escribe un numero : "))
num = len(palabra)
i = 1

while i <= len(palabra) :
    print (palabra[len(palabra) - i])
    i = i+1





        