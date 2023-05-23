"""
    Criando uma lista usando a técnica de comprehension
"""
# [ expressão for item in list if condicional] - condicional n é obrigatório

dobros_pares = [i * 2 for i in range(10) if i % 2 == 0]
print(dobros_pares)
