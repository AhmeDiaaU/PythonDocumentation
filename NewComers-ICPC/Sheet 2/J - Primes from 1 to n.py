def prime(n) :
    for i in range (2 , n) :
        if n % i == 0 :
            return False
    return True
n = int(input())
lst =[]
for i in range(2, n + 1):
    if (prime(i)):
        print(i, end=" ")