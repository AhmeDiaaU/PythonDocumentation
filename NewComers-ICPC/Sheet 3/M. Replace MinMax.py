No_of_digits = int(input())
lst = list(map(int,input().split()))
index =0
index1 =0
if len(lst) == No_of_digits :
    mini = min(lst)
    maximum = max(lst)
    for i in lst :
        if i == mini :
            break
        index +=1
    for j in lst :
        if j == maximum :
            break
        index1+=1
    lst[index], lst[index1] = lst[index1], lst[index]
    for i in lst :
        print(i,end=" ")
