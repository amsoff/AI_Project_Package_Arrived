from graphplan.search import a_star_search
from domain_create import Types
from graphplan.planning_problem import PlanningProblem, max_level, level_sum
import domain_create as dc
from surprise import Surprise
from player import Player
import Certificates
from dice import Dice
import board


board_game = board.Board().transition_dict
surprise_generator = Surprise()

def print_plan(plan):
    for a in plan:
        print(a)


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
        if player.money - amount >= 0:
            player.money -= amount
            if cell in player.need_pay_spots:
                player.need_pay_spots.remove(cell)
        else:
            player.owe.append(amount)
        return ["pay suprise %d" % -amount], 0
    if 'pay_150_from' in action.name: # TODO - if user pays 150 it doesn't mean he has some certificate
        all  = []
        cell = (int(action.name.split('_')[6]), int(action.name.split('_')[7]))
        player.money -= 150
        player.cell = cell
        if cell in player.need_pay_spots:
            player.need_pay_spots.remove(cell)
        # need to match the exact name of the certificate

        certificate = "".join(add for add in action.add if "has_" in add)
        all.append("pay 150 to go to (%d,%d)" % cell)
        if certificate != "":
            player.has_certificates.append(Certificates.Certificate[certificate])
            all.append("Congrats! you hold the %s Certificate!" % certificate)

        return all, 1
    if 'pay' in action.name:
        cell = (int(action.name.split('_')[3]), int(action.name.split('_')[4]))
        amount = int(action.name.split('_')[1])
        player.money -= amount
        if cell in player.need_pay_spots:
            player.need_pay_spots.remove(cell)
        return ["pay %d" % -amount], 0
    return None


def handle_goto(action, player):
    cell = action.split('_')[1], action.split('_')[2]
    player.cell = cell
    player.come_back_spots.remove(cell)
    return "Go back to (%d,%d)" % cell


def handle_move(plan, player):
    all = []
    turns = 1
    action = plan[0]
    action_name = plan[0].name
    if 'Move' in plan[0].name:
        player.cell = (action_name.split('_')[5], action_name.split('_')[6])
        if cell not in board.Board.loto_cells:
            all.append("Move to (%s,%s)" % player.cell)
        for prop in action.add:
            if 'has' in prop.name:
                # need to match the exact name of the certificate
                certificate = prop.name.split('has_')[1]
                for cert in Certificates.Certificate.list():
                    if cert.name == certificate:
                        player.has_certificates.append(cert)
                        all.append("Congrats! you hold the %s Certificate!" % cert.name)
        for prop in action.pre:
            if 'has' in prop.name:
                certificate = prop.name.split('has_')[1].split(".")[1].lower()
                all.append("presented the certificate: " + certificate)
    if player.cell in board.Board.loto_cells:
        dice_val = Dice.roll_dice()
        if board.BALANCE in board_game[board_game[player.cell][dice_val][0]]:
            player.money += board_game[board_game[player.cell][dice_val][0]][board.BALANCE]
            all.append("You win the lottery. YAY! You earned %s")
        turns += 1
    for i, action in enumerate(plan):
        # handle it already
        if i == 0:
            continue

        # if we encounter another move- we finished the current round
        if 'Move' in action.name or 'pay_150' in action.name :
            break

        if 'pay' in action.name:
            pay, turn = handle_payments(action, player)
            turns += 1
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

        elif 'place_comeback' in action.name:
            cb_to = (action.name.split("-")[2], action.name.split("-")[3])
            player.come_back_spots.append(cb_to)
            all.append("placed comeback at (%s,%s)" % cb_to)

        elif 'jump' in action.name:
            jump_to = (action.name.split("_")[2], action.name.split("_")[3])
            player.cell = jump_to
            all.append("jumped to (%s,%s) to search" % jump_to)

    return all, turns


if __name__ == '__main__':
    """
    input = python3 game.py player
    outout = print all moves
    """
    import sys
    import time

    start = time.process_time()

    if len(sys.argv) != 2:
        print("Usage: game.py player(optimistic or mean). Bad input")
        exit()
    input_player = sys.argv[1]
    domain_file_name = 'domain.txt'
    problem_file_name = '{}_problem.txt'
    player = Player()
    dice = Dice()
    if input_player == Types.MEAN.value or input_player == Types.OPTIMISTIC.value:
        player.set_type(input_player)
        problem_file_name = problem_file_name.format(input_player.lower())
        domain_file_name = dc.create_domain_file(domain_file_name, input_player.lower())
    else:
        print("Usage: game.py player(optimistic or mean). Bad type player.")
        exit()
    dice_val = dice.roll_dice()
    player.dice_value = dice_val
    player.build_problem()
    prob = PlanningProblem(domain_file_name, problem_file_name, None, None)
    plan = a_star_search(prob, heuristic=level_sum)
    turns = 0
    moves = ["Welcome to the package Arrive Game. You are positioned at (1,0)"]

    while len(plan) != 0:
        if 'Move' in plan[0].name:
            cell = (plan[0].name.split('_')[5], plan[0].name.split('_')[6])
            move, turn = handle_move(plan, player)
            turns += turn
            moves.extend(move)
        elif 'pay_150' in plan[0].name:
            cell = (plan[0].name.split('_')[6], plan[0].name.split('_')[7])
            move, turn = handle_payments(plan[0], player)
            turns += turn
            moves.extend(move)

            if len(plan[1:]) != 0:
                move, turn = handle_move(plan[1:], player)
                turns += turn
                moves.extend(move)
        else:
            print("plan doesn't start with move!!! The current action was:")
            print(plan[0].name)
            exit(1)

        if board.MESSAGE in board_game[int(cell[0]), int(cell[1])]:
            moves.append(board_game[int(cell[0]),int(cell[1])]["message"])

        # Starting new round- creating new problem.txt file
        actions = prob.get_actions()
        propositions = prob.get_propositions()
        player.dice_value = dice.roll_dice()
        player.build_problem()
        prob = PlanningProblem(domain_file_name, problem_file_name, actions, propositions)
        plan = a_star_search(prob, heuristic=level_sum)
    elapsed = time.process_time() - start
    if moves is not None:
        print()
        print_plan(moves)
        print("Money: %d" % player.money)
        print()
        print("game finished after %d turns in %.2f seconds" % (len(moves)-1, elapsed))
    else:
        print("Could not find a plan in %.2f seconds" % elapsed)