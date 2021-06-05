""" Revertando um nome """

#recebendo um nome
nome = input ("Informe uma palavra: ")
rev = ""

#testanto se sera um nome ou número
try:
    nome  = int(nome)

#se for nome faça isso:
except:
    #imprimir a lista de traz pa frente
    for i in range(len(nome)-1,-1,-1):
        rev += nome[i]
    print (rev)
#se for numero
else:
    print("é um numero")
    