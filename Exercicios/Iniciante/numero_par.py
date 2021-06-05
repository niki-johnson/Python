"""Calcula se um número n é primo e também calcula 
o enésimo numero primo"""

def e_primo(number):
    '''Recebo um numero inteiro como input
        avalia se é primo ou não
        Retorna boolean'''

    for i in range (2, number):

        if number % i == 0:

            return False 

    return True

def enesimo_primo(numero):
    """Recebe um número e retorna o enesimo numero primo
    Ex: input: 3
    Output: 5 (terceiro numero primo)"""

    cont = 0        #contador de numeros primos
    i = 2           #numero que vai ser iterado

    while cont < numero:

        if e_primo(i):  #verificando se é primo

            cont += 1
        
        i += 1
    
    return i - 1

numero = int(input("Informe um número inteiro: "))

print(f'O numero informado é primo? {e_primo(numero)}', '\n')
print(f'O {numero}º primo é: {enesimo_primo(numero)}')

