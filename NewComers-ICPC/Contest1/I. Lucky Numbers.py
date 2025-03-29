n = input()
a = int(n[0])
b = int(n[1])
if (b !=0 and a%b ==0)  or (a!=0 and b%a==0):
    print("YES")
else :
    print("NO")