numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3,
           42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]


def removendo_duplicadas(lista: list[int]):
    lista_limpa = []
    for numero in lista:
        print(lista_limpa)
        if numero not in lista_limpa:
            lista_limpa.append(numero)
        else:
            print(f"O número {numero} foi duplicado")
    return lista_limpa


removendo_duplicadas(numeros)
