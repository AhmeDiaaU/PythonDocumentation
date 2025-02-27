n = int(input())
while n > 0:
    n = n - 1
    a = int(input())
    if a == 0:
        print(0, end=" ")
    while a > 0:
        reminder = a % 10
        a = a // 10
        print(reminder, end=" ")
    print()