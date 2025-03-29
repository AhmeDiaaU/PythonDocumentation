def arthemtic_operation(a , b , c, d):
    if a+b-c == d or a+b*c ==d or a-b+c == d or a-b*c == d or a*b-c == d or a * b + c == d :
        return True
    return False
a , b , c , d = map(int , input().split())
if arthemtic_operation(a , b , c , d):
    print("YES")
else:
    print("NO")