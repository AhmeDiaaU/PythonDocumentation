n, m = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(input()))

x, y = map(int, input().split())

x -= 1
y -= 1

directions = [
    (-1, 0), (1, 0), (0, -1), (0, 1),
    (-1, -1), (-1, 1), (1, -1), (1, 1)
]
all_neighbors_x = True

for dx, dy in directions:
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < m:
        if grid[nx][ny] != 'x':
            all_neighbors_x = False
            break
if all_neighbors_x:
    print("yes")
else:
    print("no")
