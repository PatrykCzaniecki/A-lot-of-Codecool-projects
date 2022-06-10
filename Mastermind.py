import random
from turtle import color 

colors = ["R", "G", "B", "Y", "O", "P"]
secret = []


def opening():
    print("\n_______________Welcome to Mastermind Game_______________")
    opening = input("\nDo you need instruction or starightly enter into the game? [Instructions/Game]: ").upper()
    if opening == "I" or opening == "INSTRUCTONS":
        print("\n______________________Instructions______________________")
        print("\n1.Computer will automatically generate four colors from list.")
        print("2.Player must guess 4 colors numbers correct from the list to win the game.")
        print("3.You have 12 times chances to atempt the game.")
        print("4.There will be 6 colors in the below list:")
        print("(Y)Yellow, (R)Red, (G)Green, (B)Blue, (P)Purple, (O)Orange")
        print("5.Player no need to enter the whole word, just need to enter the first alphabetical of the colors.")
        print("Example: for Red color you just need to enter 'r' or 'R'.")
        print("6.You can display a board of game (contains game statistics) by command 'board'.")
        print("________________________________________________________")
        print("\nLet's start the game!")
    elif opening == "G" or opening == "GAME":
        print("\nLet's start the game!")


def random_secret(secret):
    for i in range(4):
        secret.append(random.choice(colors))
    #print(f"\nColors to guess are {secret}")


def game(secret):
    round = 0
    hits = 0
    close = 0
    guess_history = []  
    hits_history = []
    close_history = []
    for round in range(12):
        player_input = input("\nPlease enter the four colors: ").upper()
        check_player_input(player_input, secret, round, colors) 
        round += 1
        hits = 0
        close = 0
        if player_input == "BOARD":
            show_board(guess_history, hits_history, close_history)
            round -= 1
        try:    
            if player_input != "BOARD":
                guess_history.append(" ".join(player_input)) 
                hits = sum(player_input[ i ] == secret[ i ] for i in range(len(secret)))
                close = sum(min(secret.count(colors), player_input.count(colors)) for colors in set(secret))
                print(f"\nCorrect color and correct place: {hits}")
                hits_history.append(hits)
                print(f"Correct color but wrong place: {close}")
                close_history.append(close)
                if round >= 1 and round <= 11 and hits < 4:
                    print(f"Round number: {round}")
                    print("Next attempt: ")
        except IndexError:
            print("IndexError")
        check_win(hits, round, secret)
    return round, hits, close  


def check_player_input(player_input, secret, round, colors):
    if len(player_input) != len(secret) and player_input != "BOARD":
        print(f"\nThe color code has exactly 4 colors, not {len(player_input)}. Please try again!")
        round -= 1
        return player_input
    for i in range(len(player_input)):
        if player_input[i] not in colors and player_input != "BOARD":
            print(f"Look up what colors you can use in this game! There isn't color like this: {player_input[i]}") 
    return player_input


def show_board(guess_history, hits_history, close_history):
    print("\n_________BOARD________")
    print("  Move  | Hits | Close ")
    for (move, hits, close) in zip(guess_history, hits_history, close_history):
        print(f"{move} |  {hits}   |   {close}") 
    print()


def check_win(hits, round, secret):
    if hits == 4:
        if round == 1:
            print("\nWow! You guessed at the first round!")
        else:
            print(f"\nWell done... You needed {round} rounds to guess.")
        end_game()  
    if round == 11:
        print("\n!!!This is your last chanse to guess the color code!!!")
    elif round == 12 and hits < 4:
        print(f"\nTime-out!! You didn't guess the color code! The secret color code was: {secret}")
        end_game() 


def end_game():
    print("Thanks for game!")
    finish_game = input("\nDo you want to play again? [Yes/No]: ").upper()
    if finish_game == "N" or finish_game == "NO":
        print ("See you next time! Bye, bye!")
        quit()
    elif finish_game == "Y" or finish_game == "YES":
        print ("So, let's play again..")
        secret = []
        random_secret(secret)
        game(secret) 


if __name__ == "__main__":
    opening()
    random_secret(secret)
    game(secret)
    
