import Report 

print(Report.count_games("Game_statistics.txt"))
print(Report.decide("Game_statistics.txt", 2000))
print(Report.get_latest("Game_statistics.txt"))
print(Report.count_by_genre("Game_statistics.txt", "RPG"))
print(Report.get_line_number_by_title("Game_statistics.txt", "Doom 3"))
print(Report.sort_abc("Game_statistics.txt"))
print(Report.get_genres("Game_statistics.txt"))
print(Report.when_was_top_sold_fps("Game_statistics.txt", "First-person shooter"))