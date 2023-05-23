pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Artur', 'idade': 26},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 6},
    {'nome': 'Rebeca', 'idade': 17}
]

menores = filter(lambda p: p['idade'] < 18, pessoas)
print(list(menores))

nome_g = filter(lambda p: len(p['nome']) > 6, pessoas)
print(list(nome_g))
