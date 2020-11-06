from typing import List

import starwars.dice_pool as dice_pool
import starwars.dice as dice


class PoolWrapper(dice_pool.DicePool):
    pool: dice_pool.DicePool

    def __init__(self, pool: dice_pool.DicePool, *args, **kwargs):
        self.pool = pool

    def roll(self):
        return self.pool.roll()

    def result(self):
        return self.pool.result()

    def get_pool(self) -> List[dice.Dice]:
        return self.pool.get_pool()


