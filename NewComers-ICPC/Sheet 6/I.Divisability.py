def S(N):
    return N * (N + 1) // 2


A, B, x = map(int, input().split())
l = max(A, B)
s = min(A, B)
ans = S(l // x) * x
ans -= S((s - 1) // x) * x
print(ans)
