no1, no2 = map(int, input().split())
lst = list(map(int, input().split()))
lst = sorted(lst)
if len(lst) == no1:
    for i in range(no2):
        q = int(input())
        l, r = 0, len(lst)
        while r - l > 1:
            mid = l + (r - l) // 2
            if lst[mid] > q:
                r = mid
            else:
                l = mid
        print("found" if lst[l] == q else "not found")
