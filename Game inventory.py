def display_inventory(inventory):
    print("Your inventory contains the following:")
    for item in inventory:
        print(f"{item}: {inventory[item]}") 
    print("\n")

inventory = {"gold coin": 45, "arrow": 12, "torch": 6, "dagger": 2, "rope": 1, "ruby": 1}

def add_to_inventory(inventory, added_items):
    for new_item in added_items:
        if new_item in inventory.keys():
            inventory[new_item] += 1
        else:
            inventory.update({new_item: 1})

added_items = ["rope", "ruby", "sword", "apple", "apple"]

def remove_from_inventory(inventory, removed_items):
    for damaged_item in removed_items:
        if damaged_item in inventory.keys():
            inventory[damaged_item] -= 1 
        if inventory[damaged_item] <= 0:
            del inventory[damaged_item]      

removed_items = ["rope", "rope", "sword"] 

def print_table(inventory, order):
    print("-----------------")
    print("item name", "|", "count")
    print("-----------------")
    if order == "count, asc":
        inventory = sorted(inventory.items(), key = lambda count: count[1])
    else:
        order == "count, desc"
        inventory = sorted(inventory.items(), key = lambda count: count[1], reverse = True)
    inventory = dict(inventory)
    for i, c in inventory.items():
        print(f"{i:>9} | {c:>4}")
    print("-----------------")

def import_inventory(inventory, filename):
    f = open(filename, "r") 
    content = f.read()
    split = content.split(",")
    for item in split:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory.update({item: 1})

def export_inventory(inventory, filename):
    if filename is None:
        file = open("export_inventory.csv", "w")
        for item in inventory:
            file.write(item + ",")
    else:
        file_exists = open(filename, "w")
        for item in inventory:
            file_exists.write(item + ",")
    file_exists.close()

add_to_inventory(inventory, added_items)
remove_from_inventory(inventory, removed_items)
import_inventory(inventory, filename = "test_inventory.csv") 
export_inventory(inventory, filename = "test_inventory.csv")
print_table(inventory, "count, desc")