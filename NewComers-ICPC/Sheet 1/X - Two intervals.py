n1, n2, n3, n4 = map(int, input().split())
start = 0
end = 0
if n1 > n3 and n1 > n4 or n2 < n3 and n2 < n4:
    print(-1)
else:
    if n1 > n3:
        start = n1
    else:
        start = n3
    if n2 > n4:
        end = n4
    else:
        end = n2
    print(f"{start} {end}")