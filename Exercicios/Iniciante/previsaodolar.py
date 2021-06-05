"""Decrescimo do valor do dolar
"""
#recebendo os doláres e anos
dol = float(input("Valor de doláres: "))
anos = int(input("Daqui quantos anos: "))
taxa = 7

#calculando o valor futuro
dolf = dol * (1 + 0.01 * taxa) ** anos

print("valor futuro de ",dol," dolares será: ",dolf)