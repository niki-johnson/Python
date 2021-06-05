def is_lunchtime (hora,is_am):
    '''Ve se ja pé hora do almoço,
    recebe uma hora qq e se é am ainda
    '''
    return hora == 11 and is_am == True or hora == 12 and is_am == False

horario = int(input("Informe as horas (1 as 12): "))

if is_lunchtime(horario, True):
    print ("Hora do almoço")
else:
    print ("Não é hora do almoço")
    