from time import sleep
import sys
import random


def create_board(width, height, PLAYER_ICON):
    map_1 = []
    board = []
    char_empty_spaces = ' '
    char_wall = '▓'
    char_door = 'D'
    coliders = [char_wall, char_door, PLAYER_ICON]
    #CREATING EMPTY MAP
    for x in range(width + 1):
        map_1.append(char_empty_spaces)
    for z in range(height + 1):
        board.append(map_1.copy())
    #CREATING WALLS
    for y in range(height + 1):
        board[y][0] = 'x'
    for y in range(width + 1):
        board[0][y] = 'x'
    for y in range(height + 1):
        board[y][width] = 'x'
    for y in range(width):
        board[height][y] = 'x'
    board[-1][-1] = 'x'
    board[0][-1] = 'x'
    #CREATING DOORS
    board[0][int(width/2)] = char_door
    board[int(height/2)][0] = char_door
    board[int(height)][int(width/2)] = char_door
    board[int(height/2)][width] = char_door
    #Door location 
    door_1 = (int(height), int(width/2))
    door_2 = (int(height/2), width)
    door_3 = (0, int(width/2))
    door_4 = (int(height/2), 0)
    #CREATING ROOMS
    board = put_rooms_on_board(board, width, height, coliders)
    #PUTTING PLAYER STARTING POSITION NEAR BOTTOM DOORS
    board[int(height) - 1][int(width/2)] = PLAYER_ICON
    player_position = (int(height) - 1, int(width/2))
    return board, coliders, player_position, door_1, door_2, door_3, door_4


def put_rooms_on_board(board, width, height, coliders):
    count = 0
    maximal_wall_count = width * height/13
    while count < maximal_wall_count:
        random_number_w = (random.randrange(1, width-1))
        random_number_h = (random.randrange(1, height))
        random__wall_lenght = random.randrange(int(height/3))
        random_coordinates = [random_number_h, random_number_w]
        for number in range(random__wall_lenght):
            if check_if_can_place(board, coliders, [random_coordinates[0] + number, random_coordinates[1]], width, height) == True:
                board[random_number_h + number][random_number_w] = coliders[0]
                count += 1
            else:
                break
    return board


def boss_room(width, height, player_character):
    map_1 = []
    board = []
    char_empty_spaces = ' '
    char_wall = 'x'
    #CREATING EMPTY MAP
    for x in range(width + 1):
        map_1.append(char_empty_spaces)
    for z in range(height + 1):
        board.append(map_1.copy())
    #CREATING WALLS
    for y in range(height + 1):
        board[y][0] = char_wall
    for y in range(width + 1):
        board[0][y] = char_wall
    for y in range(height + 1):
        board[y][width] = char_wall
    for y in range(width):
        board[height][y] = char_wall
    board[13][7] = player_character
    board[4][7] = 'B'
    player_position = (13, 7)
    return board, player_position


def check_if_can_place(board, coliders, random_coordinates, width, height):
    #CHECKS IF THE OBJECT IS PLACED ON A COLIDER
    if board[random_coordinates[0]][random_coordinates[1]] in coliders:
        return False
    #CHECKS IF THERE IS A WALL NEARBY
    if board[random_coordinates[0] - 1][random_coordinates[1]] in coliders:
        return False
    if board[random_coordinates[0] - 1][random_coordinates[1]-1] in coliders:
        return False
    if board[random_coordinates[0]][random_coordinates[1] - 1] in coliders:
        return False
    #CHECKS IF THE OBJECT IS IN FRONT OF DOORS
    if [random_coordinates[0], random_coordinates[1]] == [1, int(width/2)]: #top doors
        return False
    if [random_coordinates[0], random_coordinates[1]] == [int(height/2), 1]: #left doors
        return False
    if [random_coordinates[0], random_coordinates[1]] == [int(height), int(width/2)]: #bottom doors
        return False
    if [random_coordinates[0], random_coordinates[1]] == [int(height/2), width]: #right doors
        return False
    if [random_coordinates[0], random_coordinates[1]] == [int(height) - 1, int(width/2)]: #bottom doors
        return False
    return True
    

def put_stuff_on_board(board,stuff,width,height,coliders):
    count = 0
    for items in stuff:
        coliders.append(items)
    #while stuff not in board:
    while count < len(stuff):
    #while all(item in stuff for item in board):
        for x in stuff:
            #check = any(x for item in board if x == item)
            check = False
            for line in board:
                if x in line:
                    check = True
                    break
            if check == True:
                continue
            random_number_w = (random.randrange(2, width - 2))
            random_number_h = (random.randrange(2, height - 2))
            random_coordinates = [random_number_h, random_number_w]
            if check_if_can_place(board, coliders, [random_coordinates[0], random_coordinates[1]], width, height) == True:
                board[random_number_h][random_number_w] = x
                count += 1
            else:
                break
    return board, coliders


def read_text(text, time):
    for char in text:
        print(char, end='', flush="")
        sleep(time)
        sys.stdout.flush()