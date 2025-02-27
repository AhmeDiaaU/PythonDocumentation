def Read_Matrix():
    rows = int(input())
    assert rows > 0
    lst_of_lsts = [0] * rows
    for row in range(rows):
        lst_of_lsts[row] = list(map(int, input().split()))
    return rows, len(lst_of_lsts[0]), lst_of_lsts


def Upper_Matrix(lst_of_lsts):
    upper = 0
    for r in range(len(lst_of_lsts)):
        for c in range(r, len(lst_of_lsts)):
            upper += lst_of_lsts[r][c]
    return upper


def Lower_Matrix(lst_of_lsts):
    lower = 0
    for r in range(len(lst_of_lsts)):
        for c in range(0, r+1):
            lower += lst_of_lsts[r][c]
    return lower

if __name__ == "__main__" :
    rows , cols , matrix = Read_Matrix()
    print(Upper_Matrix(matrix))
    print(Lower_Matrix(matrix))