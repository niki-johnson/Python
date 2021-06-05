def unique_list(lista):
    """Recebe uma lista c valores e retorna uma nova lista
        com valores q não se repetem
    """
    unicos = []
    for i in lista:
        #checando se esta na lista
        if i not in unicos:
            #add a nova lista
            unicos.append(i)
    
    return unicos

lista1 = [3,3,5,7,22,39,22]
unic = unique_list(lista1)
print(unic)
            
                