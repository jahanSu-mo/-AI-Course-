import math

# Initial empty board
board = [" " for _ in range(9)]

def print_board():
    for i in range(3):
        print(" " + " | ".join(board[i*3:i*3+3]))
        if i < 2:
            print("---+---+---")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_draw(board):
    return all(space != " " for space in board)

def minimax(board, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("❗ That spot is taken.")
        except (ValueError, IndexError):
            print("❗ Invalid input. Please enter a number 1-9.")

def play_game():
    print("\n Welcome to Tic Tac Toe!")
    print("You are X, AI is O. You go first.")
    print_board()

    while True:
        player_move()
        print_board()
        if check_winner(board, "X"):
            print(" You win!")
            break
        if is_draw(board):
            print(" It's a draw!")
            break

        print("AI is thinking...")
        ai_move()
        print_board()
        if check_winner(board, "O"):
            print(" AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

play_game()





# import math  # Import math to use infinity for score comparison

# # === Initialize the empty board ===
# board = [" " for _ in range(9)]  # A 1D list representing 3x3 grid with empty spaces

# # === Function to print the current board ===
# def print_board():
#     for i in range(3):
#         print(" " + " | ".join(board[i*3:i*3+3]))  # Print each row
#         if i < 2:
#             print("---+---+---")  # Divider between rows

# # === Check if a player has won ===
# def check_winner(board, player):
#     win_conditions = [
#         [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
#         [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
#         [0, 4, 8], [2, 4, 6]              # Diagonals
#     ]
#     for condition in win_conditions:
#         if all(board[i] == player for i in condition):  # Check if all positions match the player
#             return True
#     return False  # No win condition met

# # === Check if the board is full and it's a draw ===
# def is_draw(board):
#     return all(space != " " for space in board)  # Return True if no empty spaces

# # === Minimax algorithm to evaluate best move ===
# def minimax(board, is_maximizing):
#     if check_winner(board, "O"):  # If AI wins
#         return 1
#     if check_winner(board, "X"):  # If player wins
#         return -1
#     if is_draw(board):            # If it's a draw
#         return 0

#     if is_maximizing:
#         best_score = -math.inf  # Start with the lowest score
#         for i in range(9):  # Check all possible moves
#             if board[i] == " ":
#                 board[i] = "O"  # Try move for AI
#                 score = minimax(board, False)  # Recurse for player
#                 board[i] = " "  # Undo move
#                 best_score = max(score, best_score)  # Pick the highest score
#         return best_score
#     else:
#         best_score = math.inf  # Start with the highest score
#         for i in range(9):  # Check all possible moves
#             if board[i] == " ":
#                 board[i] = "X"  # Try move for player
#                 score = minimax(board, True)  # Recurse for AI
#                 board[i] = " "  # Undo move
#                 best_score = min(score, best_score)  # Pick the lowest score
#         return best_score

# # === AI picks the best move using minimax ===
# def ai_move():
#     best_score = -math.inf  # Start with worst score
#     move = -1
#     for i in range(9):  # Loop through all cells
#         if board[i] == " ":
#             board[i] = "O"  # Try move
#             score = minimax(board, False)  # Run minimax
#             board[i] = " "  # Undo move
#             if score > best_score:  # If score is better
#                 best_score = score
#                 move = i  # Save the move
#     board[move] = "O"  # Make the best move

# # === Player inputs a move ===
# def player_move():
#     while True:
#         try:
#             move = int(input("Enter your move (1-9): ")) - 1  # Input move index
#             if board[move] == " ":  # Check if cell is empty
#                 board[move] = "X"
#                 break
#             else:
#                 print("❗ That spot is taken.")  # Error for occupied cell
#         except (ValueError, IndexError):  # Handle invalid inputs
#             print("❗ Invalid input. Please enter a number 1-9.")

# # === Main game loop ===
# def play_game():
#     print("\n Welcome to Tic Tac Toe!")
#     print("You are X, AI is O. You go first.")
#     print_board()  # Show empty board

#     while True:
#         player_move()  # Human move
#         print_board()  # Print after human move
#         if check_winner(board, "X"):  # Check if player won
#             print(" You win!")
#             break
#         if is_draw(board):  # Check for draw
#             print(" It's a draw!")
#             break

#         print("AI is thinking...")
#         ai_move()  # AI makes move
#         print_board()  # Show updated board
#         if check_winner(board, "O"):  # Check if AI won
#             print(" AI wins!")
#             break
#         if is_draw(board):  # Check for draw
#             print("It's a draw!")
#             break

# # === Start the game ===
# play_game()
