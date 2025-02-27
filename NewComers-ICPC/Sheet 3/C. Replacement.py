n = int(input())
lst = list(map(int,input().split()))
for i in range(n) :
    if lst[i] >0:
        lst[i] = 1
    elif lst[i] < 0 :
        lst[i] = 2
for i in lst :
    print(i,end = " ")