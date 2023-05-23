# Demonstração das funções de string templates

from string import Template


def main():
    # TODO: Crie um template com placeholders
    templ = Template("Você está assistindo ${curso} com ${instrutora}")

    # TODO: Use o método substitute passando argumentos nomeados
    frase_2 = templ.substitute(
        curso='Python Avançado', instrutora='Jessica Temporal')
    print(frase_2)

    # TODO: Use o método substitute com um dicionario
    dados = {"curso": "Python Avançado", "instrutora": 'Jessica Temporal'}
    frase_3 = templ.substitute(dados)
    print(frase_3)


if __name__ == '__main__':
    main()
