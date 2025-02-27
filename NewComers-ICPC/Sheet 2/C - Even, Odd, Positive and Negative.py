n = int(input())
e = 0
o = 0
negative = 0
p = 0
lst = list(map(int, input().split()))
for i in range(0, n):
    if lst[i] % 2 == 0:
        e += 1
    else:
        o += 1
    if lst[i] < 0:
        negative = negative + 1
    elif lst[i] > 0:
        p = p + 1

print(f"Even: {e}")
print(f"Odd: {o}")
print(f"Positive: {p}")
print(f"Negative: {negative}")