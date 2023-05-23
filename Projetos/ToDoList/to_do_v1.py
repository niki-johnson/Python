"""
    Projeto que lista qualquer tipo de tarefa 
"""

from datetime import datetime


class Tarefa:

    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' Concluida' if self.feito else '')


def main():
    casa = []
    casa.append(Tarefa('Passar roupa'))
    casa.append(Tarefa('Lavar prato'))
    casa.append(Tarefa('Varrer casa'))

    for task in casa:
        if task.descricao == 'Lavar prato':
            task.concluir()
        print(task)


if __name__ == '__main__':
    main()
