lst_length = int(input())
lst = list(map(int, input().split()))
if len(lst) == lst_length :
    if sum(lst) % len(lst) ==0 :
        print("YES")
    else:
        print("NO")