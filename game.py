from graphplan.search import a_star_search
from domain_create import Types
from graphplan.planning_problem import PlanningProblem, max_level
import domain_create as dc
import surprise
from player import Player
import Certificates
from dice import Dice
import board


board_game = board.Board().transition_dict

def print_plan(plan):
    for a in plan:
        print(a)


def handle_stop(plan):
    all = []
    for move in plan:
        if 'Stop' in move.name:
            all.append(move)
        else:
            break
    return all


def handle_payments(action, player):
    cell = (int(action.split('_')[6]), int(action.split('_')[7]))
    if 'pay_surprise' in action:
        amount = surprise.Surprise.get_surprise()
        if player.money - amount >= 0:
            player.money -= amount
            if cell in player.need_pay_spots:
                player.need_pay_spots.remove(cell)
        else:
            player.owe.append(amount)
        return ("pay suprise %d" % -amount), 0
    if 'pay_150_from' in action:
        amount = int(action.split('_')[1])
        player.money -= amount
        player.cell = cell
        if cell in player.need_pay_spots:
            player.need_pay_spots.remove(cell)
        return ("pay 150 to go to (%d,%d)" % cell), 1
    if 'pay' in action:
        amount = int(action.split('_')[1])
        player.money -= amount
        if cell in player.need_pay_spots:
            player.need_pay_spots.remove(cell)
        return ("pay %d" % -amount), 0
    return None


def handle_goto(action, player):
    cell = action.split('_')[1], action.split('_')[2]
    player.cell = cell
    player.come_back_spots.remove(cell)
    return "Go back to (%d,%d)" % cell


def handle_move(plan, player):
    all = []
    turns = 1
    action = plan[0].name
    if 'move' in action:
        player.cell = (action.split('_')[5], action.split('_')[6])
        all.append("Move to (%d,%d)" % player.cell)
        for prop in action.add:
            if 'has' in prop:
                certificate = action.add.split('has_')[1]
                for cert in Certificates.certificates:
                    if str(cert) == certificate:
                        player.has_certificates.append(cert)
        for prop in action.pre:
            if 'has' in prop:
                certificate = action.add.split('has_')[1].split(".")[1]
                all.append("presented the certificate: " + certificate)
    if player.cell in board.Board.loto_cells:
        dice_val = Dice.roll_dice()
        if board.BALANCE in board_game[board_game[player.cell][dice_val][0]]:
            player.money += board_game[board_game[player.cell][dice_val][0]][board.BALANCE]
        turns += 1
    for action in plan:
        if 'pay' in action.name:
            pay, turn = handle_payments(action.name, player)
            turns += 1
            all.append(pay)

        elif 'Stop' in action.name:
            stops = handle_stop(plan)
            turns += len(stops)
            all.append("stop %d times" % len(stops))

        elif 'Goto' in action.name:
            goto = handle_goto(action.name, player)
            turns += 1
            all.extend(goto)

        elif 'place_comeback' in action.name:
            cb_to = (action.name.split("-")[2], action.name.split("-")[3])
            player.come_back_spots.append(cb_to)
            all.append("placed comeback at (%d,%d)" % cb_to)

        elif 'jump' in action.name:
            jump_to = (action.name.split("-")[2], action.name.split("-")[3])
            player.cell = jump_to
            all.append("jumped to (%d,%d) to search" % jump_to)

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
    if input_player == Types.MEAN.value or input_player == Types.OPTIMISTIC.value:
        player.set_type(input_player)
        problem_file_name = problem_file_name.format(input_player.lower())
        domain_file_name = dc.create_domain_file(domain_file_name, input_player.lower())
        dice = Dice()
    else:
        print("Usage: game.py player(optimistic or mean). Bad type player.")
        exit()
    dice_val = dice.roll_dice()
    player.dice_value = dice_val
    player.build_problem()
    prob = PlanningProblem(domain_file_name, problem_file_name, None, None)
    # prob = None
    plan = a_star_search(prob, heuristic=max_level)
    turns = 0
    moves = []

    while len(plan) != 0:
        if 'Move' in plan[0].name:
            cell = (plan[0].name.split('_')[5], plan[0].name.split('_')[6])
            move, turn = handle_move(plan, player)
            turns += turn
            dice = dice.roll_dice()
            player.dice_value = dice
            moves.extend(move)
            if "message" in board.Board.get_cell(cell):
                moves.append(board.Board.get_cell(cell)["message"])

            # Starting new round- creating new problem file
            player.build_problem()
            actions = prob.get_actions()
            propositions = prob.get_propositions()
            prob = PlanningProblem(domain_file_name, problem_file_name, actions, propositions)
            plan = a_star_search(prob)
        else:
            print("plan doesn't start with move!!!")
            print(plan[0].name)
            exit(1)
    elapsed = time.process_time() - start
    if moves is not None:
        print("game finished after %d turns in %.2f seconds" % (len(moves), elapsed))
        print()
        print_plan(moves)
        print()
    else:
        print("Could not find a plan in %.2f seconds" % elapsed)
