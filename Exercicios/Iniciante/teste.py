def getFactors(x):
    """Recebe um número e calcula seus fatores:
        que são numeros que ao dividirem X, sobra 0
    Por exemplo:
    o numero 8 tem: 1,2,4 e o proprio como fatores
    Retorna a lista dos fatores
    """
    fatores = []
    for i in range(1,x+1):
        #testa se a divisão é zero
        if x % i == 0:
            fatores.append(i)
    
    return fatores

def isPrime(x):
    """Returns whether or not the given number x is prime.

    A prime number is a natural number greater than 1 that
    cannot be formed by multiplying two smaller natural numbers.

    For example:

    - Calling isPrime(11) will return True
    """
    for i in range(2,x):
        #testa se a divisão é zero
        if x % i == 0:
            return False
            break
        else:
            continue
    return True

def isComposite(x):
    """function that returns whether or not the given number x
    is composite.
    This function returns a boolean."""
    #se for primo, logo, n é composto
    seprimo = isPrime(x)
    
    if seprimo == True :
        return False
    else:
        return True
    

def isPerfect(x):
    """Retorna se o numero é perfeito ou não.
        Um numero perfeito tem a soma dos fatores igual a ele
        mesmo
        ex=o 6 tem como fatores 1,2,3 e ele mesmo
        A soma dos seus fatores(1,2,3) = 6, que é igual a ele msm
        """
    fatores = getFactors(x)
    fatores.pop()
    
    #somar os valores dos fatores
    som_fat = 0
    for num in fatores:
        som_fat += num
    
    #comparar se é igual ao numero
    if som_fat == x:
        return True
    else:
        return False

def isAbundant(x):
    """ function that returns whether or not the given number x
        is abundant.  This function returns a boolean.
        For example, 12 is abundant since 1 + 2 + 3 + 4 + 6 = 16 > 12
    """
    fatores = getFactors(x)
    fatores.pop()
    
    #somar os valores dos fatores
    som_fat = 0
    for num in fatores:
        som_fat += num
    
    #vendo se é maior ou n
    if som_fat>x:
        return True
    else:
        return False

def isTriangular(x):
    """ function that returns whether or not a given number x
        is triangular.
        The triangular number Tn is a number that can be represented
        in the form of a triangular grid of points.
    """
    i=1
    #iterar do 1 até o 50º num triangular
    while i<50:
        num_triang = (i * (i + 1)) / 2
        if num_triang == x:
            return True
            break
        else:
            i += 1
            continue
        
    return False
    
def isNarcissistic(x):
    """function that returns whether or not a given number is
    Narcissistic.  This function returns a boolean.
    
    narcissistic if it is equal to the sum of its own digits
    each raised to the power of the number of digits.
    
    For example,153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    """
    qtd_num = 1
    div = 1
    #contar qnts digitos o numero tem
    while div >= 1:
        div = x / 10 ** qtd_num
        qtd_num += 1
    
    qtd_num -= 1
    
    #criando vetor com os numeros
    cent = x // 100
    dez = (x % 100) // 10
    unid = ((x % 100) % 10)
    numeros = [cent,dez,unid]
    
    #calculando o somatorio dos digitos ^a qtd de numeros
    somato_dig = 0
    for i in numeros:
        somato_dig += i ** qtd_num 
        
    #analisar a condição de narcissistic
    if somato_dig == x:
        return True
    else:
        return False

exit()
a = isPrime(1)
b = isComposite(3)
c = isPerfect(29)
d = isAbundant(10)
e = isTriangular(14)
f = isNarcissistic (152)

print (a,b,c,d,e,f)