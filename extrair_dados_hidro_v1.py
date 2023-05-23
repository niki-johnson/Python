from tika import parser
from datetime import datetime
import re
import cv2
import pytesseract

def buscar_data_coleta(conteudo):
    data_coleta = re.search(
        r'EFLUENTE\s+(\d{1,2}/\d{1,2}/\d{2,4})', conteudo['content'])
    
    data_coleta = data_coleta.group().split(' ')[1]
    return data_coleta

def buscar_codigo_laudo(conteudo):
    codigo_relatorio = re.search(r'ANAL[IÍ]TICOS \d{2}-\d{2}-\d{3}', conteudo['content'])
    codigo_relatorio = codigo_relatorio.group().split(' ')[1]
    return codigo_relatorio

def buscar_oleos_graxas(conteudo):
    #padrao = r'(Óleos e graxas|Substâncias solúveis em hexano|Óleos e Graxas Totais)(\s| _ )+(\d+.\d+|<\s*0,\d+|\d+ \d+,\d+ \d+,\d+)'
    padrao = r'Óleos e Graxas Totais\s+_?\s+(\d+\.?\d*)'
    #+([\d\.]+|[\d\,]+|[<\d]+|[\d,\d X \d]+|[<\d?,\d+>]+)
    oleo_graxa = re.findall(padrao, conteudo)
    for i in range(len(oleo_graxa)):
        oleo_graxa[i] = list(oleo_graxa[i])
        oleo_graxa[i].append('mg/L')
        if 'hexano' in oleo_graxa[i][0]:
            oleo_graxa[i][0] = 'Óleos e graxas'
    print(oleo_graxa)
    return oleo_graxa

def buscar_dbo(conteudo):
    padrao = r'(DBO)\s+(\d+.\d+)'
    #+([\d\.]+|[\d\,]+|[<\d]+|[\d,\d X \d]+|[<\d?,\d+>]+)
    dbo = re.findall(padrao, conteudo)
    for i in range(len(dbo)):
        dbo[i] = list(dbo[i])
        dbo[i].append('mg/L')
    return dbo

def buscar_dqo(conteudo):
    padrao = r'(DQO)\s+(\d+.\d+)'
    #+([\d\.]+|[\d\,]+|[<\d]+|[\d,\d X \d]+|[<\d?,\d+>]+)
    dqo = re.findall(padrao, conteudo)
    for i in range(len(dqo)):
        dqo[i] = list(dqo[i])
        dqo[i].append('mg/L')
    return dqo

def buscar_pH(conteudo):
    padrao = r'(pH)\s+(\d+.\d+)'
    #+([\d\.]+|[\d\,]+|[<\d]+|[\d,\d X \d]+|[<\d?,\d+>]+)
    pH = re.findall(padrao, conteudo)
    for i in range(len(pH)):
        pH[i] = list(pH[i])
        pH[i].append('')
    return pH

def buscar_cloro(conteudo):
    padrao = r'(Cloro [Rr]esidual [Ll]ivre)\s*+(<\s*0,\d+|\d+.\d+|<\d+,\d+_|\d+,\d+ |\d+)'
    #+([\d\.]+|[\d\,]+|[<\d]+|[\d,\d X \d]+|[<\d?,\d+>]+)
    cloro = re.findall(padrao, conteudo)
    for i in range(len(cloro)):
        cloro[i] = list(cloro[i])
        cloro[i].append('mg/L')
    print(cloro)
    return cloro

def buscar_od(conteudo):
    padrao =  r'(Oxigênio dissolvido|OD)\s+(\d+.\d+)'
    #Oxigênio dissolvido|
    resultados = re.findall(padrao, conteudo)
    for i in range(len(resultados)):
        resultados[i] = list(resultados[i])
        resultados[i].append('mg/L')
    
        if 'OD' in resultados[i][0] or 'OD' == resultados[i][0]:
            resultados[i][0] = 'Oxigênio dissolvido'
    return resultados

def buscar_solidos_sed(conteudo):
    padrao = r'(Sólidos [sS]edimentáveis)\s+(\d{1}|\d+.\d+|<\s*0,\d+)'
    #+([\d\.]+|[\d\,]+|[<\d]+|[\d,\d X \d]+|[<\d?,\d+>]+)
    solidos = re.findall(padrao, conteudo)
    for i in range(len(solidos)):
        solidos[i] = list(solidos[i])
        solidos[i].append('mL/L')
    
    return solidos

def buscar_solidos_suspensos(conteudo):
    padrao = r'(Sólidos [sS]uspensos|Materiais Flutuantes)\s+(\d+.\d+|AUSENTE|AUSENTES|PRESENTE|PRESENTES)'
    #+([\d\.]+|[\d\,]+|[<\d]+|[\d,\d X \d]+|[<\d?,\d+>]+)
    solidos = re.findall(padrao, conteudo)
    for i in range(len(solidos)):
        solidos[i] = list(solidos[i])
        if 'AUS'in solidos[i][1]:
            solidos[i][1] = '0,0'
        else:
            solidos[i][1] = '0,1'

        solidos[i].append('mg/L')
    
    return solidos

def buscar_coliformes(conteudo):
    padrao = r'(Coliformes totais)\s*+(>\s*\d[\d,]*(?:\.\d{3})*|>+\s*\d+|\d+|\d+.\d+|<\s*0,\d+|>\s*\d+,\d+|>\s*\d+)'
    coliformes = re.findall(padrao, conteudo)
    for i in range(len(coliformes)):
        coliformes[i] = list(coliformes[i])
        coliformes[i].append('NMP/mL')
    
    return coliformes

def dados_entrada(dados):
    for i in range(len(dados)):
        dados[i].append("Entrada")


def dados_saida(dados):
    for i in range(len(dados)):
        dados[i].append("Saida")


def adicionar_ponto_coleta(dados):
    for i in range(len(dados)):
            dados[i] = list(dados[i])
            dados[i][0].append('Entrada')
            dados[i][1].append('Saida')


def tratar_dados_laudos(dados):

    data = datetime.strptime(dados[2], '%d/%m/%Y').date()
    dados[2] = data

    return dados


def tratar_dados_parametros(dados):
    print(dados)
    for i in range(len(dados)):
        for j in range(len(dados[i])):
            dados[i] = list(dados[i])
            dados[i][j][1] = dados[i][j][1].replace(
                ",", ".") if "," in dados[i][j][1] else dados[i][j][1]
            dados[i][j][1] = dados[i][j][1].replace(
                "<", "") if "<" in dados[i][j][1] else dados[i][j][1]
            dados[i][j][1] = dados[i][j][1].replace(
                ">", "") if ">" in dados[i][j][1] else dados[i][j][1]
            dados[i][j][1] = float(dados[i][j][1])
            '''if not "Coliformes" in dados[i][j][0]:
                dados[i][j][1] = float(dados[i][j][1])
            else:
                valor_exp = dados[i][j][1].split('X')
                dados[i][j][1] = float(valor_exp[0]) * \
                    10 ** float(valor_exp[1][-1])
            '''
    adicionar_ponto_coleta(dados)
    #print(dados)

    return dados

def buscar_dados(pdf):
    dados_parametros = []
    dados_laudos = []
    imagem = cv2.imread(pdf)
    caminho = r"C:\Program Files\Tesseract-OCR"
    pytesseract.pytesseract.tesseract_cmd = caminho+r"\tesseract.exe"
    raw = pytesseract.image_to_string(imagem)
    #print(raw)
    #dados_laudos.append(buscar_codigo_laudo(raw))
    #dados_laudos.append(buscar_codigo_laudo(raw))
    #dados_laudos.append(buscar_data_coleta(raw))
    dados_parametros.append(buscar_oleos_graxas(raw))
    dados_parametros.append(buscar_dbo(raw))
    dados_parametros.append(buscar_dqo(raw))
    dados_parametros.append(buscar_cloro(raw))
    dados_parametros.append(buscar_pH(raw))
    dados_parametros.append(buscar_od(raw))
    dados_parametros.append(buscar_solidos_sed(raw))
    dados_parametros.append(buscar_solidos_suspensos(raw))
    dados_parametros.append(buscar_coliformes(raw))
    '''unidade = re.search(
        r'(Presídio )(Lauro De Freitas|Vitoria da Conquista|Itabuna|Lauro)', raw)
    '''
    #print(dados_parametros[0])
    #print(len(dados_parametros))
    '''dados_parametros.append(resultados)
    dados_laudos.append(codigo_relatorio[0])
    dados_laudos.append(data_coleta[0])
    # dados_laudos.append(unidade[0])
    # print(dados_parametros)'''
    dados_parametros = tratar_dados_parametros(
        dados_parametros)
    dados_laudos = tratar_dados_laudos(dados_laudos)
    for i in range(len(dados_parametros)):
        for j in range(2):
            dados_parametros[i][j].append(dados_laudos[0])
    #print('a')
    dados_parametros_f = []
    for x in dados_parametros:
        for y in x:
            dados_parametros_f.append(y)
    print(dados_parametros_f)
    print(dados_laudos)
    #print(len(dados_parametros))
    return dados_parametros_f, dados_laudos
