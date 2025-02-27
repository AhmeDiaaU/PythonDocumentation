n = int(input())
lst = list(map(int,input().split()))
l = len(lst)
s = 0
if l != n:
    exit(1)
else :
    for i in lst:
        s +=i
    if s < 0 :
        print(abs(s))
    else :
        print(s)

