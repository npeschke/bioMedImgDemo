"""
Author      Nicolas Peschke
Date        15.05.2019
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class DiceSim:
    def __init__(self, player_a_name: str, player_b_name: str, sim_rounds: int = 1000):
        """
        Initializes DiceSim object with player names and the number of game rounds to simulate.
        :param player_a_name: Name of player A
        :param player_b_name: Name of player B
        :param sim_rounds: Number of game rounds to simulate
        """
        self.player_A_name = player_a_name
        self.player_B_name = player_b_name
        self.sim_rounds = sim_rounds

        self.winners = list()
        self.throws = list()

    def simulate(self):
        """
        Runs the simulation.
        :return: None
        """
        for sim_round in range(self.sim_rounds):
            throw_a = self.roll_dice()
            throw_b = self.roll_dice()

            if throw_a > throw_b:
                self.winners.append(self.player_A_name)
            elif throw_b > throw_a:
                self.winners.append(self.player_B_name)
            else:
                self.winners.append("Draw")

    def roll_dice(self):
        """
        Rolls a dice and returns the result
        :return: Result of the dice throw
        """
        throw = np.random.randint(1, 7)
        self.throws.append(throw)
        return throw

    def display_wins(self) -> None:
        """
        Prints the number of wins for both players
        :return: None
        """
        wins = {name: 0 for name in set(self.winners)}

        for winner in self.winners:
            wins[winner] += 1

        print("Wins:")
        for key, value in wins.items():
            print("{name}: {wins}".format(name=key, wins=value))

    def plot_dice_histogram(self, ax: plt.Axes):
        """
        Plots a histogram with the distribution of the dice results
        :param ax: plt.Axes object to plot on
        :return: plt.Axes object with the histogram
        """
        ax = sns.distplot(self.throws, kde=False, ax=ax, bins=np.arange(start=1, stop=7, step=0.5) - 0.25)
        ax.set_title("Distribution of dice throws")
        ax.set_xlabel("Value")
        ax.set_ylabel("Occurrences (n = {n_throws})".format(n_throws=len(self.throws)))
        return ax


if __name__ == '__main__':
    sim1 = DiceSim("Ernie", "Bert")
    sim1.simulate()
    sim1.display_wins()

    throw_hist, throw_hist_ax = plt.subplots(1, 1)
    sim1.plot_dice_histogram(throw_hist_ax)
    throw_hist.show()

    sim_rounds_to_test = [10, 100, 1000, 10000, 100000, 1000000]

    round_comp, round_comp_ax = plt.subplots(1, len(sim_rounds_to_test), figsize=(len(sim_rounds_to_test)*5, 5))
    for idx, sim_round_to_test in enumerate(sim_rounds_to_test):
        sim = DiceSim(player_a_name="Ernie", player_b_name="Bert", sim_rounds=sim_round_to_test)
        sim.simulate()

        sim.plot_dice_histogram(round_comp_ax[idx])

    round_comp.show()
