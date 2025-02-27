def switch_zero(lst: list, n: int):
    count = 0
    for i in range(n):
        if lst[i] != 0:
            lst[count] = lst[i]
            count += 1
    while count < n:
        lst[count] = 0
        count += 1


n = int(input())
lst = list(map(int, input().split()))
if len(lst) == n:
    switch_zero(lst, len(lst))
    print(*lst)
