n = int(input())
lst = list(map(int, input().split()))
index = 0
x = 1e5
for i in range(n):
    if lst[i] < x:
        x = lst[i]
        index = i + 1
print(x, index)
