def area_circulo(radio):
    return 3.14 * radio * radio


def volumen_cilindro(radio, altura):
    area = area_circulo(radio)
    return area * altura


radio = float(input("Introduce el radio: "))
altura = float(input("Introduce la altura: "))

print(f"Área del círculo: {area_circulo(radio)}")
print(f"Volumen del cilindro: {volumen_cilindro(radio, altura)}")
