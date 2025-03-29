import math
 
r, s = map(int, input().split())
 
if s <= r * math.sqrt(2):
    print("Circle")
elif s >= 2 * r:
    print("Square")
else:
    print("Complex")