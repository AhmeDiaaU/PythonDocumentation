def read_Snake():
    rows , cols  = map(int , input().split())
    assert rows > 0
    lst_of_lsts = [[0] * cols for i in range(rows)]
    return lst_of_lsts , len(lst_of_lsts[0])


table , col = read_Snake()
case = 0
for i in range(len(table)):
    for j in range(len(table[0])):
        if i % 2 == 0 :
            table[i][j] ='#' 
        else :
            table [i][j] = '.'
    if i % 2 != 0 :
        if case == 0:
            table [i][-1] ='#'
        else :
            table[i][0] ='#'
        case = (case+1)%2
for row in table :
    for pos in row :
        print(pos , end="")
    print()