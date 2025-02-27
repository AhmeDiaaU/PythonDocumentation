def new_array(a: list, b: list, x):
    arr = []
    for i in range(x):
        arr.append(b[i])

    for i in range(x):
        arr.append(a[i])
    return arr


y = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*new_array(a, b, y))
