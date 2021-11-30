import random 

choices = ["Rock", "Paper", "Scissors"]

def newGame(winPlayer, winComputer):
    computer = random.choice(choices)

    player=input("Wybierz Rock lub Paper lub Scissors - ")
    print("Komputer wybrał "+ computer)

    

    if computer=="Rock" and player=="Paper" or computer=="Paper" and player==("Scissors") or computer==("Scissors") and player==("Rock"):
        winPlayer += 1
        print("Wygrał gracz. Gratulacje!")

    if computer =="Paper" and player=="Rock" or computer=="Scissors" and player==("Paper") or computer=="Rock" and player=="Scissors":
        winComputer += 1
        print("Wygrał komputer. Przegrałeś :/")

    print("Wynik komputer: " + str(winComputer) + " gracz: " + str(winPlayer))
    
    nextgame=input("Czy chcesz zagrać jeszcze raz? y/n")

    if nextgame=="y":
        newGame(winPlayer,winComputer)

newGame(0,0)
