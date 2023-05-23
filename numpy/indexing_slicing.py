import numpy as np

# slicing é semelhante a lsitas em python
data = np.array([[1, 2], [3, 4], [5, 6]])
print(data[0, 1])  # retorna 2
print(data[1:3])  # retorna array([[3, 4],[5, 6]])
print(data[0:2, 0])  # retorna array([1, 3])

# mas numpy tem algumas funcionalidades a mais, veremos

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# valores abaixo de 5
print(a[a < 5])

# passando a logica para uma variavel
five_up = (a >= 5)
print(a[five_up])

# qq logica pode ser passada
maior_menor = (a > 2) & (a < 11)
print(a[maior_menor])

five_up = (a > 5) | (a == 5)
print(five_up)

"""In this example, a tuple of arrays was returned: one for each dimension. 
The first array represents the row indices where these values are found, 
and the second array represents the column indices where the values are found.
"""
b = np.nonzero(a < 5)  # retorna os indices (linha, coluna)
print(b)
