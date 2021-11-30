# Implement the function unique_in_order which takes as argument a sequence 
# and returns a list of items without any elements with the same value next to each other 
# and preserving the original order of elements.

def unique_in_order(iterable):
    unique_list = []
    prev = None
    for character in iterable:
        if character != prev:
            unique_list.append(character)
        prev = character
        
    return unique_list