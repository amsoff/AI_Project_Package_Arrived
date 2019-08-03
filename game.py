from graphplan.search import a_star_search
from domain_create import Types
from graphplan.planning_problem import PlanningProblem, max_level, level_sum
import domain_create as dc
from surprise import Surprise
from player import Player
import Certificates
from dice import Dice
import board
import numpy as np
from colorama import init, Fore, Back, Style
import sys
import time
import datetime

dice_obj = Dice()
board_game = board.Board().transition_dict
surprise_generator = Surprise()
DEBUG = True


def print_plan(plan, logs):
    for a in plan:
        if type(a) != str:
            a = a.name
        print(a)
        write_to_log(a, logs)


def print_current_board(moves, player_obj: Player):
    board_obj = board.Board()
    tmp_board = np.copy(board_obj.board_to_print)
    for (x, y) in moves:
        tmp_board[x][y] = "O"
    tmp_board[player_obj.cell[0]][player_obj.cell[1]] = "P"
    tmp_board[player_obj.goal[0]][player_obj.goal[1]] = "G"

    matprint(tmp_board, board_obj)


def matprint(mat, board_obj):
    # col_maxes = [max([len(("{}").format(x)) for x in col]) for col in mat.T]
    for i, x in enumerate(mat):
        for j, y in enumerate(x):
            if (i, j) == board_obj.starting_point:
                print(Back.RED +Fore.BLACK+ "\u0332|\u0332S", end='')

            elif mat[i][j] == "X":
                print(Back.GREEN + Fore.BLACK + "\u0332|\u0332X", end='')
                continue
            elif mat[i][j] == "P":
                print(Back.LIGHTRED_EX + Fore.BLACK + "\u0332|\u0332P", end='')
            elif "orange" in board_obj.transition_dict[(i, j)]:
                print(Back.YELLOW + Fore.BLACK + "\u0332|\u0332 ", end='')
            elif "surprise" in board_obj.transition_dict[(i, j)]:
                print(Back.MAGENTA + Fore.BLACK + "\u0332|\u0332 ", end='')
            elif "wait" in board_obj.transition_dict[(i, j)]:
                print(Back.BLUE + Fore.BLACK + "\u0332|\u0332 ", end='')
            elif mat[i][j] == "G":
                print(Back.LIGHTCYAN_EX + Fore.BLACK + "\u0332|\u0332G", end='')
            elif mat[i][j] == "O":
                print(Back.LIGHTWHITE_EX + Fore.BLACK + "\u0332|\u0332O", end='')
            else:
                print(Back.WHITE + "\u0332|\u0332 ", end='')
        # background = Back.YELLOW if ("orange" in board_obj.transition_dict[(i,j)]) else  Back.MAGENTA if ("surprise" in board_obj.transition_dict[(i,j)]) else Back.BLUE if ("wait" in board_obj.transition_dict[(i,j)]) else Back.WHITE
        # print((background+"{}").format(y), end="  ")
        print(Back.RESET + "")


def handle_stop(plan):
    all = []
    for move in plan:
        if 'Stop' in move.name:
            all.append("Wait 1 turn")
        else:
            break
    return all


def handle_payments(action, player):
    if 'pay_surprise' in action.name:
        cell = (int(action.name.split('_')[2]), int(action.name.split('_')[3]))
        amount = surprise_generator.get_surprise()
        # if player.money + amount >= 0:
        player.money = min(player.money + amount, dc.MAXIMUM_POCKET * 50)
        player.money = max(0, player.money)
        # if cell in player.need_pay_spots:
        #     player.need_pay_spots.remove(cell)
        sign = "+"
        if amount < 0:  # it is a payment and not get money
            sign = "-"
        return ["got a surprise! money " + sign + "= " + str(abs(amount))], 0

        # else:
            # player.owe.append(amount)

    if 'pay_150_from' in action.name:
        all = []
        cell = (int(action.name.split('_')[6]), int(action.name.split('_')[7]))
        player.money -= 150
        player.cell = cell
        if cell in player.need_pay_spots:
            player.need_pay_spots.remove(cell)
        # need to match the exact name of the certificate
        for prop in action.add:
            if 'has' in prop.name:
                # need to match the exact name of the certificate
                certificate = prop.name.split('has_')[1]
                for cert in Certificates.Certificate.list():
                    if str(cert) == certificate and cert not in player.has_certificates:
                        player.has_certificates.append(cert)
                        all.append("Congrats! you hold the %s Certificate!" % cert.name)
        return all, 1

    if 'pay' in action.name:
        cell = (int(action.name.split('_')[3]), int(action.name.split('_')[4]))
        amount = int(action.name.split('_')[1])
        player.money -= amount
        if cell in player.need_pay_spots:
            player.need_pay_spots.remove(cell)
        sign = "+"
        if amount > 0:  # then it is a payment and not to get money
            sign = "-"
        return ["money " + sign + "= " + str(abs(amount))], 0
    return None


def handle_goto(action, player):
    cell = int(action.split('_')[1]), int(action.split('_')[2])
    player.cell = cell
    if cell in player.come_back_spots:
        player.come_back_spots.remove(cell)
    return ["Go back to (%d,%d)" % cell]


def handle_jump_to_entrance(action, player):
    jump_to = (int(action.name.split("_")[3]), int(action.name.split("_")[4]))
    player.cell = jump_to
    player.come_back_spots.append((int(action.name.split('_')[6]), int(action.name.split('_')[7])))
    return ["jumped to (%s,%s) to search" % jump_to]


def handle_move(plan, player):
    all = []
    turns = 1
    action = plan[0]
    action_name = plan[0].name
    if 'Move' in plan[0].name:
        player.cell = (int(action_name.split('_')[5]), int(action_name.split('_')[6]))
        if cell not in board.Board.loto_cells:
            all.append("Move to (%s,%s)" % player.cell)
        for prop in action.add:
            if 'has' in prop.name:
                # need to match the exact name of the certificate
                certificate = prop.name.split('has_')[1]
                for cert in Certificates.Certificate.list():
                    if str(cert) == certificate and cert not in player.has_certificates:
                        player.has_certificates.append(cert)
                        all.append("Congrats! you hold the %s Certificate!" % cert.name)
        for prop in action.pre:
            if 'has' in prop.name:
                certificate = prop.name.split('has_')[1].split(".")[1].lower()
                all.append("presented the certificate: " + certificate)
    if player.cell in board.Board.loto_cells:
        dice_val = dice_obj.roll_dice()
        if board.BALANCE in board_game[board_game[player.cell][dice_val][0]]:
            player.money += board_game[board_game[player.cell][dice_val][0]][board.BALANCE]
            all.append("You win the lottery. YAY! You earned %s" % board_game[board_game[player.cell][dice_val][0]][board.BALANCE])
        turns += 1
    for i, action in enumerate(plan):
        # handle it already
        if i == 0:
            continue

        # if we encounter another move- we finished the current round
        if 'Move' in action.name or 'pay_150' in action.name:
            break

        if 'pay' in action.name:
            pay, turn = handle_payments(action, player)
            turns += turn
            all.extend(pay)

        elif 'Stop' in action.name:
            stops = handle_stop(plan[i:])
            turns += len(stops)
            all.extend(stops)
            break

        elif 'Goto' in action.name:
            goto = handle_goto(action.name, player)
            turns += 1
            all.extend(goto)

        # elif 'place_comeback' in action.name:
        #     cb_to = (action.name.split("_")[2], action.name.split("_")[3])
        #     player.come_back_spots.append(cb_to)
        #     all.append("placed comeback at (%s,%s)" % cb_to)

        elif 'jump' in action.name:
            jump = handle_jump_to_entrance(action, player)
            all.extend(jump)

    return all, turns


def write_to_log(string, logs):
    logs.write(string + "\n") if DEBUG else None


def prints_game_over(moves, logs, player,elapsed):
    print_plan(moves, logs)
    print("Money: %d" % player.money)
    write_to_log("Money: %d" % player.money, logs)
    # print()
    print("--- Game finished after %d turns in %.2f seconds ---" % (len(moves) - 1, elapsed))
    print("The number of expanding nodes in each turn:\n%s" % "\n".join(expanded))
    write_to_log("game finished after %d turns in %.2f seconds" % (len(moves) - 1, elapsed), logs)


def print_exit(logs, plan, moves):
    print("plan doesn't start with move!!! The current action was:")
    write_to_log("plan doesn't start with move!!! The current action was:", logs)
    print(plan[0].name)
    write_to_log(plan[0].name, logs)
    write_to_log("PLAN:", logs)
    print_plan(plan, logs)
    print("moves are:")
    write_to_log("moves are:", logs)
    print_plan(moves, logs)
    exit(1)


if __name__ == '__main__':
    """
    input = python3 game.py player
    outout = print all moves
    """
    start = time.process_time()

    if len(sys.argv) != 2:
        print("Usage: game.py player(optimistic or mean). Bad input")
        exit()
    input_player = sys.argv[1]
    domain_file_name = 'domain.txt'
    problem_file_name = '{}_problem.txt'
    player = Player()

    if input_player == Types.MEAN.value or input_player == Types.OPTIMISTIC.value:
        player.set_type(input_player)
        problem_file_name = problem_file_name.format(input_player.lower())
        domain_file_name = dc.create_domain_file(domain_file_name, input_player.lower())
    else:
        print("Usage: game.py player(optimistic or mean). Bad type player.")
        exit()
    dice_val = dice_obj.roll_dice()
    player.dice_value = dice_val
    player.build_problem()
    prob = PlanningProblem(domain_file_name, problem_file_name, None, None)
    plan = a_star_search(prob, heuristic=level_sum)
    turns, expanded = 0, []
    moves = ["--- Welcome to the package Arrive Game.--- \nYou are positioned at (1,0)"]
    past_moves = [player.cell]
    with open("logs/log-{}.txt".format(str(datetime.datetime.now()).replace(":", "")), "w") as logs:
        while len(plan) != 0 and plan != 'failed':
            if 'Move' in plan[0].name:
                cell = (plan[0].name.split('_')[5], plan[0].name.split('_')[6])
                move, turn = handle_move(plan, player)
                turns += turn
                write_to_log("current moves done:", logs)
                print_plan(move,logs)
                moves.extend(move)

            elif 'pay_150' in plan[0].name:
                cell = (plan[0].name.split('_')[6], plan[0].name.split('_')[7])
                move, turn = handle_payments(plan[0], player)
                turns += turn
                moves.extend(move)
                if len(plan[1:]) != 0:
                    plan = plan[1:]
                    continue

            elif 'jump' in plan[0].name:
                cell = (int(plan[0].name.split("_")[3]), int(plan[0].name.split("_")[4]))
                move = handle_jump_to_entrance(plan[0], player)
                moves.extend(move)
                if len(plan[1:]) != 0:
                    plan = plan[1:]
                    continue

            elif 'Goto' in plan[0].name:
                cell = int(plan[0].name.split('_')[1]), int(plan[0].name.split('_')[2])
                move = handle_goto(plan[0].name, player)
                moves.extend(move)
                if len(plan[1:]) != 0:
                    plan = plan[1:]
                    continue

            else:
                print_exit(logs, plan, moves)

            write_to_log("round {}".format(turns),logs)

            if board.MESSAGE in board_game[int(cell[0]), int(cell[1])]:
                moves.append(board_game[int(cell[0]), int(cell[1])]["message"])

            # Starting new round- creating new problem.txt file
            past_moves.append((player.cell[0], player.cell[1]))
            print_current_board(past_moves, player)

            # New round- roll the dice
            actions = prob.get_actions()
            propositions = prob.get_propositions()
            player.dice_value = dice_obj.roll_dice()
            player.build_problem()
            expanded.append(str(prob.expanded))
            prob = PlanningProblem(domain_file_name, problem_file_name, actions, propositions)
            plan = a_star_search(prob, heuristic=level_sum)

            if len(plan) == 0:
                write_to_log("## LAST ##", logs)
            write_to_log("###########ACTIONS##########", logs)
            for action in actions:
                write_to_log(action.name, logs)
            write_to_log("@@@@@@@@@@@PROPOSITIONS@@@@@@@@@@@", logs)
            for state in prob.initialState:
                write_to_log(state.name, logs)

        elapsed = time.process_time() - start
        if moves is not None and plan != "failed":
            prints_game_over(moves, logs, player, elapsed)
        else:
            print("Could not find a plan in %.2f seconds" % elapsed)
            write_to_log("Could not find a plan in %.2f seconds" % elapsed, logs)
