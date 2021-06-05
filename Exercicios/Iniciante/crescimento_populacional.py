'''Programa calcula quando a cidade A ultrapassará a cidade B em tamanho populacional
Para isso, a cidade A tem que ter uma população maior que 100 menor que 1 M e menor
que a pop da cidade B. Entao, a cidade B está sujeita ao mesmo intervalo a partir 
do tamanho da população de B. Além do mais, a taxa de crescimento populacional de A
tem q ser maior que a de B, e obedecer o intervalo de 0,1 até 10, ja a taxa de B
deve ser menor que A e maior que 0.0'''


class VerificacaoDados:
    
    def validade_pop_e_taxa(self,a,b, flag):
    
        if flag == 'tax':
            guardar = a
            a = b
            b = guardar
        
        i = 0
        while i == 0:
            if a > b:
                print("Dados incoerentes. Impossível fazer o teste")
                return False
            else:
                return True
            
    def validade_intervalo(self,a,b, flag):
        
        if flag == 'pop':

            if a <100 or a >= 1000000:

                print("Dados fora do intervalo")
                return False

            elif b > 1000000:

                print("Dados fora do intervalo")
                return False

            else:
                return True
        
        else:
            if a < 0.1 or a > 10.0:
                
                print("Dados fora do intervalo")
                return False
                
            elif b < 0.0:
                
                print("Dados fora do intervalo")
                return False
                
            else:
                return True

def calculo_anos(popa, popb, txa, txb):
    i = 0
    
    while popa <= popb:
        popa = popa + popa * txa
        popa = popa // 1
        
        popb = popb + popb * txb
        popb = popb // 1
        
        i = i + 1

    if i > 100:

        print ("Levará mais de 1 século")

    else:

        print (f'Levará {i} ano(s)')
    

num_teste = int(input("Informe o número de casos de teste: "))

for i in range(num_teste):
    
    dados = VerificacaoDados()
    
    pop_a = int(input("Informe o tamanho da população da cidade A: "))
    pop_b = int(input("Agora da população de B. Dica:População de B tem que ser maior que a da de a. "))
    
    valido = dados.validade_pop_e_taxa(pop_a,pop_b,'pop')
    valido_int = dados.validade_intervalo(pop_a, pop_b, 'pop')
    
    while not valido or not valido_int:
        
        pop_a = int(input("Informe o tamanho da população da cidade A: "))
        pop_b = int(input("Agora da população de B. Dica:População de B tem que ser maior que a da de a. "))
        valido = dados.validade_pop_e_taxa(pop_a,pop_b,'pop')
        valido_int = dados.validade_intervalo(pop_a, pop_b, 'pop')
    
    cres_a = float(input("Informe a taxa de crescimento populacional da cidade A: "))
    cres_b = float(input("Informe a da cidade B. Dica: Não pode ser maior que a da cidade B. "))
    
    valido = dados.validade_pop_e_taxa(cres_a,cres_b,'tax')
    valido_int = dados.validade_intervalo(cres_a, cres_b, 'tax')
    
    while not valido or not valido_int:
        
        cres_a = int(input("Informe taxa de crescimento da população da cidade A: "))
        cres_b = int(input("Agora da população de B. Dica:Taxa de B tem que ser menor que a da de a. "))
        valido = dados.validade_pop_e_taxa(cres_a,cres_b,'tax')
        valido_int = dados.validade_intervalo(cres_a, cres_b, 'tax')
    
    calculo_anos(pop_a, pop_b, cres_a, cres_b)