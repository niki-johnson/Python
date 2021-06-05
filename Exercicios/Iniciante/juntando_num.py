"""Programa recebe uma sequência de numeros e junta tudo em um número só
Edit 1 - ainda soma os dígitos pares do numero
Edit 2 - Inverte o número"""

def juntar_num(lista):
    """Recebe a lista de número e transforma em um unico numero"""

    numero_total = ''   #criando uma str vazia

    for num in lista:

        numero_total += num     #adicionando os numeros

    return numero_total

def soma_par(numero):
    """Recebe um número e soma os algarismos pares
    Retorna um inteiro"""

    soma = 0

    for n in numero:

        if eval(n) % 2 == 0:    #verifica se o numero é par
            
            soma += eval(n)     #se sim, soma o valor

    return soma

def inverte_num(numero):
    """Recebe um numero e inverte ele de trás para frente"""

    num = []        #criando uma lista para guardar os algarismos

    for n in numero:

        num.append(n)

    num_inv = ''    #criando uma str vazia

    #invertendo a lista    
    for i in range(len(num) - 1, -1, -1):

        num_inv += num[i]

    return num_inv


list_num = []
i = 0

print("Informe uma sequência de números inteiros positivos")
print("Para terminar a sequência, informe um número negativo. Ex:'-3'")

while i == 0:
    try:

        numeros = int(input("Informe o numero: "))

    except ValueError:

        print("Numero tem que ser inteiro")
        continue

    if numeros < 0:
        break

    list_num.append(str(numeros))


num_result = juntar_num(list_num)
print(f'O numero resultante é: {num_result}','\n')
print(f'Soma dos dígitos pares: {soma_par(num_result)}','\n')
print(f'O número invertido é: {inverte_num(num_result)}', '\n')