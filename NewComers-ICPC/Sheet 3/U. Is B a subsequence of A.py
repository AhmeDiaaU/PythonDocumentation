import math

n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
if len(x) == n and len(y) == m:
    i =0
    for j in range(n):
        if i < m and x[j] == y[i] :
            i+=1
    if i == m :
        print("YES")
    else:
        print("NO")