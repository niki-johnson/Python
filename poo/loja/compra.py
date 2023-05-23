from datetime import datetime, timedelta


class Compra:

    def __init__(self, vendedor, valor, data=datetime.now()):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor
