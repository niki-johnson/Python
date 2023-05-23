import time


class Sudoku():

    def __init__(self, sudoku):

        self.dimensao = 9
        self.board = sudoku
        self.midpoint = ([1, 1], [1, 4], [1, 7], [4, 1], [
                         4, 4], [4, 7], [7, 1], [7, 4], [7, 7])
        self.grids = self.grid()
        self.posicoes = []

    def grid(self):
        grids = list()
        for i_linha, i_coluna in self.midpoint:
            grid = [[self.board[i_linha+i][i_coluna+j]
                     for j in range(-1, 2)] for i in range(-1, 2)]
            grids.append(grid)
        return grids

    def _get_grid(self, linha, col):
        soma = abs(self.midpoint[0][0] - linha) + \
            abs(self.midpoint[0][1] - col)
        index = 0
        flag = index
        for i_linha, i_coluna in self.midpoint:
            if abs(i_linha - linha) + abs(i_coluna - col) < soma:
                soma = abs(i_linha - linha) + abs(i_coluna - col)
                flag = index
            index += 1
        return flag

    def scanear_num(self, num, linha, col):

        if num in self.board[linha]:
            return False

        elif num in [self.board[i][col] for i in range(9)]:
            return False

        else:
            grid = self._get_grid(linha, col)
            for linha in self.grids[grid]:
                if num in linha:
                    return False

            return True

    def play(self, linha, col):

        if (linha == self.dimensao - 1 and col == self.dimensao):
            return True

        if col == self.dimensao:
            linha += 1
            col = 0

        if self.board[linha][col] > 0:
            return self.play(linha, col + 1)

        for num in range(1, self.dimensao + 1, 1):
            if self.scanear_num(num, linha, col):
                self.board[linha][col] = num
                if self.play(linha, col + 1):
                    return True

            self.board[linha][col] = 0

        return False

    def print_sudoku(self):
        for i in range(self.dimensao):
            for j in range(self.dimensao):
                if j == 2 or j == 5:
                    print(f'{self.board[i][j]} |', end=' ')

                else:
                    print(self.board[i][j], end=' ')

            if i == 2 or i == 5:
                print(' ', '-'*21, sep='\n')
            else:
                print('')


grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4]]


def play():

    jogo = Sudoku(grid)
    if jogo.play(0, 2):
        print("O Sudoku tem solução")
        jogo.print_sudoku()

    else:
        print("O Sudoku não tem solução")


if __name__ == '__main__':
    start = time.time()
    play()
    end = time.time()
    print(f'Tempo para solucionar {end-start:.2f} segundos')
