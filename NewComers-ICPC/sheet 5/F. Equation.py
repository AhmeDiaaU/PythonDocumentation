def is_power(x, y):
    s = 1
    for i in range(y):
        s *= x
    return s


def equation(x, n):
    p = 0
    for i in range(2, n + 1):
        if i % 2 == 0:
            p += is_power(x,i)
    return p


x, n = map(int, input().split())
print(equation(x , n))