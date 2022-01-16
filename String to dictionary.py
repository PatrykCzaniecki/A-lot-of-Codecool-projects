'''Implement a function string_to_dictionary which receives one parameter: string. 
This parameter contains a sequence of items (like sword, axe, etc) that are separated by semicolons (;). 
The function should return a dictionary, which contains the information on all items in the string, with their amounts. 
Example: sword;axe;torch;axe;sword'''

string = "sword;axe;torch;axe;sword"
dict = {}
list = string.split(";")

for item in list:
    if item not in dict.keys():
        dict.update({item: 1})
    else:
        dict[item] += 1

print(dict) 