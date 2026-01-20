clientes = {}

while True:
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")

    opcion = input("Elige una opción: ")

    #Añadir cliente
    if opcion == "1":
        nif = input("NIF: ")
        nombre = input("Nombre: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        pref = input("¿Es preferente? (s/n): ")

        preferente = False
        if pref == "s":
            preferente = True

        clientes[nif] = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
            "correo": correo,
            "preferente": preferente
        }

        print("Cliente añadido.")

    #Eliminar cliente
    elif opcion == "2":
        nif = input("NIF del cliente a eliminar: ")

        if nif in clientes:
            del clientes[nif]
            print("Cliente eliminado.")
        else:
            print("Ese NIF no existe.")

    #Mostrar cliente
    elif opcion == "3":
        nif = input("NIF del cliente a mostrar: ")

        if nif in clientes:
            print("NIF:", nif)
            print("Nombre:", clientes[nif]["nombre"])
            print("Dirección:", clientes[nif]["direccion"])
            print("Teléfono:", clientes[nif]["telefono"])
            print("Correo:", clientes[nif]["correo"])
            print("Preferente:", clientes[nif]["preferente"])
        else:
            print("Ese NIF no existe.")

    #Listar todos los clientes
    elif opcion == "4":
        for nif in clientes:
            print(nif, "-", clientes[nif]["nombre"])

    #Listar clientes preferentes
    elif opcion == "5":
        for nif in clientes:
            if clientes[nif]["preferente"] == True:
                print(nif, "-", clientes[nif]["nombre"])

    # Salir
    elif opcion == "6":
        break

    else:
        print("Opción no válida.")
