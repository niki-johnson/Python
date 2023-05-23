"""
    Utilizando o conceito de classe abstrata
    Importando algoritmos
"""
from abc import ABCMeta, abstractproperty


# metodo para ajudar a classe a n ser instanciada, ja que é abstrata
class Humano(metaclass=ABCMeta):

    # Atributo de classe
    especie = 'Homo sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None  # underline para dar ideia de atributo privado

    @abstractproperty
    def inteligente(self):
        pass

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

    @property
    def inteligente(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True


if __name__ == '__main__':

    try:
        anonimo = Humano('John Doe')
    except TypeError:
        print('Classe abstrata')

    jose = HomoSapiens('Jose')
    print('{} da classe {}, inteligente: {}'.format(
        jose.nome, jose.__class__.__name__, jose.inteligente))

    grogn = Neanderthal('Grogn')
    print('{} da classe {}, inteligente: {}'.format(
        grogn.nome, grogn.__class__.__name__, grogn.inteligente))
