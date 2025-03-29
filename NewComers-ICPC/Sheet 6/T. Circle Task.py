from decimal import Decimal

first_line = input().split()
X = Decimal(first_line[0])
Y = Decimal(first_line[1])
R = Decimal(first_line[2])
N = int(first_line[3])

R_squared = R ** 2  

for _ in range(N):
    xi_str, yi_str = input().split()
    xi = Decimal(xi_str)
    yi = Decimal(yi_str)
    dx = xi - X
    dy = yi - Y
    distance_squared = dx * dx + dy * dy  
    print("YES" if distance_squared <= R_squared else "NO")