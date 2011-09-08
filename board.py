

class Board(object):
    def __init__(self):
        self.board = [[]]*7

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
        return '\n\n'.join(lines)


