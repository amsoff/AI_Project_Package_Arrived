from enum import Enum

# File names
DOMAIN_FILE_NAME = 'domain.txt'
PROBLEM_FILE_NAME = '{}_problem.txt'

# Change goal here
GOAL = (11,9)
START = (1,0)
DEBUG = True
PLAYER_STARTING_MONEY = 1500
DUMMY_DICE = [1,2]

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
DICE_FORMAT = "dice_%s"
MONEY_FORMAT = "Money_%s"
CERTIFICATES_FORMAT = "has_%s"
NOT_STOP_FORMAT = "Not_Stop_%s"
NEED_PAY_CELL = "need_pay_%s_%s"
COME_BACK_FORMAT = "Come_back_to_%s_%s"
NOT_NEED_PAY_CELL = "not_need_pay_%s_%s"
NOT_COME_BACK_FORMAT = "Not_Come_back_%s_%s"

# ACTIONS:
# STOP:
FIRST_STOP_FORMAT = NAME + "Stop_1_at_%s_%s" + PRE + AT_FORMAT + " " + ADD + NOT_STOP_FORMAT % 1 + DEL
# Name: stop1 pre: add: not_stop_1 delete:
STOP_FORMAT = NAME + "Stop_%s_at_%s_%s" + PRE + AT_FORMAT + " " + NOT_STOP_FORMAT + ADD + NOT_STOP_FORMAT + DEL
# Name: stop(x) pre:stop(x-1) add: not_stop_x delete:

# PAYMENTS:
PAY_SURPRISE_FORMAT = NAME + "pay_surprise_%s_%s_from_%s" + PRE + AT_FORMAT + " " + NEED_PAY_CELL + " " + MONEY_FORMAT + ADD + MONEY_FORMAT + " " + NOT_NEED_PAY_CELL + DEL + MONEY_FORMAT + " " + NEED_PAY_CELL
# pay surprise p1 from m pre need pay p1 at p1 money m add money m-x not need pay p1 del money m
# PAY_FIRST_SURPRISE = NAME + "pay_%s_surprise_%s_%s_from_%s" +PRE + AT_FORMAT + " " + MONEY_FORMAT + " " + OWE + ADD + MONEY_FORMAT + " " + NOT_NEED_PAY_CELL + " " + NOT_OWE  + DEL + MONEY_FORMAT
# pay x surprise of p1 from m pre at p1 money m add money m-x not need pay p1 not owe x del money m

PAY_CELL = NAME + "pay_%s_At_%s_%s_from_%s" + PRE + NEED_PAY_CELL + " " + AT_FORMAT + " " + MONEY_FORMAT + ADD + MONEY_FORMAT + " " + NOT_NEED_PAY_CELL + DEL + MONEY_FORMAT + " " + NEED_PAY_CELL
# pay x at p1 from m pre need_pay_p1 at p1 money m add money m-x not need pay p1 del money m need pay p1

# jump to come back cell
GOTO_FORMAT = NAME + "Goto_%s_%s_from_%s_%s" + PRE + COME_BACK_FORMAT + " " + AT_FORMAT + ADD + AT_FORMAT + " " + NOT_COME_BACK_FORMAT + DEL + COME_BACK_FORMAT + " " + AT_FORMAT  # FROM_COMEBACK
# goto p2 from p1, pre comeback to p2, at p1, add at p2 not_CB_p2 del comeback p2 At_p1

GOTO_MONEY_FORMAT = NAME + "Goto_%s_%s_from_%s_%s" + PRE + NOT_NEED_PAY_CELL + " " + COME_BACK_FORMAT + " " + AT_FORMAT + ADD + AT_FORMAT + " " + NOT_COME_BACK_FORMAT + DEL + COME_BACK_FORMAT + " " + AT_FORMAT # FROM_COMEBACK
# goto p2 from p1, pre comeback to p2, at p1, add at p2 not_CB_p2 del comeback p2 At_p1

# JUMP_TO_ENTRANCE = NAME + "jump_to_%s_%s_from_%s_%s" + PRE + COME_BACK_FORMAT + " " + AT_FORMAT + ADD + AT_FORMAT + DEL + AT_FORMAT
# jump to p2 from p1 pre comeback to p1 at p1 add at p2 del at p1

# jump to a nearby cell to search for certificate/money
JUMP_TO_ENTRANCE = NAME + "jump_to_entrance_%s_%s_from_%s_%s" + PRE + AT_FORMAT + ADD + COME_BACK_FORMAT + " " + AT_FORMAT + DEL + AT_FORMAT + " " + NOT_COME_BACK_FORMAT


# jump to p2 from p1 pre at p1 add cb_to_p1 at p2 del at p1

# # no need for take certificate?
# TAKE_CERTIFICATE = "Name: Take_%s\npre: At_%s_%s\nadd: has_%s\ndelete:"
# # take id pre at p1 add has id
# SHOW_CERTIFICATE = "Name: Show_%s\npre: has_%s\nadd: not_needs_%s\ndelete:"
# show id pre has id add not needs id

class Types(Enum):
    OPTIMISTIC = "optimistic"
    AVERAGE = "average"
