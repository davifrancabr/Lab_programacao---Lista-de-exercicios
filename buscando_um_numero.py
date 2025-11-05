numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3,
           42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

entrada = int(input("Qual número você deseja procurar?"))


def buscar_numero(lista: list[int], entrada: int):
    for numero in lista:
        if entrada == numero:
            print("Número encontrado.")
            break
        else:
            print("Não encontrado")


buscar_numero(numeros, entrada)
