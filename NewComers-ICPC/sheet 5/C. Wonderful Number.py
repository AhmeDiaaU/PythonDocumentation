def Wonderful(x: int):
    binary = bin(x)[2:]
    reversed = binary[::-1]
    if x % 2 != 0 and binary == reversed:
        print("YES")
    else:
        print("NO")


x = int(input())
Wonderful(x)
