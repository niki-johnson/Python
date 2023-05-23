from mysql.connector import connect

conexao = connect(
    user='root',
    passwd='12345678',
    port=3306,
    host='localhost'
)

print(conexao)
