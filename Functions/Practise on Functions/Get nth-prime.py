import math
def is_prime(num):
    if num == 1 or num == 2 :
        return True
    for i in range(2,int(math.sqrt(num))+1):
        if num % i ==0 :
            return False
    return True

def nth_prime(n):
    counter = 0
    num = 1
    while counter != n :
        if is_prime(num):
            counter+=1
        num +=1
    return num
for i in range(1,10):
    print(i , nth_prime(i))