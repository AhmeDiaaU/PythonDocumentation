bds =int(input())
y = 0
m = 0
d = 0
if (bds >= 365):
    n = bds // 365
    for i in range(0, n):
        bds = bds - 365
        y = y + 1

if (bds > 30 or bds == 30 and bds < 365):
    n = bds // 30
    for i in range(0, n):
        bds = bds - 30
        m = m + 1
if (bds > 0 and bds < 30):
    d = bds

print(f"{y} years")
print(f"{m} months")
print(f"{d} days")