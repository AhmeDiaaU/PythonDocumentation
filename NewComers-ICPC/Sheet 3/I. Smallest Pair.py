t = int(input())
for x in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    minimum = 1329845646465432135468794321987
    for i in range (1,n):
        for j in range(i+1,n+1):
            x = j-1
            y = i-1
            total = lst[y] + lst[x] + j - i
            if total < minimum:
                minimum = total
    print(minimum)