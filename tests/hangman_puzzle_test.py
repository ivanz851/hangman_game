import unittest

from src.hangman_puzzle import Puzzle, HangmanPuzzle


class TestHangmanPuzzle(unittest.TestCase):
    def setUp(self):
        self.puzzle = Puzzle(word="apple", hint="A fruit")
        self.hangman_puzzle = HangmanPuzzle(self.puzzle)

    def test_process_correct_letter(self):
        got_mistake, message = self.hangman_puzzle.process_letter('a')
        self.assertFalse(got_mistake)
        self.assertEqual(message, "Hit!")
        self.assertEqual(self.hangman_puzzle.get_guessed_part(), ['a', '_', '_', '_', '_'])

    def test_process_incorrect_letter(self):
        got_mistake, message = self.hangman_puzzle.process_letter('z')
        self.assertTrue(got_mistake)
        self.assertEqual(message, "")
        self.assertEqual(self.hangman_puzzle.get_guessed_part(), ['_', '_', '_', '_', '_'])

    def test_remind_about_asked_letter_contained(self):
        self.hangman_puzzle.process_letter('a')
        got_mistake, message = self.hangman_puzzle.process_letter('a')
        self.assertFalse(got_mistake)
        self.assertEqual("You have already asked about this letter!\nHidden word contains it.\n", message)

    def test_remind_about_asked_letter_not_contained(self):
        self.hangman_puzzle.process_letter('b')
        got_mistake, message = self.hangman_puzzle.process_letter('b')
        self.assertFalse(got_mistake)
        self.assertEqual("You have already asked about this letter!\nHidden word doesn't contain it.\n", message)

    def test_game_won(self):
        for letter in "apple":
            self.hangman_puzzle.process_letter(letter)

        self.assertTrue(self.hangman_puzzle.get_is_guessed())
        self.assertEqual(self.hangman_puzzle.get_guessed_part(), ['a', 'p', 'p', 'l', 'e'])


if __name__ == '__main__':
    unittest.main()
