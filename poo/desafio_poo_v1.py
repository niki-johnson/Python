"""
    Implementar o Diagrama de classes, para gerir dados básicos de venda de uma loja

    Regras:
    • Tanto vendedor quanto cliente são pessoas (herdam da classe Pessoa)
    • Ao converter um cliente ou vendedor em string deve mostrar o nome e a idade
    • O cliente possui uma lista de compras efetuadas (do tipo Compra)
    • O método Cliente.registra_compra() recebe um objeto do tipo Compra
    • O método Cliente.total_compras() deve retornar o somatório de todas as compras
    • O método Cliente.get_data_ultima_compra() deve retornar a data da última compra
    • A propriedade Compra.vendedor é do tipo Vendedo
"""

from datetime import datetime, timedelta


class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'Nome: {self.nome}, idade: {self.idade}'


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def __str__(self):
        return super().__str__() + f', salário: {self.salario}'


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


class Compra:

    def __init__(self, vendedor, valor, data=datetime.now()):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor


def main():
    juracy = Cliente('Juracy Filho', 44)
    leo = Vendedor('Leonardo Leitão', 36, 1000)
    compra1 = Compra(leo, 512, datetime.now())
    compra2 = Compra(leo, 256, datetime(2018, 6, 4))
    juracy.registrar_compra(compra1)
    juracy.registrar_compra(compra2)
    print(f'Cliente: {juracy}')
    print(f'Vendedor: {leo}')
    print(f'Total: {juracy.total_compras()} em {len(juracy.compras)} compras')
    print(f'Última compra: {juracy.get_data_ultima_compra()}')


if __name__ == '__main__':
    main()
