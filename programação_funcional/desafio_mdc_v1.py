"""
    
"""


def mdc(lista):
    possiveis_div = [x for x in range(1, min(lista) + 1)]
    while len(possiveis_div) > 0:
        for num in lista:
            if not num % possiveis_div[-1] == 0:
                flag = False
                possiveis_div.pop()
                break
            flag = True

        if flag:
            return possiveis_div[-1]


if __name__ == '__main__':
    print(mdc([21, 7]))  # 7
    print(mdc([125, 40]))  # 5
    print(mdc([9, 564, 66, 3]))  # 3
    print(mdc([55, 22]))  # 11
    print(mdc([15, 150]))  # 15
    print(mdc([7, 9]))  # 1
