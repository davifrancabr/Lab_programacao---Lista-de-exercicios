lista = ["Davi", "Afonso", "Bartholomew"]

vazia = []


def lista_vazia(lista: list[str]):
    if len(lista) < 1:
        return print(True)
    return print(False)


lista_vazia(lista)
