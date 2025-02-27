n = int(input())
r = n
reminder = 0
reversed_number = 0
while n > 0 :
    reminder = n % 10
    reversed_number = (reversed_number *10) + reminder
    n = n // 10
    if reminder == 0 :
        continue
if reversed_number == r :
    print(reversed_number)
    print("YES")
else :
    print(reversed_number)
    print("NO")