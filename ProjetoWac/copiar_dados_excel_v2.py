import extrair_dados_senai_v2 as readpdf
import extrair_dados_ceniq_v1 as readpdf2
import extrair_dados_hidro_v1 as readpdf3
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


if __name__ == '__main__':
    with nova_conexao() as conexao:
        if conexao.is_connected():
            print('Está conectada')

    args_p, args_l = readpdf3.buscar_dados('analise_maio_CPLF_2022.jpg')

    sql1 = """SELECT idEstacao, Nome FROM wac_analise.estacoestratamentos;"""
    parametros_ok = int(input('Paramêtros ok?\n1 - S\n0 - N\n'))
    if parametros_ok:
        with nova_conexao() as conexao:

            cursor = conexao.cursor()
            cursor.execute(sql1)
            chave_und = collections.defaultdict()
            # x é uma tupla
            for x in cursor:
                chave_und[x[1]] = x[0]

            for x, y in chave_und.items():
                print(f'{x}: {y}')
            unidade = int(input('Informe a unidade de acordo com o menu: '))
            args_l.append(unidade)
            # print(chave_und)

            '''for x in chave_und.items():
                if args_l[3].lower() in x[0].lower():
                    args_l[3] = x[1]
                    break'''
        # 1
        inserir_novo_laudo(args_l)
        inserir_parametros(args_p)
