
from pprint import pprint

X, O, _ = 1, 0, None

TEST_BOARD = (
    O, X, O,
    X, X, O,
    O, O, X
)
O_WINS, X_WINS, UNDEFINED, DRAW = range(4)




def outcome(board_func):
    def wrapper(board_arg):
        if_none_flag = 0
        for i in board_func(board_arg):
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
    return wrapper


@outcome
def slice(board):
    return([board[:3], board[3:6], board[6:9], board[::3], board[1::3], board[2::3],  board[::4], board[2:7:2] ])

#print(slice(TEST_BOARD))
	  
if __name__ == "__main__":
    import doctest
    doctest.testmod()


