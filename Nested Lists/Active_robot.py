if __name__ == '__main__':
    rows, cols, *commands = input().split()
    rows, cols = int(rows), int(cols)
    Row_direction = [-1, 0, 1, 0]
    cols_direction = [0, 1, 0, -1]
    r, c = 0, 0
    while commands:
        dir, steps, *commands = commands
        dir = ['up' , 'right' , 'down' , 'left'].index(dir)
        steps = int(steps)
        r = (r + Row_direction[dir]*steps)%rows
        c = (c + cols_direction[dir] * steps) % cols
        print(r , c)
