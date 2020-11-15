##
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.pyplot import figure
import numpy as np


import starwars.dice as dice
import starwars.dice_pool as dp
import starwars.wrappers.unmatched_fortune as uf



##
d = dp.DicePool(*dice.string_to_dice_list("paaccddb"))
d = uf.UnmatchedFortune(d)
d.roll()
fortune = d.fortune(no_despair=True)
flipped_dice = [dd for i, dd in enumerate(d.get_pool()) if i in fortune[1]]
for dd, flip in zip(flipped_dice, fortune[2]):
    # print(dd, "::", flip)
    pass
d.apply_fortune(fortune)
# print(d.result())
##

figure(num=None, figsize=(16, 12), dpi=96, facecolor='w', edgecolor='k')

d = dp.DicePool(*dice.string_to_dice_list("pppadbbbbs"))
d = uf.UnmatchedFortune(d)
n_trials = 1000

default_rolls, fortune_rolls = [], []
for i in range(n_trials):
    if not i % (n_trials//100):
        print(f"{i//(n_trials//100)}%", end="\r")
    roll = d.roll()
    default_rolls.append(roll)
    fortune = d.fortune()
    d.apply_fortune(fortune)
    fortune_rolls.append(d.result())
default_rolls = np.array(default_rolls)
fortune_rolls = np.array(fortune_rolls)


def plot_rolls(rolls1, rolls2):
    fig, axes = plt.subplots(nrows=1, ncols=2)
    ax1 = axes.flat[0]
    ax2 = axes.flat[1]

    ax1.set_title('Default')
    ax2.set_title('Unmatched Fortune')

    bins1, bins2, full_range = get_ranges(rolls1, rolls2)

    make_plot(ax1, rolls1, bins1, full_range)
    make_plot(ax2, rolls2, bins2, full_range)

    fig.tight_layout()

    plt.show()


def get_ranges(rolls1, rolls2):
    xmax1, xmin1 = np.max(rolls1[:, 0]), np.min(rolls1[:, 0])
    ymax1, ymin1 = np.max(rolls1[:, 1]), np.min(rolls1[:, 1])
    
    bins1 = (xmax1 - xmin1, ymax1 - ymin1)
    
    xmax2, xmin2 = np.max(rolls2[:, 0]), np.min(rolls2[:, 0])
    ymax2, ymin2 = np.max(rolls2[:, 1]), np.min(rolls2[:, 1])

    bins2 = (xmax2 - xmin2, ymax2 - ymin2)

    xmax = max(xmax1, xmax2)
    ymax = max(ymax1, ymax2)
    xmin = min(xmin1, xmin2)
    ymin = min(ymin1, ymin2)

    full_range = np.array([(xmin, xmax), (ymin, ymax)])
    bin = (xmax - xmin, ymax - ymin)
    return bin, bin, full_range


def make_plot(ax, rolls, bins, full_range):
    ax.set_xlabel("Successes")
    ax.set_ylabel("Advantages")

    xmin, xmax, ymin, ymax = tuple(full_range.flatten())

    counts, xedges, yedges, Image = ax.hist2d(rolls[:, 0], rolls[:, 1], bins=bins,
                                              range=full_range)
    dx = xedges[2]-xedges[1]
    dy = yedges[2]-yedges[1]
    for i in range(xedges.size-1):
        for j in range(yedges.size-1):
            if not counts[i,j]:
                continue
            xb = xedges[i] + 0.25*dx
            yb = yedges[j] + 0.25*dy
            ax.text(xb, yb, str(int(np.round(counts[i,j],2))), fontsize=6)
    ax.set_xticks(range(xmin, xmax + 1))
    ax.set_yticks(range(ymin, ymax + 1))


plot_rolls(default_rolls, fortune_rolls)


"""
ax1.set_xticks(range(min_x, max_x + 1))
ax2.set_xticks(range(min_x, max_x + 1))
ax1.set_yticks(range(min_y, max_y + 1))
ax2.set_yticks(range(min_y, max_y + 1))
"""
