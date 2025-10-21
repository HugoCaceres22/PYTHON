#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
#Los ingredientes para cada tipo de pizza aparecen a continuación.
#● Ingredientes vegetarianos: Pimiento y tofu.
#● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y
#en función de su respuesta le muestre un menú con los ingredientes disponibles
#para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el
#tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la
#pizza elegida es vegetariana o no y todos los ingredientes que lleva.


pregunta = input("¿Quieres la pizza vegetariana? Responde si o no")
siveg = "Pimiento , Tofu"
noveg = "Peroni,Jamon,Salmon"


if pregunta == "si":
    print(f"{siveg}")
    pregunta2 = input("¿Que ingrediente quieres añadir?")
    
    if pregunta2 == "Pimiento" :
        print(f"La pizza que has elegido es vegetariana y lleva mozzarella, tomate y pimiento")
    else :
        print(f"La pizza que has elegido es vegetariana y lleva mozzarella, tomate y tofu")
        

else :
    print(f"{noveg}")
    pregunta2 = input("¿Que ingrediente quieres añadir?")
    
    if pregunta2 == "Peperoni" :
        print(f"La pizza que has elegido es no vegetariana y lleva mozzarella, tomate y Peperoni")
    elif pregunta2 == "Salmon" :
        print(f"La pizza que has elegido es no vegetariana y lleva mozzarella, tomate y Salmon")
    else :
        print(f"La pizza que has elegido es no vegetariana y lleva mozzarella, tomate y Jamon")

        


