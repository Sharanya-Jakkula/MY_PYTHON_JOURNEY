#tic
#from IPython.display import clear_output
def display_board(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])
test_board=['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)
def player_input():
    marker=''
    while(marker!='X' and marker!='O'):
        marker=input('Player: Choose X OR O : ').upper()
    if(marker=='X'):
        return('X','O')
    else:
        return ('O','X')
def place_marker(board,marker,position):
    board[position]=marker
#place_marker(test_board,'1',8)
display_board(test_board)
def win_check(board,mark):
    return ((board[1]==mark and board[2]==mark and board[3]==mark) or (board[4]==mark and board[5]==mark and board[5]==mark) or (board[7]==mark and board[8]==mark and board[9]==mark) or (board[1]==mark and board[4]==mark and board[7]==mark) or (board[2]==mark and board[5]==mark and board[6]==mark) or (board[3]==mark and board[6]==mark and board[9]==mark) or (board[1]==mark and board[5]==mark and board[9]==mark) or (board[3]==mark and board[5]==mark and board[7]==mark))
#display_board(test_board)
import random
def choose_first():
    flip=random.randint(0,1)
    if(flip==0):
        return 'Player 1'
    else:
        return 'Player 2'
def space_check(board,position):
    return board[position]==' '
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('Choose a position :(1-9) : '))
    return position
def replay():
    choice=input("Play again? Yes or No : ")
    return choice=='Yes'
#WHILE LOOP TO KEEP RUNNING THE GAME
print('----Welcome to TIC-TAC-TOE----')
while True:
    #play
    #SET (BOARD,WHOS FIRST,CHOOSE MARKERS X,O)   
    the_board=[' ']*10
    turn=choose_first()
    print(turn+' will go first..')
    player1_marker,player2_marker=player_input()
    play_game=input('Ready to play? y or n : ')
    if play_game=='y':
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn=='Player 1':
            display_board(the_board)
            #choose a position
            position=player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER1 HAS WON!!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!!')
                    game_on=False
                else:
                    turn='Player 2'
            #player to win
        else:
            display_board(the_board)
                #choose a position
            position=player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!!')
                    game_on=False
                else:
                    turn='Player 1'
    if not replay():
        break
    #BREAK OUT OF THE LOOP ON RUNNING REPLAY