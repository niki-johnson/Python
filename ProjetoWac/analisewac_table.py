import tabula

tabela = tabula.read_pdf('analise_fev.pdf', pages="all", encoding='latin-1')
dados_entrada = tabela[1]
dados_saida = tabela[5]
print(tabela)
print(type(dados_entrada))
print(type(dados_saida))
