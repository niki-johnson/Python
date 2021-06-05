"""Esse programa busca uma raiz de uma função
entre dois pontos. Mas, é necessário que tenha um 0 
no intervalo dado.
Programa usa técnicas de estrutura de blocos -
funções dentro de funções - e funcções implícitas"""

def met_raiz(funcao,pontoa,pontob):
    
    def calcula_raiz(f, linf, lsup):

        while not (abs(linf - lsup) < 0.001):

            pontomed = (lsup + linf) / 2

            if f(linf) * f(pontomed) > 0:

                linf = pontomed

            else:

                lsup = pontomed

        return pontomed
    
    fa = funcao(pontoa)

    fb = funcao(pontob)

    if fa * fb > 0:
        
        return "Intervalo não contem raiz"

    else:
        
        return calcula_raiz(funcao, pontoa, pontob)


print(f'A raiz é {met_raiz(lambda x: x * x * x - 2 * x - 3, 1, 1.2)}')

