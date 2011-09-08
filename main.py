#!/usr/bin/env python

from players import AI, Human
from board import Board

def main():
    board = Board()
    p1 = AI()
    p2 = Human()
    players = [p1, p2]
    next_player = 0
    while True:
        print board
        players[next_player].next_move(board)

if __name__ == '__main__':
    main()



