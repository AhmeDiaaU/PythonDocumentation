def binary(n):
    global bn
    if n == 0:
        return
    binary(n//2)
    print(n%2 , end="")
r = int(input())
for i in range(r):
    n = int(input())
    binary(n)
    print()


#10 % 2 = 0
#5 % 2 = 1 
#2 % 2 = 0
#1%2 = 1