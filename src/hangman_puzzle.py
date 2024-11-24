from dataclasses import dataclass


@dataclass
class Puzzle:
    def __init__(self, word: str, hint: str):
        self._word = word
        self._hint = hint

    def get_word(self) -> str:
        return self._word

    def get_hint(self) -> str:
        return self._hint


class HangmanPuzzle:
    def __init__(self, puzzle: Puzzle):
        self._puzzle = puzzle
        self._is_guessed = False
        self._guessed_letters = set()
        self._guessed_part = ['_'] * len(self._puzzle.get_word())

    def process_letter(self, letter) -> tuple[bool, str]:
        """
        Processes the entered letter and returns the result:
        - bool: True if player made an error (the letter is not in the word)
        - str: Result message (player guessed the letter, or they have already asked about this letter)
        """
        message = ""
        got_mistake = False
        if letter in self._guessed_letters:
            message = self.remind_about_asked_letter(letter)
        else:
            self._guessed_letters.add(letter)
            if letter in self.get_puzzle().get_word():
                self.update_guessed_part(letter)
                message = "Hit!"
            else:
                got_mistake = True

        return got_mistake, message

    def remind_about_asked_letter(self, c) -> str:
        """
        Returns a message if player has already asked about given letter and whether it is contained in the hidden word.
        """
        message = "You have already asked about this letter!\n"
        if c in self.get_puzzle().get_word():
            message += "Hidden word contains it.\n"
        else:
            message += "Hidden word doesn't contain it.\n"
        return message

    def update_guessed_part(self, guess_letter) -> None:
        """
        Updates the guessed part of the word if the letter was guessed correctly.
        Checks if the whole word is guessed.
        """
        for pos, let in enumerate(self.get_puzzle().get_word()):
            if let == guess_letter:
                self._guessed_part[pos] = guess_letter
        if '_' not in self._guessed_part:
            self._is_guessed = True

    def get_puzzle(self) -> Puzzle:
        return self._puzzle

    def get_is_guessed(self) -> bool:
        return self._is_guessed

    def get_guessed_part(self) -> list[str]:
        return self._guessed_part[:]
