import unittest
from textwrap import dedent
from unittest.mock import patch

from src.hangman_puzzle_generator import gen_puzzle, Category, PUZZLES_BY_CATEGORY_LIST


class TestGenPuzzle(unittest.TestCase):
    @patch('random.choice')
    @patch('random.randint')
    def test_gen_puzzle_with_random_category_and_difficulty(self, mock_randint, mock_choice):
        mock_choice.side_effect = [Category.ANIMALS, PUZZLES_BY_CATEGORY_LIST[Category.ANIMALS][0]]
        mock_randint.return_value = 3

        category, difficulty, puzzle = gen_puzzle(Category.RANDOM_FLAG, Category.RANDOM_FLAG)

        self.assertEqual(category, Category.ANIMALS)
        self.assertEqual(difficulty, 3)
        self.assertEqual(puzzle.get_puzzle().get_word(), "bat")
        self.assertEqual(puzzle.get_puzzle().get_hint(), "I sleep by day and fly at night, but I have no feathers to "
                                                         "aid my flight.")

    @patch('random.choice')
    @patch('random.randint')
    def test_gen_puzzle_with_fixed_category_and_random_difficulty(self, mock_randint, mock_choice):
        mock_choice.return_value = PUZZLES_BY_CATEGORY_LIST[Category.FRUITS][1]
        mock_randint.return_value = 4

        category, difficulty, puzzle = gen_puzzle(Category.FRUITS, Category.RANDOM_FLAG)

        self.assertEqual(category, Category.FRUITS)
        self.assertEqual(difficulty, 4)
        self.assertEqual(puzzle.get_puzzle().get_word(), "broccoli")
        self.assertEqual(puzzle.get_puzzle().get_hint(), "I'm a green veggie that looks like a tiny tree.")

    @patch('random.choice')
    def test_gen_puzzle_with_fixed_category_and_difficulty(self, mock_choice):
        mock_choice.return_value = PUZZLES_BY_CATEGORY_LIST[Category.NATURE][4]

        category, difficulty, puzzle = gen_puzzle(Category.NATURE, 2)

        self.assertEqual(category, Category.NATURE)
        self.assertEqual(difficulty, 2)
        self.assertEqual(puzzle.get_puzzle().get_word(), "air")
        self.assertEqual(puzzle.get_puzzle().get_hint(),
                         dedent("""\
                            I touch your face, I'm in your words,
                            I'm lack of space and beloved by birds.\n"""))


if __name__ == '__main__':
    unittest.main()
