import unittest

from src.hangman_representation import HangmanRepresentation


class TestHangmanRepresentation(unittest.TestCase):
    def test_update_hangman_parts(self):
        hangman = HangmanRepresentation()
        hangman.update_hangman_parts(mistakes=1, difficulty=1)
        expected_result_1 = ['O', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual(hangman.hangman_parts_drawn, expected_result_1)

        hangman = HangmanRepresentation()
        hangman.update_hangman_parts(mistakes=5, difficulty=1)
        expected_result_1 = ['O', '|', '/', '\\', '/', ' ']
        self.assertEqual(hangman.hangman_parts_drawn, expected_result_1)

        hangman = HangmanRepresentation()
        hangman.update_hangman_parts(mistakes=6, difficulty=1)
        expected_result_1 = ['O', '|', '/', '\\', '/', '\\']
        self.assertEqual(hangman.hangman_parts_drawn, expected_result_1)

        hangman = HangmanRepresentation()
        hangman.update_hangman_parts(mistakes=1, difficulty=2)
        expected_result_1 = ['O', '|', ' ', ' ', ' ', ' ']
        self.assertEqual(hangman.hangman_parts_drawn, expected_result_1)

        hangman = HangmanRepresentation()
        hangman.update_hangman_parts(mistakes=2, difficulty=2)
        expected_result_1 = ['O', '|', '/', '\\', ' ', ' ']
        self.assertEqual(hangman.hangman_parts_drawn, expected_result_1)

        hangman = HangmanRepresentation()
        hangman.update_hangman_parts(mistakes=3, difficulty=2)
        expected_result_1 = ['O', '|', '/', '\\', '/', '\\']
        self.assertEqual(hangman.hangman_parts_drawn, expected_result_1)

        hangman = HangmanRepresentation()
        hangman.update_hangman_parts(mistakes=1, difficulty=3)
        expected_result_1 = ['O', '|', '/', ' ', ' ', ' ']
        self.assertEqual(hangman.hangman_parts_drawn, expected_result_1)

        hangman = HangmanRepresentation()
        hangman.update_hangman_parts(mistakes=2, difficulty=3)
        expected_result_1 = ['O', '|', '/', '\\', '/', '\\']
        self.assertEqual(hangman.hangman_parts_drawn, expected_result_1)

        hangman = HangmanRepresentation()
        hangman.update_hangman_parts(mistakes=1, difficulty=4)
        expected_result_1 = ['O', '|', '/', '\\', '/', '\\']
        self.assertEqual(hangman.hangman_parts_drawn, expected_result_1)

        hangman = HangmanRepresentation()
        hangman.update_hangman_parts(mistakes=0, difficulty=4)
        expected_result_1 = [' ', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual(hangman.hangman_parts_drawn, expected_result_1)


if __name__ == '__main__':
    unittest.main()
