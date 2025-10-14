#Escribir un programa que pida al usuario dos números y muestre por pantalla su
#división. Si el divisor es cero el programa debe mostrar un error.

num1 = int(input("Introduce el dividendo: "))
num2 = int(input("Introduce el divisor: "))


if num2 == 0 :
    print ("No se puede dividir por cero")
else :
    print (f" El cociente de la division es: {num1 / num2}")    