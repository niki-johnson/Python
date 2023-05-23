import csv

with open('pessoas.csv') as entrada:
    # csv.reader ja separa por linha e por atributos
    for pessoa in csv.reader(entrada):
        print('Nome: {}. Idade: {}'.format(*pessoa))
