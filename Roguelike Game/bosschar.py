class Boss:

    def __init__(self, name, race, health, ascii):
        self.name = name
        self.race = race
        self.health = health 
        self.ascii = ascii 


    def class_boss(self):
        neptun_ascii = boss_ascii()
        boss = Boss("Neptun", "God", 200, neptun_ascii)
        return boss.name, boss.race, boss.health, boss.ascii 


def boss_ascii():
    neptun_ascii= """
                                                    |      ,sss.  
                                                 |  | |    $^,^$
                                                 |  | |     $$$
                                                 |_ |_|  _/ $$$  \_
                                                    |   /'  ?$?     `.
                                                    ;,-' /\ ,,     /. |
                                                    '-./' ;        ;: |
                                                    |     |`  '    |`,;
                                                         ,==========,
                                                         |   |  |   |
                                                         `-./____\.-'   
                                                              """

    return neptun_ascii 