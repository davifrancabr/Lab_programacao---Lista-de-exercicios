natureza = ["rio", "floresta", "leão", "montanha", "oceano",
            "estrela", "vento", "cachoeira", "lua", "girassol"]

tecnologia = ["algoritmo", "API", "blockchain", "código",
              "software", "nuvem", "hardware", "interface", "pixel", "servidor"]


def concatenando_lista(lista_a: list[str], lista_b: list[str]):
    for item in lista_b:
        lista_a.append(item)
    print(lista_a)


concatenando_lista(natureza, tecnologia)
