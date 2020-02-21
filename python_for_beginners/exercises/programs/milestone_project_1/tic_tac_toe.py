def show_board(board = ['null', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']):
    print(board[7]+'|'+board[8]+'|'+board[9]+'|')
    print(board[4]+'|'+board[5]+'|'+board[6]+'|')
    print(board[1]+'|'+board[2]+'|'+board[3]+'|')


def player_input():
    selection = input('Select which mark do you want to play: X or O\n')
    if selection == 'X':
        player1 = 'X'
        player2 = 'O'
    else:
        player1 = 'O'
        player2 = 'X'
    while selection != 'X' and selection != 'O':
        print('Enter a valid option\n')
        selection = input('Select which mark do you want to play: X or O\n')

def place_marker():
    position = input('select where to put the marker\n')
    return position
    

new_board = []
show_board()
counter = 0
while counter < 10:
    position = place_marker()
    new_board.insert(int(position),'X')
    show_board(new_board)
    counter += 1
    print(new_board)