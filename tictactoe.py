import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    clear_screen()
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])

def checkwhowin(board, player):
    win_conditions = [
        [board['1'], board['2'], board['3']],  # Top row
        [board['4'], board['5'], board['6']],  # Middle row
        [board['7'], board['8'], board['9']],  # Bottom row
        [board['1'], board['4'], board['7']],  # Left column
        [board['2'], board['5'], board['8']],  # Middle column
        [board['3'], board['6'], board['9']],  # Right column
        [board['1'], board['5'], board['9']],  # Diagonal 1
        [board['3'], board['5'], board['7']]   # Diagonal 2
    ]
    for condition in win_conditions:
        if all(cell == player for cell in condition):
            return True
    return False

def checkdrew(board):
    return all(cell != ' ' for cell in board.values())

def min_max(board, comp_move, comp, player):
    if checkwhowin(board, comp):
        return 1

    elif checkwhowin(board, player):
        return -1
    
    elif checkdrew(board):
        return 0

    if comp_move:
        bestscore = -float('inf')
        for key in board.keys():
            if board[key] == " ":
                board[key] = comp
                score = min_max(board, False, comp, player)
                board[key] = " "
                bestscore = max(score, bestscore)
        return bestscore               
    else:
        bestscore = float('inf')
        for key in board.keys():
            if board[key] == " ":
                board[key] = player
                score = min_max(board, True, comp, player)
                board[key] = " "
                bestscore = min(score, bestscore)
        return bestscore   
    
def compmove(board, comp, player):
    bestscore = -float('inf')
    bestmove = None

    for key in board.keys():
        if board[key] == " ":
            board[key] = comp
            score = min_max(board, False, comp, player)
            board[key] = " "
            if score > bestscore:
                bestscore = score
                bestmove = key

    return bestmove

def insertvalue(board, move, comp):
    board[move] = comp

board = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}
comp = 'X'
player = 'O'

while True:
    print("\nCurrent Board:")
    print_board(board)
    
    user_move = input("Enter your move (1-9): ")
    insertvalue(board, user_move, player)
    
    if checkwhowin(board, player):
        print_board(board)
        print("\nCongratulations! You win!")
        break
    
    if checkdrew(board):
        print_board(board)
        print("\nThe game is a draw!")
        break
    
    comp_move = compmove(board, comp, player)
    insertvalue(board, comp_move, comp)
    
    if checkwhowin(board, comp):
        print_board(board)
        print("\nSorry, the computer wins!")
        break
    
    if checkdrew(board):
        print_board(board)
        print("\nThe game is a draw!")
        break
    print("\nComputer's move:")
