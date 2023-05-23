"""
    Simulando switch com funções, dicionario e generator
"""


def get_tipo_dia(dia):
    """
        Recebe um int de 1 a 7, o dicionario vai conter duas tuplas, relacionadas com dias da semana e fim de semana
    """
    dias = {
        (1, 7,): 'Fim de semana', tuple(range(2, 7)): 'Dia de semana'
    }

    dia_escolhido = (tipo for numero, tipo in dias.items() if dia in numero)
    return next(dia_escolhido, '**dia inválido**')


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_tipo_dia(dia)}')
