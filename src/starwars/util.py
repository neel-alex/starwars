import starwars.types as types


def diff_result(res1: types.DiceTuple, res2: types.DiceTuple):
    return tuple(x - y for x, y in zip(res1, res2))


def sum_results(*args: types.DiceTuple):
    return tuple(sum(z) for z in zip(*args))


def stringify_results(result: types.DiceTuple) -> str:
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

    for _ in range(-result[3]):
        final_string += "Despair!\n"

    return final_string
