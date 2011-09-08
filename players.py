from random import choice


class AI(object):

    symbol = 'O'

    def get_next_move(self, board):
        valids = [col for col in range(7) if board.is_valid(col)]
        return choice(valids)


class Human(object):
    
    symbol = 'X'

    def get_next_move(self, board):
        move = int(raw_input("Make a move (%s): " % self.symbol))
        return move

