def b(n):
    if n == 0:
        return
    b(n-1)
    print(n , end =" ")

n = int(input())
b(n)
