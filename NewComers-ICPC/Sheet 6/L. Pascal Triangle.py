def PascalTriangle(Rowsnum:int):
    res =[[1]]
    for i in range(Rowsnum-1):
        temp =[0]+res[-1]+[0]
        row =[]
        for j in range(len(res[-1])+1):
            row.append(temp[j]+temp[j+1])
        res.append(row)
    return res

num = int(input())
pascal = PascalTriangle(num)
for row in pascal:
    for num in row :
        print(num , end=" ")
    print()
