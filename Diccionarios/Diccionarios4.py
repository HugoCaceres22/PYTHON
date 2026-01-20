fecha = input("Introduce una fecha (dd/mm/aaaa): ")

partes = fecha.split("/")

dia = partes[0]
mes = partes[1]
anio = partes[2]

meses = {
    "01": "enero",
    "02": "febrero",
    "03": "marzo",
    "04": "abril",
    "05": "mayo",
    "06": "junio",
    "07": "julio",
    "08": "agosto",
    "09": "septiembre",
    "10": "octubre",
    "11": "noviembre",
    "12": "diciembre"
}

print(dia, "de", meses[mes], "de", anio)
