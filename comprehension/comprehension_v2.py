"""
    Criando uma lista usando generators
"""
# generator usa menos memória - gera numero sob demanda
generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
