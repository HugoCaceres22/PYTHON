cantidad = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interes anual (%): "))
años = int(input("Introduce el nmmero de años: "))
capital = cantidad * (1 + interes / 100) ** años
print("El capital obtenido es", capital)





