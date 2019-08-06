from Certificates import Certificate
import board
from dice import Dice
from surprise import Surprise
from Constants import Types
import Constants

# Action constants
NAME = Constants.NAME
PRE = Constants.PRE
ADD = Constants.ADD
DEL = Constants.DEL

# Player constants
AVERAGE = Constants.AVERAGE
OPTIMISTIC = Constants.OPTIMISTIC


# PROPOSITIONS
AT_FORMAT = Constants.AT_FORMAT
DICE_FORMAT = Constants.DICE_FORMAT
MONEY_FORMAT = Constants.MONEY_FORMAT
CERTIFICATES_FORMAT = Constants.CERTIFICATES_FORMAT
NOT_STOP_FORMAT = Constants.NOT_STOP_FORMAT
NEED_PAY_CELL = Constants.NEED_PAY_CELL
COME_BACK_FORMAT = Constants.COME_BACK_FORMAT
NOT_NEED_PAY_CELL = Constants.NOT_NEED_PAY_CELL
NOT_COME_BACK_FORMAT = Constants.NOT_COME_BACK_FORMAT
# NOT_NEEDS_FORMAT = "not_needs_%s"


board_game = board.Board().transition_dict

# ACTIONS:
# STOP:
FIRST_STOP_FORMAT = Constants.FIRST_STOP_FORMAT
# Name: stop1 pre: add: not_stop_1 delete:
STOP_FORMAT = Constants.STOP_FORMAT
# Name: stop(x) pre:stop(x-1) add: not_stop_x delete:

# PAYMENTS:
PAY_SURPRISE_FORMAT = Constants.PAY_SURPRISE_FORMAT
# pay surprise p1 from m pre need pay p1 at p1 money m add money m-x not need pay p1 del money m
# PAY_FIRST_SURPRISE = NAME + "pay_%s_surprise_%s_%s_from_%s" +PRE + AT_FORMAT + " " + MONEY_FORMAT + " " + OWE + ADD + MONEY_FORMAT + " " + NOT_NEED_PAY_CELL + " " + NOT_OWE  + DEL + MONEY_FORMAT
# pay x surprise of p1 from m pre at p1 money m add money m-x not need pay p1 not owe x del money m

PAY_CELL = Constants.PAY_CELL
# pay x at p1 from m pre need_pay_p1 at p1 money m add money m-x not need pay p1 del money m need pay p1

# jump to come back cell
GOTO_FORMAT = Constants.GOTO_FORMAT
# goto p2 from p1, pre comeback to p2, at p1, add at p2 not_CB_p2 del comeback p2 At_p1

GOTO_MONEY_FORMAT = Constants.GOTO_MONEY_FORMAT
# goto p2 from p1, pre comeback to p2, at p1, add at p2 not_CB_p2 del comeback p2 At_p1

# JUMP_TO_ENTRANCE = NAME + "jump_to_%s_%s_from_%s_%s" + PRE + COME_BACK_FORMAT + " " + AT_FORMAT + ADD + AT_FORMAT + DEL + AT_FORMAT
# jump to p2 from p1 pre comeback to p1 at p1 add at p2 del at p1

# jump to a nearby cell to search for certificate/money
JUMP_TO_ENTRANCE_ = Constants.JUMP_TO_ENTRANCE

# jump to p2 from p1 pre at p1 add cb_to_p1 at p2 del at p1

# # no need for take certificate?
# TAKE_CERTIFICATE = "Name: Take_%s\npre: At_%s_%s\nadd: has_%s\ndelete:"
# # take id pre at p1 add has id
# SHOW_CERTIFICATE = "Name: Show_%s\npre: has_%s\nadd: not_needs_%s\ndelete:"
# show id pre has id add not needs id

# CREATE ACTIONS

def create_move(player):
    """
    Creates the moves according to the rules, including pre/add/delete conditions
    :param player: Average player or optimistic player
    :return: moves
    """
    moves = dict()
    ret = []
    for tile1 in board_game:  # for every tile
        for d in Dice.values:  # for every die roll
            for tile2 in board_game[tile1][d]:  # for every tile accessible from tile1
                action = dict()
                action[NAME] = "Move_from_%s_%s_to_%s_%s_with_dice_%s" % (tile1[0], tile1[1], tile2[0], tile2[1], d)

                action[PRE] = DICE_FORMAT % d + " " + AT_FORMAT % (tile1[0], tile1[1])
                for s in range(1, Constants.MAX_STOPS + 1):
                    action[PRE] += " " + NOT_STOP_FORMAT % s

                action[ADD] = AT_FORMAT % (tile2[0], tile2[1])
                action[DEL] = ""
                if tile1 != tile2:
                    action[DEL] += AT_FORMAT % (tile1[0], tile1[1])

                if player == AVERAGE:
                    # action[ADD] += " " + DICE_FORMAT % 3
                    # if True: # Todo add here certain cells
                    for i in Dice.values:
                        if i not in Constants.DUMMY_DICE:
                            action[DEL] += " " + DICE_FORMAT % i
                        else:
                            action[ADD] += " " + DICE_FORMAT % i

                elif player == OPTIMISTIC:
                    for d1 in Dice.values:
                        action[ADD] += " " + DICE_FORMAT % d1

                # payments:
                if tile2 != tile1:
                    if board.BALANCE in board_game[tile2] or board.SURPRISE in board_game[tile2]:
                        action[DEL] += " " + NOT_NEED_PAY_CELL % tile2
                        action[ADD] += " " + NEED_PAY_CELL % tile2

                if board.BALANCE in board_game[tile1] or board.SURPRISE in board_game[tile1]:
                    action[PRE] += " " + NOT_NEED_PAY_CELL % tile1

                # take certificate:
                if board.HAS in board_game[tile2]:
                    action[ADD] += " " + CERTIFICATES_FORMAT % (board_game[tile2][board.HAS])

                if board.NEED in board_game[tile2] or (board.BALANCE in board_game[tile2] and
                                                       board_game[tile2][board.BALANCE] < 0):
                    action[DEL] += " " + COME_BACK_FORMAT % tile2
                    action[ADD] += " " + NOT_COME_BACK_FORMAT % tile2

                # show certificate:
                if board.NEED in board_game[tile1]:
                    for cert in board_game[tile1][board.NEED]:
                        action[PRE] += " " + CERTIFICATES_FORMAT % cert

                # wait turns
                if tile1 != tile2:
                    if board.WAIT in board_game[tile2]:
                        for i in range(1, board_game[tile2][board.WAIT] + 1):
                            action[DEL] += " " + NOT_STOP_FORMAT % i

                moves[(tile1, tile2, d)] = action

    for move in moves:
        all_moves = ''.join(['%s%s' % (k, v) for k, v in moves[move].items()])
        ret.append(all_moves)
    return ret


def create_pay_actions():
    """
    :return: actions for cells where we need to pay a certain amount of money
    """
    actions = []
    for tile in board_game:
        if board.BALANCE in board_game[tile]:
            for m in range(max(0, -board_game[tile][board.BALANCE]), 50 * Constants.NUM_OF_50_BILLS + 1, 50):
                actions.append(PAY_CELL %
                               (-board_game[tile][board.BALANCE], tile[0], tile[1], m, tile[0], tile[1], tile[0],
                                tile[1], m,
                                min(50 * Constants.NUM_OF_50_BILLS, m + board_game[tile][board.BALANCE]), tile[0], tile[1], m,
                                tile[0], tile[1]))
    return actions


def create_jump_to_entrance_actions(player):
    """
    :return: jump to nearby cells actions
    """
    jump_to_entrance_actions = []

    for tile in board_game:
        if (board.NEED in board_game[tile] or (board.BALANCE in board_game[tile] and board_game[tile][board.BALANCE] < 0)) and board.ENTRANCE in board_game[tile]:
            for tile2 in board_game[tile][board.ENTRANCE]:
                action = dict()
                action[Constants.NAME] = "jump_to_entrance_%s_%s" % tile2 + "_from_%s_%s" % tile
                action[Constants.PRE] = AT_FORMAT % tile
                action[Constants.ADD] = COME_BACK_FORMAT % tile + " " + AT_FORMAT % tile2
                action[Constants.DEL] = AT_FORMAT % tile + " " + NOT_COME_BACK_FORMAT % tile
                for d in [1,2,3]:
                    if d in Constants.DUMMY_DICE:
                        action[Constants.ADD] += " " + DICE_FORMAT % d
                    elif player == OPTIMISTIC:
                        action[Constants.ADD] += " " + DICE_FORMAT % d
                    else:
                        action[Constants.DEL] += " " + DICE_FORMAT % d
                jump_action = ''.join(
                        ['%s%s' % (k, v) for k, v in action.items()])
                jump_to_entrance_actions.append(jump_action)






    return jump_to_entrance_actions


def create_pay_surprise_actions(player):
    """
    :param player: type of player - average or dummy
    :return: Pay surprise actions
    """
    surprise_actions = []
    for tile in board_game:
        if board.SURPRISE in board_game[tile]:
            surprise = 0
            if player == OPTIMISTIC:
                surprise = Surprise.optimistic_expected_surprise
            elif player == AVERAGE:
                surprise = Surprise.avg_player_expected_surprise
            for m in range(max(0, -int(surprise)), 50 * Constants.NUM_OF_50_BILLS + 1, 50):
                surprise_actions.append(PAY_SURPRISE_FORMAT % (
                    tile[0], tile[1], m, tile[0], tile[1], tile[0], tile[1], m, min(50 * Constants.NUM_OF_50_BILLS, m + surprise),
                    tile[0], tile[1], m, tile[0], tile[1]))
    return surprise_actions


def create_pay_150_actions(player):
    """
    :return: Pay 150 in order to jump directly to an orange cell actions
    """
    direct_jump_actions = []
    pay_format = NAME + " pay_150_from_%s_%s_to_%s_%s_with_%s"
    for tile in board_game:
        if board.ORANGE in board_game[tile]:
            for value in board_game[tile][board.ORANGE]:
                for m in range(150, 50 * Constants.NUM_OF_50_BILLS + 1, 50):
                    name = pay_format % (tile[0], tile[1], value[0], value[1], m)
                    pre = [PRE, AT_FORMAT % (tile[0], tile[1]), MONEY_FORMAT % (m)]
                    for s in range(1, Constants.MAX_STOPS + 1):
                        pre.append(NOT_STOP_FORMAT % s)
                    add = [ADD, AT_FORMAT % (value[0], value[1]), MONEY_FORMAT % (m - 150)]
                    delete = [DEL, AT_FORMAT % (tile[0], tile[1]), MONEY_FORMAT % (m)]
                    if board.HAS in board_game[board_game[tile][board.ORANGE][0]]:
                        add.append(CERTIFICATES_FORMAT % (board_game[board_game[tile][board.ORANGE][0]][board.HAS]))
                    if board.NEED in board_game[tile]:
                        pre.append(CERTIFICATES_FORMAT % board_game[tile][board.NEED][0])
                    if board.GOTO in board_game[tile] and (board.BALANCE in board_game[tile] or board.SURPRISE in board_game[tile]):
                        pre.append(NOT_NEED_PAY_CELL % tile)
                    for d in [1, 2, 3]:
                        if d in Constants.DUMMY_DICE:
                            add.append(DICE_FORMAT % d)
                        elif player == OPTIMISTIC:
                            add.append(DICE_FORMAT % d)
                        else:
                            delete.append(DICE_FORMAT % d)



                    pre = " ".join(pre)
                    add = " ".join(add)
                    delete = " ".join(delete)
                    direct_jump_actions.append("%s%s%s%s" % (name, pre, add, delete))
    return direct_jump_actions


def create_goto_from_comeback(player):
    """
    :return: go back to where we left a "come back" sign actions
    """
    goto = []
    GOTO_MONEY_FORMAT = NAME + "Goto_%s_%s_from_%s_%s" + PRE + NOT_NEED_PAY_CELL + " " + COME_BACK_FORMAT + " " + AT_FORMAT + ADD + AT_FORMAT + " " + NOT_COME_BACK_FORMAT + DEL + COME_BACK_FORMAT + " " + AT_FORMAT  # FROM_COMEBACK
    # goto p2 from p1, pre comeback to p2, at p1, add at p2 not_CB_p2 del comeback p2 At_p1

    for tile in board_game:
        if board.GOTO in board_game[tile]:
            for tile2 in board_game[tile][board.GOTO]:
                action = dict()
                action[NAME] = "Goto_%s_%s" % tile2 + "_from_%s_%s" % tile
                action[PRE] = COME_BACK_FORMAT % tile2 + " " + AT_FORMAT % tile
                action[ADD] = AT_FORMAT % tile2 + " " + NOT_COME_BACK_FORMAT % tile2
                action[DEL] = COME_BACK_FORMAT % tile2 + " " + AT_FORMAT % tile

                if board.BALANCE in board_game[tile] or board.SURPRISE in board_game[tile]:
                    action[PRE] += " " + NOT_NEED_PAY_CELL % tile2

                for d in [1, 2, 3]:
                    if d in Constants.DUMMY_DICE:
                        action[Constants.ADD] += " " + DICE_FORMAT % d
                    elif player == OPTIMISTIC:
                        action[Constants.ADD] += " " + DICE_FORMAT % d
                    else:
                        action[Constants.DEL] += " " + DICE_FORMAT % d
                goto_action = ''.join(['%s%s' % (k, v) for k, v in action.items()])
                goto.append(goto_action)

    return goto

def create_stop_action():
    """
    :return: wait turns actions
    """
    stop_actions = []
    for tile in board_game:
        if board.WAIT in board_game[tile]:
            num_stops = board_game[tile][board.WAIT]
            stops = [FIRST_STOP_FORMAT % (tile[0], tile[1], tile[0], tile[1])]
            for x in range(2, num_stops + 1):
                stops.append(STOP_FORMAT % (str(x), tile[0], tile[1], tile[0], tile[1], str(x - 1), str(x)))
            stop_actions.extend(stops)
    return stop_actions


# CREATE PROPOSITIONS

def create_not_need_pay_props():
    """
    :return: propositions for cells where we don't have to pay
    """
    not_need_pay_props = []
    for tile in board_game:
        if board.BALANCE in board_game[tile] or board.SURPRISE in board_game[tile]:
            not_need_pay_props.append(NOT_NEED_PAY_CELL % (tile[0], tile[1]))
    return not_need_pay_props


def create_need_pay_props():
    """
    :return: propositions for cells where we need to pay
    """
    need_pay_props = []
    for tile in board_game:
        if board.BALANCE in board_game[tile] or board.SURPRISE in board_game[tile]:
            need_pay_props.append(NEED_PAY_CELL % (tile[0], tile[1]))
    return need_pay_props


def create_not_stop_props():
    """
    :return: propositions for cells where we don't have to wait turns
    """
    not_stop_props = []
    for x in range(1, Constants.MAX_STOPS + 1):
        not_stop_props.append(NOT_STOP_FORMAT % (str(x)))
    return not_stop_props


def create_has_money_props():
    """
    :return: propositions for amount of money a player has
    """
    has_money_props = []
    for x in range(0, 50 * Constants.NUM_OF_50_BILLS + 1, 50):
        has_money_props.append(MONEY_FORMAT % (str(x)))
    return has_money_props


def create_dice_props():
    """
    :return: dice values
    """
    dice = []
    for d in Dice.values:
        dice.append(DICE_FORMAT % (str(d)))
    return dice


def create_at_props():
    """
    :return: propositions for players position
    """
    at = []
    for tile in board_game:
        at.append(AT_FORMAT % tile)
    return at


def create_come_back_props():
    """
    :return: propositions for come back cells
    """
    come_backs = []
    for tile in board_game:
        if board.NEED in board_game[tile] or (board.BALANCE in board_game[tile] and
                                              board_game[tile][board.BALANCE] < 0):
            come_backs.append(COME_BACK_FORMAT % (tile[0], tile[1]))
    return come_backs


def create_not_come_back_props():
    """
    :return: propositions for not come back cells
    """
    not_come_backs = []
    for tile in board_game:
        if board.NEED in board_game[tile] or board.BALANCE in board_game[tile]:
            if board.BALANCE in board_game[tile] and board_game[tile][board.BALANCE] > 0:
                continue
            not_come_backs.append(NOT_COME_BACK_FORMAT % (tile[0], tile[1]))
    return not_come_backs


def create_certificates_props():
    """
    :return: all the possible certificates in the game
    """
    certificates = {CERTIFICATES_FORMAT % Certificate.GRANDMA,
                    CERTIFICATES_FORMAT % Certificate.INTEGRITY,
                    CERTIFICATES_FORMAT % Certificate.BIRTH,
                    CERTIFICATES_FORMAT % Certificate.ID,
                    CERTIFICATES_FORMAT % Certificate.PASSPORT,
                    CERTIFICATES_FORMAT % Certificate.TAX,
                    CERTIFICATES_FORMAT % Certificate.PORT,
                    CERTIFICATES_FORMAT % Certificate.HAIRCUT}
    return certificates


#############################################################################

def get_propositions():
    props = []
    props.extend(create_not_need_pay_props())
    props.extend(create_certificates_props())
    props.extend(create_come_back_props())
    props.extend(create_not_come_back_props())
    props.extend(create_at_props())
    props.extend(create_dice_props())
    props.extend(create_has_money_props())
    props.extend(create_not_stop_props())
    props.extend(create_need_pay_props())
    return props


def get_actions(player):
    actions = []
    actions.extend(create_move(player))
    actions.extend(create_pay_actions())
    actions.extend(create_jump_to_entrance_actions(player))
    actions.extend(create_pay_surprise_actions(player))
    actions.extend(create_pay_150_actions(player))
    actions.extend(create_stop_action())
    actions.extend(create_goto_from_comeback(player))

    return actions


def create_domain_file(domain_file_name, player):
    agent = Types.OPTIMISTIC.value
    if player == AVERAGE:
        agent = Types.AVERAGE.value
    file_name = agent + "_" + domain_file_name
    domain_file = open(file_name, 'w')  # use domain_file.write(str) to write to domain_file

    # write propositions to file
    domain_file.write("Propositions:\n")
    props = get_propositions()
    domain_file.write(" ".join(props))

    # write actions to file
    actions = get_actions(player)
    domain_file.write("\nActions:\n")
    domain_file.write("\n".join(actions))
    domain_file.write("\n")
    domain_file.close()
    return file_name


# if __name__ == '__main__':
#     domain_file_name = 'domain.txt'
#     problem_file_name = 'problem.txt'
#
#     create_domain_file(domain_file_name, "average")
