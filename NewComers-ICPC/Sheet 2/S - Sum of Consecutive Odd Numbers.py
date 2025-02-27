n = int(input())
while n:
    n -= 1
    sum = 0
    x, y = map(int, input().split())
    for i in range(min(x, y) + 1, max(x, y)):
        if i % 2 != 0:
            sum += i
    print(sum)