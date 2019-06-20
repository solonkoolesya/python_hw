from pprint import pprint

class XO:
    X, O, _ = 1, 0, None

    def slice(board):
        return((board[:3], board[3:6], board[6:9], board[::3], board[1::3], board[2::3],  board[::4], board[2:7:2] ))


    def outcome(board):
        for i in board:            
            if None in i:
                return(2)
            elif len(set(i)) == 1 and i[0] == 1:
                return(1)			
            elif len(set(i)) == 1 and i[0] == 0:
                return(0)
            else:
               pass
        return(3) 

test_board1 = (0, 0, 0
               1, 1, 0
			   0, 1, 0)

test_board2 = (1, 0, 1,
               1, 1, 0, 
               1, 0, 0)

test_board3 = (1, 0, 1,
               0, None, 0, 
               1, 0, 0)

test_board4 = (1, 0, 1,
               0, 1, 0, 
               0, 1, 0)

print('board1')
pprint(slice(test_board1))
pprint(outcome(slice(test_board1)))

print('board2')
pprint(slice(test_board2))
pprint(outcome(slice(test_board2)))

print('board3')
pprint(slice(test_board3))
pprint(outcome(slice(test_board3)))

print('board4')
pprint(slice(test_board4))
pprint(outcome(slice(test_board4)))


X, O, _ = 1, 0, None

TEST_BOARD = (
    O, X, O,
    X, O, X,
    _, _, X
)

O_WINS, X_WINS, UNDEFINED, DRAW = range(4)