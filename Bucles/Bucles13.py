#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta
#que el usuario escriba “salir” que terminará.
     
eco = input("Introduce  lo que quieres repetir: ")
   
    
while eco != "salir" :
    print (f"{eco}")
    eco = input("Introduce  lo que quieres repetir: ")
    
if eco == "salir" :
    print("Cancelando eco...")


        