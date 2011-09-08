from random import choice


class AI(object):

    def __init__(self, symbol):
        self.symbol = symbol

    def get_next_move(self, board):
        valids = [col for col in range(7) if board.is_valid(col)]
        return choice(valids)


class CleverAI(AI):
    def get_next_move(self, board):
        for i,col in enumerate(board.board):
            #import pdb; pdb.set_trace()
            if len(col) > 0 and col[-1] == self.symbol and board.is_valid(i):
                return i
        return super(CleverAI, self).get_next_move(board)
                
            


class Human(object):

    def __init__(self, symbol):
        self.symbol = symbol

    def get_next_move(self, board):
        move = int(raw_input("Make a move (%s): " % self.symbol))
        return move

