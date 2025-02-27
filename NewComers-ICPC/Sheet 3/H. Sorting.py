n = int(input())
lst = map(int, input().split())
lst = list(lst)
for i in range(n):
    for j in range (i+1 , n) :# compare every element to the next to it until it sort all the list
        if lst[i] >=lst[j] :
            lst[i],lst[j] = lst[j],lst[i]
for i in lst:
    print(i, end=" ")
