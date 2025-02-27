def u_swap(x, y):
    z = 0
    z = x
    x = y
    y = z
    return print(x, y)


x, y = map(int, input().split())
u_swap(x, y)
