class Data:

    def __init__(self, dia, mes, ano):  # roda qnd o construtor é chamado
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):  # usado para transformar em string
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(5, 12, 2019)  # instanciar #chamando o construtor

print(d1)
