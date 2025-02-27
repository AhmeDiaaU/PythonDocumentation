s = input()
n = int(input())
a = list(map(int, input().split()))
for num in a:
    for i in range(0, num):
        print(s, end="")
    print()
