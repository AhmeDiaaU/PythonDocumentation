def Read_Matrix():
    rows , cols = map(int,input().split())
    assert rows >0 
    lst_of_lsts = [0] * rows
    for row in range(rows) :
        lst_of_lsts[row] = list(map(int , input().split()))
    return rows , len(lst_of_lsts[0]) , lst_of_lsts

def multiply_matrix():
    rowsA ,colsA, MA = Read_Matrix()
    rowsB , colsB , MB = Read_Matrix() 
    Result = [[0 for _ in range(colsB)]for _ in range(rowsA)]
    for i in range(rowsA):
        for j in range(colsB):
            for z in range(len(MB)):
                Result[i][j] += MA[i][z] *MB[z][j]

    return Result


result = multiply_matrix()
for row in result :
    for element in row :
        print(element , end= " ")
    print()