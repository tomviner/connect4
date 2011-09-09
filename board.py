
def list_get(lst, index, default=None, default_upon_neg_index=True):
    if index<0 and default_upon_neg_index:
        return default
    try:
        return lst[index]
    except IndexError:
        return default


class Board(object):
    def __init__(self, prepop_board=None):
        self.width = 7
        self.height = 6
        self.must_connect = 4
        self.board = prepop_board or [[] for i in range(self.width)]

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

    def connects(self, line, null_pieces=' '):
        run = 0
        token = ' '
        for piece in line:
            if piece == token[-1]:
                run += 1
                if run >= self.must_connect and piece not in null_pieces:
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
        """
        Iterate over each cell*, making a line all the way** up & right then again 
        up & left via direction=-1. i
        *Excluding a margin round 2 sides of the board where we'd be looking at lines shorter than self.must_connect
        **We actually only check at far as the diagonal of the largest square on the board
        """
        max_diag = min(self.width, self.height)
        for direction in (1, -1):
            for col_num in range(self.width-self.must_connect+1):
                for row_num in range(self.height-self.must_connect+1):
                    line = [list_get(
                                list_get(self.board[::direction], col_num+i, ' '), 
                            row_num+i, ' ') 
                        for i in range(max_diag)]
                    print 'diag:', line
                    winner = self.connects(line)
                    if winner:
                        return winner
        return None

    def get_winner(self):
        return self.vert_win() or self.hori_win() or self.diag_win()

    def is_full(self):
        return all(
            len(self.board[col]) == self.height
            for col in range(self.width)
        )
