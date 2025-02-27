n, m = map(int, input().split())
x = list(map(int, input().split()))
arr = [0] * m
if len(x) == n:
    for i in x:
        arr[i - 1] += 1
print(*arr, sep="\n")
