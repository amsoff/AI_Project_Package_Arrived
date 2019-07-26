import sys
from Certificates import Certificate


NAME = 0
PRE = 1
ADD = 2
DEL = 3
PROP_FORMAT = "d%s_p%s" # disk x on peg y
ACTION_FORMAT = "Md%s_Fp%s_Tp%s" # move disk x from peg y to peg z

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

# NOT_OWE_FORMAT = "Not_Owe_%s"
MONEY_FORMAT = "Money_%s"
AT_FORMAT = "At_%s_%s"
CERTIFICATES_FORMAT = "has_%s"
NOT_NEEDS_FORMAT = "not_needs_%s"
DICE_FORMAT = "dice_%s"
COME_BACK_FORMAT = "Come_back_to_%s_%s"
NOT_STOP_FORMAT = "Not_Stop_%s"
NOT_NEED_PAY_SURPRISE = "not_need_pay_surprise"

NOT_COME_BACK_FORMAT = "Not_Come_back_%s_%s"

# check option to add X not_comebacks and make goal be all not_comebacks and  not need glasses and hat and at END

erez_dic = dict()

# ACTIONS:

# STOP:
FIRST_STOP_FORMAT = "Name: Stop_1\nPre: \nadd: Not_Stop_1\n del:"
STOP_FORMAT = "Name: Stop_%s\nPre: Not_Stop_%s\nadd: Not_Stop_%s\n del:"

# PAYMENTS:

#in surprise you pay the maximum between what you have and the surprise.
PAY_SURPRISE_FORMAT = "Name: pay_surprise_from_%s\nPre: Money_%s\nadd: Money_%s not_need_pay_surprise\n del: Money_%s" # pay x money from the y money you have

# from certain locations in the map you can pay 150 shekels to get where you need.
PAY_150_FORMAT = "Name: Pay_150_from_%s_%s_to_%s_%s_with_%s\n Pre: at_%s_%s Money_%s\n add: at_%s_%s Money_%s\n del: at_%s_%s Money_%s"
# pay 150 to jump from p1 to p2 with x money, pre at p1, money x, add at p2, money x-150, del at p1 money x.

# jump to techef ashuv block
GOTO_FORMAT = "Name: Goto_%s_%s_from_%s_%s\n Pre: Come_back_to_%s_%s at_%s_%s\n add: at_%s_%s Not_Come_back_%s_%s\n del: Come_back_to_%s_%s at_%s_%s " # FROM_COMEBACK
# goto p2 from p1, pre comeback to p2, at specific p1, add at p2 not_CB_p2 del at_p1 comeback p2, needs x


# # no need for take certificate?
# TAKE_CERTIFICATE = "Name: Take_%s\n Pre: at_%s_%s\n add: has_%s\n del:"
# # take id pre at p1 add has id
# SHOW_CERTIFICATE = "Name: Show_%s\n Pre: has_%s\n add: not_needs_%s\n del:"
# # show id pre has id add not needs id

# put comeback:

PUT_COMEBACK = "Name: place_comeback_%s_%s\n Pre: at_%s_%s \n add: Come_back_to_%s_%s\n del: Not_Come_back_%s_%s"
# place comeback at p1 pre: at p1 add: comeback p1 del: not_CB_p1

JUMP_TO_ENTRANCE = "Name: jump_to_%s_%s_from_%s_%s\n Pre: Come_back_to_%s_%s at_%s_%s\n add: at_%s_%s \n del: at_%s_%s"
# jump to p2 from p1 pre comeback to p1 at p1 add at p2 del at p1


def create_move():
    moves = dict()
    for tile1 in erez_dic:  # lekol mishbetzet
        for d in [1,3,5]:  # lekol gilgul_kubia
            for tile2 in tile1[d]: # lekol mishbetzet she'efshar lehagia elia
                action = dict()

                action["Name: "] = "Move_from_%s_%s_to_%s_%s".format(tile1[0], tile1[1], tile2[0], tile2[1])

                action["Pre: "] = DICE_FORMAT.format(d) + " " + AT_FORMAT.format(tile1[0], tile1[1]) + " " + NOT_NEED_PAY_SURPRISE
                for s in range(1, MAX_STOPS):
                    move["Pre: "] += " " + NOT_STOP_FORMAT.format(s)

                action["Add: "] = AT_FORMAT.format(tile2[0], tile2[1])
                if player == MEAN:
                    action["Add: "] += " " + DICE_FORMAT.format(3)
                elif player == OPTIMI:
                    for d1 in [1,3,5]:
                        action["Add: "] += " " + DICE_FORMAT.format(d1)

                action["del: "] = AT_FORMAT.format(tile1[0], tile1[1]) + DICE_FORMAT.format(d)

                # surprise
                if tile2[board.SURPRISE] is not None: # heganu lehaftaa
                    action["del: "] += " " + NOT_NEED_PAY_SURPRISE

                # take certificate:
                if tile2[board.HAS] is not None:
                    action["Add: "] += " " + CERTIFICATES_FORMAT.format(tile2[board.HAS])

                # show certificate:
                if tile1[board.NEED] is not None:  # eem zu mishbetzet shezarich lehazig teuda, zarich sheihihe teuda
                    action["Pre: "] += " " + CERTIFICATES_FORMAT.format(tile1[board.NEED])


                if tile2[board.WAIT] is not None:
                    for i in range(1, tile2[board.WAIT]+1):
                        action["del: "] += " " + NOT_STOP_FORMAT(i)




                # pay - tomorrow
                # orange?




def create_jump_to_entrance():
    jumps = []
    for tile in erez_dic:
        if (tile[board.NEEDS] is not None or tile[board.PAY] is not None) and tile[board.JUMP] is not None:
            for tile2 in tile[board.JUMP]:
                jumps.append(JUMP_TO_ENTRANCE.format(tile2[0], tile2[1], tile[0], tile[1], tile[0], tile[1], tile[0], tile[1],tile2[0], tile2[1] ,  tile[0], tile[1]))
    return jumps


def create_put_comeback():
    comeback = []
    for tile in erez_dic:
        if tile[board.NEED] is not None or tile[board.PAY] is not None: # then there can be techef ashuv
                            # place comeback at p1,           pre: at p1,        add: comeback p1 del not CB p1
            comeback.append(PUT_COMEBACK.format(tile[0], tile[1], tile[0], tile[1], tile[0], tile[1], tile[0], tile[1]))
    return comeback


def create_pay_surprise():
        pays = []
        for tile in erez_dic:
            if tile[board.SURPRISE] is not None:  # check if not bug -> meaning of if: if there is a key surprise
                surprise = -1
                if player == OPTIMI:
                    surprise = OPTIMI_SURPRISE
                elif player == MEAN:
                    surprise = MEAN_SURPRISE
                for m in range(0, 50 * MAXIMUM_POCKET+1, 50):
                    pays.append(PAY_SURPRISE_FORMAT.format(m, m, m-min(m, surprise), m))

        return pays


def create_pay_150():
    pays = []
    for tile in erez_dic:
        if tile[board.ORANGE] is not None: # check if not bug -> if there is a key orange
            for value in tile[board.ORANGE]:
                for m in range(150,50*MAXIMUM_POCKET):  # can only pay 150 if you have at least 150
                                                        # from p1              to p2    with m money  pre at p1 m money add at p2 money m-150 del at p1 money m
                    pays.append(PAY_150_FORMAT.format(tile[0], tile[1], value[0], value[1], m,  tile[0], tile[1], m, value[0], value[1], m-150, tile[0], tile[1], m))
    return pays


def create_goto_from_comeback():
    goto = []
    for tile in erez_dic:
        if tile[board.JUMP] is not None:  # check if not bug -> if there is a key jump
            for value in tile[board.JUMP]:
                                            # goto      p2      from      p1  pre comeback to p2              at p1   add        at p2                not CB p2     del: pre
                goto.append(GOTO_FORMAT.format(value[0], value[1], tile[0], tile[1], value[0], value[1], tile[0], tile[1], value[0], value[1], value[0], value[1], value[0], value[1], tile[0], tile[1]))
    return goto


def create_take_certificate():
    takes = []
    for tile in erez_dic:
        if tile[board.HAS] is not None:
            takes.append(TAKE_CERTIFICATE.format(tile[board.HAS], tile[0], tile[1], tile[board.HAS]))
    return takes


def create_show_certificate():
    show = []
    for tile in erez_dic:
        if tile[board.NEED] is not None:
            takes.append(SHOW_CERTIFICATE.format(tile[board.NEED], tile[board.NEED], tile[board.NEED]))
    return show


def create_not_stop():
    not_stop = []
    for x in range(1, MAX_STOPS+1):
        not_stop.append(NOT_STOP_FORMAT.format(str(x)))
    return not_stop


def create_stop_action():
    stop = [FIRST_STOP_FORMAT]
    for x in range(2, MAX_STOPS+1):
        stop.append(STOP_FORMAT.format(str(x), str(x-1), str(x)))
    return stop


def create_has_money():
    has = []
    for x in range(MAXIMUM_POCKET):
        has.append(MONEY_FORMAT.format(str(50*x)))
    return has


def create_dice():
    dice = []
    for d in [1,3,5]:
        dice.append(DICE_FORMAT.format(str(d)))
    return dice


def create_at():
    at = []
    for x, y in erez_dic.keys():
        at.append(AT_FORMAT.format(str(x),str(y)))
    return at


def create_come_back():
    cbs = []
    for tile in erez_dic:
        if tile[board.NEED] is not None or tile[board.PAY] is not None:
            cbs.append(COME_BACK_FORMAT.format(tile[0, tile[1]]))
            cbs.append(NOT_COME_BACK_FORMAT.format(tile[0], tile[1]))
    return cbs


def create_not_needs_items():
    certificates = [NOT_NEEDS_FORMAT.format(Certificate.GLASSES),
                    NOT_NEEDS_FORMAT.format(Certificate.HAT)]
    return certificates


def create_certificates():
    certificates = [CERTIFICATES_FORMAT.format(Certificate.GRANDMA),
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
                    CERTIFICATES_FORMAT.format(Certificate.HAIRCUT)]
    return certificates


def get_actions(disks, pegs):
    """
    :param disks:
    :param pegs:
    :return:
    """
    actions = []
    for n in range(disks):
        for m in range(pegs):
            for k in range(pegs):
                if m != k:
                    name = ACTION_FORMAT % (n, m, k)  # Move disk n from peg m to peg k
                    pre = PROP_FORMAT % (n, m)
                    add = PROP_FORMAT % (n, k)
                    delete = ""
                    for i in range(n):
                        delete += PROP_FORMAT % (i, k)  # make sure no smaller disks than me on peg k
                        delete += " "
                    for j in range(n):
                        delete += PROP_FORMAT % (j, m)  # make sure no disk is above me when moving
                        delete += " "

                    delete += PROP_FORMAT % (n, m)  # remove moved disk from peg

                    actions.append((name, pre, add, delete))
    return actions


def create_domain_file(domain_file_name, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    domain_file = open(domain_file_name, 'w')  # use domain_file.write(str) to write to domain_file

    # write propositions to file
    domain_file.write("Propositions:\n")
    props = ""
    for d in range(n_):
        for p in range(m_):
            props += PROP_FORMAT % (d, p) + " "
    props = props[:-1]  # delete last space
    domain_file.write(props + '\n')

    # write actions to file
    actions = get_actions(n, m)
    domain_file.write("Actions:\n")
    for action in actions:
        domain_file.write("Name: " + action[NAME] + '\n')
        domain_file.write("pre: " + action[PRE] + '\n')
        domain_file.write("add: " + action[ADD] + '\n')
        domain_file.write("delete: " + action[DEL] + '\n')
    domain_file.close()


def create_problem_file(problem_file_name_, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    problem_file = open(problem_file_name_, 'w')  # use problem_file.write(str) to write to problem_file
    initial = "Initial state: "
    goal = "Goal state: "
    for d in range(n_):
        initial += PROP_FORMAT % (d, 0)  # all disks start on peg 0
        initial += " "
        goal += PROP_FORMAT % (d, m-1) + ' ' # all disks go to last peg

    problem_file.write(initial + '\n')
    problem_file.write(goal)
    problem_file.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: hanoi.py n m')
        sys.exit(2)

    n = int(float(sys.argv[1]))  # number of disks
    m = int(float(sys.argv[2]))  # number of pegs

    domain_file_name = 'hanoi_%s_%s_domain.txt' % (n, m)
    problem_file_name = 'hanoi_%s_%s_problem.txt' % (n, m)

    create_domain_file(domain_file_name, n, m)
    create_problem_file(problem_file_name, n, m)