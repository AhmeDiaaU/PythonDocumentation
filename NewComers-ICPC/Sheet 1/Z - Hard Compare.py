import math
n1 , n2 , n3 , n4 = map(int ,input().split())
x =math.log(n1) * n2
y = math.log(n3) * n4
if x > y:
    print("YES")
else:
    print("NO")