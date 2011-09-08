#!/usr/bin/env python

import os

from players import AI, Human
from board import Board

def main():
    board = Board()
    p1 = AI()
    p2 = Human()
    players = [p1, p2]
    current_player = 0
    while True:
        os.system('clear')
        print board
        player = players[current_player]
        board.move(player.get_next_move(board), player.symbol)
        current_player = (current_player + 1) % 2

if __name__ == '__main__':
    main()

