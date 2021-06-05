""" calcula area trinagulo equilatero
"""
def area_eq (l):
    area = l ** 2 * 3 ** 0.5 / 4
    return area

l = int(input("Tamanho lado do triangulo: "))

print (area_eq(l))