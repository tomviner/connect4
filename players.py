from random import randint

class AI(object):

    symbol = 'O'

    def get_next_move(self, board):
        return randint(0, 8)



class Human(object):
    
    symbol = 'X'

    def get_next_move(self, board):
        return randint(0, 8)

