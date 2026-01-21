def estadisticas(numeros):
    n = len(numeros)

    suma = 0
    for x in numeros:
        suma += x
    media = suma / n

    suma_cuadrados = 0
    for x in numeros:
        suma_cuadrados += (x - media) * (x - media)
    varianza = suma_cuadrados / n

    desviacion = varianza ** 0.5  # raíz cuadrada sin importar nada

    return {"media": media, "varianza": varianza, "desviacion": desviacion}


# Ejemplo de uso
lista = [1, 2, 3, 4, 5]
print(estadisticas(lista))
