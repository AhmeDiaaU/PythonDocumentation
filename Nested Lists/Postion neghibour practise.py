# find mountains

def get_matrix():
    rows = int(input())
    assert rows > 0
    lst_of_lsts = [0] * rows
    for row in range(rows):
        lst_of_lsts[row] = list(map(int, input().split()))
    return rows, len(lst_of_lsts[0]), lst_of_lsts


def is_with_in_grid(r, c, row, cols):
    return 0 <= r < row and 0 <= c < cols


def get_neighbours(i, j, row, col, cnt=8):
    di = [1, 0, -1, 0, -1, 1, -1, 1]
    dj = [0, 1, 0, -1, -1, 1, 1, -1]

    return [(r, c) for d in range(cnt) if is_with_in_grid(r := i + di[d], c := i + dj[d], row, col)]


if __name__ == "__main__":
    rows, cols, matrix = get_matrix()
    if rows == cols == 1:
        print(0, 0)
        exit(0)
    for r in range(rows):
        for c in range(cols):
            postions = get_neighbours(r, c, rows, cols)
            mx = max(([matrix[i][j] for i, j in postions]))
            if matrix[r][c] > mx:
                print(r, c)
