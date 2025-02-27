n, m = list(map(int, input().split()))
lst = []
for i in range(n):
    arr = list(map(int, input().split()))
    if len(arr) == m:
        lst.append(arr)
for i in lst:
    var = i[::-1]
    print(*var , sep=" ")