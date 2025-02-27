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


def maximum(array: list):
    ma = 0
    for i in array:
        if i > ma:
            ma = i
    return ma


def minimum(arr: list):
    mi = arr[0]
    for i in arr:
        if i < mi:
            mi = i
    return mi


def count_palin(arr: list):
    counter_palin = 0
    for palin in lst:
        palin = str(palin)
        reversed_number = palin[::-1]
        palin: int
        reversed_number: int
        if reversed_number == palin:
            counter_palin += 1
    return counter_palin


def maximum_palin(arr: list):
    cu = []
    for i in arr:
        c = 0
        for counter in range(1, i + 1):
            if i % counter == 0:
                c += 1
        cu.append(c)
    ma = maximum(cu)
    index = cu.index(ma)
    for j in range(index, len(arr)):
        if cu[j] == cu[index] and arr[j] > arr[index]:
            index = j
    return lst[index]


def five_in_one(lst: list):
    count_prime = 0
    for i in lst:
        if is_prime(i) == "YES":
            count_prime += 1

    print(f"The maximum number : {maximum(lst)}")
    print(f"The minimum number : {minimum(lst)}")
    print(f"The number of prime numbers : {count_prime}")
    print(f"The number of palindrome numbers : {count_palin(lst)}")
    print(f"The number that has the maximum number of divisors : {maximum_palin(lst)}")


n = int(input())
lst = list(map(int, input().split()))
if len(lst) == n:
    five_in_one(lst)
