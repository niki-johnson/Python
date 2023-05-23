class Data:

    def to_str(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()  # instanciar #chamando o construtor

d1.dia = 5
d1.mes = 12
d1.ano = 2019

print(d1)
