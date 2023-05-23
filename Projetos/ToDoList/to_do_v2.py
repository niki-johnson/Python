"""
    Projeto que lista qualquer tipo de tarefa 
    Essa versão traz o conceito de blocos de tarefas
    Tarefas de um determinado assunto

"""

from datetime import datetime


class Projeto:

    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def add(self, descricao):
        # chamo tarefa para registrar uma nov atarefa em tarefa
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        # os objetos dentro da lista dem metodos e atributos da classe de Tarefa
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):

        for tarefa in self.tarefas:
            if descricao in tarefa.descricao:
                return tarefa

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefas pendentes)'


class Tarefa:

    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluida)' if self.feito else '')


def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Passar roupa')
    casa.add('Lavar prato')
    print(casa)

    casa.procurar('Lavar prato').concluir()

    for tarefa in casa.tarefas:
        print(tarefa)
    print(casa)

    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas secas')
    mercado.add('Carne')
    mercado.add('Tomate')
    print(mercado)

    comprar_carne = mercado.procurar('Carne')
    comprar_carne.concluir()
    for tarefa in mercado.tarefas:
        print(f'- {tarefa}')
    print(mercado)


if __name__ == '__main__':
    main()
