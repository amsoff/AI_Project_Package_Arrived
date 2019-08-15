from enum import Enum

# File names
DOMAIN_FILE_NAME = 'domain.txt'
PROBLEM_FILE_NAME = '{}_problem.txt'

# Change goal here
GOAL = (11, 9)
START = (1, 0)
DEBUG = True
PLAYER_STARTING_MONEY = 1500
DUMMY_DICE = [1, 2]

# constants from board:
# Lottery prizes
PRIZE_1 = 1000
PRIZE_2 = 1500
PRIZE_3 = 500
# Costs
HAIRCUT_COST = -50
TAX_COST = -50
PACKAGE_COST = -500

# Other constants from domain_create
# Action constants
MAX_STOPS = 4
NUM_OF_50_BILLS = 80
NAME = "Name: "
PRE = "\npre: "
ADD = "\nadd: "
DEL = "\ndelete: "

# Player constants
AVERAGE = "average"
OPTIMISTIC = "optimistic"

# PROPOSITIONS
AT_FORMAT = "At_%s_%s"
DIE_FORMAT = "die_%s"
MONEY_FORMAT = "Money_%s"
CERTIFICATES_FORMAT = "has_%s"
NOT_STOP_FORMAT = "Not_Stop_%s"
NEED_PAY_CELL = "need_pay_%s_%s"
COME_BACK_FORMAT = "Come_back_to_%s_%s"
NOT_NEED_PAY_CELL = "not_need_pay_%s_%s"
NOT_COME_BACK_FORMAT = "Not_Come_back_%s_%s"
NOT_HAS_FORMAT = "not_has_%s"

# CSV HEADERS
TYPE = "Player type"
MONEY = "amount at start"
TURNS = "number of turns"
EXPANDED = "list of expanded per turn"
TIME = "time took to finish"
FILE = "output.csv"
FILE_average_vs_optimi = "output_players_and_optimizations.csv"
FILE_average_vs_optimi_NO_OPT = "optimistic_vs_average_no_optimization.csv"


# ACTIONS:
# STOP:
# Name: stop1 pre: add: not_stop_1 delete:
FIRST_STOP_FORMAT = NAME + "Stop_1_at_%s_%s" + PRE + AT_FORMAT + " " + ADD + NOT_STOP_FORMAT % 1 + DEL
# Name: stop(x) pre:stop(x-1) add: not_stop_x delete:
STOP_FORMAT = NAME + "Stop_%s_at_%s_%s" + PRE + AT_FORMAT + " " + NOT_STOP_FORMAT + ADD + NOT_STOP_FORMAT + DEL

# PAYMENTS:
# pay surprise p1 from m pre need pay p1 at p1 money m add money m-x not need pay p1 del money m
PAY_SURPRISE_FORMAT = NAME + "pay_surprise_%s_%s_from_%s" + PRE + AT_FORMAT + " " + NEED_PAY_CELL + " " + MONEY_FORMAT + ADD + MONEY_FORMAT + " " + NOT_NEED_PAY_CELL + DEL + MONEY_FORMAT + " " + NEED_PAY_CELL
# pay x at p1 from m pre need_pay_p1 at p1 money m add money m-x not need pay p1 del money m need pay p1
PAY_CELL = NAME + "pay_%s_At_%s_%s_from_%s" + PRE + NEED_PAY_CELL + " " + AT_FORMAT + " " + MONEY_FORMAT + ADD + MONEY_FORMAT + " " + NOT_NEED_PAY_CELL + DEL + MONEY_FORMAT + " " + NEED_PAY_CELL

# JUMPS
# goto p2 from p1, pre comeback to p2, at p1, add at p2 not_CB_p2 del comeback p2 At_p1
GOTO_FORMAT = NAME + "Goto_%s_%s_from_%s_%s" + PRE + COME_BACK_FORMAT + " " + AT_FORMAT + ADD + AT_FORMAT + " " + NOT_COME_BACK_FORMAT + DEL + COME_BACK_FORMAT + " " + AT_FORMAT  # FROM_COMEBACK
# jump to a nearby cell to search for certificate/money
JUMP_TO_ENTRANCE = NAME + "jump_to_entrance_%s_%s_from_%s_%s" + PRE + AT_FORMAT + ADD + COME_BACK_FORMAT + " " + AT_FORMAT + DEL + AT_FORMAT + " " + NOT_COME_BACK_FORMAT


class Types(Enum):
    OPTIMISTIC = "optimistic"
    AVERAGE = "average"
