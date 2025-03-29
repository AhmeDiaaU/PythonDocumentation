# لو مفيش body يبقي = 0
n, m, k = map(int, input().split())
if n == 0:
    print(0)
else:
    print(min(k , n , (n+m)//2))