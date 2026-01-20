divisas = {
    "Euro": "€",
    "Dollar": "$",
    "Yen": "¥"
}

moneda = input("Introduce una divisa: ")

if moneda in divisas:
    print("El símbolo es:", divisas[moneda])
else:
    print("Esa divisa no está en el diccionario")
