def primeFactorization(num: int):
    if num == 1:
        return 1
    n = 2
    factors = []
    while n ** 2 <= num:
        if num % n == 0:
            factors.append(n)
            num //= n
        else:
            n += 1
    if num > 1:
        factors.append(num)
    return factors


n = int(input())
factors = primeFactorization(n)
frequency_dict = {}
for num in factors:
    if num in frequency_dict:
        frequency_dict[num] += 1
    else:
        frequency_dict[num] = 1
output = "*".join([f"({num}^{freq})" for num, freq in frequency_dict.items()])
print(output)
