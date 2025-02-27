import math


def is_prime(num):
    if num == 2:
        return "YES"
    if num <= 1:
        return "NO"
    if num % 2 == 0:
        return "NO"

    limit = int(math.sqrt(num)) + 1
    for i in range(3, limit, 2):
        if num % i == 0:
            return "NO"

    return "YES"


n = int(input())
for i in range(n):
    x = int(input())
    print(is_prime(x))

