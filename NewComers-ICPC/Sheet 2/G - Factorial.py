def fact(n) :
    s = 1
    for i in range(1 , n +1 ,1) :
        s = s *i
    return s


s = int(input())
for i in range(1, s + 1):
    z = int(input())
    print(fact(z))