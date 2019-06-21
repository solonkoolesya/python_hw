
from pprint import pprint
X, O, _ = 1, 0, None
#O_WINS, X_WINS, UNDEFINED, DRAW = range(4)

def slice(board):
    return([board[:3], board[3:6], board[6:9], board[::3], board[1::3], board[2::3],  board[::4], board[2:7:2] ])

def outcome(board):
    if_none_flag = 0
    for i in board:            
        if None in i:
            if_none_flag += 1
        elif len(set(i)) == 1 and i[0] == 1:
            return(1, 'X_WINS')			
        elif len(set(i)) == 1 and i[0] == 0:
            return(0, 'O_WINS')
    if if_none_flag > 0:
      return(2, 'UNDEFINED')
    else:
      return(3, 'DRAW') 

a = (O, X, X, 
     X, O, O, 
     O, _, X)
pprint(a)
print(outcome(slice(a)))