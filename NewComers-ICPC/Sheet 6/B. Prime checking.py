import math

n = int(input())
x = int(math.sqrt(n))+1
flag = True
if n == 1 or n < 1:
    print("NO")
elif n == 2:
    print("YES")
else :
    if n % 2 != 0:
        for i in range(3, x):
            if n % i == 0:
                flag = False
        if flag:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

