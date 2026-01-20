def factorial(numero):
    resultado = 1

    for i in range(numero, 0, -1):
        resultado = resultado * i

    return resultado

print(factorial(2))
