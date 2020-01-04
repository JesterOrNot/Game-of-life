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


def get_width(board):
    return len(board)


def get_height(board):
    return len(board[0])


def live_neighbors(cell, board):
    width = get_width(board)
    height = get_height(board)
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


def next_state(board, row, column):
    alive_neighbors = live_neighbors((row, column), board)
    if board[row][column] == 0:
        if alive_neighbors == 3:
            return 1
        else:
            return 0
    else:
        if alive_neighbors <= 1:
            return 0
        elif alive_neighbors <= 3:
            return 1
        else:
            return 0


def next_board_state(board):
    width = get_width(board)
    height = get_height(board)
    future = dead_state(width, height)

    for x in range(0, width):
        for y in range(0, height):
            future[x][y] = next_state(board, x, y)

    return future


pretty_print_board_debug(next_board_state([[1, 0, 1],
                                           [0, 1, 0],
                                           [0, 0, 0]]))
