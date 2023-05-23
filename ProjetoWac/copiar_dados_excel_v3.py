import extrair_dados_senai_v2 as readpdf
import extrair_dados_ceniq_v1 as readpdf2
import collections
from mysql.connector.errors import ProgrammingError
from bd import nova_conexao


def inserir_novo_laudo(args):

    sql = """
        INSERT INTO wac_analise.laudos (idLaudos, codigo,  dataColeta, idEstacao) 
        VALUES
        (%s, %s, %s, %s)
    """
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, args)
            conexao.commit()
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
        else:
            print(f'Foram incluídos {cursor.rowcount} registros')


def inserir_parametros(args):

    sql = """
        INSERT INTO wac_analise.parametros (Nome, Valor, Unidade, idLaudo, Ponto)
        VALUES
        (%s,%s,%s,%s,%s)
    """
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.executemany(sql, args)
            conexao.commit()
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
        else:
            print(f'Foram incluídos {cursor.rowcount} registros')


def buscar_unidades():

    with nova_conexao() as conexao:
        sql = """SELECT idEstacao, Nome FROM wac_analise.estacoestratamentos;"""
        cursor = conexao.cursor()
        cursor.execute(sql)
        chave_und = collections.defaultdict()
        # x é uma tupla
        for x in cursor:
            chave_und[x[1]] = x[0]

        for x, y in chave_und.items():
            print(f'{x}: {y}')
        unidade = int(input('Informe a unidade de acordo com o menu: '))
        return unidade


if __name__ == '__main__':

    with nova_conexao() as conexao:
        if conexao.is_connected():
            print('Está conectada')

    documento = r'\analises\analise_abr_CPI_2023.pdf'

    laboratorios = {'Senai': 1, 'Ceniq': 2, 'Hidroclean': 3}
    for lab, ind in laboratorios.items():
        print(f'{lab} - {ind}')
    laboratorio = int(
        input('Informe o laboratório de acordo com o menu acima: '))

    if laboratorio == 1:
        args_p, args_l = readpdf.buscar_dados(documento)
    elif laboratorio == 2:
        args_p, args_l = readpdf2.buscar_dados(documento)
    else:
        pass

    parametros_ok = int(input('Paramêtros ok?\nSim - 1\nNão - 0\n'))
    if parametros_ok:
        args_l.append(buscar_unidades())

    inserir_novo_laudo(args_l)
    inserir_parametros(args_p)
