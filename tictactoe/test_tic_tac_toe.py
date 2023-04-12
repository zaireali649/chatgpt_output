import unittest
from unittest import mock
from unittest.mock import patch
from tic_tac_toe import tic_tac_toe, print_board, check_win, get_move

class TicTacToeTests(unittest.TestCase):

    def test_print_board(self):
        board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]
        with patch('builtins.print') as mock_print:
            print_board(board)
            calls = [mock.call('| X | O | X |'), mock.call('| O | X | O |'), mock.call('| X | O | X |')]
            mock_print.assert_has_calls(calls)

    def test_check_win_rows(self):
        board = [['X', 'X', 'X'], [' ', 'O', 'O'], [' ', ' ', ' ']]
        self.assertTrue(check_win(board, 'X', 3))

    def test_check_win_columns(self):
        board = [['X', ' ', 'O'], ['X', 'O', 'O'], ['X', ' ', ' ']]
        self.assertTrue(check_win(board, 'X', 3))

    def test_check_win_diagonal1(self):
        board = [['X', ' ', 'O'], [' ', 'X', 'O'], [' ', ' ', 'X']]
        self.assertTrue(check_win(board, 'X', 3))

    def test_check_win_diagonal2(self):
        board = [['O', 'O', 'X'], ['O', 'X', 'O'], ['X', ' ', 'X']]
        print(board)
        self.assertTrue(check_win(board, 'X', 3))

    def test_check_win_no_win(self):
        board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']]
        self.assertFalse(check_win(board, 'X', 3))

    def test_get_move_valid(self):
        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        with patch('builtins.input', side_effect=['0', '0']):
            row, col = get_move(board, 3, 3)
            self.assertEqual(row, 0)
            self.assertEqual(col, 0)

    def test_get_move_invalid(self):
        board = [['X', 'O', 'X'], ['O', 'X', 'O'], [' ', ' ', ' ']]
        with patch('builtins.input', side_effect=['3', '0']):
            self.assertRaises(ValueError, get_move, board, 3, 3)


    def test_tic_tac_toe_player1_wins(self):
        board = [['X', 'O', ' '], ['X', 'O', ' '], ['X', ' ', ' ']]
        with patch('builtins.input', side_effect=['3', '3', '3', '1', '0', '2', '2']):
            with patch('builtins.print') as mock_print:
                tic_tac_toe()
                calls = [mock.call('| X | O |   |'), mock.call('| X | O |   |'), mock.call('| X |   |   |'), mock.call('X wins!')]
                mock_print.assert_has_calls(calls)
    
    def test_tic_tac_toe_player2_wins(self):
        board = [['X', 'O', ' '], ['X', 'O', ' '], [' ', 'O', ' ']]
        with patch('builtins.input', side_effect=['2', '0', '1', '1', '2', '1', '0', '2']):
            with patch('builtins.print') as mock_print:
                tic_tac_toe()
                calls = [mock.call('| X | O |   |'), mock.call('| X | O |   |'), mock.call('|   | O |   |'), mock.call('O wins!')]
                mock_print.assert_has_calls(calls)

    def test_tic_tac_toe_draw(self):
        board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']]
        with patch('builtins.input', side_effect=['0', '2', '1', '1', '2', '1', '0', '0', '2']):
            with patch('builtins.print') as mock_print:
                tic_tac_toe()
                calls = [mock.call('| X | O | X |'), mock.call('| O | X | O |'), mock.call('| O | X | O |'), mock.call('The game is a draw.')]
                mock_print.assert_has_calls(calls)


    def test_tic_tac_toe_invalid_move(self):
        board = [['X', 'O', ' '], [' ', 'X', 'O'], [' ', ' ', ' ']]
        with patch('builtins.input', side_effect=['0', '2', '1', '2', '1', '1', '2', '2', '2']):
            with patch('builtins.print') as mock_print:
                tic_tac_toe()
                calls = [mock.call('| X | O |   |'), mock.call('|   | X | O |'), mock.call('|   | O | X |'), mock.call('Invalid move. Try again.')]
                mock_print.assert_has_calls(calls)

    def test_tic_tac_toe_empty_board(self):
        with patch('builtins.input', side_effect=['0', '0', '1', '1', '0', '1', '2', '2', '2', '0']):
            with patch('builtins.print') as mock_print:
                tic_tac_toe()
                calls = [mock.call('| X |   |   |'), mock.call('|   | O | X |'), mock.call('|   |   | O |'), mock.call('O wins!')]
                mock_print.assert_has_calls(calls)

if __name__ == '__main__':
    unittest.main()
