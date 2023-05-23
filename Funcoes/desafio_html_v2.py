def ajuste_class(string):
    """
        Recorta o html de html_class
    """
    return str(string.split("_")[-1])


def tag(tag, *args, **kwargs):

    atributos = ''.join(f'{k}="{v}"' for k, v in kwargs.items())
    html = ''.join(f'{item}' for item in args)

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
