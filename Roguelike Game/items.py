def all_player_items(player_inventory): 
    for element in player_inventory:
        all_player_items_list.append(element[0])
    return all_player_items_list


def add_item_to_inv(list_of_items):
    index_count = 0
    if list_of_items[0] not in all_player_items_list:
        player_inventory.append(list_of_items)
    else:
        for lists in player_inventory:
            if lists[0] == list_of_items[0]:
                player_inventory[index_count][2] += list_of_items[2]
            else:
                index_count +=1


def player_pos_to_index(x, y):
    x = str(x)
    y = str(y)
    player_pos = x + y
    return player_pos


def del_worse_item(player_inventory, item_type):
    index = 0
    for player_items in player_inventory:
        if player_items[1] == item_type:
            del player_inventory[index]
        else:
            index += 1


def add_attack_and_health(player_inventory, player):
    for item in player_inventory:
        if item[1] == 'weapon' :
            player[3] += item[5]
            item[5] = 0
        elif item[1] == 'armour':
            player[2] += item[5]
            item[5] = 0
        

def is_item_on_ground(player_pos,player,actual_items):
    if player_pos == '510' and actual_items == 'itemy2':
        item_type = items_level_2[0][1]
        del_worse_item(player_inventory,item_type)
        add_item_to_inv(items_level_2[0]) #dryer
    elif player_pos == '99' and actual_items == 'itemy4':
        item_type = items_level_4[0][1]
        del_worse_item(player_inventory,item_type)
        add_item_to_inv(items_level_4[0]) #trident
    elif player_pos == '123' and actual_items == 'itemy3':
        item_type = items_level_3[0][1]
        del_worse_item(player_inventory,item_type)
        add_item_to_inv(items_level_3[0]) #plastic straw
    elif player_pos == '610' and actual_items == 'itemy2':
        item_type = items_level_2[1][1]
        del_worse_item(player_inventory,item_type)
        add_item_to_inv(items_level_2[1]) #wet cardboard
    elif player_pos == '77' and actual_items == 'itemy4':
        item_type = items_level_4[2][1]
        del_worse_item(player_inventory,item_type)
        add_item_to_inv(items_level_4[2]) #full diamond set
    elif player_pos == '41' and actual_items == 'itemy3':
        item_type = items_level_3[2][1]
        del_worse_item(player_inventory,item_type)
        add_item_to_inv(items_level_3[1]) #lifeb
    elif player_pos == '1010' and actual_items == 'itemy1':
        item_type = items_level_1[0][1]
        player[2] += items_level_1[0][5] #seedweed
    elif player_pos == '910' and actual_items == 'itemy3':
        item_type = items_level_3[2][1]
        player[2] += items_level_3[2][5] #monster energy
    elif player_pos == '42' and actual_items == 'itemy4':
        item_type = items_level_4[1][1]
        player[2] += items_level_4[1][5] #golden apple
    else:
        pass


def display_inventory(inventory):
    print(f'INVENTORY__________________________')
    for index in range(len(inventory)):
        print(f'{inventory[index][0]} - {inventory[index][1]}   ({inventory[index][6]})')
list_of_keys = [['red key','key',1,'k','xxxx']]
items_level_1 = [['seeweed', 'food',1,'h','1010', 10,]]
items_level_2 = [['dryer','weapon', 1, 'd','510',20,'Rare'],['wet cardboard','armour',1,'c','610',25,'Rare']]
items_level_3 = [['plastic straw', 'weapon',1,'l','123',30,'Exceptional'],['lifebuoy','armour',1,'m','41',15,'Exceptional'],['monster energy', 'food',1,'h','910',20]]
items_level_4 = [['trident', 'weapon', 1,'w','99',40,'Legendary'],['golden apple', 'food',1,'h','41',50],['diamond armour','armour',1,'s','77',50,'Legendary']]
player_inventory = [['stick','weapon', 1, 'd','xxxx',1,'Common'],['swimming trunks','armour',1,'m','xxxx',5,'Common']]
all_player_items_list = []