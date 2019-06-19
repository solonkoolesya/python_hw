from pprint import pprint
X, O, _ = 1, 0, None

def slice(board):
    return((board[:3], board[3:6], board[6:9], board[::3], board[1::3], board[2::3],  board[::4], board[2:7:2] ))

board_tup = slice((None, 1, 0, 0, 0, 0, 1, 0, 0))

def outcome(board):
   for i in board:
      if len(set(i)) == 1 & i[0] == 1:
         print(set(i))
         return(1)
         break
      elif len(set(i)) == 1 & i[0] == 0:
         print(set(i))
         return(0)
         break
      else:
        return(3)

         


#pprint((1, 2, 3, 4, 5, 6, 7, 8, 9))
pprint(slice((1, 2, 3, 4, 5, 6, 7, 8, 9)))
pprint(board_tup)
pprint(outcome(board_tup))
