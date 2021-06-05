"""Calculando area trinagulo por heron formula
"""

#inserindo as coordenadas
x = [int(input("coordenada x0 ")),int(input("coordenada y0 "))]
y = [int(input("coordenada x1 ")),int(input("coordenada y1 "))]
z = [int(input("coordenada x2 ")),int(input("coordenada y2 "))]

#calculando a distância lado a
a = ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5

#calculando lado b
b = ((x[0] - z[0]) ** 2 + (x[1] - z[1]) ** 2) ** 0.5

#calculando lado c
c = ((y[0] - z[0]) ** 2 + (y[1] - z[1]) ** 2) ** 0.5

#calculando s
s = (a + b + c) / 2

#area pela formula de heron
area = (s*(s-a)*(s-b)*(s-c))**0.5
print ("a area do triangulo é: ",area)
