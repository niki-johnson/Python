"""
    Reduzindo tempo de execução da v1 (por volta dos 1,5 seg) para abaixo de 0,5 seg em média
"""

import time


def proxima_posicao_vazia(sudoku):

    for i_linha in range(len(sudoku)):
        for i_coluna in range(len(sudoku)):
            if sudoku[i_linha][i_coluna] == 0:

                return (i_linha, i_coluna)


def scanear_palpite(sudoku, linha, coluna, numero):

    if numero in sudoku[linha]:
        return False

    if numero in [sudoku[i][coluna] for i in range(len(sudoku))]:
        return False

    linha_inicio_grid = linha // 3 * 3
    coluna_inicio_grid = coluna // 3 * 3

    for i_linha in range(linha_inicio_grid, linha_inicio_grid + 3):
        for i_coluna in range(coluna_inicio_grid, coluna_inicio_grid+3):
            if sudoku[i_linha][i_coluna] == numero:
                return False

    return True


def solve(sudoku):

    try:
        linha, coluna = proxima_posicao_vazia(sudoku)
    except TypeError:
        return True

    for palpite in range(1, 10):
        if scanear_palpite(sudoku, linha, coluna, palpite):
            sudoku[linha][coluna] = palpite
            if solve(sudoku):
                return True

        sudoku[linha][coluna] = 0

    return False


def print_sudoku(sudoku):
    for i in range(9):
        for j in range(9):
            if j == 2 or j == 5:
                print(f'{sudoku[i][j]} |', end=' ')

            else:
                print(sudoku[i][j], end=' ')

        if i == 2 or i == 5:
            print(' ', '-'*21, sep='\n')
        else:
            print('')

    return ''


grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4]]


if __name__ == '__main__':

    start = time.time()

    if solve(grid):
        print(print_sudoku(grid))
        end = time.time()
        print(f'Tempo para solucionar {end-start:.2f} segundos')

    else:
        print("O sudoku não tem solução")
