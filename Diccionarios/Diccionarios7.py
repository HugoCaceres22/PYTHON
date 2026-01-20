compra = {}
total = 0

while True:
    articulo = input("Introduce un artículo (o 'fin' para terminar): ")

    if articulo == "fin":
        break

    precio = float(input("Introduce el precio: "))
    compra[articulo] = precio

print("\nLista de la compra")

for articulo in compra:
    print(articulo, ":", compra[articulo])
    total += compra[articulo]

print("Total:", total)
