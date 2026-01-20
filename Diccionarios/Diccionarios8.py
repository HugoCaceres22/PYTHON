texto = input("Introduce palabras (es:en separadas por comas): ")

pares = texto.split(",")

diccionario = {}

for par in pares:
    partes = par.split(":")
    diccionario[partes[0]] = partes[1]

frase = input("Introduce una frase en español: ")

palabras = frase.split(" ")

resultado = ""

for palabra in palabras:
    if palabra in diccionario:
        resultado += diccionario[palabra] + " "
    else:
        resultado += palabra + " "

print(resultado)
