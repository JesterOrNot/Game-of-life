import random
import time


def new_board():
    return [
        [random.randint(0, 1), random.randint(0, 1), random.randint(
            0, 1), random.randint(0, 1), random.randint(0, 1)],
        [random.randint(0, 1), random.randint(0, 1), random.randint(
            0, 1), random.randint(0, 1), random.randint(0, 1)],
        [random.randint(0, 1), random.randint(0, 1), random.randint(
            0, 1), random.randint(0, 1), random.randint(0, 1)],
        [random.randint(0, 1), random.randint(0, 1), random.randint(
            0, 1), random.randint(0, 1), random.randint(0, 1)],
        [random.randint(0, 1), random.randint(0, 1), random.randint(
            0, 1), random.randint(0, 1), random.randint(0, 1)],
    ]


def pretty_print_board(board):
    for row in board:
        for column in row:
            if column == 0:
                print(" ", end="")
            else:
                print("O", end="")
        print()


def next_generation(board):
    future = [[0 for i in range(5)] for i in range(5)]
    for row in range(0, 5):
        for column in range(0, 5):
            alive = 0
            for i in range(-1, 1):
                for j in range(-1, 1):
                    alive += board[i+row][j+column]
            alive -= board[4][4]
            if board[row][column] == 1 and alive < 2:
                future[row][column] = 0
            elif board[row][column] == 1 and alive > 3:
                future[row][column] = 0
            elif board[row][column] == 0 and alive == 3:
                future[row][column] = 1
            else:
                future[row][column] = board[row][column]
    return future


if __name__ == "__main__":
    print("\u001b[2J")
    board = new_board()
    pretty_print_board(board)
    print()
    while board != [[0 for i in range(5)] for i in range(5)]:
        board = next_generation(board)
        time.sleep(1)
        print("\u001b[2J")
        pretty_print_board(board)
