#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
#dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa
#anterior para que también funcione cuando el día o el mes se introduzcan con un
#solo carácter.

fn = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")

d = fn.split("/")[0] 
m = fn.split("/")[1] 
a = fn.split("/")[2] 


print (f"Naciste el día {d} del mes número {m} del año {a}") 

