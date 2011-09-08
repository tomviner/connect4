
def list_get(lst, index, default=None):
    try:
        return lst[index]
    except IndexError:
        return default


class Board(object):
    def __init__(self):
        self.width = 7
        self.height = 6
        self.board = [[] for i in range(self.width)]

    def __repr__(self):
        lines = []

        for row_num in range(self.height):
            line = '|'
            for col in self.board:
                line += ' ' + list_get(col, row_num, '_')
            line += ' |'
            lines.append(line)
            lines.append('')

        # header row of column numbers
        line = '  '
        for col in range(self.width):
            line += str(col) + ' '
        lines.append(line)

        return '\n'.join(lines[::-1])

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

    def connects(self, line, win=4, null_pieces=' '):
        run = 0
        token = ' '
        for piece in line:
            if piece == token[-1]:
                run += 1
                if run == 4 and piece not in null_pieces:
                    return piece
            else:
                run = 1
                token = piece
        return None

    def vert_win(self):
        for col in self.board:
            winner = self.connects(col)
            if winner:
                return winner
        return None

    def hori_win(self):
        for row_num in range(self.height):
            row = ''.join(list_get(col, row_num, ' ') for col in self.board)
            winner = self.connects(row)
            if winner:
                return winner
        return None

    def diag_win(self):
        #for direction in [-1, 1]:
        #    line = [list_get(col, col_num, ' ') for col, col_num in enumerate(self.board)]
        #    winner = self.connects(row)
        #    if winner:
        #        return winner
        return None

    def get_winner(self):
        return self.vert_win() or self.hori_win() or self.diag_win()

    def is_full(self):
        return all(
            len(self.board[col]) == self.height
            for col in range(self.width)
        )
