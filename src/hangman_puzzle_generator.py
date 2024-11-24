import random
from enum import StrEnum
from textwrap import dedent

from src.hangman_representation import MAX_DIFFICULTY
from src.hangman_puzzle import Puzzle, HangmanPuzzle


class Category(StrEnum):
    ANIMALS = "animals"
    FRUITS = "fruits"
    NATURE = "nature"
    RANDOM_FLAG = "random"


PUZZLES_BY_CATEGORY_LIST = {
    Category.ANIMALS: [
        Puzzle(
            word="bat",
            hint="I sleep by day and fly at night, but I have no feathers to aid my flight."
        ),
        Puzzle(
            word="lion",
            hint="A king without a crown."
        ),
        Puzzle(
            word="shark",
            hint=dedent("""\
            Some people are scared of this creature,
            Because it can have a big bite.
            So be careful out in the ocean,
            One of its kind is a Great White.
            """)
        ),
        Puzzle(
            word="turtle",
            hint=dedent("""\
            With four oars it swims but it is always at home.
            Its back is like armor, tougher than chrome.
            """)
        ),
        Puzzle(
            word="elephant",
            hint=dedent("""\
            I’m an animal you might love But I’m too big to be your pet
            I have an extremely long trunk.
            And it’s said I never forget.
            """)
        ),
        Puzzle(
            word="kangaroo",
            hint="It jumps when it walks and sits when it stands."
        ), ],
    Category.FRUITS: [
        Puzzle(
            word="strawberry",
            hint="I am a fruit with seeds on the outside."
        ),
        Puzzle(
            word="broccoli",
            hint="I'm a green veggie that looks like a tiny tree."
        ),
        Puzzle(
            word="potato",
            hint=dedent("""\
            A skin have I, more eyes than one.
            I can be very nice when I am done.
            """)
        ),
        Puzzle(
            word="carrot",
            hint="It is orange and sounds like a parrot."
        ),
        Puzzle(
            word="cherry",
            hint="I wear a red coat and have a stone in my throat."
        ),
        Puzzle(
            word="blueberry",
            hint="This fruit is always sad."
        ), ],
    Category.NATURE: [
        Puzzle(
            word="dandelion",
            hint="First you see me in the grass dressed in yellow gay; next I am in dainty white, then I fly away."
        ),
        Puzzle(
            word="tree",
            hint="It has lots of bark, but no bite?"
        ),
        Puzzle(
            word="astra",
            hint=dedent("""\
            Beautiful flowers
            Bloomed in the garden,
            Glittered colors
            And autumn is coming.
            """)
        ),
        Puzzle(
            word="wave",
            hint=dedent("""\
            The moon is my father. The sea is my mother.
            I have a million brothers. I die when I reach land.
            """)
        ),
        Puzzle(
            word="air",
            hint=dedent("""\
            I touch your face, I'm in your words,
            I'm lack of space and beloved by birds.
            """)
        ),
        Puzzle(
            word="asteroid",
            hint=dedent("""\
            Large as a mountain, small as a pea,
            Endlessly swimming in a waterless sea.
            """)
        ), ],
}


def gen_puzzle(category, difficulty) -> tuple[Category, int, HangmanPuzzle]:
    """
    Puzzle generation depending on the category and difficulty.

    Args:
        category (Category): Puzzle category (a string or Category.RANDOM_FLAG).
        difficulty (int | str): Puzzle difficulty (an int from 1 to MAX_DIFFICULTY or Category.RANDOM_FLAG).

    Returns:
        tuple[Category, int, HangmanPuzzle]: Generated puzzle category, generated puzzle difficulty,
        and the generated puzzle.
    """

    if category == Category.RANDOM_FLAG:
        category = random.choice([cat for cat in Category if cat != Category.RANDOM_FLAG])

    if difficulty == Category.RANDOM_FLAG:
        difficulty = random.randint(1, MAX_DIFFICULTY)

    puzzle = random.choice(PUZZLES_BY_CATEGORY_LIST[category])
    return category, difficulty, HangmanPuzzle(puzzle)
