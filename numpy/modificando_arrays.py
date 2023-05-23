import numpy as np

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])

# pondo em ordem crescente
print(np.sort(arr))  # np.sort(arr) retorna uma cópia
print(arr)
arr.sort()
print(arr)

# concatenando arrays
a = np.array([1, 2, 3, 4])
b = np.array([5, 11, 7, 8])

a_b = np.concatenate((a, b))
print(a_b)
