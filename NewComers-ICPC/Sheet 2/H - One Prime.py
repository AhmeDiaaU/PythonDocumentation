n = int(input())
c = True
for i in range(2, n):
    if n % i == 0:
        c = False
if c == False:
    print("NO")
else:
    print("YES")