n = float(input())


def get_decimal_part(n):
    if n < 0:
        n = n * -1
    result = n - int(n)
    return result


if n % 1 != 0:
    a = get_decimal_part(n)
    print(f"float {int(n)} {a}")
elif n % 1 == 0:
    n = int(n)
    print(f"int {n}")