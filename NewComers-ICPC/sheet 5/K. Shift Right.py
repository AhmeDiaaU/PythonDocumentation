from _collections import deque


def shift(lst: list, a):
    x = deque(lst)
    x.rotate(a)
    return list(x)


n, x = map(int, input().split())
arr = list(map(int, input().split()))
if len(arr) == n:
    print(*shift(arr, x))
