def min_max(lst:list):
    mi = lst[0]
    ma = lst[0]
    for i in lst :
        if i < mi :
            mi = i
        if i > ma :
            ma = i
    return mi , ma


x = int(input())
lst = list(map(int, input().split()))
if len(lst) == x :
    print(*min_max(lst))