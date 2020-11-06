from typing import cast, List

import starwars.dice as dice
import starwars.types as types


class DicePool:
    pool: List[dice.Dice]

    def __init__(self, *dice_list: dice.Dice):
        self.pool = list(dice_list)

    @staticmethod
    def sum_results(results: types.DiceList) -> types.DiceTuple:
        """
        :param results: (iterable) tuples of numbers
        :return: (tuple) element-wise sum of the tuples
        """
        result = tuple([int(sum(category)) for category in zip(*results)])
        return cast(types.DiceTuple, result)

    def roll(self) -> types.DiceTuple:
        """
        Rolls all dice in the pool (potentially deleting earlier results)
        :return: (tuple) sum of rolled dice
        """
        results = [d.roll() for d in self.pool]
        return self.sum_results(results)

    def result(self) -> types.DiceTuple:
        """
        Current result of the dice pool, use to check value without rolling.
        :return: (tuple) sum of rolled dice
        """
        results = [d.result for d in self.pool]
        assert all(result is not None for result in results),\
            "Some dice in the dice pool have not been rolled!"
        return self.sum_results(results)

    def get_pool(self):
        return self.pool

    def __str__(self):
        return self.print_results(self.result())

    @staticmethod
    def print_results(result: types.DiceTuple) -> str:
        """
        Prints the results of a roll nicely.
        :param result: (tuple) 4-tuple of ints
            representing (successes, advantages, triumphs, despairs)
        :return: (string) Formatted string that describes the result of the dice pool.
        """
        final_string = ""
        if result[0] > 0:
            final_string += f"Check succeeded with {result[0]} success{'es' if result[0] != 1 else ''}!\n"
        elif result[0] == 0:
            final_string += f"Check failed! No successes generated.\n"
        else:
            final_string += f"Check failed with {abs(result[0])} failure{'s' if result[0] != -1 else ''}!\n"
        final_string += "\n"

        if result[1] > 0:
            final_string += f"Created {result[1]} advantage{'s' if result[1] != 1 else ''}.\n"
        elif result[1] == 0:
            final_string += f"No advantages or threats were found.\n"
        else:
            final_string += f"Beware, discovered {abs(result[1])} threat{'s' if result[1] != -1 else ''}.\n"

        for _ in range(result[2]):
            final_string += "Triumph!\n"

        for _ in range(result[3]):
            final_string += "Despair!\n"

        return final_string
