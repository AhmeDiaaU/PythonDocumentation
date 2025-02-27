def SDigits(y):
    sum = 0
    while y > 0:
        reminder = y % 10
        sum += reminder
        y = y // 10
    return sum


n, a, b = map(int, input().split())
s = 0
sr = 0
for i in range(1, n + 1):
    x = i
    digit_sum = SDigits(x)
    if a <= digit_sum <= b:
        s += x
print(s)