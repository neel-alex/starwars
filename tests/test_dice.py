import collections

import starwars.dice as dice

NONE = (0, 0, 0, 0)

SUCCESS = (1, 0, 0, 0)
ADVANTAGE = (0, 1, 0, 0)
TWO_SUCCESS = (2, 0, 0, 0)
SUCCESS_ADV = (1, 1, 0, 0)
TWO_ADV = (0, 2, 0, 0)
TRIUMPH = (1, 0, 1, 0)

FAILURE = (-1, 0, 0, 0)
THREAT = (0, -1, 0, 0)
TWO_FAILURE = (-2, 0, 0, 0)
FAIL_THREAT = (-1, -1, 0, 0)
TWO_THREAT = (0, -2, 0, 0)
DESPAIR = (-1, 0, 0, -1)


def _test_dice(dice_class, faces):
    d = dice_class()
    assert d.roll() == d.result
    assert collections.Counter(d.faces) == collections.Counter(faces)


def test_boost():
    _test_dice(dice.Boost, [NONE, NONE, SUCCESS, ADVANTAGE, SUCCESS_ADV, TWO_ADV])


def test_ability():
    _test_dice(dice.Ability, [NONE, ADVANTAGE, ADVANTAGE, ADVANTAGE,
                              SUCCESS, TWO_ADV, SUCCESS_ADV, TWO_SUCCESS])


def test_proficiency():
    _test_dice(dice.Proficiency, [NONE, SUCCESS, SUCCESS, ADVANTAGE, TWO_ADV,
                                  TWO_ADV, SUCCESS_ADV, SUCCESS_ADV, SUCCESS_ADV,
                                  TWO_SUCCESS, TWO_SUCCESS, TRIUMPH])


def test_setback():
    _test_dice(dice.Setback, [NONE, NONE, FAILURE, FAILURE, THREAT, THREAT])


def test_difficulty():
    _test_dice(dice.Difficulty, [NONE, THREAT, THREAT, THREAT, FAILURE, FAIL_THREAT,
                                 TWO_THREAT, TWO_FAILURE])


def test_challenge():
    _test_dice(dice.Challenge, [NONE, THREAT, THREAT, FAILURE, FAILURE,
                                TWO_FAILURE, TWO_FAILURE, TWO_THREAT,
                                TWO_THREAT, FAIL_THREAT, FAIL_THREAT, DESPAIR])


def test_string_to_dice_list():
    assert type(dice.string_to_dice_list('b')[0]) == dice.Boost
    assert type(dice.string_to_dice_list('a')[0]) == dice.Ability
    assert type(dice.string_to_dice_list('p')[0]) == dice.Proficiency
    assert type(dice.string_to_dice_list('d')[0]) == dice.Difficulty
    assert type(dice.string_to_dice_list('c')[0]) == dice.Challenge
    assert type(dice.string_to_dice_list('s')[0]) == dice.Setback

    assert (collections.Counter(map(type, dice.string_to_dice_list('bbaaappppdccsss'))) ==
            collections.Counter([dice.Boost, dice.Boost, dice.Ability, dice.Ability,
                                 dice.Ability, dice.Proficiency, dice.Proficiency,
                                 dice.Proficiency, dice.Proficiency, dice.Difficulty,
                                 dice.Challenge, dice.Challenge, dice.Setback, dice.Setback,
                                 dice.Setback]))
