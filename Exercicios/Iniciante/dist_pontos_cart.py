"""Calculando a distancia de dois pontos
no plano cartesiano
"""
#inserindo as coordenadas
x = [int(input("coordenada x0 ")),int(input("coordenada y0 "))]
y = [int(input("coordenada x1 ")),int(input("coordenada y1 "))]

#calculando a distância
dist = ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5

print ("a distancia entre os pontos é: ",dist)