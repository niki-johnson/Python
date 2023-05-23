"""
    Entendendo atributos e métodos de instância x estático x classe
    
    Utilizando decorator
"""


class Humano:

    # Atributo de classe
    especie = 'Homo sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None  # underline para dar ideia de atributo privado

    # make them act as getters, setters, or deleters
    @property
    def idade(self):
        return self._idade

    # alterar valor da idade
    @idade.setter
    def idade(self, idade):
        # validação
        if idade < 0:
            raise ValueError('Idade deve ser um numero positivo')
        self._idade = idade

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'

    # para definir um metodo estatico vai ser usado um decorator

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopitecos',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('José')
    jose.idade = 40
    print(f'Nome: {jose.nome}; Idade: {jose.idade}')
