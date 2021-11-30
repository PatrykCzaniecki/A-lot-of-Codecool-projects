import random 

def init_board():
    board = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
    return board 

def get_move(board, player):
    row, col = 3, 3
    possible_moves = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
    move = input("WHERE YOU WANT TO SHOOT?: ") 
    if move.lower() == "quit":
        close_game()
    elif move.lower() not in possible_moves:
        print("TRY TO HIT THE BOARD!!!")
        return get_move(board,player)
    if "a" in move.lower():
        row = 0
    elif "b" in move.lower():
        row = 1
    elif "c" in move.lower():
        row = 2
    if "1" in move:
        col = 0
    elif "2" in move:
        col = 1
    elif "3" in move:
        col = 2
    if board[row][col] != 0:
        print("THIS SPOT IS TAKEN. TRY TO HIT ANOTHER ONE!!!")
        return get_move(board, player)
    return row, col

def get_ai_move(board, player):
    corners = [board[0][0], board[0][2], board[2][0], board[2][2]]
    winning_cases = [[board[0][0], board[0][1], board[0][2]], [board[1][0], board[1][1], board[1][2]],
                     [board[2][0], board[2][1], board[2][2]]]
    winning_cases2 = [[board[0][0], board[1][0], board[2][0]], [board[0][1], board[1][1], board[2][1]],
                      [board[0][2], board[1][2], board[2][2]]]
    winning_cases3 = [board[0][0], board[1][1], board[2][2]]
    winning_cases4 = [board[0][2], board[1][1], board[2][0]]
    for i in winning_cases:
        if sum(i) == 4 and 0 in i:
            row = board.index(i)
            col = i.index(0)
            return(row, col)
    for i in winning_cases2:
        if sum(i) == 4 and 0 in i:
            col = winning_cases2.index(i)
            row = i.index(0)
            return(row, col)
    if sum(winning_cases3) == 4 and 0 in winning_cases3:
        row = winning_cases3.index(0)
        col = winning_cases3.index(0)
        return(row, col)
    if sum(winning_cases4) == 4 and 0 in winning_cases4:
        if winning_cases4.index(0) == 1:
            row, col = 1, 1
            return (row, col)
        elif winning_cases4.index(0) == 0:
            row, col = 0, 2
            return(row, col)
        elif winning_cases4.index(0) == 2:
            row, col = 2, 0
            return(row, col)
    for i in winning_cases:
        if sum(i) == 2 and 1 in i:
            row = board.index(i)
            col = i.index(0)
            return(row, col)
    for i in winning_cases2:
        if sum(i) == 2 and 1 in i:
            col = winning_cases2.index(i)
            row = i.index(0)
            return(row, col)
    if sum(winning_cases3) == 2 and 1 in winning_cases3:
        row = winning_cases3.index(0)
        col = winning_cases3.index(0)
        return(row, col)
    if sum(winning_cases4) == 2 and 1 in winning_cases4:
        if winning_cases4.index(0) == 1:
            row, col = 1, 1
            return (row, col)
        elif winning_cases4.index(0) == 0:
            row, col = 0, 2
            return(row, col)
        elif winning_cases4.index(0) == 2:
            row, col = 2, 0
            return(row, col)
    if board[1][1] == 0:
        row, col = 1, 1
        return(row, col)
    if 0 in corners:
        row = random.randrange(0, 3, 2)
        col = random.randrange(0, 3, 2)
        while board[row][col] != 0:
            row = random.randrange(0, 3, 2)
            col = random.randrange(0, 3, 2)
        return(row, col)
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    while board[row][col] != 0:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
    return (row, col)

def mark(board, player, row, col):
    try:
        if board[row][col] == 0:
            board[row][col] = player
    except IndexError:
        return

def has_won(board, player):
    if player == board[0][0] == board[0][1] == board[0][2]: 
        return True
    elif player == board[1][0] == board[1][1] == board[1][2]: 
        return True
    elif player == board[2][0] == board[2][1] == board[2][2]: 
        return True
    elif player == board[0][0] == board[1][0] == board[2][0]: 
        return True
    elif player == board[0][1] == board[1][1] == board[2][1]:
        return True
    elif player == board[0][2] == board[1][2] == board[2][2]: 
        return True
    elif player == board[0][0] == board[1][1] == board[2][2]: 
        return True
    elif player == board[0][2] == board[1][1] == board[2][0]: 
        return True        

def is_full(board):
    if 0 in board[0]:
        return False
    elif 0 in board[1]:
        return False
    elif 0 in board[2]:
        return False
    else:
        return True

def print_board(board):
    second_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for x in range(len(board)):
        for i in range(len(board[0])):
            if board[x][i] == 0:
                second_board[x][i] = "."
            if board[x][i] == 1:
                second_board[x][i] = "X"
            if board[x][i] == 2:
                second_board[x][i] = "O"
    print('''
               1   2   3
            A  {} | {} | {}
              ---+---+---
            B  {} | {} | {}
              ---+---+---
            C  {} | {} | {}
        '''.format(second_board[0][0], second_board[0][1], second_board[0][2], second_board[1][0], second_board[1][1], second_board[1][2],
                   second_board[2][0], second_board[2][1], second_board[2][2]))   

def print_result(winner):
    if winner == 0:
        print("IT'S A DEAD-HEAT! DRAW! TRY AGAIN! \n")
    if winner == 1:
        print("X WON!!! PRAISE THE WINNER!!! \n")
    if winner == 2:
        print("O WON!!! SPLENDOR AND GLORY!!! \n")

def tictactoe_game(mode = "player-player"):
    if mode == "player-player":
        board = init_board()
        current_player = 1 
        while not has_won(board, 1) and not has_won(board, 2) and not is_full(board): 
            print_board(board)
            row, col = get_move(board, current_player) 
            mark(board, current_player, row, col)
            current_player = 2 if current_player == 1 else 1            
        if has_won(board, 1):
            winner = 1
        elif has_won(board, 2):
            winner = 2
        else:
            winner = 0
        print_result(winner)

    elif mode == "player-python":
        board = init_board()
        while not has_won(board, 1) and not has_won(board, 2) and not is_full(board):
            print_board(board)
            row, col = get_move(board, 1)
            mark(board, 1, row, col)
            print_board(board)
            if not has_won(board, 1) and not is_full(board):
                row, col = get_ai_move(board, 2)
                mark(board, 2, row, col)
                print_board(board)
        if has_won(board, 1):
            winner = 1
        elif has_won(board, 2):
            winner = 2
        else:
            winner = 0
        print_result(winner)
        
def main_menu():
    while True:
        start = input(" 1. PLAYER VS PLAYER\n 2. PLAYER VS PYTHON\n 3. SURRENDER AND QUIT\n CHOOSE WISELY (TYPE 1 or 2 or 3) ")
        if start == str(1):
            tictactoe_game(mode = "player-player")
        elif start == str(2):
            tictactoe_game(mode = "player-python")
        elif start == str(3):
            close_game()
        else:
            print("1 or 2 or 3 ITS NOT THAT HARD!!!")

def close_game():
    while True:
        close_game = input("DO YOU WANT TO CLOSE GAME? (yes/no) ") 
        if close_game == "no":
            main_menu() 
        elif close_game =="yes":    
            break

def quit():  
    quit = input("GREAT GAME! DO YOU WANT TO PLAY AGAIN? (yes/no): ")
    if quit == "yes":
        main_menu()
    elif quit == "no":
        close_game() 

if __name__ == "__main__":
    main_menu()