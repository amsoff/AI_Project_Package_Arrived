import sys
from Certificates import Certificate
import board


NAME = 0
PRE = 1
ADD = 2
DEL = 3


MAXIMUM_PAY = 100
MAXIMUM_POCKET = 200
BOARD_WIDTH = 22
BOARD_HEIGHT = 30
MAX_STOPS = 4

OPTIMI = 1
MEAN = 2
players = [OPTIMI, MEAN]

MEAN_SURPRISE = -100
OPTIMI_SURPRISE = 2000

# PROPOSITIONS

MONEY_FORMAT = "Money_%s"
AT_FORMAT = "At_%s_%s"
CERTIFICATES_FORMAT = "has_%s"
NOT_NEEDS_FORMAT = "not_needs_%s"
DICE_FORMAT = "dice_%s"
COME_BACK_FORMAT = "Come_back_to_%s_%s"
NOT_STOP_FORMAT = "Not_Stop_%s"
NOT_NEED_PAY_CELL = "not_need_pay_%s_%s"
NOT_COME_BACK_FORMAT = "Not_Come_back_%s_%s"

#  make goal be all not_comebacks and  not needs and at END


board_game = board.Board(1).transition_dict

# ACTIONS:

# STOP:
FIRST_STOP_FORMAT = "Name: Stop_1\nPre: \nAdd: Not_Stop_1\n delete:"
STOP_FORMAT = "Name: Stop_%s\nPre: Not_Stop_%s\nAdd: Not_Stop_%s\n delete:"

# PAYMENTS:

PAY_SURPRISE_FORMAT = "Name: pay_surprise_%s_%s_from_%s\nPre: at_%s_%s Money_%s\nAdd: Money_%s not_need_pay_%s_%s\n delete: Money_%s"
# pay surprise p1 from m pre at p1 money m add money m-x not need pay p1 del money m

# from certain locations in the map you can pay 150 shekels to get where you need.
PAY_150_FORMAT = "Name: Pay_150_from_%s_%s_to_%s_%s_with_%s\n Pre: at_%s_%s Money_%s\n Add: at_%s_%s Money_%s\n delete: at_%s_%s Money_%s"
# pay 150 to jump from p1 to p2 with x money, pre at p1, money x, add at p2, money x-150, del at p1 money x.

# jump to techef ashuv block
GOTO_FORMAT = "Name: Goto_%s_%s_from_%s_%s\n Pre: Come_back_to_%s_%s at_%s_%s\n Add: at_%s_%s Not_Come_back_%s_%s\n delete: Come_back_to_%s_%s at_%s_%s " # FROM_COMEBACK
# goto p2 from p1, pre comeback to p2, at specific p1, add at p2 not_CB_p2 del at_p1 comeback p2, needs x


# # no need for take certificate?
# TAKE_CERTIFICATE = "Name: Take_%s\n Pre: at_%s_%s\n Add: has_%s\n delete:"
# # take id pre at p1 add has id
SHOW_CERTIFICATE = "Name: Show_%s\n Pre: has_%s\n Add: not_needs_%s\n delete:"
# show id pre has id add not needs id

# put comeback:

PUT_COMEBACK = "Name: place_comeback_%s_%s\n Pre: at_%s_%s \n Add: Come_back_to_%s_%s\n delete: Not_Come_back_%s_%s"
# place comeback at p1 Pre: at p1 Add: comeback p1 delete: not_CB_p1

JUMP_TO_ENTRANCE = "Name: jump_to_%s_%s_from_%s_%s\n Pre: Come_back_to_%s_%s at_%s_%s\n Add: at_%s_%s \n delete: at_%s_%s"
# jump to p2 from p1 pre comeback to p1 at p1 add at p2 del at p1


PAY_CELL = "Name: pay_%s_at_%s_%s_from_%s\n Pre: at_%s_%s Money_%s \n Add: Money_%s not_need_pay_%s_%s \n delete: Money_%s"
# pay x at p1 from m pre at p1 money m add money m-x not need pay p1 del money m



############ actions ###########
def create_move(player):
    moves = dict()
    ret = []
    for tile1 in board_game:  # lekol mishbetzet
        for d in [1,3,5]:  # lekol gilgul_kubia
            for tile2 in tile1[d]: # lekol mishbetzet she'efshar lehagia elia
                action = dict()
                action["Name: "] = "Move_from_%s_%s_to_%s_%s".format(tile1[0], tile1[1], tile2[0], tile2[1])

                action["Pre: "] = DICE_FORMAT.format(d) + " " + AT_FORMAT.format(tile1[0], tile1[1])
                for s in range(1, MAX_STOPS):
                    action["Pre: "] += " " + NOT_STOP_FORMAT.format(s)

                action["Add: "] = AT_FORMAT.format(tile2[0], tile2[1])
                if player == MEAN:
                    action["Add: "] += " " + DICE_FORMAT.format(3)
                elif player == OPTIMI:
                    for d1 in [1,3,5]:
                        action["Add: "] += " " + DICE_FORMAT.format(d1)

                action["delete: "] = AT_FORMAT.format(tile1[0], tile1[1]) + DICE_FORMAT.format(d)


                # payments:
                if tile2[board.BALANCE] is not None or tile2[board.SURPRISE] is not None:
                    action["delete: "] += " " + NOT_NEED_PAY_CELL.format(tile2[0], tile2[1])

                if tile1[board.BALANCE] is not None or tile1[board.SURPRISE] is not None:
                    action["Pre: "] += " " + NOT_NEED_PAY_CELL.format(tile1[0], tile1[1])


                # take certificate:
                if tile2[board.HAS] is not None:
                    action["Add: "] += " " + CERTIFICATES_FORMAT.format(tile2[board.HAS])

                # show certificate:
                if tile1[board.NEED] is not None:  # eem zu mishbetzet shezarich lehazig teuda, zarich sheihihe teuda
                    for cert in tile1[board.NEED]:
                        if cert not in [Certificate.GLASSES, Certificate.HAT]:
                            action["Pre: "] += " " + CERTIFICATES_FORMAT.format(cert)

                # hat and glasses:
                if tile2[board.NEED] is not None:
                    for cert in tile1[board.NEED]:
                        if cert in [Certificate.GLASSES, Certificate.HAT]:
                            action["delete: "] += " " + NOT_NEEDS_FORMAT.format(cert)


                if tile2[board.WAIT] is not None:  # eem heganu leazor, naazor
                    for i in range(1, tile2[board.WAIT]+1):
                        action["delete: "] += " " + NOT_STOP_FORMAT.format(i)

                moves[(tile1, tile2)] = action

    for move in moves:
        strng = '\n'.join(['%s%s' % (k,v) for k,v in move.iteritems()])
        ret.append(strng)
    return ret



                # pay - tomorrow
                # orange?


def create_pay_cell():
    actions = []
    for tile in board_game:
        if tile[board.BALANCE] is not None:
            for m in range(-tile[board.BALANCE], 50*MAXIMUM_POCKET+1, 50):
                actions.append(PAY_CELL.format(-tile[board.BALANCE], tile[0], tile[1], m, tile[0], tile[1], m, m+tile[board.BALANCE], tile[0], tile[1], m))
    return actions


def create_jump_to_entrance():
    jumps = []
    for tile in board_game:
        if (tile[board.NEED] is not None or tile[board.BALANCE] is not None or tile[board.SURPRISE] is not None) and tile[board.ENTRANCE] is not None:
            tile2 = tile[board.ENTRANCE]
            jumps.append(JUMP_TO_ENTRANCE.format(tile2[0], tile2[1], tile[0], tile[1], tile[0], tile[1], tile[0], tile[1],tile2[0], tile2[1] ,  tile[0], tile[1]))
    return jumps


def create_put_comeback():
    comeback = []
    for tile in board_game:
        if tile[board.NEED] is not None or tile[board.BALANCE] is not None or tile[board.SURPRISE] is not None: # then there can be techef ashuv
                            # place comeback at p1,           Pre: at p1,        Add: comeback p1 del not CB p1
            comeback.append(PUT_COMEBACK.format(tile[0], tile[1], tile[0], tile[1], tile[0], tile[1], tile[0], tile[1]))
    return comeback


def create_pay_surprise(player):
        pays = []
        for tile in board_game:
            if tile[board.SURPRISE] is not None:  # check if not bug -> meaning of if: if there is a key surprise
                surprise = -1
                if player == OPTIMI:
                    surprise = OPTIMI_SURPRISE
                elif player == MEAN:
                    surprise = MEAN_SURPRISE
                for m in range(surprise, 50 * MAXIMUM_POCKET+1, 50):
                    pays.append(PAY_SURPRISE_FORMAT.format(tile[0], tile[1], m, tile[0], tile[1], m, m-surprise, tile[0], tile[1], m))
        return pays


def create_pay_150():
    pays = []
    for tile in board_game:
        if tile[board.ORANGE] is not None: # check if not bug -> if there is a key orange
            for value in tile[board.ORANGE]:
                for m in range(150,50*MAXIMUM_POCKET+1, 50):  # can only pay 150 if you have at least 150
                                                        # from p1              to p2    with m money  pre at p1 m money add at p2 money m-150 del at p1 money m
                    pays.append(PAY_150_FORMAT.format(tile[0], tile[1], value[0], value[1], m,  tile[0], tile[1], m, value[0], value[1], m-150, tile[0], tile[1], m))
    return pays


def create_goto_from_comeback():
    goto = []
    for tile in board_game:
        if tile[board.JUMP] is not None:  # check if not bug -> if there is a key jump
            for value in tile[board.JUMP]:
                                            # goto      p2      from      p1  pre comeback to p2              at p1   add        at p2                not CB p2     delete: pre
                goto.append(GOTO_FORMAT.format(value[0], value[1], tile[0], tile[1], value[0], value[1], tile[0], tile[1], value[0], value[1], value[0], value[1], value[0], value[1], tile[0], tile[1]))
    return goto


# don't use for now
# def create_take_certificate():
#     takes = []
#     for tile in erez_dic:
#         if tile[board.HAS] is not None:
#             takes.append(TAKE_CERTIFICATE.format(tile[board.HAS], tile[0], tile[1], tile[board.HAS]))
#     return takes


def create_show_certificate():
    show = []
    for tile in board_game:
        if tile[board.NEED] is not None:
            show.append(SHOW_CERTIFICATE.format(tile[board.NEED], tile[board.NEED], tile[board.NEED]))
    return show


def create_stop_action():
    stop = [FIRST_STOP_FORMAT]
    for x in range(2, MAX_STOPS+1):
        stop.append(STOP_FORMAT.format(str(x), str(x-1), str(x)))
    return stop



############ PROPOSITIONS ############

def create_not_need_pay():
    pays = []
    for tile in board_game:
        if tile[board.BALANCE] is not None or tile[board.SURPRISE] is not None:
            pays.append(NOT_NEED_PAY_CELL.format(tile[0], tile[1]))
    return pays


def create_not_stop():
    not_stop = []
    for x in range(1, MAX_STOPS+1):
        not_stop.append(NOT_STOP_FORMAT.format(str(x)))
    return not_stop


def create_has_money():
    has = []
    for x in range(50*MAXIMUM_POCKET+1, 50):
        has.append(MONEY_FORMAT.format(str(50*x)))
    return has


def create_dice():
    dice = []
    for d in [1,3,5]:
        dice.append(DICE_FORMAT.format(str(d)))
    return dice


def create_at():
    at = []
    for x, y in board_game.keys():
        at.append(AT_FORMAT.format(str(x),str(y)))
    return at


def create_come_back():
    cbs = []
    for tile in board_game:
        if tile[board.NEED] is not None or tile[board.BALANCE] is not None or tile[board.SURPRISE] is not None:
            if tile[board.BALANCE] is not None and tile[board.BALANCE] > 0:
                continue
            cbs.append(COME_BACK_FORMAT.format(tile[0, tile[1]]))
            cbs.append(NOT_COME_BACK_FORMAT.format(tile[0], tile[1]))
    return cbs


def create_not_needs_items():
    certificates = [NOT_NEEDS_FORMAT.format(Certificate.GRANDMA),
                    NOT_NEEDS_FORMAT.format(Certificate.INTEGRITY),
                    NOT_NEEDS_FORMAT.format(Certificate.ID),
                    NOT_NEEDS_FORMAT.format(Certificate.RABIES),
                    NOT_NEEDS_FORMAT.format(Certificate.PASSPORT),
                    NOT_NEEDS_FORMAT.format(Certificate.MILITARY),
                    NOT_NEEDS_FORMAT.format(Certificate.TAX),
                    NOT_NEEDS_FORMAT.format(Certificate.PORT),
                    NOT_NEEDS_FORMAT.format(Certificate.PACKAGE),
                    NOT_NEEDS_FORMAT.format(Certificate.HAIRCUT),
                    NOT_NEEDS_FORMAT.format(Certificate.GLASSES),
                    NOT_NEEDS_FORMAT.format(Certificate.HAT)]
    return certificates


def create_certificates():
    certificates = {CERTIFICATES_FORMAT.format(Certificate.GRANDMA),
                    CERTIFICATES_FORMAT.format(Certificate.INTEGRITY),
                    CERTIFICATES_FORMAT.format(Certificate.BIRTH),
                    CERTIFICATES_FORMAT.format(Certificate.ID),
                    CERTIFICATES_FORMAT.format(Certificate.RABIES),
                    CERTIFICATES_FORMAT.format(Certificate.PASSPORT),
                    CERTIFICATES_FORMAT.format(Certificate.MILITARY),
                    CERTIFICATES_FORMAT.format(Certificate.TAX),
                    CERTIFICATES_FORMAT.format(Certificate.PORT),
                    CERTIFICATES_FORMAT.format(Certificate.GLASSES),
                    CERTIFICATES_FORMAT.format(Certificate.HAT),
                    CERTIFICATES_FORMAT.format(Certificate.PACKAGE),
                    CERTIFICATES_FORMAT.format(Certificate.HAIRCUT)}
    return certificates

#############################################################################

def get_propositions():
    props = []
    props.extend(create_not_need_pay())
    props.extend(create_certificates())
    props.extend(create_not_needs_items())
    props.extend(create_come_back())
    props.extend(create_at())
    props.extend(create_dice())
    props.extend(create_has_money())
    props.extend(create_not_stop())
    return props


def get_actions(player):
    actions = []
    actions.extend(create_move(player))
    actions.extend(create_pay_cell())
    actions.extend(create_jump_to_entrance())
    actions.extend(create_put_comeback())
    actions.extend(create_pay_surprise(player))
    actions.extend(create_pay_150())
    actions.extend(create_show_certificate())
    actions.extend(create_stop_action())
    return actions


def create_domain_file(domain_file_name, player):
    agent = "optimistic"
    if player == MEAN:
        agent = "mean"
    file_name = agent + "_" + domain_file_name
    domain_file = open(file_name, 'w')  # use domain_file.write(str) to write to domain_file

    # write propositions to file
    domain_file.write("Propositions:\n")
    props = get_propositions()
    domain_file.write(" ".join(props))

    # write actions to file
    actions = get_actions(player)
    domain_file.write("Actions:\n")
    domain_file.write("\n".join(actions))
    domain_file.close()




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

    code = int(float(sys.argv[1]))  # agent_Code

    domain_file_name = 'domain.txt'
    problem_file_name = 'problem.txt'

    create_domain_file(domain_file_name, code)
    # create_problem_file(problem_file_name, code)