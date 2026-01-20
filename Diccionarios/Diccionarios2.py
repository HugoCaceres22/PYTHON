nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")
direccion = input("Introduce tu dirección: ")
telefono = input("Introduce tu teléfono: ")

persona = {
    "nombre": nombre,
    "edad": edad,
    "direccion": direccion,
    "telefono": telefono
}

print(persona["nombre"], "tiene", persona["edad"], "años, vive en",
      persona["direccion"], "y su número de teléfono es",
      persona["telefono"])
