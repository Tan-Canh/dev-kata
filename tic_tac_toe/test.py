from unittest import TestCase

from tic_tac_toe.board import Board
from tic_tac_toe.game import Game


class TestTicTacToe(TestCase):
    def setUp(self):
        self.filled_board = [
            ['x', 'x', 'o'],
            ['o', 'o', 'x'],
            ['x', 'o', 'x']
        ]
        self.vertical_filled_board = [
            ['o', 'x', 0],
            [0, 'x', 'o'],
            [0, 'x', 'o']
        ]
        self.horizontal_filled_board = [
            ['y', 'y', 'y'],
            [0, 0, 'x'],
            ['x', 'x', 0]
        ]
        self.diagonal_filled_board = [
            ['x', 'y', 0],
            ['y', 'x', 0],
            ['y', 'y', 'x']
        ]
        self.counter_diagonal_filled_board = [
            ['x', 'x', 'y'],
            [0, 'y', 'x'],
            ['y', 0, 0]
        ]

    def _init_board(self):
        self.board = Board()
        self.game = Game(board=self.board)

    def _load_board(self, fixture):
        self.board._board = fixture

    def test_it_should_update_board_correctly(self):
        x, y = 0, 0
        self._init_board()

        self.game.check_at(x, y)
        self.assertIsNotNone(self.board._board[x][y])

    def test_it_should_raise_error_when_position_is_invalid(self):
        x, y = 4, 4
        self._init_board()
        self.assertRaises(ValueError, self.game.check_at, x, y)

    def test_it_should_raise_error_when_position_is_not_empty(self):
        x, y = 0, 0
        self._init_board()

        self.game.check_at(x, y)
        self.assertRaises(ValueError, self.game.check_at, x, y)

    def test_it_should_over_if_board_is_filled(self):
        self._init_board()
        self._load_board(self.filled_board)
        self.game._check_game_over()
        self.assertEqual(self.game.is_over, True)
        self.assertEqual(self.game.winner, None)

    def test_it_should_over_if_board_is_vertical_filled(self):
        self._init_board()
        self._load_board(self.vertical_filled_board)
        self.game._check_game_over()

        self.assertEqual(self.game.is_over, True)
        self.assertEqual(self.game.winner, 1)

    def test_it_should_over_if_board_is_horizontal_filled(self):
        self._init_board()
        self._load_board(self.horizontal_filled_board)
        self.game._check_game_over()

        self.assertEqual(self.game.is_over, True)
        self.assertEqual(self.game.winner, 2)

    def test_it_should_over_if_board_is_diagonal_filled(self):
        self._init_board()
        self._load_board(self.diagonal_filled_board)
        self.game._check_game_over()

        self.assertEqual(self.game.is_over, True)
        self.assertEqual(self.game.winner, 1)

    def test_it_should_over_if_board_is_counter_dian_filled(self):
        self._init_board()
        self._load_board(self.counter_diagonal_filled_board)
        self.game._check_game_over()

        self.assertEqual(self.game.is_over, True)
        self.assertEqual(self.game.winner, 2)
