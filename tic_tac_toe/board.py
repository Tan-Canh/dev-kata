class Board(object):
    def __init__(self, rows=3, cols=3):
        self._board = [[0] * cols] * rows

    def update_board(self, x, y, token):
        if x > len(self._board[0]) or y > len(self._board):
            raise ValueError("Invalid position")
        if self._board[x][y]:
            raise ValueError("Field is not empty")
        row = list(self._board[x])
        row[y] = token
        self._board[x] = list(row)

    def is_game_over(self, token):
        if self._is_board_filled():
            return None
        if (
            self._is_diagonal_filled(token)
            or self._is_vertical_filled(token)
            or self._is_horizontal_filled(token)
        ):
            return True
        return False

    def _is_board_filled(self):
        for row in self._board:
            for value in row:
                if value == 0:
                    return False
        return True

    def _is_diagonal_filled(self, token):
        diagonal = [r[i] for i, r in enumerate(self._board)]
        counter_diagonal = [r[i] for i, r in enumerate(self._board[::-1])]
        if self.is_array_filled(diagonal, token) or self.is_array_filled(counter_diagonal, token):
            return True
        return False

    def _is_horizontal_filled(self, token):
        for row in self._board:
            if self.is_array_filled(row, token):
                return True
        return False

    def _is_vertical_filled(self, token):
        flipped_board = list(zip(*self._board))
        for row in flipped_board:
            if self.is_array_filled(row, token):
                return True
        return False

    @staticmethod
    def is_array_filled(array, token):
        return array.count(token) == len(array)
    
    def show_board(self):
        for row in self._board:
            for val in row:
                print('{:4}'.format(val))
            print()
