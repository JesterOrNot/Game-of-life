import random


def dead_state(width, height):
    return [[0 for _ in range(width)] for _ in range(height)]


def random_state(width, height):
    return [[round(random.random()) for _ in range(width)]
            for _ in range(height)]


def pretty_print_board(board):
    for row in board:
        for column in row:
            if column == 0:
                print(" ", end="")
            else:
                print("O", end="")
        print()


def pretty_print_board_debug(board):
    for row in board:
        print(row)


def live_neighbors(cell, board):
    width = len(board)
    height = len(board[0])
    x = cell[0]
    y = cell[1]
    alive = 0
    for x1 in range((x-1), (x+2)):
        if x1 < 0 or x1 >= width:
            continue
        for y1 in range((y-1), (y+2)):
            if y1 < 0 or y1 >= height:
                continue

            if x1 == x and y1 == y:
                continue

            if board[x1][y1] == 1:
                alive += 1
    return alive


board = random_state(10, 10)
pretty_print_board_debug(board)

print(live_neighbors((1, 1), board))
