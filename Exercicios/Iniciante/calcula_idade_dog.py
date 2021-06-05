"""Programa calcula idade de um cachorro
"""

#receber a nota do user
dog_age = input("Informe a idade do seu cachorro: ")

#testando se é str
try:
    dog_age = float(dog_age)
    
    if dog_age<0:
        print("Negative value can´t be given")
        exit()
#formata qnts casas decimais o numero vai mostrar
#human_age = "{:.2f}".format(human_age)     
except ValueError as erro:
    print ("Invalid")
    print (erro)

else:
    #testanto idade que eu dou
    if (dog_age <= 1):
        human_age = dog_age * 15
        
        print ("The given dog age ",float(dog_age)," is ",\
               float(human_age)," in human years")

    elif (dog_age <= 2):
        human_age = dog_age * 12
        
        print ("The given dog age ",float(dog_age)," is ",\
               float(human_age)," in human years")
    
    elif (dog_age <= 3):
        human_age = dog_age * 9.3
        
        print ("The given dog age ",float(dog_age)," is ",\
               float(human_age)," in human years")
    
    elif (dog_age <= 4):
        human_age = dog_age * 8
        
        print ("The given dog age ",float(dog_age)," is ",\
               float(human_age)," in human years")
    
    elif (dog_age <= 5):
        human_age = dog_age * 7.2
        
        print ("The given dog age ",float(dog_age)," is ",\
               float(human_age)," in human years")

    else:
        human_age = dog_age * 7
        
        print ("The given dog age ",float(dog_age)," is ",\
               float(human_age)," in human years")