a , s , b ,d , e = input().split()
a= int(a)
b = int(b)
e = int (e)
if e == a+b and s =='+' and d=='=':
    print("Yes")
elif e ==a*b and s=='*' and d=='=':
        print("Yes")
elif e == a-b and s == '-' and d =='=' :
      print("Yes")
elif e != a+b and s =='+' and d=='=':
    print(a+b)
elif e !=a*b and s=='*' and d=='=':
        print(a*b)
elif e != a-b and s == '-' and d =='=' :
      print(a-b)