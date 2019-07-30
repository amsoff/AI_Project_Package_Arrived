import sys
from Certificates import Certificate
import board
import enum

# from player import Types


# problems = pay surprise can make agent stuck.
# NAME = 0
# PRE = 1
# ADD = 2
# DEL = 3


class Types(enum.Enum):
    OPTIMISTIC = "optimistic"
    MEAN = "mean"


MAXIMUM_PAY = 30
MAXIMUM_POCKET = 80
MAX_STOPS = 4

OPTIMI = Types.OPTIMISTIC.value
MEAN = Types.MEAN.value
players = [OPTIMI, MEAN]

MEAN_SURPRISE = -100
OPTIMI_SURPRISE = 100
NAME = "Name: "
PRE = "\npre: "
ADD = "\nadd: "
DEL = "\ndelete: "
# PROPOSITIONS
MONEY_FORMAT = "Money_%s"
AT_FORMAT = "At_%s_%s"
CERTIFICATES_FORMAT = "has_%s"
# NOT_NEEDS_FORMAT = "not_needs_%s"
DICE_FORMAT = "dice_%s"
COME_BACK_FORMAT = "Come_back_to_%s_%s"
NOT_COME_BACK_FORMAT = "Not_Come_back_%s_%s"
NOT_STOP_FORMAT = "Not_Stop_%s"
NOT_NEED_PAY_CELL = "not_need_pay_%s_%s"
NOT_OWE = "not_owe_%s"
OWE = "owe_%s"

#  make goal be all not_comebacks and  not needs and at END


board_game = board.Board(1).transition_dict

# ACTIONS:

# STOP:
FIRST_STOP_FORMAT = NAME + "Stop_1_at_%s_%s" + PRE + AT_FORMAT + " " + ADD + NOT_STOP_FORMAT % 1 + DEL
# Name: stop1 pre: add: not_stop_1 delete:
STOP_FORMAT = NAME + "Stop_%s_at_%s_%s" + PRE + AT_FORMAT + " " + NOT_STOP_FORMAT + ADD + NOT_STOP_FORMAT + DEL
# Name: stop(x) pre:stop(x-1) add: not_stop_x delete:


# PAYMENTS:

PAY_SURPRISE_FORMAT = NAME + "pay_surprise_%s_%s_from_%s" + PRE + AT_FORMAT + " " + MONEY_FORMAT  + ADD + MONEY_FORMAT + " " + NOT_NEED_PAY_CELL  + DEL + MONEY_FORMAT
# pay surprise p1 from m pre at p1 money m add money m-x not need pay p1 del money m
PAY_FIRST_SURPRISE = NAME + "pay_%s_surprise_%s_%s_from_%s" +PRE + AT_FORMAT + " " + MONEY_FORMAT + " " + OWE + ADD + MONEY_FORMAT + " " + NOT_NEED_PAY_CELL + " " + NOT_OWE  + DEL + MONEY_FORMAT
# pay x surprise of p1 from m pre at p1 money m add money m-x not need pay p1 not owe x del money m

# from certain locations in the map you can pay 150 shekels to get where you need.
PAY_150_FORMAT = NAME + "pay_150_from_%s_%s_to_%s_%s_with_%s" + PRE +AT_FORMAT + " " + MONEY_FORMAT + ADD + AT_FORMAT + " " + MONEY_FORMAT + DEL + AT_FORMAT + " " + MONEY_FORMAT
# pay 150 to jump from p1 to p2 with x money, pre at p1, money x, add at p2, money x-150, del at p1 money x.

PAY_CELL = NAME + "pay_%s_At_%s_%s_from_%s" + PRE + AT_FORMAT +" " + MONEY_FORMAT + ADD +MONEY_FORMAT +" " + NOT_NEED_PAY_CELL  + DEL + MONEY_FORMAT
# pay x at p1 from m pre at p1 money m add money m-x not need pay p1 del money m


# jump to techef ashuv block
GOTO_FORMAT = NAME + "Goto_%s_%s_from_%s_%s" + PRE + COME_BACK_FORMAT + " " + AT_FORMAT + ADD + AT_FORMAT + " " + NOT_COME_BACK_FORMAT + DEL + COME_BACK_FORMAT + " " + AT_FORMAT # FROM_COMEBACK
# goto p2 from p1, pre comeback to p2, at p1, add at p2 not_CB_p2 del comeback p2 At_p1

JUMP_TO_ENTRANCE = NAME + "jump_to_%s_%s_from_%s_%s" + PRE + COME_BACK_FORMAT + " " + AT_FORMAT + ADD + AT_FORMAT +DEL + AT_FORMAT
# jump to p2 from p1 pre comeback to p1 at p1 add at p2 del at p1


# # no need for take certificate?
# TAKE_CERTIFICATE = "Name: Take_%s\npre: At_%s_%s\nadd: has_%s\ndelete:"
# # take id pre at p1 add has id
# SHOW_CERTIFICATE = "Name: Show_%s\npre: has_%s\nadd: not_needs_%s\ndelete:"
# show id pre has id add not needs id

# put comeback:
PUT_COMEBACK = "Name: place_comeback_%s_%s" + PRE + AT_FORMAT + ADD +COME_BACK_FORMAT + DEL + NOT_COME_BACK_FORMAT
# place comeback at p1 pre: at p1 add: comeback p1 delete: not_CB_p1


############ actions ###########
def create_move(player):
    moves = dict()
    ret = []
    for tile1 in board_game:  # lekol mishbetzet
        for d in [1,3,5]:  # lekol gilgul_kubia
            for tile2 in board_game[tile1][d]: # lekol mishbetzet she'efshar lehagia elia
                action = dict()
                action[NAME] = "Move_from_%s_%s_to_%s_%s" % (tile1[0], tile1[1], tile2[0], tile2[1])

                action[PRE] = DICE_FORMAT % d + " " + AT_FORMAT % (tile1[0], tile1[1])
                for s in range(1, MAX_STOPS+1):
                    action[PRE] += " " + NOT_STOP_FORMAT % s

                action[ADD] = AT_FORMAT % (tile2[0], tile2[1])
                if player == MEAN:
                    action[ADD] += " " + DICE_FORMAT % 3
                    if True: # Todo add here certain cells
                        action[ADD] += " " + DICE_FORMAT % 1
                elif player == OPTIMI:
                    for d1 in [1,3,5]:
                        action[ADD] += " " + DICE_FORMAT % d1

                action[DEL] = AT_FORMAT % (tile1[0], tile1[1]) + " " + DICE_FORMAT % d


                # payments:
                if board.BALANCE in board_game[tile2] or board.SURPRISE in board_game[tile2]:
                    action[DEL] += " " + NOT_NEED_PAY_CELL % (tile2[0], tile2[1])

                if board.BALANCE in board_game[tile1] or board.SURPRISE in board_game[tile1]:
                    action[PRE] += " " + NOT_NEED_PAY_CELL % (tile1[0], tile1[1])


                # Surprises:
                if board.SURPRISE in board_game[tile1]:
                    for i in [100, 200, 300]:
                        action[PRE] += " " + NOT_OWE % i



                # take certificate:
                if board.HAS in board_game[tile2]:
                    action[ADD] += " " + CERTIFICATES_FORMAT % (board_game[tile2][board.HAS])

                # show certificate:
                if board.NEED in board_game[tile1]:  # eem zu mishbetzet shezarich lehazig teuda, zarich sheihihe teuda
                    for cert in board_game[tile1][board.NEED]:
                        if cert not in [Certificate.GLASSES, Certificate.HAT]:
                            action[PRE] += " " + CERTIFICATES_FORMAT % cert

                # # hat and glasses:
                # if board.NEED in board_game[tile2]:
                #     for cert in board_game[tile2][board.NEED]:
                #         if cert in [Certificate.GLASSES, Certificate.HAT]:
                #             action["delete: "] += " " + NOT_NEEDS_FORMAT % cert


                if board.WAIT in board_game[tile2]:  # eem heganu leazor, naazor
                    for i in range(1, board_game[tile2][board.WAIT]+1):
                        action[DEL] += " " + NOT_STOP_FORMAT % i

                moves[(tile1, tile2)] = action

    for move in moves:
        strng = ''.join(['%s%s' % (k,v) for k,v in moves[move].items()])
        ret.append(strng)
    return ret



                # pay - tomorrow
                # orange?


def create_pay_cell():
    actions = []
    for tile in board_game:
        if board.BALANCE in board_game[tile]:
            for m in range(max(0,-board_game[tile][board.BALANCE]), 50*MAXIMUM_POCKET+1, 50):
                actions.append(PAY_CELL % (-board_game[tile][board.BALANCE], tile[0], tile[1], m, tile[0], tile[1], m, min(50*MAXIMUM_POCKET,m+board_game[tile][board.BALANCE]), tile[0], tile[1], m))
    return actions


def create_jump_to_entrance():
    jumps = []
    for tile in board_game:
        if (board.NEED in board_game[tile] or board.BALANCE in board_game[tile] or board.SURPRISE in board_game[tile]) and board.ENTRANCE in board_game[tile]:
            tile2 = board_game[tile][board.ENTRANCE]
            jumps.append(JUMP_TO_ENTRANCE % (tile2[0], tile2[1], tile[0], tile[1], tile[0], tile[1], tile[0], tile[1],tile2[0], tile2[1] ,  tile[0], tile[1]))
    return jumps


def create_put_comeback():
    comeback = []
    for tile in board_game:
        if board.NEED in board_game[tile] or (board.BALANCE in board_game[tile] and board_game[tile][board.BALANCE]<0) or board.SURPRISE in board_game[tile]: # then there can be techef ashuv
                            # place comeback at p1,           pre: at p1,        add: comeback p1 del not CB p1
            comeback.append(PUT_COMEBACK % (tile[0], tile[1], tile[0], tile[1], tile[0], tile[1], tile[0], tile[1]))
    return comeback


def create_pay_surprise(player):
        pays = []
        for tile in board_game:
            if board.SURPRISE in board_game[tile]:  # check if not bug -> meaning of if: if there is a key surprise
                surprise = -1
                if player == OPTIMI:
                    surprise = OPTIMI_SURPRISE
                elif player == MEAN:
                    surprise = MEAN_SURPRISE
                for m in range(max(0,-surprise), 50 * MAXIMUM_POCKET+1, 50):
                    pays.append(PAY_SURPRISE_FORMAT % (tile[0], tile[1], m, tile[0], tile[1], m, min(50*MAXIMUM_POCKET, m+surprise), tile[0], tile[1], m))
        return pays

def create_pay_first_surprise():
    pays = []
    for tile in board_game:
        if board.SURPRISE in board_game[tile]:
            for s in [100, 200, 300]:
                for m in range(s, 50*MAXIMUM_POCKET+1, 50):
                    pays.append(PAY_FIRST_SURPRISE % (s, tile[0], tile[1], m, tile[0], tile[1], m, s, m-s, tile[0], tile[1], s, m))
    return pays
# pay x surprise of p1 from m pre at p1 money m add money m-x not need pay p1 not owe x del money m


def create_pay_150():
    pays = []
    for tile in board_game:
        if board.ORANGE in board_game[tile]: # check if not bug -> if there is a key orange
            for value in board_game[tile][board.ORANGE]:
                for m in range(150,50*MAXIMUM_POCKET+1, 50):  # can only pay 150 if you have at least 150
                                                        # from p1              to p2    with m money  pre at p1 m money add at p2 money m-150 del at p1 money m
                    pays.append(PAY_150_FORMAT % (tile[0], tile[1], value[0], value[1], m,  tile[0], tile[1], m, value[0], value[1], m-150, tile[0], tile[1], m))
    return pays


def create_goto_from_comeback():
    goto = []
    for tile in board_game:
        if board.JUMP in board_game[tile]:  
            for value in tile[board.JUMP]:
                                            # goto      p2      from      p1  pre comeback to p2              at p1   add        at p2                not CB p2     delete: pre
                goto.append(GOTO_FORMAT % (value[0], value[1], tile[0], tile[1], value[0], value[1], tile[0], tile[1], value[0], value[1], value[0], value[1], value[0], value[1], tile[0], tile[1]))
    return goto


# don't use for now
# def create_take_certificate():
#     takes = []
#     for tile in erez_dic:
#         if board.HAS in board_game[tile]:
#             takes.append(TAKE_CERTIFICATE % (tile[board.HAS], tile[0], tile[1], tile[board.HAS]))
#     return takes


# def create_show_certificate():
#     show = []
#     for tile in board_game:
#         if board.NEED in board_game[tile]:
#             show.extend([SHOW_CERTIFICATE % (d,d,d) for d in board_game[tile][board.NEED]])
#     return show


def create_stop_action():
    STOP_FORMAT = NAME + "Stop_%s_at_%s_%s" + PRE + AT_FORMAT + " " + NOT_STOP_FORMAT + ADD + NOT_STOP_FORMAT + DEL
    FIRST_STOP_FORMAT = NAME + "Stop_1_at_%s_%s" + PRE + AT_FORMAT + " " + ADD + NOT_STOP_FORMAT % 1 + DEL
    for tile in board_game:
        if board.WAIT in board_game[tile]:
            num_stops = board_game[tile][board.WAIT]
            stops = [FIRST_STOP_FORMAT % (tile[0], tile[1],tile[0], tile[1])]
            for x in range(2, num_stops+1):
                stops.append(STOP_FORMAT % (str(x), tile[0], tile[1], tile[0],tile[1], str(x-1), str(x)))
            return stops



############ PROPOSITIONS ############

def create_owe_not_owe():
    owes = []
    for i in [100, 200, 300]:
        owes.append(NOT_OWE % i)
        owes.append(OWE % i)
    return owes


def create_not_need_pay():
    pays = []
    for tile in board_game:
        if board.BALANCE in board_game[tile] or board.SURPRISE in board_game[tile]:
            pays.append(NOT_NEED_PAY_CELL % (tile[0], tile[1]))
    return pays


def create_not_stop():
    not_stop = []
    for x in range(1, MAX_STOPS+1):
        not_stop.append(NOT_STOP_FORMAT % (str(x)))
    return not_stop


def create_has_money():
    has = []
    for x in range(0, 50*MAXIMUM_POCKET+1, 50):
        has.append(MONEY_FORMAT % (str(x)))
    return has


def create_dice():
    dice = []
    for d in [1,3,5]:
        dice.append(DICE_FORMAT % (str(d)))
    return dice


def create_at():
    at = []
    for tile in board_game:
        at.append(AT_FORMAT % tile)
    return at


def create_come_back():
    cbs = []
    for tile in board_game:
        if board.NEED in board_game[tile] or (board.BALANCE in board_game[tile] and board_game[tile][board.BALANCE] <0) or board.SURPRISE in board_game[tile]:
            cbs.append(COME_BACK_FORMAT % (tile[0], tile[1]))
    return cbs


def create_not_come_back():
    cbs = []
    for tile in board_game:
        if board.NEED in board_game[tile] or board.BALANCE in board_game[tile] or board.SURPRISE in board_game[tile]:
            if board.BALANCE in board_game[tile] and board_game[tile][board.BALANCE] > 0:
                continue
            cbs.append(NOT_COME_BACK_FORMAT % (tile[0], tile[1]))
    return cbs


# def create_not_needs_items():
#     certificates = [NOT_NEEDS_FORMAT % Certificate.GRANDMA,
#                     NOT_NEEDS_FORMAT % Certificate.INTEGRITY,
#                     NOT_NEEDS_FORMAT % Certificate.BIRTH,
#                     NOT_NEEDS_FORMAT % Certificate.ID,
#                     NOT_NEEDS_FORMAT % Certificate.RABIES,
#                     NOT_NEEDS_FORMAT % Certificate.PASSPORT,
#                     NOT_NEEDS_FORMAT % Certificate.MILITARY,
#                     NOT_NEEDS_FORMAT % Certificate.TAX,
#                     NOT_NEEDS_FORMAT % Certificate.PORT,
#                     NOT_NEEDS_FORMAT % Certificate.PACKAGE,
#                     NOT_NEEDS_FORMAT % Certificate.HAIRCUT,
#                     NOT_NEEDS_FORMAT % Certificate.GLASSES,
#                     NOT_NEEDS_FORMAT % Certificate.HAT]
#     return certificates


def create_certificates():
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
    props.extend(create_not_need_pay())
    props.extend(create_certificates())
    # props.extend(create_not_needs_items())
    props.extend(create_come_back())
    props.extend(create_not_come_back())
    props.extend(create_at())
    props.extend(create_dice())
    props.extend(create_has_money())
    props.extend(create_not_stop())
    props.extend(create_owe_not_owe())
    return props


def get_actions(player):
    actions = []
    actions.extend(create_move(player))
    actions.extend(create_pay_cell())
    actions.extend(create_jump_to_entrance())
    actions.extend(create_put_comeback())
    actions.extend(create_pay_surprise(player))
    actions.extend(create_pay_first_surprise())
    actions.extend(create_pay_150())
    # actions.extend(create_show_certificate())
    actions.extend(create_stop_action())
    return actions


def create_domain_file(domain_file_name, player):
    agent = Types.OPTIMISTIC.value
    if player == MEAN:
        agent = Types.MEAN.value
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




### change ###
# def create_problem_file(problem_file_name_, n_, m_):
#     disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
#     pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
#     problem_file = open(problem_file_name_, 'w')  # use problem_file.write(str) to write to problem_file
#     initial = "Initial state: "
#     goal = "Goal state: "
#     for d in range(n_):
#         initial += PROP_FORMAT % (d, 0)  # all disks start on peg 0
#         initial += " "
#         goal += PROP_FORMAT % (d, m-1) + ' ' # all disks go to last peg
#
#     problem_file.write(initial + '\n')
#     problem_file.write(goal)
#     problem_file.close()
#

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: domain_create.py agent_code')
        sys.exit(2)

    input_player = sys.argv[1] # agent_Code
    if input_player != Types.MEAN.value and input_player != Types.OPTIMISTIC.value:
        print("Usage: game.py player(optimistic or mean). Bad type player.")
        exit()

    domain_file_name = 'domain.txt'
    problem_file_name = 'problem.txt'

    create_domain_file(domain_file_name, input_player)
    # create_problem_file(problem_file_name, code)
