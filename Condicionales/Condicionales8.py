#En una determinada empresa, sus empleados son evaluados al final de cada año.
#Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir
#aumentando, traduciéndose en mejores beneficios. Los puntos que pueden
#conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores
#intermedios entre las cifras mencionadas. A continuación se muestra una tabla con
#los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida
#en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
        #Nivel Puntuación
        #Inaceptable 0.0
        #Aceptable 0.4
        #Meritorio 0.6 o más
#Escribir un programa que lea la puntuación del usuario e indique su nivel de
#rendimiento, así como la cantidad de dinero que recibirá el usuario.

punt = 0.5
nivel = "Inaceptable, Aceptable, Meritorio"

if punt == 0.0:
    print(f"El nivel es {nivel.split(',')[0]}, recibirás 0 euros")

elif punt == 0.4:
    print(f"El nivel es {nivel.split(',')[1]}, recibirás {punt * 2400} euros")

elif punt == 0.6:
    print(f"El nivel es {nivel.split(',')[2]}, recibirás {punt * 2400} euros")
    
else:
    print("El numero introducido no es correcto")

