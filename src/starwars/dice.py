from abc import ABC, abstractmethod
import random

from starwars.dice_faces import (BOOST, PROFICIENCY, ABILITY,
                                 SETBACK, DIFFICULTY, CHALLENGE,
                                 dice_data,)
from starwars.types import (DiceTuple, DiceList, DiceDict,
                            DiceTupleOrNone, DiceListOrNone)


class Dice(ABC):
    faces: DiceList
    adjacency: DiceDict
    _result: DiceTupleOrNone
    _adjacent_faces = DiceListOrNone

    @abstractmethod
    def __init__(self, dice_ref: str = None):
        self.faces, self.adjacency = dice_data(dice_ref)
        self._result = None
        self._adjacent_faces = None

    def roll(self) -> DiceTuple:
        self._result = random.choice(self.faces)

        possible_faces = [self.adjacency[key] for key in self.adjacency if key[1] == self._result]
        self._adjacent_faces = random.choice(possible_faces)

        return self._result

    @property
    def result(self) -> DiceTupleOrNone:
        return self._result

    @property
    def adjacent_faces(self) -> DiceListOrNone:
        return self._adjacent_faces

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
