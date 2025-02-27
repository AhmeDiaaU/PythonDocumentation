def Read_Matrix():
    rows = int(input())
    assert rows > 0
    lst_of_lsts = [0] * rows
    for row in range(rows):
        lst_of_lsts[row] = list(map(int, input().split()))
    return rows, len(lst_of_lsts[0]), lst_of_lsts


def if_empty(lst_of_lsts):
    return [row for row in lst_of_lsts if len(row) != 0]


if __name__ == "__main__":
    rows, cols, matrix = Read_Matrix()
    print(if_empty(matrix))