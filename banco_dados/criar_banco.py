from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='12345678'
)

cursor = conexao.cursor()  # executar comandos nele e receber resultados
cursor.execute('CREATE DATABASE IF NOT EXISTS WAC_Analise')
