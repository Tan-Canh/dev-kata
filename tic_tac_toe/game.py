from .board import Board


class Game(object):
    is_over = False
    winner = None

    def __init__(self, board: Board):
        self._board = board
        self._player = 1

    def _get_token(self):
        return "x" if self._player == 1 else "o"

    def _next_player(self):
        return 2 if self._player == 1 else 1

    def check_at(self, x, y):
        if self.is_over:
            raise AssertionError('Game is Over')
        self._board.update_board(x, y, self._get_token())
        self._check_game_over()

    def show_result(self):
        self._board.show_board()
        if self.is_over:
            print(self._get_winner())

    def _get_winner(self):
        if self.winner is None:
            return "Tie"
        return f"Player {self.winner}"

    def _check_game_over(self):
        is_x_win = self._board.is_game_over(token='x')
        is_y_win = self._board.is_game_over(token='y')
        self.is_over = is_x_win or is_y_win
        if self.is_over is None:
            self.is_over = True
            return
        if self.is_over:
            self.winner = 1 if is_x_win else 2
