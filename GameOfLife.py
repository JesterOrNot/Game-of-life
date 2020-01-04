import random


def dead_state(width, height):
    return [[0 for j in range(width)] for i in range(height)]


def random_state(width, height):
    return [[round(random.random()) for j in range(width)] for i in range(height)]


def pretty_print_board(board):
    for row in board:
        for column in row:
            if column == 0:
                print(" ", end="")
            else:
                print("O", end="")
        print()


pretty_print_board(random_state(10, 10))
