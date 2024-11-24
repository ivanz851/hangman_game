from textwrap import dedent

HANGMAN_PARTS = ['O', '|', '/', '\\', '/', '\\']
DIFFICULTY_LEVELS = [6, 3, 2, 1]
MAX_DIFFICULTY = len(DIFFICULTY_LEVELS)


class HangmanRepresentation:
    def __init__(self):
        self.hangman_parts_drawn = [' '] * DIFFICULTY_LEVELS[0]

    def update_hangman_parts(self, mistakes, difficulty) -> None:
        """
        Updates the hangman picture depending on the error number and difficulty level.
        Args:
            mistakes (int): number of mistakes made.
            difficulty (int): Difficulty level, from 1 to MAX_DIFFICULTY.
        """
        parts_per_mistake = DIFFICULTY_LEVELS[0] // DIFFICULTY_LEVELS[difficulty-1]
        end = mistakes * parts_per_mistake
        self.hangman_parts_drawn[0:end] = HANGMAN_PARTS[0:end]

    @property
    def hangman_picture(self) -> str:
        """
        Generates a string representing the current picture of the hangman.
        """
        return dedent(f"""\
        +---+
        |   |
        |   {self.hangman_parts_drawn[0]}
        |  {self.hangman_parts_drawn[2]}{self.hangman_parts_drawn[1]}{self.hangman_parts_drawn[3]}
        |  {self.hangman_parts_drawn[4]} {self.hangman_parts_drawn[5]}
        |
        =======
        """)

    def display(self) -> None:
        """
        Displays the current picture of the hangman in the console.
        """
        print(self.hangman_picture)

    @staticmethod
    def report_difficulty_levels() -> str:
        """
        Returns a string describing the difficulty levels and the maximum number of errors for each level.
        """
        message = "Difficulty levels:\n"
        for dif_level_ind, dif_level_val in enumerate(DIFFICULTY_LEVELS):
            message += f"{dif_level_ind + 1} - {dif_level_val} mistakes\n"
        return message
