import numpy as np

a = np.array([3, 2, 1])
print(a)

zeros = np.zeros(3)
print(zeros)

# criando array com 2 elementos 'vazios'
vazios = np.empty(2)
print(vazios)

# array sequencial - arange literalmente funciona como range para for
sequencia = np.arange(4)
print(sequencia)

sequencia2 = np.arange(1, 10, 2)
print(sequencia2)

# definindo qual datatype eu quero
zero = np.zeros(3, dtype=np.int64)

# comparando o arrray de zero float com int
print(zeros)
print(zero)
