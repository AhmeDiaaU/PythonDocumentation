n = int(input())
lst = list(map(int, input().split()))
flag = False
s = 0
x = 0
arr = []
if n == len(lst):
    while not flag:
        for i in lst :
            if i%2 !=0 :
                flag = True
                break
            else:
                lst[s] = lst[s]//2
                s+=1
                if s == n:
                    s =0
                    x+=1
    print(x)
