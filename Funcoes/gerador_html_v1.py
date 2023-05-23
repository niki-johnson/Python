"""
    Gera um html bem simples
"""


def tag_bloco(texto, classe='success'):
    return f'<div class = "{classe}">{texto}</div>'


if __name__ == '__main__':
    # testes (assertions)
    assert tag_bloco('Incluido com sucesso') == \
        '<div class = "success">Incluido com sucesso</div>'
    print(tag_bloco('bloco'))
