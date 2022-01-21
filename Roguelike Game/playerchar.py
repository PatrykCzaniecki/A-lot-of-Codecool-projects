class Player:

    def __init__(self, name, race, health, strength, ascii):
        self.name = name 
        self.race = race
        self.health = health 
        self.strength = strength
        self.ascii = ascii 


    def class_new_player(self):
        human_ascii, shark_ascii, tryton_ascii = new_player_ascii()
        print()
        print("< Character creation panel >")
        self.name = input("Provide name for your character: ")
        while True:
            self.race = input(f"Choose type of race for {self.name}. You can choose between [Human, Shark, Tryton]: ").lower()
            if self.race == "human":
                human = Player(self.name, "Human", 40, 40, human_ascii)
                print(f"Your character's name is {human.name}, your race is Human, your health level is {human.health} and your strength is {human.strength}.")
                return human.name, human.race, human.health, human.strength, human_ascii
                break   
            elif self.race == "shark":
                shark = Player(self.name, "Shark", 50, 50, shark_ascii)
                print(f"Your character's name is {shark.name}, your race is Shark, your health level is {shark.health} and your strength is {shark.strength}.")
                return shark.name, shark.race, shark.health, shark.strength, shark_ascii
                break  
            elif self.race == "tryton":
                tryton = Player(self.name, "Tryton", 160, 160, tryton_ascii)
                print(f"Your character's name is {tryton.name}, your race is Tryton, your health level is {tryton.health} and your strength is {tryton.strength}.")
                return tryton.name, tryton.race, tryton.health, tryton.strength, tryton_ascii
                break
            else:
                print("You selected an incorrect player race, please try again!")
                continue 
    

def new_player_ascii():
    human_ascii =       '''    ___
                     / ,_\    ,,,,,
                    /  _)/   /o    (
                    |  \    (_ `    \_________
                    |   \____ >__,_  \        |
                    |              ))  )__,   |
                    \,___________ //  /   \   |_
                              )__//__/     \  __).
                     ________/o     /       \____/
                    /`              \
                   /   \_______   _//
                 _/     \     \     \____ __,--.
                /      /       \          \_),  \
                \_____/         \_________/  \\  \
           ______/_/                         (___/
          /       o\
         '-----^--'                             '''


    shark_ascii =     '''_________         .    .
                        (..       \_    ,  |\  /|
                         \       O  \  /|  \ \/ /
                          \______    \/ |   \  / 
                             vvvv\    \ |   /  |
                             \^^^^  ==   \_/   |
                              `\_   ===    \.  |
                              / /\_   \ /      |
                              |/   \_  \|      /
                                    \_________/ '''


    tryton_ascii = '''
~         ~            ~     w   W   w
                   ~          \  |  /       ~
       ~        ~        ~     \.|./    ~
                                 |
                      ~       ~  |           ~
      o        ~   .:.:.:.       | ~
 ~                 wwWWWww      //   ~
           ((c     //"""\\     //|        ~
  o       /\/\((  (. @ @ .)   // |  ~
         (d d  ((  \\\^///   //  |
    o    /   / c((-\\\'///-.//   |     ~
        /===/ `) (( \\|// ,_/    |~
 ~     /o o/  / c((( \|/  |      |  ~          ~
    ~  `~`^  / c (((  '   |      |          ~
            /c  c(((      |  ~   |      ~
     ~     /  c  (((  .   |      |   ~           ~
          / c   c ((^^^^^^`\   ~ | ~        ~       
         |c  c c  c((^^^ ^^^`\   |
 ~        \ c   c   c(^^^^^^^^`\ |    ~       
      ~    `\ c   c  c;`\^^^^^./ |             ~
             `\c c  c  ;/^^^^^/  |  ~
  ~        ~   `\ c  c /^^^^/' ~ |       ~
        ~        `;c   |^^/'     o
            .-.  ,' c c//^\\         ~
    ~      ( @ `.`c  -///^\\\  ~             ~
            \ -` c__/|/     \|jgs
     ~       `---'   '   ~   '          ~
~          ~          ~           ~             ~ '''
    
    return human_ascii, shark_ascii, tryton_ascii