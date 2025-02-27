def Read_Matrix():
    rows = int(input())
    assert rows > 0
    lst_of_lsts = [0] * rows
    for row in range(rows):
        lst_of_lsts[row] = list(map(int, input().split()))
    return rows, len(lst_of_lsts[0]), lst_of_lsts


def switch_index(lst_of_lsts):
    for row in lst_of_lsts:
        for index in range(len(row)):
            row[0], row[len(row) - 1] = row[len(row) - 1], row[0]
    return lst_of_lsts

if __name__ == "__main__":
    rows, cols, matrix = Read_Matrix()
    if rows == cols == 1:
        print(0, 0)
        exit(0)

    R_matrix = switch_index(matrix)
    print(R_matrix)