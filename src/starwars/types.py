from typing import Dict, Tuple, List, Union

# 4-tuple: (successes, advantages, triumphs, despairs)
DiceTuple = Tuple[int, int, int, int]
DiceList = List[DiceTuple]
#
DiceTupleOrNone = Union[DiceTuple, None]
DiceListOrNone = Union[DiceList, None]
# Dictionary:
#   (index, face): [adjacent faces]
DiceDict = Dict[Tuple[int, DiceTuple], DiceList]
