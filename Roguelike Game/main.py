import util
import engine
import ui
import inhabitants
import items
from time import sleep
from playerchar import Player
from bosschar import Boss 

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20

def print_player_stats(player): 
    print("< Character stats >")
    print(f"Name: {player[0]}\nRace: {player[1]}\nHealth: {player[2]}\nStrength: {player[3]}")


def create_new_player():
    new_player = Player("", "", "", "", "")
    new_player = new_player.class_new_player()
    name = new_player[0]
    race = new_player[1]
    health = new_player[2]
    strength = new_player[3]
    ascii = new_player[4]
    player = [name, race, health, strength, ascii]
    return player 


def print_boss_stats(boss):
    print("< Boss stats >")
    print(f"Name: {boss[0]}\nRace: {boss[1]}\nHealth: {boss[2]}")


def new_boss():
    new_boss = Boss("", "", "", "")
    new_boss = new_boss.class_boss()
    name = new_boss[0]
    race = new_boss[1]
    health = new_boss[2]
    ascii = new_boss[3]
    boss = [name, race, health, ascii] 
    return boss 


def welcome_screen():
    util.clear_screen()
    sleep(0.3)
    engine.read_text("\n                Welcome \n",0.0)
    sleep(1)
    engine.read_text("                  to",0.0)
    sleep(1)
    engine.read_text("\n            The Dry Underwear", 0.0)
    sleep(1.8)
    engine.read_text("\n                At The", 0.008)
    engine.read_text("\n           BOTTOM OF THE SEA \n\n", 0.008)
    sleep(2)


def prologue():
    util.clear_screen()
    engine.read_text('    "It''s a wonderfull day."', 0.06)
    engine.read_text(' "It''s a wonderfull day."', 0.06)
    engine.read_text(' "It''s a wonderfull day..."\n', 0.06)
    sleep(2)
    util.clear_screen()
    engine.read_text('    It does not matter how many times you will keep saying that line.\n', 0.06)
    engine.read_text('    You lost your Legendary Limited edition DRY UNDERWEAR,\n    so it will be a terrible day unless you find them.', 0.06)
    input("\n<PRESS ENTER>")
    util.clear_screen()
    engine.read_text('    You rush on a journey to the bottom of the sea to look for them.\n', 0.06)
    sleep(1)
    engine.read_text('    Best of luck! You will need it.\n', 0.06)
    input("<PRESS ENTER>")
    util.clear_screen()
    engine.read_text('    Press WSAD to move your character in game.\n    Press I to acess inventory.\n', 0.06)
    input("<PRESS ENTER>")


def enter_boss_room():
    util.clear_screen()
    engine.read_text('    You entered Kings Chamber.\n', 0.06)
    sleep(2)
    engine.read_text('    In the middle of the room is a throne with a man-fish hovering over it...\n', 0.06)
    input("<PRESS ENTER>")
    engine.read_text('    He got a brand new shiny golden Trident in his hand \nand on his head you spot...\n', 0.06)
    sleep(1)
    engine.read_text('    HE IS WEARING YOUR UNDERWEAR!!!.\n', 0.02)
    input("<PRESS ENTER>")
    util.clear_screen()


def main_menu():
    print("1. New game\n0. Quit")
    print()
    print("< Control Instruction >")
    print("Move Player: WSAD")
    print("Show player's inventory: I")
    print("Quit game: Q") 
    mode_choices = ["0","1"]
    game_mode = input("Enter: ")
    while game_mode not in mode_choices:
        game_mode = input("Enter: ")
    if game_mode == '0':
        close_game()
    util.clear_screen()


def check_fight (game_board):
    count = 0
    for line in game_board:
        if "O" not in line and "N" not in line and  "A" not in line and "S" not in line and "C" not in line and "B" not in line:
            pass
        else:
            count +=1
    if count == 0:
        return True


def check_door (game_board, letter):
    inhabitants_count = 0
    for lists in game_board:
        if letter in lists:
            inhabitants_count += 1
            break
    if inhabitants_count == 0:
        for lists in game_board:
            for element in lists:
                if element == "D":
                    lists[lists.index(element)] = " "


def move_player(x,y, game_board):
    player_position = (x,y)
    colision = ['▓',"x","D"]
    while True:
        move = util.key_pressed()
        if move == "d" and game_board[x][y + 1] not in colision:
                game_board[x][y + 1] = PLAYER_ICON
                game_board [x][y] = " "
                y += 1 
                player_position = (x, y)
        elif move == "a" and game_board[x][y - 1]  not in colision:
                game_board[x][y - 1] = PLAYER_ICON
                game_board [x][y] = " "
                y -= 1
                player_position = (x, y)
        elif move == "w" and game_board[x - 1][y]  not in colision:
            game_board[x - 1][y] = PLAYER_ICON
            game_board [x][y] = " "
            x -= 1
            player_position = (x, y)
        elif move == "s" and game_board[x + 1][y] not in colision:
            game_board[x + 1][y] = PLAYER_ICON
            game_board [x][y] = " "
            x += 1
            player_position = (x, y)
        elif move == "i":
            items.display_inventory(items.player_inventory)
            move = util.key_pressed()
            while move != 'i':
                move = util.key_pressed()
        return player_position
    

def create_level(characters, items_list):
    board, coliders, player_position, door_1, door_2, door_3, door_4 = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT, PLAYER_ICON)
    board = engine.put_rooms_on_board(board, BOARD_WIDTH, BOARD_HEIGHT, coliders)
    board, coliders = engine.put_stuff_on_board(board, characters, BOARD_WIDTH, BOARD_HEIGHT, coliders)
    return board, player_position, door_1, door_2, door_3, door_4


def create_boss_level(characters, items_list): 
    board, coliders, player_position, door_1, door_2, door_3, door_4 = engine.create_board(15, 15, PLAYER_ICON)
    board, coliders = engine.put_stuff_on_board(board, characters, BOARD_WIDTH, BOARD_HEIGHT, coliders)
    return board, player_position, door_1, door_2, door_3, door_4


def put_static_items(list_of_items,board):
    if list_of_items == items.items_level_1:
        print('cos')
        board[10][10] = items.items_level_1[0][3]
        print(board[10][10])
    elif list_of_items == items.items_level_2:
        board[5][10] = items.items_level_2[0][3]  
        board[6][10] = items.items_level_2[1][3]  
    elif list_of_items == items.items_level_3:
        board[12][3] = items.items_level_3[0][3] 
        board[4][1] = items.items_level_3[1][3] 
        board[9][10] = items.items_level_3[2][3]
    elif list_of_items == items.items_level_4:
        board[9][9] = items.items_level_4[0][3] 
        board[4][2] = items.items_level_4[1][3] 
        board[7][7] = items.items_level_4[2][3] 
    return board


def main():
    welcome_screen()
    main_menu()       
    player = create_new_player()
    prologue()
    siren, nemo, odysseus, aquamen, oscar, boss = inhabitants.create_inhabitants()
    characters = nemo.appearance
    items_level_1 = items.items_level_1
    items_level_2 = items.items_level_2
    items_level_3 = items.items_level_3
    items_level_4 = items.items_level_4
    inhabitant = nemo
    board, player_position, door_1, door_2, door_3, door_4  = create_level([characters], [items.items_level_1[0][3]])  
    board = put_static_items(items.items_level_1,board)
    actual_item_list = 'itemy1'
    fights = 0
    is_running = True
    while True:
        util.clear_screen()
        print_player_stats(player) 
        ui.display_board(player_position[0],player_position[1], board, PLAYER_ICON)
        inhabitants.check_dialogue(player_position[0], player_position[1], board)
        player_position = move_player (player_position[0], player_position[1], board)
        player_pos = items.player_pos_to_index(player_position[0], player_position[1])
        items.is_item_on_ground(player_pos,player, actual_item_list)
        items.add_attack_and_health(items.player_inventory, player)
        if check_fight(board) == True and fights == 0:
            inhabitants.inhabitants_fight (inhabitant, player)
            fights += 1
        check_door (board, "N")
        if player_position == door_1 or player_position == door_2 or player_position == door_3 or player_position == door_4:
            break

    characters = siren.appearance
    inhabitant = siren
    board, player_position, door_1, door_2, door_3, door_4 = create_level([characters], [items.items_level_2[0][3]])
    board = put_static_items(items.items_level_2, board)
    actual_item_list = 'itemy2'
    fights = 0
    while True:
        util.clear_screen()
        print_player_stats(player)
        ui.display_board(player_position[0], player_position[1], board, PLAYER_ICON)
        inhabitants.check_dialogue(player_position[0], player_position[1], board)
        player_position = move_player (player_position[0], player_position[1], board)
        player_pos = items.player_pos_to_index(player_position[0], player_position[1])
        items.is_item_on_ground(player_pos, player, actual_item_list)
        items.add_attack_and_health(items.player_inventory, player)
        if check_fight(board) == True and fights == 0:
            inhabitants.inhabitants_fight (inhabitant, player)
            fights += 1
        check_door(board, "S")
        if player_position == door_1 or player_position == door_2 or player_position == door_3 or player_position == door_4:
            break

    characters = oscar.appearance
    inhabitant = oscar
    board, player_position, door_1, door_2, door_3, door_4 = create_level([characters], [items.items_level_2[0][3]])
    board = put_static_items(items.items_level_3, board)
    actual_item_list = 'itemy3'
    fights = 0
    while True:
        util.clear_screen()
        print_player_stats(player)
        ui.display_board(player_position[0], player_position[1], board, PLAYER_ICON)
        inhabitants.check_dialogue(player_position[0], player_position[1], board)
        player_position = move_player (player_position[0], player_position[1], board)
        player_pos = items.player_pos_to_index(player_position[0], player_position[1])
        items.is_item_on_ground(player_pos, player, actual_item_list)
        items.add_attack_and_health(items.player_inventory, player)
        if check_fight(board) == True and fights == 0:
            inhabitants.inhabitants_fight (inhabitant, player)
            fights += 1
        check_door(board, "C")
        if player_position == door_1 or player_position == door_2 or player_position == door_3 or player_position == door_4:
            break

    characters = odysseus.appearance
    inhabitant = odysseus
    board, player_position, door_1, door_2, door_3, door_4 = create_level([characters], [items.items_level_2[0][3]])
    board = put_static_items(items.items_level_4, board)
    actual_item_list = 'itemy4'
    fights = 0
    while is_running:
        util.clear_screen()
        print_player_stats(player)
        ui.display_board(player_position[0], player_position[1], board, PLAYER_ICON)
        inhabitants.check_dialogue(player_position[0], player_position[1], board)
        player_position = move_player (player_position[0], player_position[1], board)
        player_pos = items.player_pos_to_index(player_position[0], player_position[1])
        items.is_item_on_ground(player_pos, player, actual_item_list)
        items.add_attack_and_health(items.player_inventory, player)
        if check_fight(board) == True and fights == 0:
            inhabitants.inhabitants_fight (inhabitant, player)
            fights += 1
        check_door(board, "O")
        if player_position == door_1 or player_position == door_2 or player_position == door_3 or player_position == door_4:
            break

    enter_boss_room()
    characters = boss.appearance
    inhabitant = boss
    player_position = (14, 7)
    board, player_position, door_1, door_2, door_3, door_4 = create_boss_level([characters], [items.items_level_2[0][3]])
    fights = 0
    while True:
        util.clear_screen()
        print_player_stats(player)
        print_boss_stats(boss)
        ui.display_board(player_position[0], player_position[1], board, PLAYER_ICON)
        inhabitants.check_dialogue(player_position[0], player_position[1], board)
        player_position = move_player (player_position[0], player_position[1], board)
        player_pos = items.player_pos_to_index(player_position[0], player_position[1])
        items.is_item_on_ground(player_pos, player)
        items.add_attack_and_health(items.player_inventory, player)
        if check_fight(board) == True and fights == 0:
            inhabitants.inhabitants_fight (inhabitant, player)
            fights += 1
            final_ascii = inhabitants.ascii_win()
            print(final_ascii)
            quit()
        

def close_game():
    while True:
        close_game = input("DO YOU WANT TO CLOSE GAME? (yes/no) ") 
        if close_game == "no":
            main_menu() 
        elif close_game =="yes":    
            exit()


def quit():  
    quit = input("GREAT GAME! DO YOU WANT TO PLAY AGAIN? (yes/no): ")
    if quit == "yes":
        main_menu()
    elif quit == "no":
        close_game() 


if __name__ == '__main__':
    main()