import random


def print_board_nums():
    # 0 | 1 | 2 etc (tells us what number corresponds to what box)
    numbers_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
    print(numbers_board)

    for row in numbers_board:
        print('| ' + ' | '.join(row) + ' |')


# print_board_nums()
board = ['0', '3', '2', '3', '4', '2', '3', '7', '3']


def empty_squares():
    return ' ' in board


def random_empty_spot():
    return [i for i, spot in enumerate(board) if spot == ' ']


print(empty_squares())
