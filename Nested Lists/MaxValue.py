def Read_Matrix():
    rows = int(input())
    assert rows > 0
    lst_of_lsts = [0] * rows
    for row in range(rows):
        lst_of_lsts[row] = list(map(int, input().split()))
    return rows, len(lst_of_lsts[0]), lst_of_lsts


def max_value(matrix):
    max = 0
    R = 0
    C = 0
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] > max:
                R = r
                C = c
                max = matrix[r][c]
    return max, R, C


if __name__ == "__main__":
    rows, cols, matrix = Read_Matrix()
    print(max_value(matrix))
