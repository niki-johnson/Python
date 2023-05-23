class Carro:

    def __init__(self, vel_max, vel_inicial=0):
        self.vel_max = vel_max
        self.vel_inicial = vel_inicial
        self.vel_insta = vel_inicial

    def acelerar(self, delta=5):
        self.vel_insta += delta
        self.vel_insta = (self.vel_max if self.vel_insta >
                          self.vel_max else self.vel_insta)
        return f'O carro está a {self.vel_insta} km/h'

    def frear(self, delta=5):
        self.vel_insta -= delta
        self.vel_insta = (0 if self.vel_insta < 0 else self.vel_insta)
        return f'O carro está a {self.vel_insta} km/h.'


if __name__ == '__main__':
    c1 = Carro(230, 150)

    for _ in range(25):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.frear(delta=20))
