n, q = map(int, input().split())
lst = list(map(int, input().split()))
p = []
p = [0] * (n + 1)
p[1] = lst[0]
if len(lst) == n:
    for index in range(1, n + 1):
        p[index] = p[index - 1] + lst[index - 1]
    while q:
        x, y = map(int, input().split())
        s = 0
        x -= 1
        y -= 1
        q -= 1
        s = p[y + 1] - p[x]
        print(s)
