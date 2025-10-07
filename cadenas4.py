#Los teléfonos de una empresa tienen el siguiente formato
#prefijo-número-extension donde el prefijo es el código del país +34, y la
#extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un
#programa que pregunte por un número de teléfono con este formato y muestre por
#pantalla el número de teléfono sin el prefijo y la extensión.


telefono = input("Introduce el número de teléfono (formato +34-XXXXXXXXX-XX): ")

numero = telefono.split("-")[1] 

# lo que está dentro del split es el separador de "zonas" y el uno la posicion del valor que le vamos
#a asignar a la variable, empieza en 0, por lo que esa es la segunda posicion.

print(f"Número sin prefijo ni extensión: {numero}")






