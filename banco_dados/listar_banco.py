from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    passwd='12345678',
    user='root'

)

cursor = conexao.cursor()
cursor.execute('SHOW DATABASES')  # armazena o proprio resultado

for i, database in enumerate(cursor, start=1):
    print(f'Banco de dados {i}: {database[0]}')
