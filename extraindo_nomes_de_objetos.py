lista = [
    {"nome": "Davi", "idade": 23},
    {"nome": "João", "idade": 18},
    {"nome": "Arthur", "idade": 77},
    {"nome": "Amanda", "idade": 41},
    {"nome": "Lucas", "idade": 27},
    {"nome": "Victor", "idade": 32}
]


def extracao_nomes(lista: list):
    for nome in lista:
        print(nome["nome"])


extracao_nomes(lista)
