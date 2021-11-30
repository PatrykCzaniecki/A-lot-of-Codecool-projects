import sys 

idea_list = []

with open("Ideabank_list.txt", "r") as ideabank:
    for i, line in enumerate(ideabank):
        print("{}. {}".format(i+1, line.strip()))
    ideabank.close() 

while True:
    with open("Ideabank_list.txt", "a") as ideabank:
        idea = input("What is your new idea? ")
        idea_list.append(idea)
        for number, word in enumerate(idea_list, 1):
            print("{}. {}".format(number, word))  
        ideabank.write(idea + "\n")  
        if idea == "":
            break
        ideabank.close()

# with open("Ideabank_list.txt", "w") as ideabank:
#     ask = input("Chcesz usunąć jakiś składnik z listy? Yes/No ")
#     if ask == "Yes":
#         delete = int(input("Wybierz numer składnika do usunięcia: "))
#         ideabank.strip(delete)
#     ideabank.close() 