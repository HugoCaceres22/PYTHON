palabra = input("Introduce una palabra: ")


# Convertir a lista
lista_palabra = list(palabra)

a = 0
e = 0
i = 0
o = 0
u = 0


for j in range(len(lista_palabra) -1, -1, -1):
    if "a" == lista_palabra[j]:
        a += 1
        
    elif "e" == lista_palabra[j]:
        e += 1

    elif "i" == lista_palabra[j]:
        i += 1
        
    elif "o" == lista_palabra[j]:
        o += 1
        
    elif "u" == lista_palabra[j]:
        u += 1



print (f"En tu palabra hay {a} A, {e} E , {i} I , {o} O , {u} U")