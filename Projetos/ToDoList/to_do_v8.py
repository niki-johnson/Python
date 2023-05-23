"""
    Projeto que lista qualquer tipo de tarefa em blocos
    Aolicar tratamento de erro/exceção
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

    # sobrecarga do operador +=

    def __iadd__(self, tarefa):
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self

    def add(self, tarefa, vencimento=None, **kwargs):
        # chamo tarefa para registrar uma nova tarefa em tarefa
        # verifico se a tarefa
        funcao_chamada = self._add_tarefa if isinstance(tarefa, Tarefa) \
            else self._add_nova_tarefa

        kwargs['vencimento'] = vencimento
        funcao_chamada(tarefa, **kwargs)

    def _add_tarefa(self, tarefa, **kwargs):  # começar com 1 underline é convenção
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    def pendentes(self):
        # os objetos dentro da lista tem metodos e atributos da classe de Tarefa
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):

        for tarefa in self.tarefas:
            if descricao == tarefa.descricao:
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


# recebendo por herança tudo que foi definido em tarefa
class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento=None, dia_rec=7):
        super().__init__(descricao, vencimento)
        self.dias = dia_rec
        self.dono = None

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_task = TarefaRecorrente(self.descricao, novo_vencimento)
        if self.dono:
            self.dono += nova_task
        return nova_task


def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar prato', datetime.now() +
             timedelta(days=3, minutes=27, seconds=1))
    casa += TarefaRecorrente('Trocar lençóis', datetime.now())

    try:
        casa.procurar('a').concluir()  # add automaticamente quando conclui
    except Exception as e:
        print(e)
        print('A pesquisa não trouxe nenhum resultado\n')

    print(casa)
    casa.procurar('Lavar prato').concluir()
    for tarefa in casa:
        print(tarefa)
    print(casa)


if __name__ == '__main__':
    main()
