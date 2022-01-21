from turtle import position
from engine import read_text
from util import key_pressed
import main
import os
import random


class Inhabitant:
    
    def __init__(self, name, health, appearance, dialogue, ascii, punches):
        self.name = name
        self.health = health
        self.appearance = appearance
        self.dialogue = dialogue
        self.position = position
        self.ascii = ascii
        self.punches = punches


def ascii_characters():
    siren_ascii = """
                                                    ((@ @))       \\\\.////
                                                    ))\=/((        \\\|///
                                                    .((/"\))         \\|//
                                                    //)W)(W(``''--.._/`'/
                                                    `m(\,_))__________.' ldb"""
    nemo_ascii = """                                                                                     
                                            | '_ \ / _ \ '_ ` _ \ / _ \ 
                                            | | | |  __/ | | | | | (_) |
                                            |_| |_|\___|_| |_| |_|\___/ """

    odysseus_ascii = """                                        
                                                                                                            | |                             
                                                                                                        ___   __| |_   _ ___ ___  ___ _   _ ___ 
                                                                                                    / _ \ / _` | | | / __/ __|/ _ \ | | / __|
                                                                                                     | (_) | (_| | |_| \__ \__ \  __/ |_| \__ 
                                                                                                    \___/ \__,_|\__, |___/___/\___|\__,_|___/
                                                                                                                 __/ |                       
                                                                                                                |___/                        """
    aquamen_ascii = """                                                                               █████   ██████  ██    ██  █████  ███    ███ ███████ ███    ██ 
                                                                                                     █   ██ ██    ██ ██    ██ ██   ██ ████  ████ ██      ████   ██ 
                                                                                                     ██████ ██    ██ ██    ██ ███████ ██ ████ ██ █████   ██ ██  ██ 
                                                                                                     █   ██ ██ ▄▄ ██ ██    ██ ██   ██ ██  ██  ██ ██      ██  ██ ██ 
                                                                                                     █   ██  ██████   ██████  ██   ██ ██      ██ ███████ ██   ████ """
    oscar_ascii = """
                                                                  ___  ___  ___ __ _ _ __ 
                                                                 / _ \/ __|/ __/ _` | '__|
                                                                | (_) \__ \ (_| (_| | |   
                                                                 \___/|___/\___\__,_|_|   """
    
    neptun_ascii = """
                                                                                                                       |      ,sss.  
                                                                                                                    |  | |    $^,^$
                                                                                                                    |  | |     $$$
                                                                                                                    |_ |_|  _/ $$$  \_
                                                                                                                        |   /'         `.
                                                                                                                        ;,-' /\ ,,     /. |
                                                                                                                        '-./' ;        ;: |
                                                                                                                        |     |`  '    |`,;
                                                                                                                             ,==========,
                                                                                                                             |   |  |   |
                                                                                                                             `-./____\.-'
                                                                                                                             |  |     | |
                                                                                                                             |  |     | |
                                                              """                                                                                         
    return siren_ascii, nemo_ascii, odysseus_ascii, aquamen_ascii, oscar_ascii, neptun_ascii


def ascii_win ():
        neptun_win_ascii = """
                                                                       |      ,sss.  
                                                                    |  | |    $^,^$
                                                                    |  | |     $$$
                                                                    |_ |_|  _/ $$$  \_
                                                                       |   /'         `.
                                                                      ;,-' /\ ,,     /. |
                                                                      '-./' ;        ;: |
                                                                       |    |`  '    |`,;
                                                                           /         |
                                                                           | | +18 | |
                                                                           | |     | |
                                                                           | |     | |
                                                                           | |     | |"""
        return neptun_win_ascii                                                                                                                      


def create_inhabitants():
    siren_ascii, nemo_ascii, odysseus_ascii, aquamen_ascii, oscar_ascii, neptun_ascii= ascii_characters()
    dialogue_siren = "    Hello lost traveler, I'm Siren.\nI think your pants are covering your eyes since you haven't found them yet. Take a good look."
    dialogue_nemo = "    My name is Nemo. Have you seen my father anywhere?"
    dialogue_odysseus = "    I am Odysseus. I don't have time for your pants. I have a job to do in Troy.\nI will not believe that they can fall for an wooden horse."
    dialogue_aquamen = "    I am Aquamen. Another person lost their pants. I think I know who took them from you.\n There's one guy with a trident, thinks he's a strong god. H's lost his mind for a long time. Do what you need to do with him"
    dialogue_oscar = "    I am Oscar the Sharkslayer. I could help you, but I'm busy."
    dialogue_boss = ""

    siren = Inhabitant("SIREN", 50, "S", dialogue_siren, siren_ascii, [0, 0, 0, 0, 0, 1, 1])
    nemo = Inhabitant("NEMO", 40, "N", dialogue_nemo, nemo_ascii, [0, 0, 0, 0, 0, 1, 1])
    odysseus = Inhabitant("ODYSSEUS", 80, "O",
                          dialogue_odysseus, odysseus_ascii, [0, 0, 0, 0, 0, 1, 2])
    aquamen = Inhabitant("AQUAMEN", 100, "A", dialogue_aquamen, aquamen_ascii,[0, 0, 0, 0, 1, 2, 2])
    oscar = Inhabitant("OSCAR", 60, "C", dialogue_oscar, oscar_ascii, [0, 0, 0, 0, 0, 1, 2])
    boss = Inhabitant("Neptun", 160, "B", dialogue_boss, neptun_ascii, [0, 0, 0, 0, 0, 1, 2])
    inhabitants_list = [siren, nemo, odysseus, aquamen, oscar, boss]
    return inhabitants_list


def check_dialogue(x,y,game_board):
    siren, nemo, odysseus, aquamen, oscar, boss = create_inhabitants()
    if siren.appearance == game_board[x+1][y] or siren.appearance == game_board[x-1][y] or siren.appearance == game_board[x][y-1] or siren.appearance == game_board[x][y+1]:
        read_text(siren.dialogue, 0.08)
        siren.appearance = "%"
    elif nemo.appearance == game_board[x+1][y] or nemo.appearance == game_board[x-1][y] or nemo.appearance == game_board[x][y-1] or nemo.appearance == game_board[x][y+1]:
        read_text(nemo.dialogue, 0.08)
        nemo.appearance = "%"
    elif odysseus.appearance == game_board[x+1][y] or odysseus.appearance == game_board[x-1][y] or odysseus.appearance == game_board[x][y-1] or odysseus.appearance == game_board[x][y+1]:
        read_text(odysseus.dialogue, 0.08)
    elif aquamen.appearance == game_board[x+1][y] or aquamen.appearance == game_board[x-1][y] or aquamen.appearance == game_board[x][y-1] or aquamen.appearance == game_board[x][y+1]:
        read_text(aquamen.dialogue, 0.08)
    elif oscar.appearance == game_board[x+1][y] or oscar.appearance == game_board[x-1][y] or oscar.appearance == game_board[x][y-1] or oscar.appearance == game_board[x][y+1]:
        read_text(oscar.dialogue, 0.08)
    elif boss.appearance == game_board[x+1][y] or boss.appearance == game_board[x-1][y] or boss.appearance == game_board[x][y-1] or boss.appearance == game_board[x][y+1]:
        read_text(boss.dialogue, 0.08)
    else:
        pass


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def create_fight_board(inhabitant):
    board_fight = [" " for x in range(inhabitant.health)]
    arrow = "--->"
    ball_position = 0
    board_fight[ball_position] = arrow
    board_fight[-1] = inhabitant.ascii
    return [board_fight, ball_position, arrow]


def inhabitants_fight(inhabitant, player): 
    board_fight, ball_position, arrow = create_fight_board(inhabitant)
    create_fight_board(inhabitant)
    inhabitant_health = inhabitant.health
    player_strenght = 0
    if player_strenght <= 60:
        player_punches = [1]
    if player_strenght > 60 and player_strenght < 80:
        player_punches = [1, 1, 2]
    if player_strenght >= 80 and player_strenght <= 100:
        player_punches = [1, 1, 2, 3]
    print ("""  
                / _(_)      | |   | |  
                | |_ _  __ _| |__ | |_ 
                |  _| |/ _` | '_ \| __|
                | | | | (_| | | | | |_ 
                |_| |_|\__, |_| |_|\__|
                        __/ |          
                        |___/    """)
    print(f"\n IT'S A FIGHT! PRESS SPACE TO HIT {inhabitant.name}")
    while True:
        key = key_pressed()
        player_punch = random.choice(player_punches)
        inhabitant_punch = random.choice(inhabitant.punches)
        if ball_position == inhabitant.health - 1:
            clearConsole()
            print(f"YOU WON. {inhabitant.name} IS DEAD.")
            return True
        if key == " ":
            clearConsole()
            board_fight[ball_position] = " "
            ball_position += player_punch
            inhabitant_health -= player_punch
            if inhabitant_health >= 3:
                board_fight[ball_position] = arrow
            else:
                board_fight[-2] = arrow
            print(
                f"{inhabitant.name}'s health: {inhabitant_health} {player[0]}'s health: {player[2]}")
            print("".join(board_fight))
        if key != " ":
            print ("PRESS SPACE TO HIT")
        if ball_position > 10 and inhabitant_punch > 0:
            ball_position -= inhabitant_punch
            player[2] -= inhabitant_punch
            if player[2] <= 0:
                clearConsole()
                print ("You've lost your pants forever. You're Dead.")
                main.close_game()
            board_fight = [" " for x in range(inhabitant.health)]
            inhabitant_health += inhabitant_punch
            board_fight[-1] = inhabitant.ascii
            board_fight[ball_position] == arrow
            print(f'YOU MISSED AND {inhabitant.name} HIT YOU! DAMAGE: {inhabitant_punch}. FIGHT BETTER OR SAY GOODBYE TO UNDERPANTS')