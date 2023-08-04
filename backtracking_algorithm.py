N = 8

all_board_states = []


def solve_n_queens(board, col):
    if col == N:
        print(board)
        return True
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens(board, col + 1):
                return True
            board[i][col] = 0
    return False


def is_safe(board, row, col):
    for x in range(col):
        if board[row][x] == 1:
            return False
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    for x, y in zip(range(row, N, 1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    return True


b = [[0 for x in range(N)] for y in range(N)]

if not solve_n_queens(b, 0):
    print("No solution found")
