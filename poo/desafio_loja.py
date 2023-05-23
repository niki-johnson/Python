from datetime import datetime
from loja import Cliente, Vendedor, Compra


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
