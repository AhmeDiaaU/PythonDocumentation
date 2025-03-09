def m_and_m():
    a , b , k = map(int , input().split())
    if a % k ==0 and b % k ==0 :
        return "Both"
    elif a % k == 0 and b %k !=0 :
        return "Memo"
    elif a % k != 0 and b %k ==0 :
        return "Momo"
    if a % k !=0 and b % k !=0 :
        return "No One"

print(m_and_m())