import time
import game_Amit
import Constants
import sys
import player
import pandas as pd




def run_script(type, amount,domain_file_name,problem_file_name):
    player_init = player.Player(type, (11, 9), (11,10), amount)
    return game_Amit.run_game(player_init,domain_file_name,problem_file_name)


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
    for amnt in range(start_money,end_money+1,200):
        elapsed, expanded, turns = run_script(type,amnt,domain_file_name,problem_file_name)
        res.append([type, amnt, turns,expanded, elapsed])

    df = pd.DataFrame(res,
                      columns=[Constants.TYPE,Constants.MONEY,Constants.TURNS,Constants.EXPANDED,Constants.TIME])
    df.to_csv(r'output.csv',header=True)

    # game_Amit.run_game()
    # erez_money = [0, 200]
    # nitzan_money = [400, 600]
    # reut_money = [800, 1000]
    # amit_money = [1200, 1400]

    # extra_money1 = [1600, 1800]
    # extra_money2 = [2000, 2200]

    # money = extra_money2  # todo don't forget to change to your own money
    # for amount in money:
    #     start_time = time.time()

