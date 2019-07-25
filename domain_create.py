import sys
from Certificates import Certificate


NAME = 0
PRE = 1
ADD = 2
DEL = 3
PROP_FORMAT = "d%s_p%s" # disk x on peg y
ACTION_FORMAT = "Md%s_Fp%s_Tp%s" # move disk x from peg y to peg z

MAXIMUM_PAY = 101
MAXIMUM_POCKET = 201
BOARD_WIDTH = 23
BOARD_HEIGHT = 31


# NOT_OWE_FORMAT = "Not_Owe_%s"
MONEY_FORMAT = "Money_%s"
AT_FORMAT = "At_%s_%s"
CERTIFICATES_FORMAT = "has_%s"
NOT_NEEDS_FORMAT = "not_needs_%s"
DICE_FORMAT = "dice_%s"
COME_BACK_FORMAT = "Come_back_to_%s_%s"
NOT_STOP_FORMAT = "Not_Stop_%s"

erez_dic = dict()


FIRST_STOP_FORMAT = "Name: Stop_1\nPre: \nadd: Not_Stop_1\n del:"
STOP_FORMAT = "Name: Stop_%s\nPre: Not_Stop_%s\nadd: Not_Stop_%s\n del:"
PAY_SURPRISE_FORMAT = "Name: pay_%s_from_%s\nPre: Money_%s\nadd: Not_Owe_%s Money_%s\n del: Money_%s" # pay x money from the y money you have
PAY_150_FORMAT = "Name: Pay_150_from_%s_%s_to_%s_%s_with_%s\n Pre: at_%s_%s Money_%s\n add: at_%s_%s Money_%s\n del: at_%s_%s Money_%s"
# pay 150 to jump from p1 to p2 with x money, pre at p1, money x, add at p2, money x-150, del at p1 money x.
GOTO_FORMAT = "Name: Goto_%s_%s\n Pre: Come_back_to_%s_%s at_%s_%s\n add: at_%s_%s has_%s\n del: at_%s_%s Come_back_to_%s_%s needs_%s"
GOTO_MONEY_FORMAT = "Name: Goto_%s_%s\n Pre: Come_back_to_%s_%s at_%s_%s\n add: at_%s_%s has_%s\n del: at_%s_%s Come_back_to_%s_%s needs_%s"
# goto p2, pre comeback to p2, at specific p1, add at p2 has X (id) del at_p1 comeback p2, needs x

def create_pay_150():
    pass


#def create_not_owe():
#    no = []
#    for x in range(101):
#        no.append(NOT_OWE_FORMAT.format(str(50*x)))
#    return no


def create_pay_surprise():
    pay = []
    for x in range(MAXIMUM_PAY):
        for y in range(MAXIMUM_POCKET):
                                             #pay x from y pre money y add notoweX money(y-(x or y)) del money y
            pay.append(PAY_SURPRISE_FORMAT.format(str(x), str(y), str(y), str(x), str(y - min(y, x)), str(y)))


def create_not_stop():
    not_stop = []
    for x in range(1, 5):
        not_stop.append(NOT_STOP_FORMAT.format(str(x)))
    return not_stop


def create_stop_action():
    stop = [FIRST_STOP_FORMAT]
    for x in range(2, 5):
        stop.append(STOP_FORMAT.format(str(x), str(x-1), str(x)))
    return stop


def create_has_money():
    has = []
    for x in range(MAXIMUM_POCKET):
        has.append(MONEY_FORMAT.format(str(50*x)))


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


def create_not_needs_certificates():
    certificates = [NOT_NEEDS_FORMAT.format(Certificate.GRANDMA),
                    NOT_NEEDS_FORMAT.format(Certificate.INTEGRITY),
                    NOT_NEEDS_FORMAT.format(Certificate.BIRTH),
                    NOT_NEEDS_FORMAT.format(Certificate.ID),
                    NOT_NEEDS_FORMAT.format(Certificate.RABIES),
                    NOT_NEEDS_FORMAT.format(Certificate.PASSPORT),
                    NOT_NEEDS_FORMAT.format(Certificate.MILITARY),
                    NOT_NEEDS_FORMAT.format(Certificate.TAX),
                    NOT_NEEDS_FORMAT.format(Certificate.PORT),
                    NOT_NEEDS_FORMAT.format(Certificate.GLASSES),
                    NOT_NEEDS_FORMAT.format(Certificate.HAT),
                    NOT_NEEDS_FORMAT.format(Certificate.PACKAGE),
                    NOT_NEEDS_FORMAT.format("money")]
    return certificates


def create_certificates():
    certificates = [NOT_NEEDS_FORMAT.format(Certificate.GRANDMA),
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
                    CERTIFICATES_FORMAT.format(Certificate.PACKAGE)]
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
