list = ["Matemáticas", "Física","Química","Historia","Lengua"]

i = 0
while i <= len(list) - 1:
    nota = input(f"¿Cual es tu nota en {list[i]}? ")
    print (f"Tu nota en {list[i]} es {nota}")
    i = i + 1
    
