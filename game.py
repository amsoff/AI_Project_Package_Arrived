from graphplan.search import a_star_search
from domain_create import Types
from graphplan.planning_problem import PlanningProblem, level_sum, max_level
import domain_create as dc
import Constants
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

ROLLING = "-- You rolled a %s --"
START = "--- Welcome to The Package Arrived game.--- \nYou are positioned at (%s,%s)"

### Game Objects ###
board_game = board.Board().transition_dict
surprise_generator = Surprise()


def print_plan(plan, logs):
    """
    Prints the plan to the screen and to the log file
    :param plan: the plan
    :param logs: the log file
    """
    for a in plan:
        if type(a) != str:
            a = a.name
        print(a)
        write_to_log(a, logs)


def print_current_board(moves, player_obj: Player):
    """
    Prints the board to the screen and updates the board with the location of
    the goal and starting point. Also updates the path the player went through.
    :param moves: the player's moves
    :param player_obj:
    """
    board_obj = board.Board()
    tmp_board = np.copy(board_obj.board_to_print)
    for i, (x, y) in enumerate(moves):
        try:
            tmp_board[x][y] = "O%s" % i
        except:
            print(type(tmp_board[x][y]))
    tmp_board[player_obj.cell[0]][player_obj.cell[1]] = "P"
    tmp_board[player_obj.goal[0]][player_obj.goal[1]] = "G"

    matprint_backwards(tmp_board, board_obj, player_obj)


def matprint_backwards(mat, board_obj, player_obj):
    """
    Prints the board to the screen according to the board properties and the agent's actions
    :param mat: the current board
    :param board_obj: the board
    :param player_obj: the player
    """
    for i in range(len(mat) - 1, -1, -1):
        for j in range(len(mat[i]) - 1, -1, -1):
            if (i, j) == player_obj.start:
                print(Back.RED + Fore.BLACK + "|\u0332S\u0332", end='')

            elif mat[i][j] == "X":
                print(Back.GREEN + Fore.BLACK + "|\u0332X\u0332", end='')
                continue
            elif mat[i][j] == "P":
                print(Back.LIGHTRED_EX + Fore.BLACK + "|\u0332P\u0332", end='')
            elif (i, j) in board.Board.orange_cells:
                print(Back.YELLOW + Fore.BLACK + "|\u0332\u0332 ", end='')
            elif "surprise" in board_obj.transition_dict[(i, j)]:
                print(Back.MAGENTA + Fore.BLACK + "|\u0332\u0332 ", end='')
            elif "wait" in board_obj.transition_dict[(i, j)]:
                print(Back.BLUE + Fore.BLACK + "|\u0332\u0332 ", end='')
            elif mat[i][j] == "G":
                print(Back.LIGHTCYAN_EX + Fore.BLACK + "|\u0332G\u0332", end='')
            elif mat[i][j] == "O":
                print(Back.WHITE + Fore.BLACK + "|\u0332O\u0332", end='')
            else:
                print(Back.WHITE + "|\u0332\u0332 ", end='')
        print(Back.RESET + "")


def matprint(mat, board_obj, player_obj):
    """
    Prints the screen of the game, and defines the color of the special cells.
    Surprise- purple
    Wait turn- blue
    Player- red with p
    Circle- cell the agent visited
    Yellow- orange cell
    Grey- can step on this cell
    """
    for i, x in enumerate(mat):
        for j, y in enumerate(x):
            if (i, j) == player_obj.start:
                print(Back.RED + Fore.BLACK + "|\u0332S\u0332|", end='')

            elif mat[i][j] == "X":
                print(Back.GREEN + Fore.BLACK + "|\u0332X\u0332|", end='')
                continue
            elif mat[i][j] == "P":
                print(Back.LIGHTRED_EX + Fore.BLACK + "|\u0332P\u0332|", end='')
            elif (i, j) in board.Board.orange_cells:
                print(Back.RESET + Fore.BLACK + "|\u0332\u0332| ", end='')
            elif "surprise" in board_obj.transition_dict[(i, j)]:
                print(Back.MAGENTA + Fore.BLACK + "|\u0332\u0332| ", end='')
            elif "wait" in board_obj.transition_dict[(i, j)]:
                print(Back.BLUE + Fore.BLACK + "|\u0332\u0332| ", end='')
            elif mat[i][j] == "G":
                print(Back.LIGHTCYAN_EX + Fore.BLACK + "|\u0332G\u0332|", end='')
            elif mat[i][j] == "O":
                print(Back.WHITE + Fore.BLACK + "|\u0332O\u0332|", end='')
            else:
                print(Back.WHITE + "|\u0332\u0332| ", end='')
        print(Back.RESET + "")


def handle_stop(plan):
    """
    Handles the case we need to wait turn/s
    :param plan: the plan
    :return: the description of the moves + number of turns
    """
    all = []
    for move in plan:
        if 'Stop' in move.name:
            all.append("Wait 1 turn")
        else:
            break
    return all


def handle_payments(action, player):
    """
    Handle payment- update the player's position and money, and puts need_pay on this cell.
    Always makes sure the amount of money will be non negative.
    The actions:
    1. Pay 150 in order to move from one cell to an orange cell in case the agent
        can land on it in 1,2,3 steps
    2. Pay X amount if landed on a cell that requires payment
    3. Surprise- earn or lose money
    (Lottery is being handled in the handle_move)
    :param action: the action of the payment
    :param player: the agent that performed the move
    :return: description of the move + turns
    """
    # Pink cell- the Surprise. Randomly choose amount of money
    if 'pay_surprise' in action.name:
        amount = surprise_generator.get_surprise()
        player.money = min(player.money + amount, Constants.NUM_OF_50_BILLS * 50)
        player.money = max(0, player.money)
        sign = "+"
        if amount < 0:  # it is a payment and not get money
            sign = "-"
        return ["Got a surprise! Money " + sign + "= " + str(abs(amount)) + "\nMoney Balance: " + str(player.money)], 0

    # Pay 150 to move to orange cell. update the player location
    if 'pay_150_from' in action.name:
        if player.money < 150:
            return [], 0
        all = []
        cell = (int(action.name.split('_')[6]), int(action.name.split('_')[7]))
        player.money -= 150
        player.cell = cell
        all.append("Paid 150 to jump to (%s,%s)" % cell + "\nMoney Balance: " + str(player.money))
        if cell in player.need_pay_spots:
            if cell not in player.need_pay_spots:
                player.need_pay_spots.append(cell)
            player.need_pay_spots.remove(cell)
        # handle the case a cell we are moving to provides a certificate
        for prop in action.add:
            if 'has' in prop.name:
                # need to match the exact name of the certificate
                certificate = prop.name.split('has_')[1]
                for cert in Certificates.Certificate.list():
                    if str(cert) == certificate and cert not in player.has_certificates:
                        player.has_certificates.append(cert)
                        all.append("Congrats! you hold the %s Certificate!" % cert.name)

        # Next cell has payment
        if board.BALANCE in board_game[cell] and board_game[cell][
            board.BALANCE] < 0 and cell not in player.need_pay_spots:
            player.need_pay_spots.append(cell)
        return all, 1

    # Pay X money
    if 'pay' in action.name:
        cell = (int(action.name.split('_')[3]), int(action.name.split('_')[4]))
        amount = int(action.name.split('_')[1])
        total_amount = player.money - amount

        # In cell we already visited and we have enough money
        if cell in player.need_pay_spots and total_amount >= 0:
            player.need_pay_spots.remove(cell)
        elif total_amount < 0:
            if cell not in player.need_pay_spots:
                player.need_pay_spots.append(cell)
            return [], 0

        player.money = total_amount
        sign = "+"
        if amount > 0:  # then it is a payment and not to get money
            sign = "-"
        return ["Money " + sign + "= " + str(abs(amount)) + "\nMoney Balance: " + str(player.money)], 0
    return [], 0


def handle_goto(action, player):
    """
    Handle Goto- update the player's position, and removes come_back from this cell.
    Can only be performed by the player if a jump action was made
    :param action: the jump action
    :param player: the agent that performed the move
    :return: description of the move
    """
    cell = int(action.split('_')[1]), int(action.split('_')[2])
    player.cell = cell
    if cell in player.come_back_spots:
        player.come_back_spots.remove(cell)
    return ["Go back to (%d,%d)" % cell]


def handle_jump_to_entrance(action, player):
    """
    Handle jump- update the player's position, and puts come_back on this cell.
    Can only be performed if the player doesn't have the certificate/money the cell requires.
    :param action: the jump action
    :param player: the agent that performed the move
    :return: description of the move
    """
    jump_to = (int(action.name.split("_")[3]), int(action.name.split("_")[4]))
    player.cell = jump_to
    player.come_back_spots.append((int(action.name.split('_')[6]), int(action.name.split('_')[7])))
    return ["Jumped to (%s,%s) to search" % jump_to]


def handle_move(plan, player):
    """
    A function that handles the Move action. Updates the player properties in
    order to build the next plan, and to remember the moves we already made.
    The Move action can lead to another action- goto, pay (all the types), jump,
    we will handle them too, and stop to process the plan when
    we get to the next Move action
    :param plan: The plan A* build
    :param player: the agent we need to update
    :return: all the moves we processed + the amount of turns (usually 1, but in cases like Stop, can be more)
    """
    all_current_moves = []
    turns = 1
    action = plan[0]
    action_name = plan[0].name
    if 'Move' in plan[0].name:
        cell = (int(action_name.split('_')[5]), int(action_name.split('_')[6]))
        player.cell = cell

        # update the moves we performed so far in the current round
        if cell not in board.Board.fake_cells:
            all_current_moves.append("Move to (%s,%s)" % player.cell)
        if board.MESSAGE in board_game[cell]:
            all_current_moves.append(board_game[cell][board.MESSAGE])

        # if we come back to a cell to pay money or show certificate, update the player
        if cell in player.come_back_spots:
            player.come_back_spots.remove(cell)

        # check for certificate
        for prop in action.add:
            if 'has' in prop.name:
                # need to match the exact name of the certificate
                certificate = prop.name.split('has_')[1]
                for cert in Certificates.Certificate.list():
                    if str(cert) == certificate and cert not in player.has_certificates:
                        player.has_certificates.append(cert)
                        all_current_moves.append("Congrats! you hold the %s Certificate!" % cert.name)

        # Next cell has payment
        if board.BALANCE in board_game[cell] and board_game[cell][
            board.BALANCE] < 0 and cell not in player.need_pay_spots:
            player.need_pay_spots.append(cell)

        for prop in action.pre:
            if 'has' in prop.name:
                certificate = prop.name.split('has_')[1].split(".")[1].lower()
                all_current_moves.append("Presented the certificate: " + certificate)

    for i, action in enumerate(plan):

        # handled the move already
        if i == 0:
            continue

        # if we encounter another move- we finished the current round
        if 'Move' in action.name:
            break

        # In case the next move is payment, we will perform the payment (lottery, Surprise, a cell
        # that requires  money, move that requires money) + update the player properties
        if 'pay' in action.name:
            pay, turn = handle_payments(action, player)
            turns += turn
            all_current_moves.extend(pay)

        # In case the move we did led us to a cell that require us to wait X turns,
        # we will wait X turns and update the moves the player did in this round + update the player properties
        elif 'Stop' in action.name:
            stops = handle_stop(plan[i:])
            turns += len(stops)
            all_current_moves.extend(stops)
            break

        # In case we can go back to a certain cell that we already visited + update the player properties
        elif 'Goto' in action.name:
            goto = handle_goto(action.name, player)
            turns += 1
            all_current_moves.extend(goto)

        # In case we can't pay or don't hold a certain certificate the cell requests we jump
        # to a nearby cell + update the player properties + update the moves we did in the current round
        elif 'jump' in action.name:
            jump = handle_jump_to_entrance(action, player)
            all_current_moves.extend(jump)

    return all_current_moves, turns


def write_to_log(string, logs):
    """
    Writing to the log file of the current game
    :param string: the string to write to the log file
    :param logs: the file to write to
    """
    logs.write(string + "\n") if Constants.DEBUG else None


def prints_game_over(moves, logs, player, elapsed, turns, expanded):
    """
    Prints messages to the screen and to the log in case of success
    :param moves: the moves the player performed
    :param logs: the file we write to
    :param player: the agent that plays
    :param elapsed: the time in seconds
    """
    print_plan(moves, logs)
    print("Money: %d" % player.money)
    write_to_log("Money: %d" % player.money, logs)
    # print()
    print("--- Game finished after %d turns in %.2f seconds ---" % (turns, elapsed))
    print("The number of expanding nodes in each turn:\n%s" % "\n".join(expanded))
    write_to_log("game finished after %d turns in %.2f seconds" % (turns, elapsed), logs)
    write_to_log("The number of expanding nodes in each turn:\n%s" % "\n".join(expanded), logs)


def print_exit(logs, plan, moves):
    """
    Prints messages in case the plan fails, and exits the game
    :param logs: the file tp write to
    :param plan: the plan the A* built
    :param moves: the moves so far the agent performed
    """
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


def write_current_move_logs(inner_past_moves, inner_player, inner_turns, inner_logs):
    """
    Writes to the log file all the moves the agent performed in this round
    :param inner_past_moves: all the moves up to this round
    :param inner_player: the agent that plays
    :param inner_turns: the number of turns the agent played so far
    :param inner_logs: the file we are writing to
    """
    write_to_log("round %s" % inner_turns, inner_logs)
    inner_past_moves.append((inner_player.cell[0], inner_player.cell[1]))
    print_current_board(inner_past_moves, inner_player)


def print_plan_test(plan):
    for p in plan:
        print(p)


def find_last_dice(plan):
    for i, p in enumerate(plan):
        if i == 0:
            continue
        action = p.name
        if 'Move' not in action:
            continue
        else:
            return i, int(action[-1])
    return None, None


def assert_arguments():
    if len(sys.argv) != 2 and len(sys.argv) != 3 and len(sys.argv) != 4 and len(sys.argv) != 5:
        print(
            "Usage: game_old.py player: optimistic \ average optional--> goal_point: x,y start point: x,y starting money: m. Bad input")
        exit()

    if sys.argv[1] != Types.AVERAGE.value and sys.argv[1] != Types.OPTIMISTIC.value:
        print(
            "Usage: game_old.py player: optimistic \ average optional--> goal_point: x,y start point: x,y starting money: m. Bad input")
        exit()


def init_player(input_player):
    if len(sys.argv) == 2:
        player_init = Player(input_player)
    else:
        goal = sys.argv[2]
        goal = goal.split(",")
        goal = (int(goal[0]), int(goal[1]))
        if len(sys.argv) == 3:
            player_init = Player(input_player, goal)
        else:
            start_cell = sys.argv[3]
            start_cell = start_cell.split(",")
            start_cell = (int(start_cell[0]), int(start_cell[1]))
            if len(sys.argv) == 4:
                player_init = Player(input_player, goal, start_cell)

            else:
                money = int(sys.argv[4])
                player_init = Player(input_player, goal, start_cell, money)
    return player_init


def play_for_pay_150(turns, plan, moves, logs, player):
    # cell = (plan[0].name.split('_')[6], plan[0].name.split('_')[7])
    is_continue = False
    move, turn = handle_payments(plan[0], player)
    turns += turn
    write_to_log("current moves done:", logs)
    print_plan(move, logs)
    moves.extend(move)
    if len(plan) > 1 and 'pay_500' in plan[1].name:
        move, turn = handle_payments(plan[1], player)
        moves.extend(move)
        plan = plan[2:]
    if len(plan[1:]) != 0:
        plan = plan[1:]
        is_continue = True
    return turns, plan, is_continue


def play_for_move(turns, plan, moves, logs, player):
    moves.append(ROLLING % player.dice_value)
    # cell = (int(plan[0].name.split('_')[5]), int(plan[0].name.split('_')[6]))
    move, turn = handle_move(plan, player)
    turns += turn
    write_to_log("current moves done:", logs)
    print_plan(move, logs)
    moves.extend(move)
    return turns, moves


def play_for_jump(turns, plan, moves, logs, player):
    is_continue = False
    # cell = (int(plan[0].name.split("_")[3]), int(plan[0].name.split("_")[4]))
    move = handle_jump_to_entrance(plan[0], player)
    moves.extend(move)
    write_to_log("current moves done:", logs)
    print_plan(move, logs)
    if len(plan[1:]) != 0:
        plan = plan[1:]
        is_continue = True

    return turns, plan, moves, is_continue


def play_for_goto(plan, moves, logs, player):
    is_continue = False
    cell = int(plan[0].name.split('_')[1]), int(plan[0].name.split('_')[2])
    move = handle_goto(plan[0].name, player)
    player.cell = cell
    write_to_log("current moves done:", logs)
    print_plan(move, logs)
    moves.extend(move)
    if len(plan[1:]) != 0:
        plan = plan[1:]
        is_continue = True
    return plan, moves, is_continue


def run_game(heuristic_name, player, domain_file_name, problem_file_name, gen_flag):
    # Start the first round: roll a dice, and build the first problem, and creates the first
    # plan

    # Update the file names
    heuristic = max_level
    if heuristic_name == "sum":
        heuristic = level_sum
    dice_obj = Dice(gen_flag)
    start = time.process_time()
    domain_file_name = dc.create_domain_file(domain_file_name, player.type)
    problem_file_name = problem_file_name.format(player.type)
    dice_val = dice_obj.roll_dice()
    player.dice_value = dice_val
    player.build_problem()
    print(ROLLING % player.dice_value + "MONEY: " + str(player.money))
    prob = PlanningProblem(domain_file_name, problem_file_name, None, None)
    plan = a_star_search(prob, heuristic=heuristic)

    for p in plan:
        print(p)
    turns, expanded = 0, []
    print(player.goal)
    # All the moves the player does in the game
    moves = [START % player.cell]
    moves.append("Amount of money: %s " % player.money)
    past_moves = [player.cell]
    with open("logs\log-{}.txt".format(str(datetime.datetime.now()).replace(":", "")), "w") as logs:
        while len(plan) != 0 and plan != 'failed':
            # Each plan most start with a movement from one cell to other cell
            # Move- move from one cell to the other, according to the dice
            if 'Move' in plan[0].name:
                turns, moves = play_for_move(turns, plan, moves, logs, player)
            # Move from one cell to "orange" cell, and pay 150, if it is achievable according to the dice
            elif 'pay_150' in plan[0].name:
                turns, plan, isContinue = play_for_pay_150(turns, plan, moves, logs, player)
                if isContinue: continue
                # Jump to a certain entrance if you don't have enough money to pay, or if you don't hold the
            # requested certificate
            elif 'jump' in plan[0].name:
                turns, plan, moves, isContinue = play_for_jump(turns, plan, moves, logs, player)
                if isContinue: continue

            # Go back to a cell already visited, if the player has the certificate/money to pay
            elif 'Goto' in plan[0].name:
                plan, moves, isContinue = play_for_goto(plan, moves, logs, player)
                if isContinue: continue

            else:
                # A plan can only start with a move from one cell to another
                print_exit(logs, plan, moves)

            # Starting a new round- creating a new problem.txt file
            # New round- roll the dice, and build a new plan according to the previous move
            write_current_move_logs(past_moves, player, turns, logs)
            actions = prob.get_actions()
            propositions = prob.get_propositions()
            player.dice_value = dice_obj.roll_dice()
            loc, last_dice = find_last_dice(plan)
            player.build_problem()
            expanded.append(str(prob.expanded))
            print(ROLLING % player.dice_value)
            prob = PlanningProblem(domain_file_name, problem_file_name, actions, propositions)
            if last_dice == player.dice_value and last_dice is not None and len(player.need_pay_spots) == 0:
                plan = plan[loc:]
            else:
                plan = a_star_search(prob, heuristic=heuristic)
            print_plan(plan, logs)

            if len(plan) == 0:
                write_to_log("## LAST ##", logs)
            # write_to_log("###########ACTIONS##########", logs)
            # for action in actions:
            #     write_to_log(action.name, logs)
            write_to_log("@@@@@@@@@@@PROPOSITIONS@@@@@@@@@@@", logs)
            for state in prob.initialState:
                write_to_log(state.name, logs)

        elapsed = time.process_time() - start
        if moves is not None and plan != "failed":
            prints_game_over(moves, logs, player, elapsed, turns, expanded)
        else:
            print("Could not find a plan in %.2f seconds" % elapsed)
            write_to_log("Could not find a plan in %.2f seconds" % elapsed, logs)
    return elapsed, expanded, turns


if __name__ == '__main__':
    """
    Input = python3 game_old.py player
    Output = print all moves + position on the board at each round

    Runs the game. It build the initial plan (domain and problem) according to a given player, and at every plan the A* 
    search builds, it creates a new problem (the domain stays the same), update the board, and run the search again
    until the agent gets to the final cell
    """
    assert_arguments()
    input_player = sys.argv[1]
    player = init_player(input_player)

    domain_file_name = 'domain.txt'
    problem_file_name = '{}_problem.txt'

    run_game("sum", player, domain_file_name, problem_file_name, 1)
