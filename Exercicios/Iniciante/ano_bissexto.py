'''informa se um ano é bissexto
'''
def ano_bissexto(ano):
    return ano % 4 == 0

year = int(input("Informe um ano: "))

if ano_bissexto(year):
    print(year , " é um ano bissexto")
else:
    print(year , " não é um ano bissexto")