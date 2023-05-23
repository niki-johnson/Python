import numpy as np

array = np.array([[[0, 1, 2, 3],
                   [4, 5, 6, 7]],
                  [[0, 1, 2, 3],
                   [4, 5, 6, 7]],
                  [[0, 1, 2, 3],
                   [4, 5, 6, 7]]])

print(array.ndim)
print(array.size)
print(array.shape)

"""
Using arr.reshape() will give a new shape to an array without changing the data
"""
# o array orignial n muda de forma - so podemos guardar a modificação e uma nova variavel
b = array.reshape(4, 3, 2)
print(b)
print('\n')
print(array)


# convertendo um array de 1D para 2D
a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)
print(a)
a2 = a[np.newaxis, :]
print(a2.shape)
print(a2)
