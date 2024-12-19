
board = [
    ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],  # Black back rank
    ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],  # Black pawns
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],  # Empty row
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],  # Empty row
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],  # Empty row
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],  # Empty row
    ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],  # White pawns
    ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"]   # White back rank
]


def print_board(board):
    for row in board:
        print(" ".join(row))

def parse_move(move):
    start_col = ord(move[0]) - ord('a')  
    start_row = 8 - int(move[1])         
    end_col = ord(move[2]) - ord('a')    
    end_row = 8 - int(move[3])           
    return (start_row, start_col, end_row, end_col)

def move_piece(board, start_row, start_col, end_row, end_col):
    piece = board[start_row][start_col]
    
    if piece == "  ":
        print("Invalid move: No piece at the starting position.")
        return False

    board[start_row][start_col] = "  "
    board[end_row][end_col] = piece
    return True

def is_valid_pawn_move(board, start_row, start_col, end_row, end_col, piece):
    direction = -1 if piece[0] == "W" else 1  
    start_row_offset = 6 if piece[0] == "W" else 1 

    if start_col == end_col and board[end_row][end_col] == "  ":
        if (end_row == start_row + direction):
            return True
        elif (start_row == start_row_offset and end_row == start_row + 2 * direction):
            if board[start_row + direction][start_col] == "  ":
                return True

    # Pawn capturing move
    if abs(start_col - end_col) == 1 and end_row == start_row + direction and board[end_row][end_col] != "  ":
        if (piece[0] == "W" and board[end_row][end_col][0] == "B") or (piece[0] == "B" and board[end_row][end_col][0] == "W"):
            return True

    return False

def is_valid_move(board, start_row, start_col, end_row, end_col):
    piece = board[start_row][start_col]
    if piece[1] == "P":  # Pawn movement
        return is_valid_pawn_move(board, start_row, start_col, end_row, end_col, piece)

    return True

def game():
    global turn
    turn = "White"
    while True:
        print(f"\n{turn}'s turn:")
        print_board(board)

        move = input("Enter your move (e.g., 'e2e4'): ")
        if len(move) != 4:
            print("Invalid move format. Try again.")
            continue

        try:
            start_row, start_col, end_row, end_col = parse_move(move)
        except IndexError:
            print("Invalid move. Try again.")
            continue

        piece = board[start_row][start_col]
        if piece == "  ":
            print("No piece at that position. Try again.")
            continue

        if (turn == "White" and piece[0] == "B") or (turn == "Black" and piece[0] == "W"):
            print("You cannot move the opponent's pieces. Try again.")
            continue

        
        if is_valid_move(board, start_row, start_col, end_row, end_col):
            move_piece(board, start_row, start_col, end_row, end_col)
            turn = "Black" if turn == "White" else "White"
        else:
            print("Invalid move for this piece. Try again.")


game()
