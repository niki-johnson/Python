from tika import parser
from datetime import datetime
import re


def dados_entrada(dados):
    for i in range(len(dados)):
        dados[i].append("Entrada")


def dados_saida(dados):
    for i in range(len(dados)):
        dados[i].append("Saida")


def tratar_dados_laudos(dados):

    dados[2] = dados[2][10:]
    dados[1] = dados[1][7:14]
    data = datetime.strptime(dados[2], '%d/%m/%y').date()
    dados[2] = data
    dados[0] = dados[0][0][1]

    return dados


def tratar_dados_parametros(dados, qtd_parametros):
    for i in range(len(dados[0])):
        dados[0][i] = list(dados[0][i])
        dados[0][i].append(dados[1][0][1])
        dados[0][i][1] = dados[0][i][1].replace(
            ",", ".") if "," in dados[0][i][1] else dados[0][i][1]
        dados[0][i][1] = dados[0][i][1].replace(
            "<", "") if "<" in dados[0][i][1] else dados[0][i][1]
        if not "Coliformes" in dados[0][i][0]:
            dados[0][i][1] = float(dados[0][i][1])
        else:
            valor_exp = dados[0][i][1].split('X')
            dados[0][i][1] = float(valor_exp[0]) * \
                10 ** float(valor_exp[1][-1])

    if dados[0][0][1] > dados[0][qtd_parametros][1] or dados[0][1][1] > dados[0][qtd_parametros+1][1]:
        dados_entrada(dados[0][:qtd_parametros])
        dados_saida(dados[0][qtd_parametros:])
    else:
        dados_saida(dados[0][:qtd_parametros])
        dados_entrada(dados[0][qtd_parametros:])

    return dados[0]


def buscar_dados(pdf):
    dados_parametros = []
    dados_laudos = []
    raw = parser.from_file(pdf)
    # print(raw['content'])
    padrao_amostra = re.findall(
        r'(Amostra 1-|Amostra 2-|Amostra\s*)([A-Z0-9]+)', raw['content'])
    data_coleta = re.search(
        r'Recepção:\s+(\d{1,2}/\d{1,2}/\d{2,4})', raw['content'])
    codigo_relatorio = re.search(r'Código\s+(\d+/\d+-\d+)', raw['content'])
    padrao_parametro = r'(DBO|DQO|Óleos e graxas|pH|pH\s+\(Medição em campo\)|Oxigênio dissolvido|Sólidos sedimentáveis|Sólidos suspensos|Sólidos Não Filtráveis Totais|Cloro Residual Livre|Coliformes totais)\s+([\d\.]+|[\d\,]+|[<\d]+|[\d,\d X \d]+|[<\d?,\d+>]+)\s+(mg/L|mL/L|min|--|UFC/100mL)'
    resultados = re.findall(padrao_parametro, raw['content'])
    '''unidade = re.search(
        r'(Presídio )(Lauro De Freitas|Vitoria da Conquista|Itabuna|Lauro)', raw['content'])
    '''
    for i in range(len(resultados)):
        if 'pH' in resultados[i][0] and 'campo' in resultados[i][0]:
            resultados[i] = list(resultados[i])
            resultados[i][0] = 'pH'
            resultados[i] = tuple(resultados[i])

    dados_parametros.append(resultados)
    dados_parametros.append(padrao_amostra)
    dados_laudos.append(padrao_amostra)
    dados_laudos.append(codigo_relatorio[0])
    dados_laudos.append(data_coleta[0])
    # dados_laudos.append(unidade[0])
    # print(dados_parametros)
    dados_parametros = tratar_dados_parametros(
        dados_parametros, int(len(dados_parametros[0])/2))
    dados_laudos = tratar_dados_laudos(dados_laudos)
    dados_laudos[0] = dados_laudos[0]+dados_laudos[1]
    for i in range(len(dados_parametros)):
        dados_parametros[i][3] = dados_laudos[0]
    print(dados_parametros)
    return dados_parametros, dados_laudos
