"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    numX=0;
    numO=0;
    for n in range(3):
        for i in range(3):
            if board[n][i] == "X":
                numX = numX + 1
            if board[n][i] == "O":
                numO = numO + 1
    if numX == 0 and numO == 0: #Empieza X 
        
        return "X"
    elif numX > numO:
        
        return "O"
    elif numX < numO:
        
        return "X"
    elif numX == numO:
        
        return "X"
    

    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    lista = []
    for i in range(3):
        for k in range(3):
            if board[i][k] is None:
                lista.append((i,k))

    
    return lista 
    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if  (board[action[0]][action[1]] is not EMPTY):
         raise EmptyAction("The acton is not valid")
    else :
        auxBoard=copy.deepcopy(board)
        
        auxBoard[action[0]][action[1]]=player(board)
        return auxBoard   
    
    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    listWin = [ board[0], board[1], board[2], [ board[0][0],board[1][0],board[2][0] ], [ board[0][1],board[1][1],board[2][1] ],
    [ board[0][2],board[1][2],board[2][2] ], [ board[0][0],board[1][1],board[2][2] ], [ board[0][2],board[1][1],board[2][0] ] ]
    

    if ["X","X","X"] in listWin:
        return "X"
    elif ["O","O","O"] in listWin:
        return "O"
    else:
        return None

    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    var = False
    if actions(board) == [] or winner(board) == "X" or winner(board) == "O" : 
        var = True
        
    
        
    
    return var 

    #raise NotImplementedError

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    util=0

    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0

    #raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #print("Into minimax")
    optimo=None

    if player(board) == "X":
        v = -math.inf
        for action in actions(board):
            vAux = minValue(result(board,action))
            if vAux > v:
                v=vAux
                optimo =action

    if player(board) == "O":
        v = math.inf
        for action in actions(board):
            vAux = maxValue(result(board,action))
            if vAux < v:
                v=vAux
                optimo =action        
    
 
    
    return optimo
    
    #raise NotImplementedError

def maxValue(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v,minValue(result(board,action)))
    return v

def minValue(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v , maxValue(result(board,action)))
    return v

