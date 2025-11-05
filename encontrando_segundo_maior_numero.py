numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3,
           42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]


def segundo_maior_numero(lista: list[int]):
    if len(lista) < 2:
        return None

    primeiro_maior = segundo_maior = float('-inf')

    for numero in lista:
        if numero > primeiro_maior:
            segundo_maior = primeiro_maior
            primeiro_maior = numero
        elif primeiro_maior > numero > segundo_maior:
            segundo_maior = numero
    return segundo_maior if segundo_maior != float('-inf') else None


resultado = segundo_maior_numero(numeros)
print("O segundo maior número é: ", resultado)
