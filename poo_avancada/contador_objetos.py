class SimpleClass:
    count = 0

    def __init__(self):
        SimpleClass.count += 1


if __name__ == '__main__':
    lista = [SimpleClass(), SimpleClass(), SimpleClass()]
    print(SimpleClass.count)  # Esperado 2
