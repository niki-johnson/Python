"""calculando perimetro e area
"""
#recebendo tamanho dos lados
ladox=float(input("Informe tamanho do lado maior(cm) "))
ladoy=float(input("Informe tamanho do lado menor(cm) "))

#trnasormando de cm pra inch
x=0.394*ladox
y=0.394*ladoy

#calculando perimetro
per=2*x+2*y

#calculando area
area=int(x*y)

print("O perímetro vale ",per," inches e a area vale ",area,"inches^2")