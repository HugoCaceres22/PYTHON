lista = [1,2,3,4]

def cuadrado(lista):
    resultado = []
    
    for i in lista:
        resultado.append(i**2)
    
    return (resultado)

print(cuadrado(lista))