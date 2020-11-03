from starwars.dice import Boost, Ability, Proficiency, Setback, Difficulty, Challenge


class DicePool:
    def __init__(self, *dice):
        self.dice_pool = list(dice)

    @staticmethod
    def sum_results(results):
        """
        :param results: (iterable) tuples of numbers
        :return: (tuple) element-wise sum of the tuples
        """
        return (sum(category) for category in zip(*results))

    def roll(self):
        """
        Rolls all dice in the pool (potentially deleting earlier results)
        :return: (tuple) sum of rolled dice
        """
        results = [dice.roll() for dice in self.dice_pool]
        return self.sum_results(results)

    def add_dice(self, *dice):
        """
        Adds dice to the pool.
        :param dice: list of new dice to add to the pool.
        """
        self.dice_pool += list(dice)

    def result(self):
        """
        Current result of the dice pool, use to check value without rolling.
        :return: (tuple) sum of rolled dice
        """
        results = [dice.result() for dice in self.dice_pool]
        assert all(result is not None for result in results),\
            "Some dice in the dice pool have not been rolled!"
        return self.sum_results(results)

    def roll_unrolled(self):
        """
        Rolls dice that haven't yet been rolled. Meant to be used after add_dice.
        :return: sum of only the unrolled dice - use result() if you want the new total.
        """
        results = [dice.roll() for dice in self.dice_pool if dice.result is None]
        return self.sum_results(results)

    def print(self):
        return self.print_results(self.result())

    @staticmethod
    def print_results(result):
        """
        Prints the results of a roll nicely.
        :param result: (tuple) 4-tuple of ints
            representing (successes, advantages, triumphs, despairs)
        :return: (string) Formatted string that describes the result of the dice pool.
        """
        final_string = ""
        if result[0] > 0:
            final_string += f"Check succeeded with {result[0]} successes!\n"
        elif result[0] == 0:
            final_string += f"Check failed! No successes generated.\n"
        else:
            final_string += f"Check failed with {abs(result[0])} failures!\n"
        final_string += "\n"

        if result[1] > 0:
            final_string += f"Additionally, made {result[1]} advantages.\n"
        elif result[1] == 0:
            final_string += f"No advantages or threats were made.\n"
        else:
            final_string += f"Beware, made {abs(result[1])} threats.\n"

        for _ in range(len(result[2])):
            final_string += "Triumph!\n"

        for _ in range(len(result[3])):
            final_string += "Despair!\n"

        return final_string
