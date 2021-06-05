"""Soma os dígitos presente num número
por meio de função recursiva"""


def soma_dig (x):

    num = str(x)
    
    if eval(num[0]) % 2 == 0:
        soma += num[0]
    
    
    try:
        num.pop(0)
    
    except:
    
        return soma 
    
    soma_dig(num)

print(soma_dig(234567))