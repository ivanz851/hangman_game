import os
from textwrap import dedent

from src.hangman_puzzle import HangmanPuzzle
from src.hangman_puzzle_generator import Category, gen_puzzle
from src.hangman_representation import HangmanRepresentation, DIFFICULTY_LEVELS, MAX_DIFFICULTY
from enum import StrEnum


def clear_console() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def set_category() -> Category:
    """
    Asks user to select a category for the puzzle and checks the entered value.

    Returns:
        Category: Returns the user-selected category or Category.RANDOM_FLAG for a random category.
    """
    message = dedent(f"""
        Please, choose hidden word category.
        Available categories: {", ".join(list(Category))}. 
        To choose random category, print "random".
        """)
    print(message)

    while True:
        category = input().lower()
        try:
            category = Category(category)
            break
        except ValueError:
            print("ERROR! INVALID INPUT")

    print("ACCEPTED\n")
    return category


def set_difficulty() -> int | str:
    """
    Asks user to select puzzle difficulty and checks the entered value.

    Returns:
        int | str: Returns the selected difficulty level or "random" for random selection.
    """
    message = dedent(f"""
        Please, choose difficulty.
        Enter X - integer number from 1 to {MAX_DIFFICULTY}.\n
        To choose random difficulty, print "random".\n
        """)
    message += HangmanRepresentation.report_difficulty_levels()
    print(message)

    while True:
        difficulty = input().lower()
        if (difficulty.isdigit() and 1 <= int(difficulty) <= MAX_DIFFICULTY) or \
                difficulty == Category.RANDOM_FLAG:
            break
        else:
            print("ERROR! INVALID INPUT.\n")

    if difficulty != Category.RANDOM_FLAG:
        difficulty = int(difficulty)

    print("ACCEPTED\n")
    return difficulty


class SpecialCommand(StrEnum):
    """
    After selecting the category and difficulty of the puzzle, player can enter commands from the list below
    instead of the next letter to quit the game (STOP_WORD) or to get a clue (HELP_WORD).
    """
    STOP_WORD = "quit"
    HELP_WORD = "help"


def report_game_parameters_and_info(category: Category, difficulty: int) -> str:
    """
    Returns a string with information about the game parameters: the selected category, difficulty, and rules.
    """
    return dedent(f"""\
            OK! Chosen category: {category}.
            If you guess the word by making X mistakes, you will get 2^({DIFFICULTY_LEVELS[0]}-X) points
            If you make more than {DIFFICULTY_LEVELS[difficulty - 1]} mistakes, you lose!
            Enter '{SpecialCommand.STOP_WORD}' to quit.
            Enter '{SpecialCommand.HELP_WORD}' to get a clue.
            """)


class HangmanGame:
    """
    A class representing the "Hangman" game.
    It contains logic for initialization, playing and summarizing the game.
    """
    def __init__(self):
        self.current_score = None
        self.max_mistakes = None
        self.mistakes = None
        self.hangman_puzzle = None
        self.hangman_representation = None
        self.reset_game()

    def reset_game(self) -> None:
        self.hangman_puzzle = HangmanPuzzle
        self.mistakes = 0
        self.max_mistakes = 0
        self.current_score = 0
        self.hangman_representation = HangmanRepresentation()

    def play_game(self) -> None:
        """
        Basic game logic. The player enters letters to guess the word,
        or they use special commands to get a clue or quit the game.
        """
        difficulty = self.init_game()

        while self.mistakes < self.max_mistakes and not self.hangman_puzzle.get_is_guessed():
            print(dedent(f"""\
                The word: {''.join(self.hangman_puzzle.get_guessed_part())}
                Guess a letter:
                """))

            guess_string = input().lower().strip()
            clear_console()

            if guess_string == SpecialCommand.STOP_WORD:
                self.sum_up_the_game()
                return

            if guess_string == SpecialCommand.HELP_WORD:
                message = f"{self.hangman_puzzle.get_puzzle().get_hint()}\n"
            elif len(guess_string) == 1 and guess_string.isalpha():
                got_mistake, message = self.hangman_puzzle.process_letter(guess_string)
                if got_mistake:
                    self.mistakes += 1
                    message += f"Missed, mistake {self.mistakes} out of {self.max_mistakes}."
                    self.hangman_representation.update_hangman_parts(self.mistakes, difficulty)
                    self.hangman_representation.display()
            else:
                message = "Please, enter a single Latin letter.\n"
            print(message)

        self.sum_up_the_game()

    def init_game(self) -> int:
        """
        Initializes a new game: asks the user for the category and difficulty level,
        generates a puzzle, sets the number of acceptable errors.

        Returns:
            int: The difficulty level for the current game.
        """
        self.reset_game()
        print(self.report_game_intro())

        category = set_category()
        difficulty = set_difficulty()
        category, difficulty, self.hangman_puzzle = gen_puzzle(category, difficulty)
        self.max_mistakes = DIFFICULTY_LEVELS[difficulty - 1]

        print(report_game_parameters_and_info(category, difficulty))
        return difficulty

    @staticmethod
    def report_game_intro() -> str:
        return dedent("""\
            Welcome to Hangman game!
            Your goal is to guess the hidden word.
            The hidden word consists of small Latin letters.
            """)

    def sum_up_the_game(self) -> None:
        """
        Displays a message about victory or defeat, shows the hidden word and the final score.
        """
        message = ""
        if self.hangman_puzzle.get_is_guessed():
            message += "You won!\n"
            self.current_score += 1 << (DIFFICULTY_LEVELS[0] - self.mistakes)
        else:
            message += "You lost!\n"

        message += dedent(f"""\
            The hidden word is {self.hangman_puzzle.get_puzzle().get_word()}.
            Final score is {self.current_score}.
            """).strip()

        print(message)
