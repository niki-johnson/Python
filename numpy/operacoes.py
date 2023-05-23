import numpy as np

data = np.array([1, 2])
ones = np.ones(2, dtype=int)
print(data+ones)
print(data-ones)
print(data/ones)

# note que aqui é uma multiplicação numero por numero, n multiplicação de matriz
print(data*data)

# caso queria q seja de matriz - temos 2 opções:
print(data.dot(ones))
print(data@ones)

# usando métodos
a = np.array([1, 2, 3, 4])
print(a.sum())

# somando cada coluna
b = np.array([[1, 1], [2, 2]])
print(b.sum(axis=0))

# somando cada linha
print(b.sum(axis=1))
