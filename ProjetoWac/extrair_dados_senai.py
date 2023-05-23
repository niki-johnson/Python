from tika import parser
import re


def dados_entrada(dados):
    print('c')

    for i in range(len(dados)):
        dados[i].append("Entrada")


def dados_saida(dados):
    print('d')

    for i in range(len(dados)):
        dados[i].append("Saida")


def tratar_dados(dados, qtd_parametros):
    print('b')
    dados[3] = dados[3][10:]
    dados[1] = dados[1][7:14]
    for i in range(len(dados[0])):
        dados[0][i] = list(dados[0][i])
        dados[0][i].append(dados[1])
        dados[0][i].append(dados[2][0][1])
        dados[0][i].append(dados[3])
        dados[0][i][1] = dados[0][i][1].replace(
            ",", ".") if "," in dados[0][i][1] else dados[0][i][1]
        dados[0][i][1] = dados[0][i][1].replace(
            "<", "") if "<" in dados[0][i][1] else dados[0][i][1]
        if not "Coliformes" in dados[0][i][0]:
            dados[0][i][1] = float(dados[0][i][1])
        dados[0][i].append(dados[4])

    if dados[0][0][1] > dados[0][qtd_parametros][1] or dados[0][1][1] > dados[0][qtd_parametros+1][1]:

        dados_entrada(dados[0][:qtd_parametros])
        dados_saida(dados[0][qtd_parametros:])
    else:
        dados_saida(dados[0][:qtd_parametros])
        dados_entrada(dados[0][qtd_parametros:])

    return dados


def buscar_dados(pdf, qtd_parametros):
    print('a')
    dados = []
    raw = parser.from_file(pdf)
    padrao_amostra = re.findall(
        r'(Amostra 1-|Amostra 2-|Amostra\s*)([A-Z0-9]+)', raw['content'])
    data_coleta = re.search(
        r'Recepção:\s+(\d{1,2}/\d{1,2}/\d{2,4})', raw['content'])
    codigo_relatorio = re.search(r'Código\s+(\d+/\d+-\d+)', raw['content'])
    padrao_parametro = r'(DBO|DQO|Óleos e graxas|pH|Oxigênio dissolvido|Sólidos sedimentáveis|Sólidos suspensos|Sólidos Não Filtráveis Totais|Cloro Residual Livre|Coliformes totais)\s+([\d\.]+|[\d\,]+|[<\d]+|[\d,\d X \d]+|[<\d?,\d+>]+)\s+(mg/L|mL/L|min|--|UFC/100mL)'
    resultados = re.findall(padrao_parametro, raw['content'])
    print('a1')
    unidade = re.search(
        r'(Presídio )(Lauro De Freitas|Vitoria da Conquista|Itabuna)', raw['content'])
    print('a2')
    dados.append(resultados)
    dados.append(codigo_relatorio[0])
    dados.append(padrao_amostra)
    dados.append(data_coleta[0])
    dados.append(unidade[0])

    dados = tratar_dados(dados, qtd_parametros)

    return dados
