import random

def main():
    print(hangman_logo())
    print("Welcome in Hangman Game!\n")
    print("Choose game difficulty: ")
    difficulty = choose_difficulty()
    if difficulty == 1:
        word = get_word(difficulty)
        word = word.lower().strip() 
        lives = 6
        play(word, lives)
    elif difficulty == 2:
        word = get_word(difficulty)
        word = word.lower().strip()
        lives = 5
        play(word, lives)
    elif difficulty == 3:
        word = get_word(difficulty)
        word = word.lower().strip()
        lives = 4
        play(word, lives)
    elif difficulty != 1 or 2 or 3:
        print("Exiting...")

def choose_difficulty():
    loop = True
    while loop:
        print("1) Easy - small pool of words, 6 lives")
        print("2) Normal - larger pool of words, 5 lives")
        print("3) Hard - biggest pool of words, 4 lives")
        user_inp = input("\nChoose difficulty (1), (2), (3) or type 'quit' to exit: ").strip().lower()
        if user_inp == "1":
            loop = False
            return int(1)
        elif user_inp == "2":
            loop = False
            return int(2)
        elif user_inp == "3":
            loop = False
            return int(3)
        elif user_inp == "quit":
            break
        else:
            print("Not valid entry")
            pass

def get_word(difficulty):
    # przed uruchomieniem upewnij się, że ścieżka poniżej do pliku .txt jest prawidłowa! 
    f = open("hangman-python-kamil-kornek96/countries-and-capitals.txt")
    lines = f.readlines()
    list_of_countires = [] 
    for i in lines:
        x = (i.rpartition("|")[0])
        list_of_countires.append(x)
    if difficulty == 1:
        return random.choice(list_of_countires[0:61])
    elif difficulty == 2:
        return random.choice(list_of_countires[0:122])
    elif difficulty == 3:
        return random.choice(list_of_countires)

def play(word, lives):
    word_that_user_see = "_" * len(word)
    is_guessed = False
    guessed_letters = []
    guessed_words = []
    print(display_hangman(lives))
    print(f"Word to guess: {word_that_user_see}")
    print("\n")
    while not is_guessed and lives > 0:
        user_guess = input("Please guess a letter or whole word: ").lower()
        if len(user_guess) == 1:
#and user_guess.isalpha() or user_guess == " " - dodatkowa opcja jesli chcemy aby były rozpatrywane tylko litery i spacja
            if user_guess in guessed_letters:
                print(f"You already guessed the letter, \"{user_guess}\"")
            elif user_guess not in word:
                print(f"\"{user_guess}\", is not in the word.")
                lives -= 1
                guessed_letters.append(user_guess)
            else:
                print(f"Correct!, \"{user_guess}\", is in the word!")
                guessed_letters.append(user_guess)
                word_as_list = list(word_that_user_see)
                indices = [i for i, letter in enumerate(word) if letter == user_guess]
                for index in indices:
                    word_as_list[index] = user_guess
                    word_that_user_see = "".join(word_as_list)
                if "_" not in word_that_user_see:
                    is_guessed = True
        elif len(user_guess) == len(word):
            if user_guess in guessed_words:
                print(f"You already guessed the word, \"{user_guess}\"")
            elif user_guess != word:
                print(f"\"{user_guess}\", is not the word.")
                lives -= 1
                guessed_words.append(user_guess)
            else:
                is_guessed = True
                word_that_user_see = word
        elif user_guess == "quit":
            print("Quitting")
            return is_guessed == "Quitting"
        else:
            print("Not a valid guess.")
        print(display_hangman(lives))
        print(word_that_user_see)
        print("\n")
    if is_guessed:
        print(f"Congrats, you guessed the word: \"{word}\"! You win!")
        nextGame()
    if is_guessed == "Quitting":
        pass
    elif not is_guessed:
        print(f"Sorry, you ran out of tries. The word was \"{word}\". Maybe next time!")
        nextGame()

def nextGame():
    nextgame=input("Do you want to play again? (yes/no): ").lower().strip()

    if nextgame=="yes":
        main()
    else:
        print("Quitting")

def hangman_logo():
    return '''
    88                                                                            
    88                                                                            
    88                                                                            
    88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba, 8b,dPPYba,  
    88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8 88P'   `"8a 
    88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88 88       88 
    88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88 88       88 
    88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8 88       88 
                                        aa,    ,88                                
                                         "Y8bbdP"
    '''

def display_hangman(lives):
    stages = [  # lives = 0
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                ---|----
               /   |   /
               --------
                """,
                # lives = 1
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                ---|----
               /   |   /
               --------
                """,
                # lives = 2
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                ---|----
               /   |   /
               --------
                """,
                # lives = 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                ---|----
               /   |   /
               --------
                """,
                # lives = 4
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                ---|----
               /   |   /
               --------
                """,
                # lives = 5
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                ---|----
               /   |   /
               --------
                """,
                # lives = 6
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                ---|----
               /   |   /
               --------
                """
    ]
    return stages[lives]

if __name__ == "__main__":
    main()