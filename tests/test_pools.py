import starwars.dice as dice
from starwars.dice_pool import DicePool
from starwars.mutable_pool import MutablePool
from starwars.double_or_nothing import DoubleOrNothing


def count_dice_in_pool(pool, d_type):
    i = 0
    for d in pool:
        if type(d) == d_type:
            i += 1

    return i


def test_default_pool():
    dp = DicePool(*dice.string_to_dice_list("aaapddcbbs"))
    dp.roll()
    dp.result()
    assert count_dice_in_pool(dp.get_pool(), dice.Ability) == 3
    assert count_dice_in_pool(dp.get_pool(), dice.Proficiency) == 1
    assert count_dice_in_pool(dp.get_pool(), dice.Difficulty) == 2
    assert count_dice_in_pool(dp.get_pool(), dice.Challenge) == 1
    assert count_dice_in_pool(dp.get_pool(), dice.Boost) == 2
    assert count_dice_in_pool(dp.get_pool(), dice.Setback) == 1


def test_mutable_pool():
    dp = DicePool(*dice.string_to_dice_list("aaapdddbbs"))
    dp.roll()
    dp.result()
    assert count_dice_in_pool(dp.get_pool(), dice.Ability) == 3
    assert count_dice_in_pool(dp.get_pool(), dice.Proficiency) == 1
    assert count_dice_in_pool(dp.get_pool(), dice.Difficulty) == 3
    assert count_dice_in_pool(dp.get_pool(), dice.Challenge) == 0
    assert count_dice_in_pool(dp.get_pool(), dice.Boost) == 2
    assert count_dice_in_pool(dp.get_pool(), dice.Setback) == 1

    mdp = MutablePool(dp)
    mdp.upgrade_difficulty()
    assert count_dice_in_pool(mdp.get_pool(), dice.Difficulty) == 2
    assert count_dice_in_pool(mdp.get_pool(), dice.Challenge) == 1

    mdp.upgrade_difficulty()
    assert count_dice_in_pool(mdp.get_pool(), dice.Difficulty) == 1
    assert count_dice_in_pool(mdp.get_pool(), dice.Challenge) == 2

    mdp.upgrade_difficulty()
    assert count_dice_in_pool(mdp.get_pool(), dice.Difficulty) == 0
    assert count_dice_in_pool(mdp.get_pool(), dice.Challenge) == 3

    mdp.upgrade_difficulty()
    assert count_dice_in_pool(mdp.get_pool(), dice.Difficulty) == 1
    assert count_dice_in_pool(mdp.get_pool(), dice.Challenge) == 3

    mdp.upgrade_ability()
    assert count_dice_in_pool(mdp.get_pool(), dice.Ability) == 2
    assert count_dice_in_pool(mdp.get_pool(), dice.Proficiency) == 2

    mdp.upgrade_ability()
    assert count_dice_in_pool(mdp.get_pool(), dice.Ability) == 1
    assert count_dice_in_pool(mdp.get_pool(), dice.Proficiency) == 3

    mdp.upgrade_ability()
    assert count_dice_in_pool(mdp.get_pool(), dice.Ability) == 0
    assert count_dice_in_pool(mdp.get_pool(), dice.Proficiency) == 4

    mdp.upgrade_ability()
    assert count_dice_in_pool(mdp.get_pool(), dice.Ability) == 1
    assert count_dice_in_pool(mdp.get_pool(), dice.Proficiency) == 4

    assert count_dice_in_pool(mdp.get_pool(), dice.Boost) == 2
    assert count_dice_in_pool(mdp.get_pool(), dice.Setback) == 1

    mdp.add_dice(*dice.string_to_dice_list('bbbbssad'))
    mdp.add_dice(*dice.string_to_dice_list('pc'))
    mdp.add_dice()
    mdp.roll_unrolled()
    mdp.roll_unrolled()
    mdp.roll()
    mdp.result()


def test_double_or_nothing():
    d = DicePool(*dice.string_to_dice_list("aaapdddbb"))
    dd = DoubleOrNothing(d)
    res = dd.roll()
    while res[1] < 1:
        res = dd.roll()
    assert 2 * (d.result()[1]) == res[1]
