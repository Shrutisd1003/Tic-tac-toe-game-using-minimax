import math
from copy import deepcopy

X = "X"
O = "O"         
EMPTY = None

def minmax_values(board, alpha, beta, player):
    if terminal(board):
        return utility(board)

    if player == X:
        value = -math.inf
        for action in actions(board):
            value = max(value, minmax_values(result(board, action),alpha, beta, O))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = math.inf
        for action in actions(board):
            value = min(value, minmax_values(result(board, action), alpha, beta, X))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                count=count+1
    if count%2 == 0:
        return X
    else:
        return O

def actions(board):
    possible_actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.append((i,j))   
    return possible_actions

def result(board, action):
    a,b = action
    new_board =  deepcopy(board)
    turn = player(board)
    if new_board[a][b] != EMPTY:
        raise Exception("Invalid action")
    elif turn == X:
        new_board[a][b] = "X"
    else:
        new_board[a][b] = "O"    
    return new_board

def winner(board):
    if (board[0][0] == board[0][1] == board[0][2] == "X" or
        board[1][0] == board[1][1] == board[1][2] == "X" or
        board[2][0] == board[2][1] == board[2][2] == "X" or
        board[0][0] == board[1][0] == board[2][0] == "X" or
        board[0][1] == board[1][1] == board[2][1] == "X" or
        board[0][2] == board[1][2] == board[2][2] == "X" or
        board[0][0] == board[1][1] == board[2][2] == "X" or
        board[0][2] == board[1][1] == board[2][0] == "X"):
            return X
    elif (board[0][0] == board[0][1] == board[0][2] == "O" or
        board[1][0] == board[1][1] == board[1][2] == "O" or
        board[2][0] == board[2][1] == board[2][2] == "O" or
        board[0][0] == board[1][0] == board[2][0] == "O" or
        board[0][1] == board[1][1] == board[2][1] == "O" or
        board[0][2] == board[1][2] == board[2][2] == "O" or
        board[0][0] == board[1][1] == board[2][2] == "O" or
        board[0][2] == board[1][1] == board[2][0] == "O"):
            return O
    else:
        return None

def terminal(board):
    if winner(board) == 'X' or winner(board) == 'O':
        return True
    elif not actions(board):
        return True
    else:
        return False

def utility(board):
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    else:
        return 0

def minimax(board):
    if terminal(board):
        return None
    move = None
    alpha = -math.inf
    beta = math.inf
    if player(board) == X:
        value = -math.inf
        for action in actions(board):
            updated_value = minmax_values(result(board, action), alpha, beta, O)
            alpha = max(value, updated_value)
            if updated_value > value:
                value = updated_value
                move = action
    else:
        value = math.inf
        for action in actions(board):
            updated_value = minmax_values(result(board, action), alpha, beta, X)
            beta = min(value, updated_value)
            if updated_value < value:
                value = updated_value
                move = action
    return move