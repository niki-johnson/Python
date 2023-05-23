"""
    Entendendo atributos e métodos de instância x estático x classe
"""


class Humano:

    # Atributo de classe
    especie = 'Homo sapiens'

    def __init__(self, nome):
        self.nome = nome

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
    grokn = Neanderthal('Grokn')

    print(
        f'Evolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(
        f'Evolução (a partir da classe): {", ".join(Neanderthal.especies())}')
    print(f'Homo Sapiens evoluido? {HomoSapiens.is_evoluido()}')
    print(f'Homo Sapiens evoluido? {Neanderthal.is_evoluido()}')
