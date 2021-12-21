import operator 

def count_games(file_name):
    try:
        f = open(file_name, "r")
        content = f.readlines()
        length = len(content)
        return length
    finally:
        f.close()

def decide(file_name, year):
    year = str(year)
    try:
        f = open(file_name)
        if year in f.read():
            return True
        else:
            return False
    finally: 
        f.close()

def get_latest(file_name):
    try:
        f = open(file_name)
        content = [word.split("\t") for word in f.readlines()]
        year = 2021
        counter = 0 
        while counter < year:
            for i in content:
                if str(year) in i:
                    return i[0] 
            year -= 1
            counter += 1  
    finally:
        f.close() 

def count_by_genre(file_name, genre):
    try:
        f = open(file_name)
        content = [word.split("\t") for word in f.readlines()]
        genre_list = []
        for i in content:
            if genre in i:
                genre_list.append(i[0])
        return len(genre_list)
    finally:
        f.close()

def get_line_number_by_title(file_name, title):
    try:
        f = open(file_name)
        content = [word.split("\t") for word in f.readlines()]
        line = 0
        for i in content:
            line += 1
            if title in i:
                return line
    finally:
        f.close()

def sort_abc(file_name):
    try:
        f = open(file_name)
        content = [word.split("\t") for word in f.readlines()]
        game_list = [i[0] for i in content]
        game_list.sort() 
        return game_list           
    finally:
        f.close() 

def get_genres(file_name):
    try:
        f = open(file_name)
        content = [word.split("\t") for word in f.readlines()]
        genre_list = [] 
        for i in content:
            genre_list.append(i[3])
        genre_list.sort()
        genre_list = list(dict.fromkeys(genre_list))
        return genre_list          
    finally:
        f.close()

def when_was_top_sold_fps(file_name, genre):
    try:
        f = open(file_name)
        content = [word.split("\t") for word in f.readlines()]
        top_sell_fps = {}
        for i in content:
            if genre in i:
                top_sell_fps[i[2]] = i[1]         
        for i, j in top_sell_fps.items():
            top_sell_fps[i] = float(j)
        return max(top_sell_fps.items(), key = operator.itemgetter(1))[0]
    finally:
        f.close()