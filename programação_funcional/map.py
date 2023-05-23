lista_1 = [1, 2, 3]
dobro = map(lambda x: x * 2, lista_1)

print(list(dobro))


lista_2 = [
    {'nome': 'João', 'idade': 23},
    {'nome': 'Maria', 'idade': 31},
    {'nome': 'José', 'idade': 41}
]
so_nomes = map(lambda p: p['nome'], lista_2)
print(list(so_nomes))

# desafio: usar a função map para retornar frases <Nome> tem <idade> anos


def formar_frase(dicio):
    return f'{dicio["nome"]} tem {dicio["idade"]} anos.'


frases = map(formar_frase, lista_2)

print(list(frases))

# por lambda
frases_2 = map(lambda d: f'{d["nome"]} tem {d["idade"]} anos.', lista_2)
print(list(frases_2))
