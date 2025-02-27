
def decimaltobinary (num) :
    binary = 0
    while num > 0 :
        reminder = num %2
        if reminder == 1:
            binary = (binary * 10) + reminder
        num = num // 2
    return binary


t = int(input())
for i in range(t):
    x = 0
    sum = 0
    n = int(input())
    db = decimaltobinary(n)
    while db > 0:
        reminder = db % 10
        sum = sum + reminder * (pow(2, x))
        x += 1
        db = db // 10
    print(sum)