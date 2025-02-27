def p(x: int):
    for i in range(1, x + 1):
        if i == x:
            print(x)
        else:
            print(i, end=" ")


x = int(input())
p(x)
