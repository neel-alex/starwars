import starwars.pool_wrapper as wrapper
import starwars.dice as dice
import starwars.types as types
import starwars.util as util


class MutablePool(wrapper.PoolWrapper):
    def __init__(self, pool, *args, **kwargs):
        super().__init__(pool, *args, **kwargs)

    def upgrade_ability(self):
        """
        Upgrades the positive dice in the pool. If there are green (ability) dice,
            replaces one with a yellow (proficiency) die. Otherwise, adds a green
            die.
        """
        dp = self.get_pool()
        for d in dp:
            if type(d) == dice.Ability:
                dp.remove(d)
                self.add_dice(dice.Proficiency())
                return
        self.add_dice(dice.Ability())

    def upgrade_difficulty(self):
        """
        Upgrades the negative dice in the pool. If there are purple (difficulty) dice,
            replaces one with a red (challenge) die. Otherwise, adds a purple die.
        """
        dp = self.get_pool()
        for d in dp:
            if type(d) == dice.Difficulty:
                dp.remove(d)
                self.add_dice(dice.Challenge())
                return
        self.add_dice(dice.Difficulty())
    """
    def downgrade_ability(self):
        
        Inverse of upgrading. If there's a green, take it away, otherwise 
        
        dp = self.get_pool()
        for d in dp:
            if type(d) == dice.Difficulty:
                dp.remove(d)
                self.add_dice(dice.Challenge())
                return
        self.add_dice(dice.Difficulty())

    def downgrade_difficulty(self):
        dp = self.get_pool()
        for d in dp:
            if type(d) == dice.Difficulty:
                dp.remove(d)
                self.add_dice(dice.Challenge())
                return
        self.add_dice(dice.Difficulty())
    """
    def add_dice(self, *dice_list: dice.Dice):
        """
        Adds dice to the pool.
        :param dice_list: list of new dice to add to the pool.
        """
        dp = self.get_pool()
        dp.extend(dice_list)

    def roll_unrolled(self) -> types.DiceTuple:
        """
        Rolls dice that haven't yet been rolled. Meant to be used after add_dice.
        :return: sum of only the unrolled dice - use result() if you want the new total.
        """
        results = [d.roll() for d in self.get_pool() if d.result is None]
        return util.sum_results(*results)
