def mean(array):
    s = 0
    for i in array:
        s += i
    s = s / len(array)
    return s


a = int(input())
lst = list(map(float, input().split()))
if len(lst) == a:
    print(mean(lst))
