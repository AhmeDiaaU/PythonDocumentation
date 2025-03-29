t = int(input())
 
for case in range(1, t + 1):
    n = int(input())
    x_min = float('-inf')
    y_min = float('-inf')
    x_max = float('inf')
    y_max = float('inf')
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        x_min = max(x_min, x1)
        y_min = max(y_min, y1)
        x_max = min(x_max, x2)
        y_max = min(y_max, y2)
    width = x_max - x_min
    height = y_max - y_min
    if width <= 0 or height <= 0:
        area = 0
    else:
        area = width * height
    print(f"Case #{case}: {area}")