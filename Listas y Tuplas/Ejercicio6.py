lista = ["Matemáticas", "Física","Química","Historia","Lengua"]

# Se puede hacer sin la copia, pero ay que me lo ha dicho el profesor lo añado
repetir = lista.copy()

mate = int(input("Introduce tu nota en matemáticas: "))
fisi = int(input("Introduce tu nota en Física: "))
quimi = int(input("Introduce tu nota en Química: "))
hist = int(input("Introduce tu nota en Historia: "))
leng = int(input("Introduce tu nota en Lengua: "))

#de final al principio para no peder el orden
if leng >= 5:
    repetir.pop(4)
if hist >= 5:
    repetir.pop(3)
if quimi >= 5:
    repetir.pop(2)
if fisi >= 5:
    repetir.pop(1)
if mate >= 5:
    repetir.pop(0)

print("Debes repetir:", repetir)
