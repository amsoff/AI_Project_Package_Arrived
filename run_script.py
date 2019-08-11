import time
import game
import Constants
import sys

import game_no_opt
import player
import pandas as pd


def run_script(type, amount, domain_file_name, problem_file_name):
    player_init = player.Player(type, (11, 9), (1, 0), amount)
    return game.run_game(player_init, domain_file_name, problem_file_name)


if __name__ == "__main__":
    domain_file_name = 'domain.txt'
    problem_file_name = '{}_problem.txt'
    res = []
    start_money = int(sys.argv[1])
    end_money = int(sys.argv[2])
    if len(sys.argv) == 4:
        type = sys.argv[3]
    else:
        type = Constants.OPTIMISTIC
    for amnt in range(start_money, end_money + 1, 200):
        elapsed, expanded, turns = run_script(type, amnt, domain_file_name, problem_file_name)
        res.append([type, amnt, turns, expanded, elapsed])

    df = pd.DataFrame(res,
                      columns=[Constants.TYPE, Constants.MONEY, Constants.TURNS, Constants.EXPANDED, Constants.TIME])
    df.to_csv(r'output.csv', header=True)
