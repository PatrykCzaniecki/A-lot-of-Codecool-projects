# In this kata you will create a function that takes a list of non-negative integers and strings 
# and returns a new list with the strings filtered out.

def filter_list(l):
    def is_int(var):
        if type(var) == int:
            return True
        else:
            return False
        
    return list(filter(is_int, l)) 