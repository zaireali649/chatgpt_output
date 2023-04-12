def print_board(board):
    for row in board:
        print("| " + " | ".join(row) + " |")

def check_win(board, player, n):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # Check columns
    for col in range(n):
        if all([board[row][col] == player for row in range(n)]):
            return True

    # Check diagonals
    print([board[i][i] for i in range(n)])
    print([board[i][n-i-1] for i in range(n)])
    if all([board[i][i] == player for i in range(n)]) or all([board[i][n-i-1] == player for i in range(n)]):
        return True

    return False



def get_move(board, m, n):
    while True:
        try:
            row = int(input("Enter row number (0 - {}): ".format(m-1)))
            col = int(input("Enter column number (0 - {}): ".format(n-1)))
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != ' ':
                raise ValueError("Invalid move. Try again.")
            return row, col
        except ValueError as e:
            print(e)



def tic_tac_toe():
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    win_length = int(input("Enter win length: "))
    board = [[' ' for x in range(n)] for y in range(m)]
    player = 'X'
    while True:
        print_board(board)
        row, col = get_move(board, m, n)
        board[row][col] = player
        if check_win(board, player, win_length):
            print_board(board)
            print(player + " wins!")
            return
        if all(' ' not in sublist for sublist in board):
            print_board(board)
            print("Tie!")
            return
        player = 'O' if player == 'X' else 'X'


if __name__ == '__main__':
    tic_tac_toe()
