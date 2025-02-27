n, m = map(int, input().split())
v = False
for i in range(n, m + 1):
    flag = False
    a = i
    while a > 0:
        reminder = a % 10
        if reminder != 4 and reminder != 7:
            flag = True

        a = a // 10
    if flag == False:
        print(i, end=" ")
        v = True
if not v:
    print(-1)