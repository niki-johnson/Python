"""
    Gera um html bem simples utilizando packing
"""

# tuplas com os atributos suportados por cada tag
bloco_atrs = ('bloco_accesskey', 'bloco_id',)
ul_atrs = ('ul_id', 'ul_style',)


def filtro_atrs(informados, suportados):
    """
    remover o prefixo bloco e ul das kwargs e add apenas os suprotados por cada tag
    """
    return ' '.join(f'{k.split("_")[-1]}="{v}"'
                    for k, v in informados.items() if k in suportados)


def tag_bloco(conteudo, *args, classe='success', inline=False, **kwargs):

    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args, **kwargs)
    atributos = filtro_atrs(kwargs, bloco_atrs)
    return f'<{tag} {atributos} class = "{classe}">{html}</{tag}>'


def tag_lista(*itens, **novos_atrs):

    lista = ''.join(f'<li><{item}></li>' for item in itens)
    return f'<ul {filtro_atrs(novos_atrs, ul_atrs)}>{lista}</ul>'


if __name__ == '__main__':

    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', classe='info', inline=True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
    print(tag_bloco(tag_lista, 'Sábado', 'Domingo', classe='info', inline=True))
    print(tag_bloco(tag_lista, 'Item 1', 'Item 2', classe='info',
                    bloco_accesskey='m', bloco_id='conteudo', ul_id='lista'))
