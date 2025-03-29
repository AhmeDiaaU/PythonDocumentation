points = [list(map(int, input().split())) for _ in range(2)]
x1, y1, x2, y2 = points[0]
a1, b1, a2, b2 = points[1]

def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0: 
        return None
    return (y2 - y1) / (x2 - x1)

slope1 = calculate_slope(x1, y1, x2, y2)
slope2 = calculate_slope(a1, b1, a2, b2)

if slope1 == slope2:
    print("YES")
else:
    print("NO")