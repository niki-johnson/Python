"""
    Desafio: pegar todos os meses do ano que tem 31 dias
    Usando conceito de imutabilidade - nada foi modificado
"""
from calendar import mdays, month_name
from functools import reduce

meses_31d = filter(lambda i: mdays[i] == 31, range(1, 13))
nome_meses_31d = map(lambda i: month_name[i], meses_31d)
juntar_meses = reduce(lambda todos, mes: f'{todos}\n-{mes}',
                      nome_meses_31d, 'Meses com 31 dias:')

print(juntar_meses)
