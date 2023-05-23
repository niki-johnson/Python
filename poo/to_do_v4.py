"""
    Projeto que lista qualquer tipo de tarefa em blocos 
    Essa versão traz a ideia de vencimento da tarefa

"""


from datetime import datetime, timedelta


class Projeto:

    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):  # por padrão esse metodo vai iterar o unico item iteravel - a lista de tarefas
        # algo pode ser iterado
        # não preciso criar um for para casa.tarefas, so chamar casa nesse ex
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        # chamo tarefa para registrar uma nov atarefa em tarefa
        self.tarefas.append(Tarefa(descricao, vencimento))

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

    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):

        if self.feito:
            return self.descricao + (' (Concluida)')

        elif self.vencimento:
            if datetime.now() > self.vencimento:
                return self.descricao + (' (Vencida)')

            else:
                return f'{self.descricao} {(self.vencimento - datetime.today()).days} dia(s) para vencer'
        return self.descricao + (' Concluida' if self.feito else '')


def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar prato', datetime.now() +
             timedelta(days=3, minutes=27, seconds=1))
    print(casa)

    # casa.procurar('Lavar prato').concluir()

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
