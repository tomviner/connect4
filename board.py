

class Board(object):
    def __init__(self):
        self.board = [[] for i in range(7)] 

    def __repr__(self):
        lines = []
        for row_num in range(6):
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
            if len(self.board[col_num]) < 7:
                return True
        return False

    def move(self,col_num, symbol):
        if self.is_valid(col_num):
            self.board[col_num].append(symbol)
        else:
            raise ValueError("Invalid move!")
