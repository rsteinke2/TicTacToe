board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'
game_over = False

def print_board():
    for row in board:
        print("    | ".join(row))
        print("-" * 18)

def make_move(player):
    print(f"PLAYER {1 if player == 'X' else 2} TURN:")
    print(
        f"Which location do you want to place the {player}? (1,1 - 1,2 - 1,3 - 2,1 - 2,2 - 2,3 - 3,"
        f"1 - 3,2 - 3,3)")
    move = input("Enter your move: ").split(',')
    row = (int(move[0].strip()))-1
    col = (int(move[1].strip()))-1
    if board[row][col] == ' ':
        board[row][col] = player
    else:
        print("This position is already taken! Please try again!")
        make_move(player)
def check_result():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    # Check for a tie
    for row in board:
        if ' ' in row:
            return None
    return 'Tie'

print("Welcome to Tic Tac Toe Game!")
print(f"PLAYER 1 = X\nPLAYER 2 = O")
print_board()

while not game_over:
    make_move(current_player)
    print_board()
    result = check_result()

    if result:
        if result == 'Tie':
            print("It's a tie!")
        else:
            print(f"Player {1 if result == 'X' else 2} wins!")
        game_over = True
    else:
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'
