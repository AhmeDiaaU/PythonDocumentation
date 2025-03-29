x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
 
x_coords = [x1, x2, x3, x4]
y_coords = [y1, y2, y3, y4]
x_min = min(x_coords)
x_max = max(x_coords)
y_min = min(y_coords)
y_max = max(y_coords)
 
n = int(input())
 
for _ in range(n):
    xi, yi = map(int, input().split())
    if x_min <= xi <= x_max and y_min <= yi <= y_max:
        print("YES")
    else:
        print("NO")
