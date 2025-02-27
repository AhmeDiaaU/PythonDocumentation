r , c = map(int,input().split())
n = []
for i in range(r):
    v = list(map(int,input().split()))
    if len(v) == c:
        if len(n) <= r:
          n.append(v)
        else :
            break
x = int(input())
for i in n:
    if x in i :
        print("will not take number")
    else :
        print("will take number")
