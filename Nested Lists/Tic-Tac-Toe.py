def printboard(board):
    for row in board:
        print('|', end=' ')
        for cell in row:
            print(cell, end=' | ')
        print()
        print('-' * (len(board) * 4 + 1)) 

def move(board, row , col , sympol):
    n = len(board)
    if with_in_grid(row , col , n ) and board[row][col]== ' '  :
        board[row][col] = sympol
        return True
    else :
        print("Invalid move")
        return False
def chcek_winner(board):
    n = len(board)
    start_dir = [(r , 0 , 0 , 1 )for r in range(n)]
    start_dir.extend([(0 , c , 1, 0) for c in range(n)])
    start_dir.append((0 , 0 , 1 , 1))
    start_dir.append((0 , n-1 , 1 , -1))
    for row , col , dir_row , dir_col in start_dir:
        player = board[row][col]
        if player == ' ':
            continue
        is_winner = True
        for i in range(n):
            if board[row + i * dir_row][col + i * dir_col] != player:
                is_winner = False
                break
        if is_winner:
            return player
    return None
def createMatrix():
    row = int(int(input("Enter the number of rows: ")))
    assert row > 0 
    lst_Of_lst = [[' ']*row for _ in range(row)] 
    return row , lst_Of_lst[0] , lst_Of_lst
def with_in_grid(r , c , n ):
    return 0 <= r < n and 0 <= c < n
if __name__ == '__main__':
    row , col , matrix = createMatrix()
    symbol = ['X' , 'O']
    steps , turn = 0 , 0
    while True :
        if steps == row * col:
            print("Draw")
            break
        printboard(matrix)
        row , col = map(int , input(f"Enter row and column player {symbol[turn]}: ").split())
        row , col = row - 1 , col - 1
        if(move(matrix , row , col , symbol[turn])):         
         if(winner := chcek_winner(matrix)):
            printboard(matrix)
            print(f"Player {winner} wins")
            break
        turn = 1 - turn
        steps+=1