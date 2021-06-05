"""Recebo uma sequencia de numeros e virgulas
e crio um tuple e lista
"""

sequencia = input('Informe uma sequencia de número e vírgulas\
    Ex- 34,67,55,33,12,98 ')

list_seq = sequencia.split(',')
tuple_seq = tuple(list_seq)

print(list_seq,tuple_seq)