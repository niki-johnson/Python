from .pessoa import Pessoa


class Cliente(Pessoa):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []
        self.total = 0

    def __iter__(self):
        return self.compras.__iter__()

    def registrar_compra(self, compra):
        self.compras.append(compra)

    def total_compras(self):
        for compra in self.compras:
            self.total += compra.valor
        return self.total

    def get_data_ultima_compra(self):
        datas_compra = []
        for compra in self:
            datas_compra.append(compra.data)
        return sorted(datas_compra)[-1]

    def __str__(self):
        return super().__str__()
