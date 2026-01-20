texto = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

#separar por líneas
lineas = texto.split("\n")

#obtener  campos
campos = lineas[0].split(";")

clientes = {}

# recorrer líneas clientes
for i in range(1, len(lineas)):
    datos = lineas[i].split(";")

    nif = datos[0]

    clientes[nif] = {}

    #guardar
    clientes[nif]["nombre"] = datos[1]
    clientes[nif]["email"] = datos[2]
    clientes[nif]["teléfono"] = datos[3]
    clientes[nif]["descuento"] = float(datos[4])

print(clientes)
