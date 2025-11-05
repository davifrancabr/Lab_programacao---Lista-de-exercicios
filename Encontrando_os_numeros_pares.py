numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3,
           42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]


def numeros_pares(lista: list[int]):
    numero_pares = []
    for numero in lista:
        if numero % 2 == 0:
            numero_pares.append(numero)
    print(numero_pares)
    return numero_pares


numeros_pares(numeros)
