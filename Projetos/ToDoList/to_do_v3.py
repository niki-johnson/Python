"""
    Projeto que lista qualquer tipo de tarefa em blocos
    Essa versão traz a possibilidade de guardar a hora exata que foi criado a task
    Traz também o método iter, que permite que o objeto seja iterado
"""


from datetime import datetime


class Projeto:

    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):  # por padrão esse metodo vai iterar o unico item iteravel - a lista de tarefas
        # algo pode ser iterado
        # não preciso criar um for para casa.tarefas, so chamar casa nesse ex
        return self.tarefas.__iter__()

    def add(self, descricao):
        # chamo tarefa para registrar uma nov atarefa em tarefa
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        # os objetos dentro da lista tem metodos e atributos da classe de Tarefa
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

    for tarefa in casa:
        print(tarefa)
    print(casa)

    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas secas')
    mercado.add('Carne')
    mercado.add('Tomate')
    print(mercado)

    comprar_carne = mercado.procurar('Carne')
    comprar_carne.concluir()
    for tarefa in mercado:
        print(f'- {tarefa}')
    print(mercado)


if __name__ == '__main__':
    main()
