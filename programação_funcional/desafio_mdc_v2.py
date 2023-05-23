"""
    Calculando maximo divisor comum
    Paradigma funcional
"""
from functools import reduce


def mdc(lista):
    def calc_div(num):
        return num if sum(map(lambda x: x % num, lista)) == 0\
            else calc_div(num - 1)
    return calc_div(min(lista))


if __name__ == '__main__':
    print(mdc([21, 7]))  # 7
    print(mdc([125, 40]))  # 5
    print(mdc([9, 564, 66, 3]))  # 3
    print(mdc([55, 22]))  # 11
    print(mdc([15, 150]))  # 15
    print(mdc([7, 9]))  # 1
