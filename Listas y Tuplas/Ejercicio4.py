numeros = []          

for i in range(6):     
    num = int(input("Introduce un número ganador: "))
    numeros.append(num)  

numeros.sort()         

print("Los números ganadores ordenados son:", numeros)
