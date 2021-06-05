"""Calcula fatorial de um número
Esse programa busca utilizar o conceito de funções 
recursivas - ou seja, uma função que chama a si mesma"""

def fatorial(n):
    
    if n == 0:

        return 1
    
    else:

        return n * fatorial(n-1)

print(fatorial(5))
