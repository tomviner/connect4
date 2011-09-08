

class Board(object):
    def __init__(self):
        self.width = 7
        self.height = 6
        self.board = [[] for i in range(self.width)]

    def __repr__(self):
        lines = []

        print ' ',
        for col in range(self.width):
            print col,
        print

        for row_num in range(self.height):
            line = '|'
            for col in self.board:
                try:
                    line += ' ' + col[row_num]
                except IndexError:
                    line += ' _'
            line += ' |'
            lines.append(line)
        return '\n\n'.join(lines[::-1])

    def is_valid(self, col_num):
        if col_num < len(self.board) and col_num > -1:
            if len(self.board[col_num]) < self.height:
                return True
        return False

    def move(self,col_num, symbol):
        if self.is_valid(col_num):
            self.board[col_num].append(symbol)
        else:
            raise ValueError("Invalid move!")

    def is_full(self):
        return all(
            len(self.board[col]) == self.height
            for col in range(self.width)
        )
