import unittest
from textwrap import dedent
from unittest.mock import patch, MagicMock

from src.hangman_game import set_category, set_difficulty, HangmanGame
from src.hangman_puzzle import HangmanPuzzle, Puzzle
from src.hangman_puzzle_generator import Category
from src.hangman_representation import MAX_DIFFICULTY, DIFFICULTY_LEVELS


class TestSetup(unittest.TestCase):
    @patch('builtins.input', side_effect=['animals'])
    def test_set_category_valid(self, mock_input):
        category = set_category()
        self.assertEqual(category, 'animals')

    @patch('builtins.input', side_effect=['rAndoM'])
    def test_set_category_random(self, mock_input):
        category = set_category()
        self.assertEqual(category, Category.RANDOM_FLAG)

    @patch('builtins.input', side_effect=['invalid', 'fruits'])
    def test_set_category_invalid_then_valid(self, mock_input):
        category = set_category()
        self.assertEqual(category, 'fruits')

    @patch('builtins.input', side_effect=['3'])
    def test_set_difficulty_valid(self, mock_input):
        difficulty = set_difficulty()
        self.assertEqual(difficulty, 3)

    @patch('builtins.input', side_effect=[str(MAX_DIFFICULTY)])
    def test_set_difficulty_max(self, mock_input):
        difficulty = set_difficulty()
        self.assertEqual(difficulty, MAX_DIFFICULTY)

    @patch('builtins.input', side_effect=['RanDoM'])
    def test_set_difficulty_random(self, mock_input):
        difficulty = set_difficulty()
        self.assertEqual(difficulty, Category.RANDOM_FLAG)

    @patch('builtins.input', side_effect=['-10', '2'])
    def test_set_difficulty_invalid_then_valid(self, mock_input):
        difficulty = set_difficulty()
        self.assertEqual(difficulty, 2)


class TestInitGame(unittest.TestCase):
    @patch('src.hangman_game.set_category', return_value=Category.ANIMALS)
    @patch('src.hangman_game.set_difficulty', return_value=3)
    @patch('src.hangman_game.gen_puzzle',
           return_value=(Category.ANIMALS, 3, HangmanPuzzle(Puzzle("lion", "A king without a crown."))))
    def test_init_game(self, mock_set_category, mock_set_difficulty, mock_gen_puzzle):
        game = HangmanGame()
        difficulty = game.init_game()

        self.assertEqual(difficulty, 3)
        self.assertEqual(game.hangman_puzzle.get_puzzle().get_word(), "lion")
        self.assertEqual(game.max_mistakes, DIFFICULTY_LEVELS[2])

        mock_set_category.assert_called_once()
        mock_set_difficulty.assert_called_once()
        mock_gen_puzzle.assert_called_once()


class TestPlayGame(unittest.TestCase):
    @patch('builtins.input', side_effect=['l', 'i', 'o', 'n'])
    @patch('src.hangman_game.clear_console', return_value=None)
    @patch('src.hangman_game.HangmanGame.init_game', return_value=3)
    def test_play_game_win(self, mock_init_game, mock_clear, mock_input):
        game = HangmanGame()

        game.hangman_puzzle = MagicMock(spec=HangmanPuzzle)
        game.hangman_puzzle.get_puzzle().get_word.return_value = "lion"
        game.hangman_puzzle.get_puzzle().get_hint.return_value = "A king without a crown."

        game.hangman_puzzle.get_is_guessed.side_effect = [False, False, False, True] + [
            True] * 10
        game.hangman_puzzle.get_guessed_part.side_effect = ['l____', 'li___', 'lio__', 'lion']

        game.hangman_puzzle.process_letter.side_effect = [
            (False, "Hit!"),
            (False, "Hit!"),
            (False, "Hit!"),
            (False, "Hit!")
        ]

        game.max_mistakes = 5
        game.mistakes = 0

        game.hangman_representation = MagicMock()

        game.play_game()
        self.assertTrue(game.hangman_puzzle.get_is_guessed())
        self.assertEqual(game.mistakes, 0)
        game.hangman_representation.update_hangman_parts.assert_not_called()

    @patch('builtins.input', side_effect=['x', 'y', 'l', 'i', 'o', 'n'])
    @patch('src.hangman_game.clear_console', return_value=None)
    @patch('src.hangman_game.HangmanGame.init_game', return_value=3)
    def test_play_game_with_mistakes(self, mock_init_game, mock_clear, mock_input):
        game = HangmanGame()

        game.hangman_puzzle = MagicMock(spec=HangmanPuzzle)
        game.hangman_puzzle.get_puzzle().get_word.return_value = "lion"
        game.hangman_puzzle.get_puzzle().get_hint.return_value = "A king without a crown."

        game.hangman_puzzle.get_is_guessed.side_effect = [False, False, False, False, False, True] + [
            True] * 10
        game.hangman_puzzle.get_guessed_part.side_effect = ['____', '____', 'l___', 'li__', 'lio_', 'lion']

        game.hangman_puzzle.process_letter.side_effect = [
            (True, ""),
            (True, ""),
            (False, "Hit!"),
            (False, "Hit!"),
            (False, "Hit!"),
            (False, "Hit!")
        ]

        game.max_mistakes = 5
        game.mistakes = 0

        game.hangman_representation = MagicMock()

        game.play_game()
        self.assertTrue(game.hangman_puzzle.get_is_guessed())
        self.assertEqual(game.mistakes, 2)
        self.assertEqual(game.hangman_representation.update_hangman_parts.call_count, 2)


class TestSumUpTheGame(unittest.TestCase):
    @patch('builtins.print')
    def test_sum_up_the_game_win(self, mock_print):
        game = HangmanGame()
        game.hangman_puzzle = HangmanPuzzle(Puzzle("lion", "A king without a crown."))
        game.hangman_puzzle._is_guessed = True
        game.mistakes = 2
        game.max_mistakes = 5

        game.sum_up_the_game()

        mock_print.assert_any_call(dedent("""\
            You won!
            The hidden word is lion.
            Final score is 16.
            """).strip())


if __name__ == '__main__':
    unittest.main()
