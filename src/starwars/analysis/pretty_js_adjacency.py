from collections import defaultdict

import json

import starwars.dice as dice


b = dice.Boost()
a = dice.Ability()
p = dice.Proficiency()
s = dice.Setback()
d = dice.Difficulty()
c = dice.Challenge()

available_dice = [b, a, p, s, d, c]

for die in available_dice:
    new_faces = defaultdict(lambda: [])

    for k in die.adjacency:
        _, f = k
        f = ",".join([str(n) for n in f])
        new_faces[f].append(die.adjacency[k])

    print(json.dumps(new_faces))
