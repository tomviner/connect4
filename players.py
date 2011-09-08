from random import randint

class AI(object):

    def next_move(self, board):
        return randint(0, 8)



class Human(object):

    def next_move(self, board):
        return randint(0, 8)

