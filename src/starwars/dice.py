from abc import ABC, abstractmethod
from typing import List
import random

from starwars.dice_faces import (BOOST, PROFICIENCY, ABILITY,
                                 SETBACK, DIFFICULTY, CHALLENGE)
from starwars.dice_faces import dice_data
import starwars.types as types


class Dice(ABC):
    faces: types.DiceList
    adjacency: types.DiceDict
    _result: types.DiceTupleOrNone
    _adjacent_faces = types.DiceListOrNone

    @abstractmethod
    def __init__(self, dice_ref: str = None):
        self.faces, self.adjacency = dice_data(dice_ref)
        self._result = None
        self._adjacent_faces = None

    def roll(self) -> types.DiceTuple:
        self._result = random.choice(self.faces)

        possible_faces = [self.adjacency[key] for key in self.adjacency if key[1] == self._result]
        self._adjacent_faces = random.choice(possible_faces)

        return self._result

    @property
    def result(self) -> types.DiceTupleOrNone:
        return self._result

    @result.setter
    def result(self, result):
        self._result = result

    @property
    def adjacent_faces(self) -> types.DiceListOrNone:
        return self._adjacent_faces

    @adjacent_faces.setter
    def adjacent_faces(self, adj):
        self._adjacent_faces = adj

    def __str__(self):
        return f"{type(self).__name__}: {'Unrolled' if self._result is None else self._result}"


class Boost(Dice):
    def __init__(self):
        super().__init__(dice_ref=BOOST)


class Ability(Dice):
    def __init__(self):
        super().__init__(dice_ref=ABILITY)


class Proficiency(Dice):
    def __init__(self):
        super().__init__(dice_ref=PROFICIENCY)


class Setback(Dice):
    def __init__(self):
        super().__init__(dice_ref=SETBACK)


class Difficulty(Dice):
    def __init__(self):
        super().__init__(dice_ref=DIFFICULTY)


class Challenge(Dice):
    def __init__(self):
        super().__init__(dice_ref=CHALLENGE)


def string_to_dice_list(string: str) -> List[Dice]:
    """
    b: boost
    a: ability
    p: proficiency
    s: setback
    d: difficulty
    c: challenge
    :param string: Any string, only listed characters will count.
    :return: list of instantiated dice objects.
    """
    return [Boost() for _ in range(string.count('b'))] + \
           [Ability() for _ in range(string.count('a'))] + \
           [Proficiency() for _ in range(string.count('p'))] + \
           [Setback() for _ in range(string.count('s'))] + \
           [Difficulty() for _ in range(string.count('d'))] + \
           [Challenge() for _ in range(string.count('c'))]
