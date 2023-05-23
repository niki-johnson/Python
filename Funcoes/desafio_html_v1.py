def ajuste_class(string):
    """
        Recorta o html de html_class
    """
    return str(string.split("_")[-1])


def style_atrs(conteudo):
    return ''.join(f'{k}="{v}"' for k, v in conteudo.items())


def style_html(conteudo):
    return ''.join(f'{item}' for item in conteudo)


def tag(tag, *args, **kwargs):

    atributos = style_atrs(kwargs)
    html = style_html(args)

    if 'html' in atributos:
        atributos = ajuste_class(atributos)

    return f'<{tag} {atributos}>{html}</{tag}>'


if __name__ == "__main__":
    print(
        tag('p',
            tag('span', 'Curso de Python 3, por '),
            tag('strong', 'Juracy Filho', id='jf'),
            tag('span', ' e '),
            tag('strong', 'Leonardo Leitão', id='ll'),
            tag('span', '.'),
            html_class='alert'
            )
    )
