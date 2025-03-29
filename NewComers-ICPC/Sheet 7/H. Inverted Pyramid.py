def pyramid(h):
    if h==1: return ["*"]
    return ["*"*(2*h-1)]+[" "+p+" " for p in pyramid(h-1)]
n = int(input())
lst = pyramid(n)
for s in range(len(lst)):
    lst[s] = lst[s].rstrip() 
print(*lst, sep="\n")