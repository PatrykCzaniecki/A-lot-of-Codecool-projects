def display_board(x, y, game_board, player_icon):
    game_board[x][y] = player_icon
    for element in range(len(game_board)):
        print(' '.join(game_board[element]))