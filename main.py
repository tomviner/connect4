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
    while not board.is_full() or board.get_winner():
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

    # display final state
    os.system('clear')
    print board
    print
    winner = board.get_winner()
    if winner:
        print winner + ' wins!'
    else:
        print 'A draw!'

if __name__ == '__main__':
    main()

