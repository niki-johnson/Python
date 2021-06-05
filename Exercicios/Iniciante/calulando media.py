"""Calcula valor médio dos numeros
"""

num = 0
lista_num = []
soma = 0

print ("Informe os números para calcularmos a média")
print ("Digite '-1' para não por mais números")
    

# recebendo os numeros ate for -1
while num != -1:
    
    num = int(input(""))
    #add os numeros numa lista
    lista_num.append(num)    

#calculando a soma dos numeros dados
for i in range(0,len(lista_num)-1):
    soma += lista_num[i]

#calculando a media 
media = soma/(len(lista_num) - 1)    
print (media)