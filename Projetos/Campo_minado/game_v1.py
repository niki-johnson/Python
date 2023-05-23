import random
from functools import reduce


def make_move():
    posicao = input("Faça sua jogada: ").split(',')
    return posicao


class CampoMinado():

    def __init__(self):
        self.board = []
        self.board_jogador = []
        self.jogada = list()
        self._criar_board()
        self.valor_casa()

    def _criar_board(self):
        for i in range(8):
            self.board.append([" "] * 8)

        self.board.insert(0, ["0", "1", "2", "3", "4", "5", "6", "7", "8"])
        i = 1
        for linha in self.board[1:]:
            linha.insert(0, str(i))
            i += 1

        self._plantar_bomba()

    def _plantar_bomba(self):
        posicoes = [1, 2, 3, 4, 5, 6, 7, 8]
        aleatorio1 = random.choices(posicoes, k=9)
        aleatorio2 = random.choices(posicoes, k=9)

        for i in range(9):
            self.board[aleatorio1[i]][aleatorio2[i]] = '*'

    def scanear_jogada(self, coordenadas):
        linha = int(coordenadas[0])
        coluna = int(coordenadas[1])

        self.jogada.append([linha, coluna])

        if self.board[linha][coluna] == "*":
            return False
        elif int(self.board[linha][coluna]) > 0:
            return True

        else:
            for l in range(max(0, linha-1), min(len(self.board), linha+2)):
                for c in range(max(0, coluna-1), min(len(self.board), coluna+2)):
                    if [l, c] in self.jogada:
                        continue
                    self.scanear_jogada([l, c])
            return True

    def valor_casa(self):

        for linha in range(1, 9):
            for coluna in range(1, 9):
                if self.board[linha][coluna] == '*':
                    continue

                bomba = 0
                for i in range(max(0, linha-1), min(len(self.board), linha+2)):
                    for j in range(max(0, coluna-1), min(len(self.board), coluna+2)):
                        if i == linha and j == coluna:
                            continue
                        if self.board[i][j] == '*':
                            bomba += 1
                self.board[linha][coluna] = str(bomba)

    def move_disponivel(self):
        print(len(self.board_jogador))
        count = False
        for linha in range(9):
            for coluna in range(9):
                if self.board_jogador[linha][coluna] == ' ':
                    count = True
        return count

    def print_game_over(self):
        print("   ".join(self.board[0]))
        for linha in self.board[1:]:
            print(f'{linha[0]}   {" | ".join(linha[1:])}')

    def print_game_player(self):

        self.board_jogador = [
            [' ' for _ in range(len(self.board))] for _ in range(len(self.board))]
        for linha in range(len(self.board_jogador)):
            for coluna in range(len(self.board_jogador)):
                if [linha, coluna] in self.jogada:
                    self.board_jogador[linha][coluna] = str(
                        self.board[linha][coluna])

        print("   ".join(self.board[0]))
        i = 1
        for linha in self.board_jogador[1:]:
            print(f'{i}   {" | ".join(linha[1:])}')
            i += 1


def play():
    jogo = CampoMinado()
    jogo.print_game_player()

    while jogo.move_disponivel():
        jogo.print_game_player()
        jogada = make_move()
        if int(jogada[0]) < 1 or int(jogada[0]) > 8 or int(jogada[1]) < 1 or int(jogada[1]) > 8:
            print("Coordenadas inválidas.")
            continue
        else:
            if not jogo.scanear_jogada(jogada):
                print("Você perdeu! :/")
                jogo.print_game_over()
                exit()
            else:
                continue

    print("Você ganhou!!")
    jogo.print_game_over()


if __name__ == '__main__':
    play()
