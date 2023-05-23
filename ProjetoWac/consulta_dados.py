from mysql.connector.errors import ProgrammingError
from bd import nova_conexao


def deletar_parametros():
    sql = """DELETE FROM wac_analise.parametros
            WHERE idLaudo = 'EV00957941876/23';"""
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)

        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
        else:
            print(f'Foram excluídos {cursor.rowcount} registros')


def busca_parametros():

    sql = """SELECT * FROM wac_analise.parametros
            WHERE idLaudo = 'EV00957941876/23';"""
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)

        except ProgrammingError as e:
            print(f'Erro: {e.msg}')

        else:
            for parametro in cursor.fetchall():  # retorna tupla
                print('\t'.join(str(campo) for campo in parametro))


def busca_laudos():

    sql = """SELECT * FROM wac_analise.laudos;"""
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)

        except ProgrammingError as e:
            print(f'Erro: {e.msg}')

        else:
            for laudo in cursor.fetchall():  # retorna tupla
                print('\t'.join(str(campo) for campo in laudo))


if __name__ == '__main__':
    busca_parametros()
    # busca_laudos()
    # deletar_parametros()
