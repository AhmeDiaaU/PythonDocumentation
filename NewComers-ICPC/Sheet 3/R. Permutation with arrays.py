n = int(input())
lst = list(map(int, input().split()))
arr = list(map(int, input().split()))
if n == len(lst) and n == len(arr):
    if sorted(lst) == sorted(arr):
        print("yes")
    else :
        print("no")