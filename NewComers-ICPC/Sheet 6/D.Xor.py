def xor(a, b, q):
    if q == 1 :
        return a
    elif q == 2 :
        return  b
    else:
        return a ^ b


a, b, q = map(int, input().split())
print(xor(a,b,q))