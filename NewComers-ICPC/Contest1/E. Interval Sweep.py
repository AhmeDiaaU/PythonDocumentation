a, b = map(int, input().split())
lst = [num for num in range(0 , a+b+1)]
even_counter = 0
odd_counter = 0
if a == b == 0 :
    print("NO")
    exit()
for num in lst:
    if num % 2 == 0:
        even_counter += 1
    else:
        odd_counter += 1
if even_counter >= b and odd_counter >= a:
    print("YES")
else:
    print("NO")