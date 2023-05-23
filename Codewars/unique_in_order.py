"""
Exemplos:
    unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
    unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
    unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
    unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
"""
import string


def unique_in_order(objeto):

    objeto_copy = []
    for i in range(len(objeto)):
        if i == 0:
            objeto_copy.append(objeto[i])
        else:
            if (objeto[i] != objeto[min(i+1, len(objeto) - 1)] or objeto[i] != objeto[i-1]) and objeto[i] != objeto_copy[-1]:
                objeto_copy.append(objeto[i])
    return objeto_copy


def unique_in_order2(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res


def unique_in_order3(l): return [
    z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]


print(unique_in_order3('AAAABBBCCDAABBB'))
