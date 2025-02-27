a, b = map(int, input().split())
s = input()
if s[a] == '-' and len(s) == a + b + 1 :
    for i in s :
        if i == a :continue
        elif '0' < i < '10':
            continue
    if len(s[:a]) == a and len(s[a+1:])==b:
        print("Yes")
    else :
        print("No")

else :
    print("No")