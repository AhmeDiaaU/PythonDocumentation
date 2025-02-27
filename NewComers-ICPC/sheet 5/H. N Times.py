def times(t: int, n: str):
    for i in range(t):
        print(n, end=" ")


x = int(input())
for i in range(x):
    a , b = input().split()
    a = int(a)
    times(a , b)
    print()