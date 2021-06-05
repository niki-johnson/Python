'''Programa produz uma tabela com os valores farenheits 
e os correspondentes em celsius'''

def farenheit_to_celsius (temp):
    '''Recebe a variável temp em farenheit e transforma
    em celsius
    Retorna os graus celsius'''

    celsius = 5 / 9 * (temp - 32)

    return celsius

def criar_tabela(dados):
    '''Recebe os dados para montar a tabela
    O parâmetro recebido é um dicionário
    Não retorna nada. Printa a tabela'''

    print("Farenheitº\tCelsiusº\n")
    for key in dados:
        print("%d\t\t%f" % (key, dados[key]))


tabela = {}
j = 0

for i in range(-40, 130, 10):

    tabela[i] = farenheit_to_celsius(i)


criar_tabela(tabela)
