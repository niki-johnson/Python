"""
    Programa para estabelecer conexao
"""

from mysql.connector import connect
from contextlib import contextmanager

parametros = dict(
    host='localhost',
    port=3306,
    passwd='12345678',
    user='root',
    database='agenda'
)


@contextmanager
def nova_conexao():
    conexao = connect(**parametros)
    try:
        yield conexao
    finally:
        if (conexao and conexao.is_connected()):
            #print('Conexão encerrada')
            conexao.close()
