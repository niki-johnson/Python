import extrair_dados_senai_v2 as readpdf
from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

with nova_conexao() as conexao:
    if conexao.is_connected():
        print('Está conectada')

dados = readpdf.buscar_dados('analise_fev_CPLF_2023.pdf', 9)
args = []

for dado in dados[0]:
    args.append(tuple(dado))

print(args)
