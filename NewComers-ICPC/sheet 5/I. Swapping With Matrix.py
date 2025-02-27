def matrix_swap(array: list, x, y):
    array[a - 1], array[b - 1] = array[b - 1], array[a - 1]
    for i in range(n):
        array[i][b - 1], array[i][a - 1] = array[i][a - 1], array[i][b - 1]
    for j in array :
        print(*j)


n, a, b = map(int, input().split())
lst = []
for i in range(n):
    arr = list(map(int, input().split()))
    if len(arr) == n:
        lst.append(arr)
matrix_swap(lst, a, b)
