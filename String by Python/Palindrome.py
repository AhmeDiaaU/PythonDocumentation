x = input()
reversed_string = []
for i in range(len(x)-1 ,-1 ,-1):
    reversed_string.append(x[i])
if x == "".join(reversed_string) :
    print("Yes")
else :
    print("No")