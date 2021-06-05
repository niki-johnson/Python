"""calculando perimetro e area por função
"""
#recebendo tamanho dos lados
ladox=float(input("Informe tamanho do lado maior(cm) "))
ladoy=float(input("Informe tamanho do lado menor(cm) "))

#trnasormando de cm pra inch
x=0.394*ladox
y=0.394*ladoy

def calc_per(x,y):
    #calculando perimetro
    per=2*x+2*y
    return per

def calc_area(x,y):
    #calculando area
    area=x*y
    return area

per=calc_per(x,y)
area=calc_area(x,y)
print("O perímetro vale ",per," inches e a area vale ",area,"inches^2")