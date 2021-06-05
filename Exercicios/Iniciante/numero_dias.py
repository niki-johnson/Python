'''Programa transforma um número de segundos em número de dias'''

def num_dias(seg):
    '''Função calcula o numero de dias dado o valor de segundos
    seg = é um valor inteiro que representa os segundos'''

    dias = seg / (60 * 60 * 24)

    return dias

segundos = 0
i = 0

while i == 0:
    
    print("Para sair do programa, tecle um número negativo. Ex: '-3'")

    try:

        segundos = int(input("Informe o número de segundos: "))

    except ValueError:

        print("Número deve ser inteiro")
        
        continue
    
    if segundos < 0:

        break

    else:

        qtd_dias = num_dias(segundos)

        print(f'{segundos} segundos corresponde a {qtd_dias} dias')