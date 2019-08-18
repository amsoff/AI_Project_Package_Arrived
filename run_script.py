import time
import game
import Constants
import sys

import game_no_opt
import player
import pandas as pd


def run_script(heuristic, type, amount, domain_file_name, problem_file_name, gen_flag=2):
    player_init = player.Player(type, (11, 9), (1, 0), amount)
    return game.run_game(heuristic, player_init, domain_file_name, problem_file_name, gen_flag)


if __name__ == "__main__":
    domain_file_name = 'domain.txt'
    problem_file_name = '{}_problem.txt'
    res = []
    amnt = int(sys.argv[1])
    type = sys.argv[2]
    heuristic = sys.argv[3]
    gen_flag = sys.argv[4]
    elapsed, expanded, turns = run_script(heuristic, type, amnt, domain_file_name, problem_file_name, gen_flag)
    res.append([type, amnt, turns, expanded, elapsed])

    df = pd.DataFrame(res,
                      columns=[Constants.TYPE, Constants.MONEY, Constants.TURNS, Constants.EXPANDED, Constants.TIME])
    df.to_csv(r'' + type + "_" + heuristic + "-" + str(amnt) + "_gen" + str(gen_flag) + '.csv', header=True)

