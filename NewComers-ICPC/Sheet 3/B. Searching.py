n = int(input())
lst = list(map(int, input().split()))
x = int(input())
index = 0
flag = False
for i in range(n):
    if lst[i] == x:
        print(index)
        flag = True
        break
    index += 1
if not flag:
    print(-1)
