import sys


NAME = 0
PRE = 1
ADD = 2
DEL = 3
PROP_FORMAT = "d%s_p%s" # disk x on peg y
ACTION_FORMAT = "Md%s_Fp%s_Tp%s" # move disk x from peg y to peg z
NOT_OWE_FORMAT = "Not_Owe_%s"



MONEY_FORMAT = "Money_%s"
AT_FORMAT = "At_%s_%s"
CERTIFICATES_FORMAT = "has_%s"
DICE_FORMAT = "dice_%s"
PAY_FORMAT = "Name: pay_%s_from_%s\nPre: Money_%s\nadd: Not_Owe_%s\n Money_%s\n del: Money_%s" # pay x money from the y money you have

def create_not_owe():
    no = []
    for x in range(101):
        no.append(NOT_OWE_FORMAT.format(str(50*x)))
    return no


def create_pay():
    pay = []
    for x in range(101):
        for y in range(201):
            pay.append(PAY_FORMAT.format(str(x), str(y), str(y),str(y-x), str(x)))




def create_has_money(amount):
    has = []
    for x in range(201):
        has.append(MONEY_FORMAT.format(str(50*x)))


def create_has_money_problem(amount):
    has = []
    if amount >= 10:
        has.append(MONEY_FORMAT.format(str(10)))
    if amount >= 35:
        has.append(MONEY_FORMAT.format(str(35)))
    if amount >= 50:
        has.append(MONEY_FORMAT.format(str(50)))
    if amount >= 95:
        has.append(MONEY_FORMAT.format(str(95)))
    if amount >= 120:
        has.append(MONEY_FORMAT.format(str(120)))
    if amount >= 250:
        has.append(MONEY_FORMAT.format(str(250)))
    if amount >= 330:
        has.append(MONEY_FORMAT.format(str(330)))
    if amount >= 540:
        has.append(MONEY_FORMAT.format(str(540)))
    if amount >= 750:
        has.append(MONEY_FORMAT.format(str(750)))
    if amount >= 850:
        has.append(MONEY_FORMAT.format(str(850)))
    if amount >= 1320:
        has.append(MONEY_FORMAT.format(str(1320)))
    if amount >= 2150:
        has.append(MONEY_FORMAT.format(str(2150)))
    if amount >= 3680:
        has.append(MONEY_FORMAT.format(str(3680)))

def create_dice():
    dice = []
    for d in [1,3,5]:
        dice.append(DICE_FORMAT.format(str(d)))
    return dice


def create_at():
    at = []
    for x in range(23):
        for y in range(31):
            at.append(AT_FORMAT.format(str(x),str(y)))
    return at


def create_certificates():
    certificates = []
    certificates.append(CERTIFICATES_FORMAT.format("grandmas_marriage_certificate"))
    certificates.append(CERTIFICATES_FORMAT.format("integrity_certificate"))
    certificates.append(CERTIFICATES_FORMAT.format("birth_certificate"))
    certificates.append(CERTIFICATES_FORMAT.format("id"))
    certificates.append(CERTIFICATES_FORMAT.format("rabies_certificate"))
    certificates.append(CERTIFICATES_FORMAT.format("passport_photo"))
    certificates.append(CERTIFICATES_FORMAT.format("military_pad"))
    certificates.append(CERTIFICATES_FORMAT.format("tax_payment_authorization"))
    certificates.append(CERTIFICATES_FORMAT.format("entrance_to_port"))
    certificates.append(CERTIFICATES_FORMAT.format("glasses"))
    certificates.append(CERTIFICATES_FORMAT.format("hat"))
    certificates.append(CERTIFICATES_FORMAT.format("package"))
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
