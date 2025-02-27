def factorial(num: int):
        summation = 1
        for i in range(1, num + 1):
            summation *= i
        return summation


n, r = map(int, input().split())
combination = (factorial(n)//(factorial(n-r)*factorial(r)))
permutation = factorial(n) // factorial(n-r)
print(combination , end=" ")
print(permutation)