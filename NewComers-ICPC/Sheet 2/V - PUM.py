n = int(input())
a = 1
b = 4
for i in range(n):
    for j in range(a, b):
        print(j, end=" ")
    print("PUM")
    a += 4
    b += 4
