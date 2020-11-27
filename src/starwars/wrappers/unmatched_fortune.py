import itertools

from starwars.wrappers.mutable_pool import MutablePool
import starwars.util as util


class UnmatchedFortune(MutablePool):
    def __init__(self, pool, *args, num_dice=3, negative=True, **kwargs):

        super().__init__(pool, *args, **kwargs)
        self.num_dice = num_dice
        self.negative = negative

    @staticmethod
    def get_max_order(maximize_order=None):
        if maximize_order is None:
            maximize_order = ["Advantage", "Success", "Triumph", "Despair"]
        # Strategy: compile all possible flips, ordered by how well they accomplish the maximize objective
        #           rule out the ones that don't apply if there's no success, then select the remaining max
        assert all(m in {"Advantage", "Success", "Triumph", "Despair"} for m in maximize_order)
        max_indices = {"Success": 0, "Advantage": 1, "Triumph": 2, "Despair": 3}

        return [max_indices[m] for m in maximize_order]

    @staticmethod
    def get_flips(pool):
        flips = {i: [] for i in range(len(pool))}

        for i, d in enumerate(pool):
            flips[i] = [util.diff_result(adjacent, d.result)
                        for adjacent in d.adjacent_faces]

        # Only consider "reasonable" flips, i.e. the ones that improve in one axis.
        for i, d in enumerate(flips):
            flips[i] = [f for f in flips[i] if not all(n <= 0 for n in f)]

        return flips

    @staticmethod
    def generate_fortunes(num_dice, flips, result):
        possible_fortunes = []
        dice_available = [flips[key] for key in flips if flips[key]]
        num_dice = min(len(dice_available), num_dice)
        for dice_selected in itertools.combinations(flips, num_dice):
            dice_flips = [flips[i] for i in dice_selected]
            for flips_selected in itertools.product(*dice_flips):
                flip_difference = util.sum_results(*flips_selected)
                possible_fortunes.append((util.sum_results(result, flip_difference),
                                          dice_selected, flips_selected))
        return possible_fortunes

    @staticmethod
    def filter_outcomes(fortunes, succeed, no_despair):
        if succeed:
            success_filtered = [pf for pf in fortunes if pf[0][0] > 0]
            if not success_filtered:
                print("WARNING: Cannot succeed on this check!")
                fortunes = fortunes
            else:
                fortunes = success_filtered
        if no_despair:
            despair_filtered = [pf for pf in fortunes if pf[0][3] == 0]
            if not despair_filtered:
                print(f"WARNING: Cannot remove despairs"
                      f"{' after succeeding' if succeed else ''} on this check!")
                fortunes = fortunes
            else:
                fortunes = despair_filtered

        return fortunes

    @staticmethod
    def maximize_fortune(fortunes, max_order):
        for m in max_order:
            max_objective = max(fortunes, key=lambda x: x[0][m])[0][m]
            fortunes = [f for f in fortunes if f[0][m] == max_objective]
        return fortunes

    def fortune(self, succeed=True, no_despair=False,
                maximize_order=None):
        maximize_order = self.get_max_order(maximize_order)
        pool = self.get_pool()
        flips = self.get_flips(pool)

        possible_fortunes = self.generate_fortunes(self.num_dice, flips, self.result())
        possible_fortunes = self.filter_outcomes(possible_fortunes, succeed, no_despair)
        possible_fortunes = self.maximize_fortune(possible_fortunes, maximize_order)

        return possible_fortunes[0]

    def apply_fortune(self, fortune):
        pool = self.get_pool()
        for dice_index, flip in zip(fortune[1], fortune[2]):
            d = pool[dice_index]
            d.result = util.sum_results(d.result, flip)
            d.adjacent_faces = []
        return fortune[0]
