from typing import cast, List

import starwars.dice as dice
import starwars.types as types
import starwars.util as util


class DicePool:
    pool: List[dice.Dice]

    def __init__(self, *dice_list: dice.Dice):
        self.pool = list(dice_list)

    def roll(self) -> types.DiceTuple:
        """
        Rolls all dice in the pool (potentially deleting earlier results)
        :return: (tuple) sum of rolled dice
        """
        results = [d.roll() for d in self.pool]
        return util.sum_results(*results)

    def result(self) -> types.DiceTuple:
        """
        Current result of the dice pool, use to check value without rolling.
        :return: (tuple) sum of rolled dice
        """
        results = [d.result for d in self.pool]
        assert all(result is not None for result in results),\
            "Some dice in the dice pool have not been rolled!"
        return util.sum_results(*results)

    def get_pool(self):
        return self.pool

    def __str__(self):
        return util.stringify_results(self.result())
