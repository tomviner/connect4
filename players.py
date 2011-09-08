from random import choice


class AI(object):

    def __init__(self, symbol):
        self.symbol = symbol

    def get_valids(self, board):
        return [col for col in range(7) if board.is_valid(col)]

    def get_next_move(self, board):
        return choice(self.get_valids(board))


class CleverAI(AI):

    def get_next_move(self, board):
        for i,col in enumerate(board.board):
            #import pdb; pdb.set_trace()
            if len(col) > 0 and col[-1] == self.symbol and board.is_valid(i):
                return i
        return super(CleverAI, self).get_next_move(board)
                
            

class GeniusAI(AI):

    def get_score(self, board, col):
        column = board.board[col]
        if column and column[-1] == self.symbol:
            return 1
        else:
            return 0

    def find_max(self, scores):
        return scores.keys().index(max(scores.values()))

    def get_next_move(self, board):
        valids = self.get_valids(board)
        scores = {}
        for col in valids:
            scores[col] = self.get_score(board, col)

        return self.find_max(scores)
        


class Human(object):

    def __init__(self, symbol):
        self.symbol = symbol

    def get_next_move(self, board):
        move = int(raw_input("Make a move (%s): " % self.symbol))
        return move

