#Escribir un programa para una empresa que tiene salas de juegos para todas las
#edades y quiere calcular de forma automática el precio que debe cobrar a sus
#clientes por entrar. El programa debe preguntar al usuario la edad del cliente y
#mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis,
#si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

año = int(input("Introduce tu edad: "))
precios = "GRATIS,5€,10€"


if año < 4:
    print(f"El precio es {precios.split(',')[0]}")

elif año >=4 and año <18:
    print(f"El precio es {precios.split(',')[1]}")

else:
    print(f"El precio es {precios.split(',')[2]}")


