#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y
#el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y
#los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un
#programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo
#que le corresponde

nom = input("Introduce tu nombre: ")
sex = input("Introduce tu sexo (H o M): ")

if sex == "M" and nom < "M"  :
     print ("Perteneces a la clase A")

elif sex == "H" and nom > "N" :
    print ("Perteneces a la clase A")
    
else:
    print ("Perteneces a la clase B")






