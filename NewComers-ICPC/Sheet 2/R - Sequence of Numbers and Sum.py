flag = True
while flag :
    sum = 0
    n ,m = map(int ,input().split())
    if n <= 0 or m <= 0 :
        flag = False
    else :
        for i in range(min(m ,n), max(m ,n ) +1):
            sum +=i
            print(i ,end=" ")
        print(f"sum ={sum}")