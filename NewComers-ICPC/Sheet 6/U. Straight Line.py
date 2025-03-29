def read_points():
    return [list(map(int , input().split())) for _ in range(3)]

points = read_points()
(x1,y1) , (x2,y2) , (x3,y3) = points
cross_product = (x2 - x1) *(y3-y1) - (y2-y1)*(x3-x1)
print("YES" if cross_product == 0 else "NO")