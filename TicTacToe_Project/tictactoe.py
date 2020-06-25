# Simple Tic tac Toe Game

import itertools


def win(current_game):
    #horizontal
    for row in game:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print('Spieler hat horizontal gewonnen')
            return True
        
    

    #vertical
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print('Spieler hat vertikal gewonnen')
            return True

    #diagonal
    cols = list(reversed(range(len(game))))
    rows = range(len(game))

    diags = []
    for col, row, in zip(cols, rows):
        diags.append(game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print('Spieler hat diagonal gewonnen (/)')
        return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print('Spieler hat diagonal gewonnen (\\)')
        return True
    
    check = [ ]
    for row in game:
        if(row.count(0)>0):
            check.append(row)
    if len(check) == 0:
        print('Unentschieden!')
        return True
    return False


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print('Diese Position ist bereits besetzt! Wähle eine andere')
            return game_map, False
        print('   ' + '  '.join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)  

        return game_map, True
    except IndexError as e: #exact error is saved in e
        print('Error: make sure you input row/column as 0 1 or 2', e) #prints out the print aswell as the exact error
        return game_map, False

    except Exception as e: #general exeption
        print('Da ist etwas schief gelaufen', e)
        return game_map, False

play = True
players = [1, 2]
while play:
    game_size = int(input('Welche Spielfeldgröße ist gewünscht?: '))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f'Current Player: {current_player}')
        played = False

        while not played:
            column_choice = int(input('Wähle die gewünschte Spalte (0, 1, 2): '))
            row_choice = int(input('Wähle die gewünschte Zeile (0, 1, 2): '))
            game, played = game_board(game, current_player, row_choice, column_choice)
        
        if win(game):
            game_won = True
            again = input('Das Spiel ist vorbei, möchtest du noch eine Runde spielen?: (j/n) ')
            if again.lower() == 'j':
                print('restarting')
            elif again.lower() == 'n':
                print('Bye')
                play = False
            else:
                print('Keine gültige Antwort')
                play = False


#game_board(game, 1, 2, 2)

'''horizontal

    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print('winner!')

#vertical

   for col in range(len(game)):
       check = []
       for row in game:
           check.append(row[col])
       if check.count(check[0]) == len(check) and check[0] != 0:
               print('winner!')



#diagonal

cols = list(reversed(range(len(game))))
rows = range(len(game))

diags = []
for col, row, in zip(cols, rows):
    diags.append(game[row][col])
print(diags)

diags = []
for ix in range(len(game)):
    diags.append(game[ix][ix])
print(diags)
#game_board(game, just_display=True)

#game [0][1] = 1

#game_board()'''

