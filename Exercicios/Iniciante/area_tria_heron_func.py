"""Calculando area trinagulo por heron
formula
"""

#inserindo as coordenadas
x = [int(input("coordenada x0 ")),int(input("coordenada y0 "))]
y = [int(input("coordenada x1 ")),int(input("coordenada y1 "))]
z = [int(input("coordenada x2 ")),int(input("coordenada y2 "))]

def dist_pontos_cart(x,y):
    #calculando a distância de dois pontos
    dist = ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5
    return dist

def area_heron(a,b,c):
    #calculando s
    s = (a + b + c) / 2
    #area pela formula de heron
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    return area
    
#calculando a distância lado a
a = dist_pontos_cart(x,y)

#calculando lado b
b = dist_pontos_cart(x,z)
#calculando lado c
c = dist_pontos_cart(z,y)

area = area_heron(a,b,c)

print ("a area do triangulo é: ",area)
