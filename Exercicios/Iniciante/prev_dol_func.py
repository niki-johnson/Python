"""Decrescimo do valor do dolar
"""
#recebendo os doláres e anos
dol = float(input("Valor de doláres: "))
anos = int(input("Daqui quantos anos: "))
taxa = float(input("Taxa anual "))
peranos = int(input("Periodo por ano (dias) "))
def prevdolar(dol,taxa, perano,anos):
    #calculando o valor futuro
    taxaper = taxa / perano
    periodo = perano * anos
    dolf = dol * (1 + 0.01 * taxaper) ** periodo
    return dolf

print("valor futuro de ",dol," dolares será: ",prevdolar(dol,taxa,peranos,anos))