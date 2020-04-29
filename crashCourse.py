"""
Author      Nicolas Peschke
Date        12.05.2019
"""

# Simulate a simple dice game!
# 1. Throw two dices, whichever is higher wins.
# 2. Log who won
# 3. Log the results of the dice throws
# 4. Plot statistics (Histogram etc.)
# 5. Save results

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def roll_dice():
    """
    Rolls a dice and returns the result
    :return: Result of the dice throw
    """
    return np.random.randint(1, 7)


def display_wins(win_list: list) -> None:
    """
    Prints the number of wins for both players
    :param win_list: List with the winner of each simulated round
    :return: None
    """
    wins = {name: 0 for name in set(win_list)}

    for winner in win_list:
        wins[winner] += 1

    print("Wins:")
    for key, value in wins.items():
        print("{name}: {wins}".format(name=key, wins=value))


def plot_dice_histogram(throw_list: list, ax: plt.Axes):
    """
    Plots a histogram with the distribution of the dice results
    :param throw_list: List of dice throw results
    :param ax: plt.Axes object to plot on
    :return: plt.Axes object with the histogram
    """
    ax = sns.distplot(throw_list, kde=False, ax=ax, bins=np.arange(start=1, stop=7, step=0.5) - 0.25)
    ax.set_title("Distribution of dice throws")
    ax.set_xlabel("Value")
    ax.set_ylabel("Occurrences (n = {n_throws})".format(n_throws=len(throw_list)))
    return ax


if __name__ == '__main__':
    player_A_name = "Ernie"
    player_B_name = "Bert"

    # sns.set("darkgrid")

    sim_rounds = 100

    winners = list()
    throws = list()

    for sim_round in range(sim_rounds):
        throw_player_A = roll_dice()
        throw_player_B = roll_dice()

        throws.append(throw_player_A)
        throws.append(throw_player_B)

        if throw_player_A > throw_player_B:
            winners.append(player_A_name)
        elif throw_player_B > throw_player_A:
            winners.append(player_B_name)
        else:
            winners.append("Draw")

    display_wins(winners)

    throw_hist_fig, throw_hist_ax = plt.subplots(1, 1)
    plot_dice_histogram(throw_list=throws, ax=throw_hist_ax)

    throw_hist_fig.show()
    throw_hist_fig.savefig("throw_hist.svg")
