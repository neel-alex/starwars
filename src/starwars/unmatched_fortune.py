import itertools

from starwars.mutable_pool import MutablePool


class UnmatchedFortune(MutablePool):
    def __init__(self, pool, *args, num_dice=3, negative=True, **kwargs):

        super().__init__(pool, *args, **kwargs)
        self.num_dice = num_dice
        self.negative = negative

    @staticmethod
    def diff_result(res1, res2):
        return tuple(x - y for x, y in zip(res1, res2))

    def fortune(self, succeed=True, no_despair=False,
                maximize_order=None):
        if maximize_order is None:
            maximize_order = ["Advantage", "Success", "Triumph", "Despair"]
        # Strategy: compile all possible flips, ordered by how well they accomplish the maximize objective
        #           rule out the ones that don't apply if there's no success, then select the remaining max
        assert all(m in {"Advantage", "Success", "Triumph", "Despair"} for m in maximize_order)
        max_indices = {"Success": 0, "Advantage": 1, "Triumph": 2, "Despair": 3}

        maximize_order = [max_indices[m] for m in maximize_order]
        result = super().result()
        pool = self.get_pool()
        flips = {i: [] for i in range(len(pool))}

        for i, d in enumerate(pool):
            flips[i] = [UnmatchedFortune.diff_result(adjacent, d.result)
                        for adjacent in d.adjacent_faces]

        # Only consider "reasonable" flips, i.e. the ones that improve in one axis.
        for i, d in enumerate(flips):
            flips[i] = [f for f in flips[i] if not all(n <= 0 for n in f)]

        possible_fortunes = []
        for dice_selected in itertools.combinations(flips, self.num_dice):
            dice_flips = [flips[i] for i in dice_selected]
            for flips_selected in itertools.product(*dice_flips):
                flip_difference = self.pool.sum_results(flips_selected)
                possible_fortunes.append(self.pool.sum_results([result, flip_difference]))

        if succeed:
            possible_fortunes = [pf for pf in possible_fortunes if pf[0] > 0]
        if no_despair:
            possible_fortunes = [pf for pf in possible_fortunes if pf[3] == 0]

        for m in maximize_order:
            max_objective = max(possible_fortunes, key=lambda x: x[m])[m]
            possible_fortunes = [pf for pf in possible_fortunes if pf[m] == max_objective]

        return possible_fortunes[0]


"""
import starwars.dice as dice
from starwars.double_or_nothing import DoubleOrNothing
from starwars.dice_pool import DicePool
from starwars.mutable_pool import MutablePool
from starwars.unmatched_fortune import UnmatchedFortune
d = DicePool(*dice.string_to_dice_list("pppaaccddbbs"))
uf = UnmatchedFortune(d)

_ = uf.roll()
l = uf.fortune()
print(l)

for dd, flip in zip(uf.get_pool(), uf.fortune()):
    print(dd, "::", flip)

"""
