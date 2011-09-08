#!/usr/bin/env python

import os

from players import AI, Human, CleverAI, GeniusAI
from board import Board

def main():
    board = Board()
    p1 = Human('O')
    p2 = CleverAI('X')
    players = [p1, p2]
    current_player = 0
    while not board.is_full():
        os.system('clear')
        print board
        print
        player = players[current_player]
        while True:
            move = player.get_next_move(board)
            try:
                board.move(move, player.symbol)
                break
            except:
                pass
        current_player = (current_player + 1) % 2

    os.system('clear')
    print board
    print

if __name__ == '__main__':
    main()

