frutas = {
    "Plátano": 1.35,
    "Manzana": 0.80,
    "Pera": 0.85,
    "Naranja": 0.70
}

fruta = input("Introduce una fruta: ")
kilos = float(input("Introduce los kilos: "))

if fruta in frutas:
    precio = frutas[fruta] * kilos
    print("El precio es:", precio, "euros")
else:
    print("Esa fruta no está en la tabla")
