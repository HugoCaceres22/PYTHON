#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
#año que dura la inversión.


dinero = int(input ("Introduce la cantidad a invertir : "))
interes = int(input ("Introduce el interés anual : "))
año = int(input ("Introduce el numero de años que va a durar la inversion : "))

i = 0


while i <= año  :
  capital = dinero * (1 + interes / 100) ** i
  print(f"El año {i} tendrás amasados {capital} euros")
  i = i + 1
  
  
  
  



     

     
