import math

# Initialize the board
board = [" " for _ in range(9)]

def print_board():
    """Display the current board"""
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

def check_winner(b, player):
    win_cond = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for cond in win_cond:
        if b[cond[0]] == b[cond[1]] == b[cond[2]] == player:
            return True
    return False

def check_draw(b):
    return " " not in b

def minimax(b, depth, is_maximizing):
    """Minimax algorithm to evaluate best move"""
    if check_winner(b, "O"):  # AI wins
        return 1
    if check_winner(b, "X"):  # Player wins
        return -1
    if check_draw(b):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth + 1, False)
                b[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth + 1, True)
                b[i] = " "
                best_score = min(score, best_score)
        return best_score

def ai_move():
    """AI chooses the best move using Minimax"""
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"
    print(f"\n🤖 AI chose position {move + 1}")
    return move

def google_colab_tictactoe():
    """Main game loop"""
    print("🎮 Welcome to Tic Tac Toe AI (Minimax)")
    print("You are X | AI is O")
    print("Use positions 1–9 as shown below:")
    print("1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9\n")
    print_board()

    while True:
        # Player Move
        move = input("\nEnter your move (1-9): ").strip()
        if not move.isdigit() or int(move) not in range(1,10):
            print("❌ Invalid input. Try again.")
            continue
        move = int(move) - 1
        if board[move] != " ":
            print("❌ That spot is taken. Try again.")
            continue

        board[move] = "X"
        print_board()

        if check_winner(board, "X"):
            print("\n🎉 You win!")
            break
        if check_draw(board):
            print("\nIt's a draw!")
            break

        # AI Move
        ai_move()
        print_board()

        if check_winner(board, "O"):
            print("\n🤖 AI wins!")
            break
        if check_draw(board):
            print("\nIt's a draw!")
            break

# Run the game
google_colab_tictactoe()