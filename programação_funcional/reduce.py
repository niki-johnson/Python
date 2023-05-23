from functools import reduce

pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Artur', 'idade': 26},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 6},
    {'nome': 'Rebeca', 'idade': 17}
]

soma_idades = reduce(lambda idades, p: idades + p['idade'], pessoas, 0)

print(soma_idades)
