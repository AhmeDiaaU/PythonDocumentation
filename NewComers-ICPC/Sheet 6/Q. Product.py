def product_modularity(l,r,m):
    product = 1 
    for num in range(l , r+1):
        product *= num 
    result = product % m 
    return result
L,R,M = map(int,input().split())
print(product_modularity(L,R,M))