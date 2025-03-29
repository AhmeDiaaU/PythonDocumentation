import math

x1, y1, x2, y2 = map(int, input().split())

x3, y3, x4, y4 = map(int, input().split())

center_a_x = (x1 + x2) / 2
center_a_y = (y1 + y2) / 2
center_b_x = (x3 + x4) / 2
center_b_y = (y3 + y4) / 2

radius_a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) / 2
radius_b = math.sqrt((x4 - x3)**2 + (y4 - y3)**2) / 2

distance = math.sqrt((center_a_x - center_b_x)**2 + (center_a_y - center_b_y)**2)

if distance <= radius_a + radius_b:
    print("YES")
else:
    print("NO")