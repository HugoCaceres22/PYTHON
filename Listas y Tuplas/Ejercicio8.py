palabra = input("Introduce una palabra: ")

# Convertir a lista
lista_palabra = list(palabra)

# Copiar lista
lista_reves = lista_palabra.copy()


lista_reves.reverse()



if lista_palabra == lista_reves:
    print ("Tu palabra es un palindromo")
else:
    print ("Tu palabra NO es un palindromo")