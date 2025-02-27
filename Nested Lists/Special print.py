def Read_Matrix():
    rows = int(input())
    assert rows > 0
    lst_of_lsts = [0] * rows
    for row in range(rows):
        lst_of_lsts[row] = list(map(int, input().split()))
    return rows, len(lst_of_lsts[0]), lst_of_lsts


def L_Rows(matrix):
    r = len(matrix) - 1
    return sum(matrix[r][c] for c in range(len(matrix) + 1))


def L_cols(matrix, rows):
    c = rows
    return sum(matrix[r][c] for r in range(len(matrix)))


def Left_diagonal(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))


def right_diagonal(matrix, rows , cols):
    return sum(matrix[r][cols - r - 1] for r in range(rows))


if __name__ == "__main__":
    rows, cols, matrix = Read_Matrix()
    print(L_cols(matrix, rows), L_Rows(matrix))
    print(Left_diagonal(matrix), right_diagonal(matrix, rows , cols))
