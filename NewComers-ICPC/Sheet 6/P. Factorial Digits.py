import math

def factorial_digits(n):
    if n == 0 or n == 1:
        return 1 
    log10_fact = (n * math.log10(n) - n * math.log10(math.e) +
                  0.5 * (math.log10(2 * math.pi * n)))
    return int(log10_fact) + 1


n = int(input())
digits = factorial_digits(n)
print(f"Number of digits of {n}! is {digits}")