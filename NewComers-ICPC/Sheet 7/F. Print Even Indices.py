def indices(lst : list):
    n = len(lst) - 1
    if n < 0:
        return
    if n % 2 == 0:
 
        print(lst[n] ,  end = " " )
    indices(lst[:n])

l = int(input())
lst = list(map(int,input().split()))
if len(lst) == l:
    indices(lst)
    