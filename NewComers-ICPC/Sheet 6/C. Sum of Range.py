def sum_a(a, b):
    sum_all = b * (b + 1) // 2 - a * (a + 1) // 2 + a
    return sum_all


def sum_even(a, b):
    if a % 2 == 0:
        sum_all_even = b // 2 * (b // 2 + 1) - a // 2 * (a // 2 + 1) + a
    else:
        sum_all_even = b // 2 * (b // 2 + 1) - a // 2 * (a // 2 + 1)
    return sum_all_even


a, b = map(int, input().split())
mi = min(a, b)
ma = max(a, b)
print(sum_a(mi, ma))
print(sum_even(mi, ma))
print(sum_a(mi, ma) - sum_even(mi, ma))
