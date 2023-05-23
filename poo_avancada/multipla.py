"""
    Estudo sobre herança múltipla

"""


class Animal:

    @property
    def capacidade(self):
        return ('dormir', 'comer', 'beber')


class Homem(Animal):
    @property
    def capacidade(self):
        return super().capacidade + ('amar', 'falar', 'estudar')


class Aranha(Animal):
    @property
    def capacidade(self):
        return super().capacidade + ('fazer teia', 'andar pelas paredes')


class HomemAranha(Homem, Aranha):
    @property
    def capacidade(self):
        return super().capacidade + \
            ('bater em bandidos', 'atirar teias entre prédios')


if __name__ == '__main__':
    john = Homem()
    print(john.capacidade)
    print('')

    aranha = Aranha()
    print(aranha.capacidade)
    print('')

    peter = HomemAranha()
    print(peter.capacidade)
