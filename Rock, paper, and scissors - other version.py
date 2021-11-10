'''import random
str1 = "rock"
str2 = "paper" 
str3 = "scissors"

str1 > str3 
str1 < str2
str2 > str1
str2 < str3
str3 > str2
str3 < str1

choices = [str1, str2, str3]
computerchoice = random.choice(choices)

user_input = input("Wybierz symbol ")

if computerchoice > user_input:
    print ("You win!")
elif computerchoice < user_input: 
    print ("You lose :/")
else:
    print ("It's draw.")

print ("Computer choice was -", computerchoice)


#input ("Do you want to play again? y/n") 
#if input == y

#if user_input == computerchoice:
   # print ("You win!")
#else:   
   #print ("You lose!"

   '''
import random

str1 = "Rock"
str2 = "Paper" 
str3 = "Scissors"

str1 > str3 and str1 < str2
str2 > str1 and str2 < str3
str3 > str2 and str3 < str1

choices = str1, str2, str3 

def newGame(winPlayer, winComputer):
    computer = random.choice(choices) 

    player=input("Wybierz Rock lub Paper lub Scissors ")
    print("Wybrałeś",player)
    print("Komputer wybrał "+ computer)

    if computer==player:
        print("Remis")

    if computer < player:
         winPlayer += 1
         print("Wygrał gracz. Gratulacje!")
    
    if computer > player:
        winComputer += 1
        print("Wygrał komputer.")

    print("Wynik komputer: " + str(winComputer) + " gracz: " + str(winPlayer))
    nextgame=input("Czy chcesz zagrać jeszcze raz? y/n ")

    if nextgame=="y":
        
        newGame(winPlayer,winComputer)

newGame(0,0)
