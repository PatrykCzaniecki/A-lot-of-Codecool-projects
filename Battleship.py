import string
import copy

def init_board(size):
    board = [['0'], ['0'], ['0'], ['0'], ['0'],
             ['0'], ['0'], ['0'], ['0'], ['0']]
    del board[size:]
    for i in range(size):
        board[i] *= size
    player1_board = copy.deepcopy(board)
    player2_board = copy.deepcopy(board)
    player1_ship_board = copy.deepcopy(board)
    player2_ship_board = copy.deepcopy(board)
    return player1_board, player2_board, player1_ship_board, player2_ship_board

def print_board(board, size):
    col_mark = [" ", '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    row_mark = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    print_col = ' '.join(col_mark[:size + 1])
    print(print_col)
    for i in range(len(board)):
        string = ' '.join(board[i])
        print(f'{row_mark[i]} {string}')

def has_won(player_ship_board, player):
    win_list = []
    for i in range(len(player_ship_board)):
        for x in player_ship_board[i]:
            win_list += x
    if 'X' in win_list:
        pass
    else:
        print(f'Player {player} has won!')
        return True

def get_move(size):
    alphabet = list(string.ascii_letters)
    count = 0
    pos_count = 0
    row = -2
    col = -1
    reversed_pos = -1
    done = True
    while done == True:
        position_list = []
        position = input('Enter position to shoot: ')
        for i in position:
            position_list += i.upper()
        if get_move_input_check(position_list, size) == True:
            done = False
    for p in position_list:
        if position_list[0 + count] in alphabet:
            if position_list[0] in alphabet:
                reversed_pos = 1
            else:
                pass
            letter_to_number_conventer(position_list, count)
            count += 1
        else:
            count += 1
    for t in position_list:
        if pos_count == 0:
            row = int(position_list[pos_count])
            pos_count += 1
        elif pos_count == 1:
            col = int(position_list[pos_count]) - 1
    if reversed_pos == 1:
        row, col = col, row
    return(row, col)

def letter_to_number_conventer(position_list, count):
    if position_list[0 + count] == 'A':
        position_list[0 + count] = 0
    elif position_list[0 + count] == 'B':
        position_list[0 + count] = 1
    elif position_list[0 + count] == 'C':
        position_list[0 + count] = 2
    elif position_list[0 + count] == 'D':
        position_list[0 + count] = 3
    elif position_list[0 + count] == 'E':
        position_list[0 + count] = 4
    elif position_list[0 + count] == 'F':
        position_list[0 + count] = 5
    elif position_list[0 + count] == 'G':
        position_list[0 + count] = 6
    elif position_list[0 + count] == 'H':
        position_list[0 + count] = 7
    elif position_list[0 + count] == 'I':
        position_list[0 + count] = 8
    elif position_list[0 + count] == 'J':
        position_list[0 + count] = 9
    return position_list[0 + count]

def get_move_input_check(position_list, size):
    row_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    column_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    if len(position_list) != 2:
        print('Error field')
        return False
    else:
        pass
    if position_list[0] in row_list[:size]:
        if position_list[1] in column_list[:size]:
            return True
        else:
            print('Error field')
    elif position_list[1] in row_list[:size]:
        if position_list[0] in column_list[:size]:
            return True
        else:
            print('Error field')
    else:
        print('Error field')
        return False

def letter_to_number(letter, size):
    if letter[0] == "A":
        return 0
    if letter[0] == "B":
        return 1
    if letter[0] == "C":
        return 2
    if letter[0] == "D":
        return 3
    if letter[0] == "E":
        return 4
    if letter[0] == "F" and size >= 6:
        return 5
    if letter[0] == "G" and size >= 7:
        return 6
    if letter[0] == "H" and size >= 8:
        return 7
    if letter[0] == "I" and size >= 9:
        return 8
    if letter[0] == "J" and size >= 10:
        return 9

def ship_coordinates_validate(ship_position):
    row_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    column_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    if len(ship_position) >= 2:
        if ship_position[0] in row_list and (ship_position[1] in column_list or (ship_position[1] + ship_position[2]) in column_list):
            return True
        else:
            return False
    else:
        return False

def ship_position_validate(ship_position, player_ships_board, size):
    row = letter_to_number(ship_position, size)
    try:
        if ship_position[0].isalpha and ship_position[1].isdigit:
            if player_ships_board[row][int((ship_position[1]) + (ship_position[2])) - 1] == "0":
                return True
    except IndexError:
        if ship_position[0].isalpha and ship_position[1].isdigit:
            if player_ships_board[row][int(ship_position[1]) - 1] == "0":
                return True
            else:
                return False
        else:
            return False

def ship_distance_validate(ship_position, player_ships_board, size):
    row = letter_to_number(ship_position[0], size)
    column = (int(ship_position[1])) - 1
    while True:
        try:
            if player_ships_board[row][column-1] == 'X':
                return False
        except IndexError:
            None
        try:
            if player_ships_board[row][column+1] == 'X':
                return False
        except IndexError:
            None
        try:
            if player_ships_board[row+1][column] == 'X':
                return False
        except IndexError:
            None
        try:
            if player_ships_board[row-1][column] == 'X':
                return False
        except IndexError:
            None
        return True

def init_ship(player_ships_board, size):
    while True:
        ship_position = input(
            "Please choose position of your ship (e.g. A1):").upper()
        print(ship_position)
        if not ship_coordinates_validate(ship_position):
            print("There is no such position!")
            continue
        if ship_position_validate(ship_position, player_ships_board, size) and ship_distance_validate(ship_position, player_ships_board, size):
            return ship_position
        elif not ship_position_validate(ship_position, player_ships_board, size):
            print("You repeated the coordinates!")
            continue
        elif not size:
            print('The ship is too close another ship or is not next to this')
            continue

def ship_direction_validate(ship_position, ship_direction, player_ships_board, size):
    row = letter_to_number(ship_position[0], size)
    column = (int(ship_position[1])) - 1
    if ship_direction == "H":
        while True:
            try:
                if player_ships_board[row][column-1] == 'X':
                    return True
            except IndexError:
                pass
            try:
                if player_ships_board[row][column+1] == 'X':
                    return True
            except IndexError:
                pass
            return False
    elif ship_direction == "V":
        while True:
            try:
                if player_ships_board[row-1][column] == 'X':
                    return True
            except IndexError:
                pass
            try:
                if player_ships_board[row+1][column] == 'X':
                    return True
            except IndexError:
                pass
            return False

def one_x_ship(player_ships_board, size):
    ship_position = init_ship(player_ships_board, size)
    row = letter_to_number(ship_position[0], size)
    player_ships_board[row][int(ship_position[1]) - 1] = 'X'
    print_board(player_ships_board, size)

def two_x_ship(player_ships_board, check_last_ships, size):
    check_last_ships = copy.deepcopy(player_ships_board)
    ship_position = init_ship(check_last_ships, size)
    while True:
        ship_direction = input(
            "Choose direction of your ship: vertical (v) or horizontal (h)").upper()
        print(ship_direction)
        if ship_direction == "V" or ship_direction == "H":
            pass
        else:
            print("The format of direction is wrong!")
            continue
        row = letter_to_number(ship_position[0], size)
        player_ships_board[row][int(ship_position[1]) - 1] = 'X'
        print_board(player_ships_board, size)
        break
    while True:
        ship_position = init_ship(check_last_ships, size)
        if not ship_direction_validate(ship_position, ship_direction, player_ships_board, size):
            print("You can't make a ship in this place!")
            continue
        row = letter_to_number(ship_position[0], size)
        player_ships_board[row][int(ship_position[1]) - 1] = 'X'
        print_board(player_ships_board, size)
        break

def three_x_ship(player_ships_board, size):
    for ship in range(1):
        ship_position = init_ship(player_ships_board, size)
        row = letter_to_number(ship_position[0], size)
        player_ships_board[row][int(ship_position[1]) - 1] = 'X'
    while True:
        ship_direction = input(
            "Choose direction of your ship: vertical (v) or horizontal (h)").upper()
        if ship_direction == "V" or ship_direction == "H":
            break
        else:
            continue
    print_board(player_ships_board, size)
    for ship in range(2):
        while True:
            ship_position = init_ship(player_ships_board, size)
            if not ship_direction_validate(ship_position, ship_direction, player_ships_board, size):
                print("You can't make a ship in this place!")
                continue
            else:
                break
        row = letter_to_number(ship_position[0], size)
        player_ships_board[row][int(ship_position[1]) - 1] = 'X'
        print_board(player_ships_board, size)

def ship_to_the_board(board, size):
    print_board(board, size)
    player_ships_board = copy.deepcopy(board)
    check_last_ships = []
    print("Time for 1-X ships! Make your first three ships.")
    for ship in range(3):
        one_x_ship(player_ships_board, size)
    print("Time for 2-X ships! You have to make two ships.")
    for ship in range(2):
        two_x_ship(player_ships_board, check_last_ships, size)
    print("Time for 3-X ships!")
    three_x_ship(player_ships_board, size)
    return player_ships_board

def mark_shoot(col, row, player_board, player_ship_board):
    if player_ship_board[row][col] == 'X':
        if not check_sunk_ship(player_ship_board, row, col):
            player_board[row][col] = "H"
            player_ship_board[row][col] = "H"
            print('You hit an enemy ship!') 
            return True
        else:
            player_board[row][col] = "S"
            player_ship_board[row][col] = "S"
            sunk_ship(player_ship_board, row, col, player_board)
            print('You sank an enemy ship!')
            return True
    elif player_ship_board[row][col] == '0':
        player_board[row][col] = "M"
        player_ship_board[row][col] = "M"
        print('You missed!')
        return True
    else:
        return False

def check_sunk_ship(board, row, col):
    if board[row][col] == "X":
        try:
                if board[row-1][col] == "0" and board[row+1][col] == "0" and board[row][col-1] == "0" and board[row][col+1] == "0":
                    return True
        except IndexError:
            try:
                if board[row][col] == "X":
                    if board[row-1][col] == "0" and board[row+1][col] == "0" and board[row][col-1] == "0" :
                        return True
            except IndexError:
                try:
                    if board[row][col] == "X":
                        if board[row-1][col] == "0" and board[row+1][col] == "0"  and board[row][col-1] == "0":
                            return True
                except IndexError:
                    try:
                        if board[row][col] == "X":
                            if board[row-1][col] == "0" and board[row][col-1] == "0" and board[row][col+1] == "0":
                                return True
                    except IndexError:
                        try:
                            if board[row][col] == "X":
                                if board[row+1][col] == "0" and board[row][col-1] == "0" and board[row][col-1] == "0":
                                 return True
                        except IndexError:
                            pass
    if board[row][col] == "X":
        try:  
            if board[row][col+1] == 'H' and board[row][col+2] == 'H':
                return True
            elif board[row][col-1] == 'H' and board[row][col-2] == 'H':
                return True
            elif board[row-1][col] == 'H' and board[row-2][col] == 'H':
                return True
            elif board[row+2][col] == 'H' and board[row+2][col] == 'H':
                return True
            elif board[row+1][col] == 'H' and board[row-1][col] == 'H':
                return True    
            elif board[row][col-1] == 'H' and board[row][col+1] == 'H':
                 return True
        except IndexError:
            None
    if board[row][col] == "X":
        try:
            if board[row][col-1] == 'H':
                return True
        except IndexError:
            None
        try:
            if board[row][col+1] == 'H':
                return True
        except IndexError:
            None
        try:
            if board[row+1][col] == 'H':
                return True
        except IndexError:
            None
        try:
            if board[row-1][col] == 'H':
                return True
        except IndexError:
            None
        return False

def sunk_ship(player_ship_board, row, col, player_board):
    if player_ship_board[row+1][col] == "H":
        player_board[row+1][col] = "S"
        if player_ship_board[row+2][col] == "H":
            player_board[row+2][col] = "S"
    if player_ship_board[row-1][col] == "H":
        player_board[row-1][col] = "S"
        if player_ship_board[row-2][col] == "H":
            player_board[row-2][col] = "S"
    if player_ship_board[row][col+1] == "H":
        player_board[row][col+1] = "S"
        if player_ship_board[row][col+2] == "H":
            player_board[row][col+2] = "S"
    if player_ship_board[row][col-1] == "H":
        player_board[row][col-1] = "S"
        if player_ship_board[row][col-2] == "H":
            player_board[row][col-2] = "S"

def print_players_boards(size, player1_board, player2_board):
    col_mark = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    row_mark = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    print_col = ' '.join(col_mark[:size + 1])
    if size == 6:
        print(f'PLAYER 1 {" " * size}   PLAYER 2')
    if size == 7:
        print(f'PLAYER 1 {" " * size}    PLAYER 2')
    if size == 8:
        print(f'PLAYER 1 {" " * size}     PLAYER 2')
    if size == 9:
        print(f'PLAYER 1 {" " * size}      PLAYER 2')
    if size == 10:
        print(f'PLAYER 1 {" " * size}       PLAYER 2')
        print(f'{print_col}    {print_col}')
    if size != 10:
        print(f'{print_col}     {print_col}')
    for i in range(size):
        print_player1_board = ' '.join(player1_board[i])
        print_player2_board = ' '.join(player2_board[i])
        print(
            f'{row_mark[i]} {print_player1_board}     {row_mark[i]} {print_player2_board}')

def main_menu():
    print('Battleship game!')
    print('Choose game mode: ')
    print('1. Casual')
    print('2. Advanced')
    choose = input()
    if choose == '1':
        size = 5
        return size
    elif choose == '2':
        while True:
            size = int(input('Choose board size(6-10): '))
            if size <= 10 and size >= 6:
                return size
            else:
                print('Invalid number!')

def main():
    size = main_menu()
    player1_board, player2_board, player1_ship_board, player2_ship_board = init_board(
        size)
    player1_ship_board = ship_to_the_board(player1_ship_board, size)
    player2_ship_board = ship_to_the_board(player2_ship_board, size)
    while True:
        while True:
            print_players_boards(size, player1_board, player2_board)
            print("Player 1")
            row, col = get_move(size)
            if mark_shoot(row, col, player1_board, player2_ship_board):
                if has_won (player2_ship_board, "Player_1"):
                    quit()
                break
            if not mark_shoot(row, col, player1_board, player2_ship_board):
                continue
        while True:
            print_players_boards(size, player1_board, player2_board)
            print("Player 2")
            row, col = get_move(size)
            if mark_shoot(row, col, player2_board, player1_ship_board):
                if has_won (player1_ship_board, "Player_2"):
                    quit()
                break
            if not mark_shoot(row, col, player2_board, player1_ship_board):
                continue

if __name__ == "__main__":
    main()