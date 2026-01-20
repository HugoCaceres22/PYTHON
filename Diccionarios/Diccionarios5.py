asignaturas = {
    "Matemáticas": 6,
    "Física": 4,
    "Química": 5
}

total = 0

for asignatura in asignaturas:
    print(asignatura, "tiene", asignaturas[asignatura], "créditos")
    total += asignaturas[asignatura]

print("Total de créditos:", total)
