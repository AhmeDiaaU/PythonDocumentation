n = int(input())
lst = list(map(int,input().split()))
index = 0
for i in range(n):
    if lst[i] <= 10:
        print(f"A[{index}] = {lst[i]}")
    index += 1
