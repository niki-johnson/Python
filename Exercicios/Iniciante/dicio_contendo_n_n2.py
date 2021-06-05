"""Cria um dicionário que armazena como chave
numeros de 1 até o que o usuário põe e como
valores dessas chaves temos o numero elevado 
ao quadrado
Ex:{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

"""

def n_elev_2 (num):
    """Recebe um inteiro num e eleva esse ao quadrado
    enquanto salva os resultados nas respectivas chaves
    """
    dicio ={}
    for i in range(1,num+1):
        dicio[i] = i * i

    return dicio

numero = int(input("Informe um número: "))

while type(numero) != int:
    print("Entrada não é um número inteiro. Digite novamente")
    numero = int(input("Informe um número"))

num_w_quad = n_elev_2(numero)    
print(num_w_quad)