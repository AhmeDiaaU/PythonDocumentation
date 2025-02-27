x, s, y = input().split()
x = int(x)
y = int(y)
if x > y and s == '>':
    print("Right")
elif x < y and s == '<':
    print("Right")
elif x == y and s == '=':
    print("Right")
else:
    print("Wrong")