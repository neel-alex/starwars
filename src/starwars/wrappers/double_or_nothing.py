from starwars.mutable_pool import MutablePool
import starwars.types as types


class DoubleOrNothing(MutablePool):
    def __init__(self, pool, *args, success=False, tf=False, **kwargs):
        super().__init__(pool, *args, **kwargs)
        self.success = success
        self.tf = tf
        self.upgraded = False

    def roll(self):
        if not self.upgraded:
            self.upgrade_difficulty()
            self.upgraded = True
        result = super().roll()
        return self.double(result)

    def result(self):
        assert self.upgraded, "Double or nothing requires a dice upgrade."
        result = super().result()
        return self.double(result)

    def double(self, result: types.DiceTuple) -> types.DiceTuple:
        s = 2 if result[0] > 0 and self.success else 1
        a = 2 if result[1] > 0 else 1
        t = 2 if self.tf else 1
        d = 2 if self.tf else 1
        return result[0] * s, result[1] * a, result[2] * t, result[3] * d
