##
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np


import starwars.dice as dice
import starwars.dice_pool as dp
import starwars.wrappers.unmatched_fortune as uf



##
d = dp.DicePool(*dice.string_to_dice_list("paaccddb"))
d = uf.UnmatchedFortune(d)
print(d.roll())
fortune = d.fortune(no_despair=True)
flipped_dice = [dd for i, dd in enumerate(d.get_pool()) if i in fortune[1]]
for dd, flip in zip(flipped_dice, fortune[2]):
    print(dd, "::", flip)
d.apply_fortune(fortune)
print(d.result())
##

from matplotlib.pyplot import figure
figure(num=None, figsize=(16, 12), dpi=96, facecolor='w', edgecolor='k')

d = dp.DicePool(*dice.string_to_dice_list("paaccddb"))
d = uf.UnmatchedFortune(d)
n_trials = 1000

fig, axes = plt.subplots(nrows=1, ncols=2)
ax1 = axes.flat[0]
ax2 = axes.flat[1]

ax1.set_title('Default')
ax1.set_xlabel("Successes")
ax1.set_ylabel("Advantages")
rolls = [d.roll() for _ in range(n_trials)]
rolls = np.array(rolls)

xrange = np.max(rolls[:, 0]) - np.min(rolls[:, 0])
yrange = np.max(rolls[:, 1]) - np.min(rolls[:, 1])
counts, xedges, yedges, Image = ax1.hist2d(rolls[:, 0], rolls[:, 1], bins=(xrange, yrange))

dx = xedges[2]-xedges[1]
dy = yedges[2]-yedges[1]
for i in range(xedges.size-1):
    for j in range(yedges.size-1):
        if not counts[i,j]:
            continue
        xb = xedges[i] + 0.25*dx
        yb = yedges[j] + 0.25*dy
        ax1.text(xb, yb, str(int(np.round(counts[i,j],2))), fontsize=6)


ax2.set_title('Unmatched Fortune')
ax2.set_xlabel("Successes")
ax2.set_ylabel("Advantages")

fortune_rolls = []
for i in range(n_trials):
    if not i % (n_trials//100):
        print(f"{i//(n_trials//100)}%", end="\r")
    roll = d.roll()
    fortune = d.fortune()
    d.apply_fortune(fortune)
    fortune_rolls.append(d.result())
fortune_rolls = np.array(fortune_rolls)

xrange = np.max(fortune_rolls[:, 0]) - np.min(fortune_rolls[:, 0])
yrange = np.max(fortune_rolls[:, 1]) - np.min(fortune_rolls[:, 1])
counts, xedges, yedges, Image = ax2.hist2d(fortune_rolls[:, 0], fortune_rolls[:, 1], bins=(xrange, yrange))

dx = xedges[2]-xedges[1]
dy = yedges[2]-yedges[1]
for i in range(xedges.size-1):
    for j in range(yedges.size-1):
        if not counts[i,j]:
            continue
        xb = xedges[i] + 0.25*dx
        yb = yedges[j] + 0.25*dy
        ax2.text(xb, yb, str(int(np.round(counts[i,j],2))), fontsize=6)


min_x = min(np.min(rolls[:, 0]), np.min(fortune_rolls[:, 0]))
max_x = max(np.max(rolls[:, 0]), np.max(fortune_rolls[:, 0]))
min_y = min(np.min(rolls[:, 1]), np.min(fortune_rolls[:, 1]))
max_y = max(np.max(rolls[:, 1]), np.max(fortune_rolls[:, 1]))


ax1.set_xticks(range(min_x, max_x + 1))
ax2.set_xticks(range(min_x, max_x + 1))
ax1.set_yticks(range(min_y, max_y + 1))
ax2.set_yticks(range(min_y, max_y + 1))


fig.tight_layout()

plt.show()



##

