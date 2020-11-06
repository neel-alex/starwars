import ast
from typing import Tuple

import starwars.types as types

BOOST = """
0: [A, 2A, S, SA]
0: [A, 2A, S, SA]
A: [0, 0, 2A, SA]
S: [0, 0, 2A, SA]
SA: [0, 0, S, A]
2A: [0, 0, S, A]
"""

ABILITY = """
2S: [S, SA, A]
S: [2S, A, 0]
A: [2S, 0, S]
SA: [2S, S, A]
A: [2A, S, SA]
0: [2A, S, A]
A: [2A, SA, A]
2A: [0, S, A]
"""

PROFICIENCY = """
T: [S, 2S, A, SA, 2A]
S: [T, 2S, 2A, SA, SA]
2S: [T, S, A, SA, 2A]
A: [T, 2S, 2A, S, SA]
SA: [T, A, S, 2A, 2S]
2A: [T, SA, 2S, SA, S]
SA: [SA, S, 2S, 2A, 0]
2A: [SA, 2A, A, S, 0]
S: [2A, A, SA, 2S, 0]
2S: [S, SA, 2A, SA, 0]
SA: [2S, 2A, S, SA, 0]
0: [S, 2A, SA, SA, 2S]
"""

SETBACK = """
0: [F, T, F, T]
0: [F, T, F, T]
F: [0, T, 0, T]
F: [0, T, 0, T]
T: [0, F, 0, F]
T: [0, F, 0, F]
"""

DIFFICULTY = """
2F: [T, T, 0]
T: [2F, F, 2T]
T: [2F, F, FT]
0: [2F, 2T, FT]
2T: [0, T, T]
F: [T, T, T]
FT: [0, T, T]
T: [F, FT, 2T]
"""

CHALLENGE = """
D: [F, T, 2F, FT, 2T]
F: [D, T, FT, 2F, 2T]
T: [D, F, FT, 2T, 2F]
2F: [D, T, 2T, F, FT]
FT: [D, 2F, F, T, 2T]
2T: [D, FT, T, 2F, F]
F: [0, T, FT, 2F, 2T]
T: [0, F, FT, 2T, 2F]
2F: [0, T, 2T, F, FT]
FT: [0, 2F, F, T, 2T]
2T: [0, FT, T, 2F, F]
0: [F, T, 2F, FT, 2T]
"""


positive_dice = (BOOST, ABILITY, PROFICIENCY)
negative_dice = (SETBACK, DIFFICULTY, CHALLENGE)


def positive_dice_parse(dice: str) -> str:
    """
    :param dice: Formatted string, where each line is blank or matches
                    t: [(t, )*t]
                    t = (0|T|2A|SA|2S|S|A)
                        (note: T stands for Triumph here)
    :return: Formatted string matching above, except tokens are replaced
                    with their corresponding values in the 4-tuple system,
                    (successes, advantages, triumphs, despairs)
    """
    return dice.replace("0", "(0, 0, 0, 0)")\
               .replace("T", "(1, 0, 1, 0)")\
               .replace("2A", "(0, 2, 0, 0)")\
               .replace("SA", "(1, 1, 0, 0)")\
               .replace("2S", "(2, 0, 0, 0)")\
               .replace("S", "(1, 0, 0, 0)")\
               .replace("A", "(0, 1, 0, 0)")


def negative_dice_parse(dice: str) -> str:
    """
    :param dice: Formatted string, where each line is blank or matches
                    t: [(t, )*t]
                    t = (0|D|2T|FT|2F|F|T)
                        (note: T stands for Threat here)
    :return: Formatted string matching above, except tokens are replaced
                    with their corresponding values in the 4-tuple system,
                    (successes, advantages, triumphs, despairs)
    """
    return dice.replace("0", "(0, 0, 0, 0)") \
               .replace("D", "(-1, 0, 0, 1)") \
               .replace("2T", "(0, -2, 0, 0)") \
               .replace("FT", "(-1, -1, 0, 0)") \
               .replace("2F", "(-2, 0, 0, 0)") \
               .replace("F", "(-1, 0, 0, 0)") \
               .replace("T", "(0, -1, 0, 0)")


def dice_str_to_dict(dice_string: str) -> types.DiceDict:
    """
    :param dice_string: output of (positive|negative)_dice_parse
    :return: (dict) dict, where keys are 2-tuples where the first entry is an int
                        and the second is a 4-tuple, and the values are lists of
                        4-tuples.
    """
    lines = [line for line in dice_string.split("\n") if line != '']
    for i, line in enumerate(lines):
        face, edges = line.split(":")
        face = f"({i}, {face})"
        lines[i] = ":".join((face, edges))
    dice_string = ",\n".join(lines)
    return ast.literal_eval("{" + dice_string + "}")


def get_faces(dice_dict: types.DiceDict) -> types.DiceList:
    """
    :param dice_dict: Output from dice_str_to_dict
    :return: The second entry of each key in the dict as a list. List of 4-tuples.
    """
    return [pair[1] for pair in dice_dict.keys()]


def dice_data(dice_string: str) -> Tuple[types.DiceList, types.DiceDict]:
    """
    Given a dice string (such as the above 4), parse into faces and the adjacency dictionary.
    :param dice_string: Formatted string, where each line is blank or matches
                    t: [(t, )*t]
                    t = (0|T|2A|SA|2S|S|A)
    :return: faces, adjacency dict
    """
    if dice_string in positive_dice:
        processed_string = positive_dice_parse(dice_string)
    elif dice_string in negative_dice:
        processed_string = negative_dice_parse(dice_string)
    else:
        raise ValueError(f"Cannot find dice string: {dice_string}\n" +
                         "Is it a valid dice code?\n" +
                         "Register it in dice_faces.py under positive or negative dice.")
    dice_dict = dice_str_to_dict(processed_string)
    return get_faces(dice_dict), dice_dict


def main():
    for dice in positive_dice:
        print(positive_dice_parse(dice))
        print()

    for dice in negative_dice:
        print(negative_dice_parse(dice))
        print()


if __name__ == "__main__":
    main()
