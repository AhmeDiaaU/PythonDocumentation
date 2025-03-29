def b(n):
    if n == 0 :
        return
    if n != 1:
       print(n , end=" ")
    else :
        print(n)
    b(n-1)
    
n = int(input())
b(n)