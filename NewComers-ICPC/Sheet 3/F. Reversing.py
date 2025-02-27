n = int(input())
lst = list(map(int,input().split()))
lst1=[]
while n-1 >= 0 :
    n = n - 1
    lst1.append(lst[n])
for i in lst1 :
    print(i,end=" ")