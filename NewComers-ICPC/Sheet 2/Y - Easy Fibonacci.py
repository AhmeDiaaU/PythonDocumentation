def fibonacci(num):
    n1 = 0
    n2 = 1
    res = 0
    for i in range(1, num + 1):
        print(n1, end=" ")
        res = n1 + n2
        n1 = n2
        n2 = res


n = int(input())
fibonacci(n)