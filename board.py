import numpy as np
from enum import Enum
from Certificates import Certificate

MESSAGE = "message"
JUMP = 'jump'
ENTRANCE = 'entrance'
BALANCE = 'balance'
WAIT = 'wait'
NEED = 'need'
HAS = 'has'
SURPRISE = 'surprise'
PACKAGE = 'package'
ORANGE = 150
ONE = 1
THREE = 3
FIVE = 5

TAX_PAYMENT = -50
PRISE_1 = 1000
PRISE_2 = 1500
PRISE_3 = 500
PACKAGE_COST = -50


class Board:

    def __init__(self, num_players, starting_point=(1, 0)):
        self.board_w = 23
        self.board_h = 31
        self.starting_point = starting_point
        self.num_players = num_players

        self.state = np.full((self.board_h, self.board_w), -1, np.int8)

        self.transition_matrix = np.full((self.board_h, self.board_w), -1, np.int8)

        self.transition_dict = {}
        self.init_dict()

    def get_cell(self, cell):
        return self.transition_dict[cell]

    def init_dict(self):
        self.init_row0()
        self.init_row1()
        self.init_row2()
        self.init_row3()
        self.init_row4()
        self.init_row5()
        self.init_row6()
        self.init_row7()
        self.init_row8()
        self.init_row9()
        self.init_row10()
        self.init_row11()

    def init_row11(self):
        self.transition_dict[(11, 0)] = {1: [(11, 0), (11, 1), (10, 0)],
                                         2: [(11, 0), (11, 2), (9, 0)],
                                         3: [(8, 0), (9, 1), (11, 3)],
                                         ORANGE: [(11, 3)],
                                         MESSAGE: "You entered the Hospital!"}

        self.transition_dict[(11, 1)] = {1: [(11, 1), (11, 2)],
                                         2: [(11, 3)],
                                         3: [(11, 1)],
                                         ORANGE: [(11, 3)],
                                         NEED: [Certificate.GRANDMA],
                                         ENTRANCE: [(11, 5)]}

        self.transition_dict[(11, 2)] = {1: [(11, 3)],
                                         2: [(11, 2)],
                                         3: [(11, 2)],
                                         ORANGE: [(11, 3)],
                                         WAIT: 2}

        self.transition_dict[(11, 3)] = {1: [(11, 4)],
                                         2: [(11, 5)],
                                         3: [(10, 5)],
                                         HAS: Certificate.BIRTH,
                                         JUMP: [(9, 11), (1, 5)]}
        self.transition_dict[(11, 4)] = {1: [(11, 5)],
                                         2: [(10, 5)],
                                         3: [(9, 5)]}

        self.transition_dict[(11, 5)] = {1: [(10, 5)],
                                         2: [(9, 5)],
                                         3: [(9, 6), (8, 5), (9, 4)]}

        self.transition_dict[(11, 8)] = {1: [(10, 8)],
                                         2: [(10, 7), (9, 8)],
                                         3: [(8, 8), (9, 7)]}

        self.transition_dict[(11, 10)] = {1: [(11, 9)],
                                          2: [(11, 10)],
                                          3: [(11, 10)],
                                          ORANGE: [(11, 9)]}

        self.transition_dict[(11, 11)] = {1: [(11, 10)],
                                          2: [(11, 11)],
                                          3: [(11, 11)],
                                          BALANCE: PACKAGE_COST,
                                          ENTRANCE: (11, 8)}

    def init_row10(self):
        self.transition_dict[(10, 0)] = {1: [(9, 0), (11, 0)],
                                         2: [(11, 1), (8, 0), (9, 1)],
                                         3: [(11, 2), (8, 1), (9, 2)]}

        self.transition_dict[(10, 5)] = {1: [(9, 5)],
                                         2: [(9, 6), (8, 5), (9, 4)],
                                         3: [(9, 7), (7, 5), (9, 3)]}

        self.transition_dict[(10, 6)] = {1: [(10, 5)],
                                         2: [(9, 5)],
                                         3: [(9, 6), (8, 5), (9, 4)]}

        self.transition_dict[(10, 7)] = {1: [(10, 6)],
                                         2: [(10, 5)],
                                         3: [(11, 7)],
                                         MESSAGE: "Lottery! you have a chance to earn some money!"}

        self.transition_dict[(11, 7)] = {1: [(10, 6)],
                                         2: [(10, 5)],
                                         3: [(9, 5)],
                                         BALANCE: PRISE_3,  # POSITIVE
                                         JUMP: [(2, 5), (5, 10), (7, 10), (8, 4), (11, 11)]}

        self.transition_dict[(10, 8)] = {1: [(9, 8), (10, 7)],
                                         2: [(9, 7), (8, 8)],
                                         3: [(7, 8), (9, 6)]}

        self.transition_dict[(10, 11)] = {1: [(11, 11)],
                                          2: [(10, 11)],
                                          3: [(10, 11)],
                                          NEED: [Certificate.GRANDMA],
                                          ENTRANCE: (11, 8)}

    def init_row9(self):
        self.transition_dict[(9, 0)] = {1: [(8, 0), (9, 1), (10, 0)],
                                        2: [(8, 1), (9, 2), (11, 0)],
                                        3: [(7, 1), (8, 2), (9, 3), (11, 1)]}

        self.transition_dict[(9, 1)] = {1: [(8, 1), (9, 0), (9, 2)],
                                        2: [(10, 0), (7, 1), (8, 0), (8, 2), (9, 3)],
                                        3: [(11, 0), (6, 1), (8, 3), (9, 4)]}

        self.transition_dict[(9, 2)] = {1: [(8, 2), (9, 1), (9, 3), (9, 2)],
                                        2: [(8, 1), (9, 0), (8, 3), (9, 4), (9, 2)],
                                        3: [(10, 0), (8, 0), (7, 1), (8, 4), (9, 5)],
                                        ORANGE: [(8, 4)]}

        self.transition_dict[(9, 3)] = {1: [(9, 4), (9, 2)],
                                        2: [(9, 1), (8, 2), (9, 5)],
                                        3: [(9, 6), (8, 5), (8, 1), (8, 3), (9, 0)]}

        self.transition_dict[(9, 4)] = {1: [(9, 3), (9, 5)],
                                        2: [(8, 5), (9, 2), (9, 6)],
                                        3: [(7, 5), (9, 1), (8, 2), (9, 7)]}

        self.transition_dict[(9, 5)] = {1: [(9, 4), (8, 5), (9, 6)],
                                        2: [(7, 5), (9, 3), (9, 7)],
                                        3: [(7, 6), (9, 8), (9, 2), (6, 5)],
                                        SURPRISE: True, JUMP: [(2, 5), (5, 10), (7, 10), (8, 4), (11, 11)]}

        self.transition_dict[(9, 6)] = {1: [(9, 7), (9, 5)],
                                        2: [(8, 5), (9, 4), (9, 8)],
                                        3: [(10, 8), (8, 8), (7, 5), (9, 3)]}

        self.transition_dict[(9, 7)] = {1: [(9, 8), (9, 6)],
                                        2: [(8, 8), (9, 5), (10, 8)],
                                        3: [(10, 7), (7, 8), (8, 5), (9, 4)]}

        self.transition_dict[(9, 8)] = {1: [(9, 7), (10, 8), (8, 8)],
                                        2: [(10, 7), (9, 6), (7, 8)],
                                        3: [(6, 8), (9, 5)],
                                        WAIT: 4,
                                        MESSAGE: "That was stupid. You are in Prison"} #Prison

        self.transition_dict[(9, 9)] = {1: [(9, 10)],
                                        2: [(9, 11)],
                                        3: [(10, 11)],
                                        NEED: [Certificate.TAX],
                                        ENTRANCE: (11, 8)}

        self.transition_dict[(9, 10)] = {1: [(9, 10), (9, 11)],
                                         2: [(9, 10), (10, 11)],
                                         3: [(11, 11)], ORANGE: [(11, 11)]}

        self.transition_dict[(9, 11)] = {1: [(10, 11), (9, 11)],
                                         2: [(11, 11)],
                                         3: [(9, 11)],
                                         ORANGE: [(11, 11)],
                                         NEED: [Certificate.BIRTH],
                                         ENTRANCE: (11, 8)}

    def init_row8(self):
        self.transition_dict[(8, 0)] = {1: [(8, 1)],
                                        2: [(9, 1), (7, 1)],
                                        3: [(9, 0), (6, 1), (9, 2)],
                                        HAS: Certificate.GRANDMA,
                                        JUMP: [(11, 1), (10, 11)]}

        self.transition_dict[(8, 1)] = {1: [(9, 1), (7, 1)],
                                        2: [(9, 2), (6, 1)],
                                        3: [(10, 0), (8, 0), (5, 1), (8, 2)]}

        self.transition_dict[(8, 2)] = {1: [(8, 3), (8, 2)],
                                        2: [(8, 4)],
                                        3: [(8, 2)],
                                        ORANGE: [(8, 4)],
                                        MESSAGE: "You entered the Photography studio."}

        self.transition_dict[(8, 3)] = {1: [(8, 4)],
                                        2: [(8, 3)],
                                        3: [(8, 3)],
                                        ORANGE: [(8, 4)]}

        self.transition_dict[(8, 4)] = {1: [(8, 5)],
                                        2: [(9, 5), (7, 5)],
                                        3: [(7, 6), (6, 5), (9, 6), (9, 4)],
                                        BALANCE: PACKAGE_COST,  # negative
                                        JUMP: [(8, 5), (11, 11)],
                                        HAS: Certificate.PASSPORT}

        self.transition_dict[(8, 5)] = {1: [(7, 5), (9, 5), (8, 5)],
                                        2: [(7, 6), (6, 5), (9, 6), (9, 4), (8, 5)],
                                        3: [(6, 6), (6, 4), (9, 7), (9, 3), (5, 5)],
                                        ORANGE: [(6, 4)]}

        self.transition_dict[(8, 8)] = {1: [(9, 8), (7, 8)],
                                        2: [(6, 8), (10, 8), (9, 7)],
                                        3: [(5, 8), (10, 7), (9, 6)]}

        self.transition_dict[(8, 9)] = {1: [(9, 9)],
                                        2: [(9, 10)],
                                        3: [(9, 11)],
                                        NEED: [Certificate.ID],
                                        ENTRANCE: (11, 8)}

    def init_row7(self):
        self.transition_dict[(7, 11)] = {1: [(7, 10)], 2: [(7, 9)], 3: [(8, 9)], WAIT: 2}
        self.transition_dict[(7, 10)] = {1: [(7, 9)], 2: [(8, 9)], 3: [(9, 9)],
                                         BALANCE: -100, ENTRANCE: (11, 8)}
        self.transition_dict[(7, 9)] = {1: [(8, 9)], 2: [(9, 9)], 3: [(9, 10)]}
        self.transition_dict[(7, 8)] = {1: [(7, 8), (8, 8), (6, 8)], 2: [(7, 8), (5, 8), (9, 8)],
                                        3: [(10, 8), (9, 7), (5, 9), (5, 7)],
                                        ORANGE: [(5, 9)]}
        self.transition_dict[(7, 6)] = {1: [(7, 6), (6, 6)], 2: [(6, 7)], 3: [(7, 6)],
                                        ORANGE: [(6, 7)]}
        self.transition_dict[(7, 5)] = {1: [(8, 5), (6, 5), (7, 6)], 2: [(6, 6), (9, 5), (6, 4), (5, 5)],
                                        3: [(10, 5), (9, 6), (9, 4), (5, 6), (6, 7)], ORANGE: [(6, 7), (6, 4)]}
        self.transition_dict[(7, 1)] = {1: [(8, 1), (6, 1)], 2: [(9, 1), (5, 1)],
                                        3: [(9, 2), (9, 0), (4, 1)], SURPRISE: True, JUMP: [(2, 5), (5, 10), (7, 10), (8, 4), (11, 11)]}

    def init_row6(self):
        self.transition_dict[(6, 11)] = {1: [(7, 11)], 2: [(7, 10)], 3: [(7, 9)]}
        self.transition_dict[(6, 8)] = {1: [(5, 8), (7, 8)], 2: [(5, 9), (5, 7), (8, 8)],
                                        3: [(5, 6), (9, 8)], ORANGE: [(5, 9)]}
        self.transition_dict[(6, 7)] = {1: [(6, 7), (5, 7)], 2: [(6, 7), (5, 8), (5, 6)],
                                        3: [(5, 9), (6, 8), (4, 6), (5, 5)],
                                        HAS: Certificate.PORT, JUMP: [(5, 9)], ORANGE: [(5, 9)]}
        self.transition_dict[(6, 6)] = {1: [(6, 7)], 2: [(6, 6)], 3: [(6, 6)], ORANGE: [(6, 7)], WAIT: 1}
        self.transition_dict[(6, 5)] = {1: [(7, 5), (5, 5), (6, 4)], 2: [(6, 5), (8, 5), (7, 6), (5, 6)],
                                        3: [(6, 5), (9, 5), (6, 6), (5, 7), (4, 6)], ORANGE: [(6, 4)]}
        self.transition_dict[(6, 4)] = {1: [(6, 4), (6, 3)], 2: [(6, 4), (6, 2)], 3: [(5, 2)], ORANGE: [(5, 2)]}
        self.transition_dict[(6, 3)] = {1: [(6, 3), (6, 2)], 2: [(5, 2)], 3: [(6, 3)], ORANGE: [(5, 2)]}
        self.transition_dict[(6, 2)] = {1: [(5, 2)], 2: [(6, 2)], 3: [(6, 2)], ORANGE: [(5, 2)], WAIT: 1}
        self.transition_dict[(6, 1)] = {1: [(7, 1), (5, 1)], 2: [(8, 1), (4, 1)], 3: [(9, 1), (4, 2)]}

    def init_row5(self):
        self.transition_dict[(5, 11)] = {1: [(6, 11)], 2: [(7, 11)], 3: [(7, 10)],
                                         NEED: [Certificate.INTEGRITY], ENTRANCE: (11, 8)}
        self.transition_dict[(5, 10)] = {1: [(5, 11)], 2: [(6, 11)], 3: [(7, 11)], BALANCE: -100, ENTRANCE: (11, 8)}
        self.transition_dict[(5, 9)] = {1: [(5, 10)], 2: [(5, 11)], 3: [(6, 11)],
                                        NEED: [Certificate.PORT], ENTRANCE: (11, 8)}
        self.transition_dict[(5, 8)] = {1: [(5, 9)], 2: [(5, 8)], 3: [(5, 8)], ORANGE: [(5, 9)],
                                        SURPRISE: True, ENTRANCE: (11, 8), JUMP: [(2, 5), (5, 10), (7, 10), (8, 4), (11, 11)]}

        self.transition_dict[(5, 7)] = {1: [(5, 7), (5, 8), (5, 6)], 2: [(6, 8), (5, 5), (4, 6), (5, 9)],
                                        3: [(5, 7), (6, 5), (4, 5), (4, 7), (7, 8)], ORANGE: [(5, 9)]}
        self.transition_dict[(5, 6)] = {1: [(5, 6), (5, 7), (5, 5), (4, 6)],
                                        2: [(5, 6), (5, 8), (6, 5), (4, 7), (4, 5), (3, 6)],
                                        3: [(5, 9), (6, 8), (4, 4), (3, 5), (6, 4), (7, 5)],
                                        ORANGE: [(5, 9), (6, 4)]}
        self.transition_dict[(5, 5)] = {1: [(5, 5), (6, 5), (5, 6)], 2: [(6, 4), (5, 7), (4, 6), (7, 5)],
                                        3: [(5, 5), (5, 8), (4, 7), (4, 5), (3, 6), (7, 6), (8, 5)],
                                        ORANGE: [(6, 4)]}
        self.transition_dict[(5, 2)] = {1: [(4, 2)], 2: [(3, 2), (4, 1)], 3: [(5, 1), (2, 2), (3, 3)],
                                        HAS: Certificate.INTEGRITY, JUMP: [(5, 11)]}
        self.transition_dict[(5, 1)] = {1: [(6, 1), (4, 1)], 2: [(7, 1), (4, 2)], 3: [(8, 1), (3, 2)]}

    def init_row4(self):
        self.transition_dict[(4, 7)] = {1: [(3, 7)], 2: [(4, 7), (5, 8), (5, 6), (3, 6), (4, 5)],
                                        3: [(6, 8), (5, 5), (4, 6), (4, 4), (5, 9)],
                                        ORANGE: [(5, 9)]}
        self.transition_dict[(3, 7)] = {1: [(5, 7)], 2: [(5, 8), (5, 6), (3, 6), (4, 5)],
                                        3: [(6, 8), (5, 5), (4, 6), (4, 4), (5, 9)], BALANCE: PRISE_1,
                                        JUMP: [(2, 5), (5, 10), (7, 10), (8, 4), (11, 11)]}
        self.transition_dict[(4, 6)] = {1: [(4, 6), (4, 7), (3, 6), (5, 6), (4, 5)],
                                        2: [(4, 6), (5, 7), (5, 5), (4, 4), (3, 5)],
                                        3: [(5, 8), (5, 5), (4, 3), (3, 4)], ORANGE: [(4, 3)]}
        self.transition_dict[(4, 5)] = {1: [(4, 5), (4, 4)], 2: [(4, 3)], 3: [(4, 5)], ORANGE: [(4, 3)]}
        self.transition_dict[(4, 4)] = {1: [(4, 3)], 2: [(4, 4)], 3: [(4, 4)], ORANGE: [(4, 3)]}
        self.transition_dict[(4, 3)] = {1: [(4, 2)], 2: [(3, 2), (4, 1)], 3: [(5, 1), (2, 2), (3, 3)],
                                        HAS: Certificate.HAIRCUT, JUMP: [(8, 3)]}
        self.transition_dict[(4, 2)] = {1: [(3, 2), (4, 1)], 2: [(2, 2), (3, 3), (5, 1)],
                                        3: [(6, 1), (1, 2), (3, 4), (2, 3)]}
        self.transition_dict[(4, 1)] = {1: [(4, 2), (5, 1)], 2: [(6, 1), (3, 2)], 3: [(7, 1), (3, 3), (2, 2)]}

    def init_row3(self):
        self.transition_dict[(3, 6)] = {1: [(4, 6), (3, 5)], 2: [(4, 7), (5, 6), (4, 5), (3, 4)],
                                        3: [(5, 7), (5, 5), (4, 4)]}
        self.transition_dict[(3, 5)] = {1: [(3, 6), (3, 4)], 2: [(4, 6), (3, 3)],
                                        3: [(4, 7), (4, 5), (3, 2), (2, 3)]}
        self.transition_dict[(3, 4)] = {1: [(3, 5), (3, 3)], 2: [(3, 6), (3, 2), (2, 3)],
                                        3: [(4, 6), (4, 2), (2, 4), (2, 1)]}
        self.transition_dict[(3, 3)] = {1: [(3, 4), (3, 2), (2, 3)], 2: [(3, 5), (4, 2), (2, 2), (2, 4)],
                                        3: [(3, 6), (4, 1), (1, 2), (2, 5)]}
        self.transition_dict[(3, 2)] = {1: [(4, 2), (2, 2), (3, 3)], 2: [(4, 1), (3, 4), (2, 3), (1, 2)],
                                        3: [(5, 1), (3, 5), (2, 4), (1, 1)],
                                        SURPRISE: True, ENTRANCE: (3, 3), JUMP: [(2, 5), (5, 10), (7, 10), (8, 4), (11, 11)]}

    def init_row2(self):
        self.transition_dict[(2, 5)] = {1: [(2, 5), (1, 6)], 2: [(2, 5), (1, 5)], 3: [(1, 4)], ORANGE: [(1, 4)],
                                        BALANCE: -50, ENTRANCE: (1, 2)}
        self.transition_dict[(2, 4)] = {1: [(2, 5)], 2: [(1, 6)], 3: [(1, 5)]}
        self.transition_dict[(2, 3)] = {1: [(2, 4), (3, 3), (2, 2)], 2: [(2, 5), (1, 2), (3, 4), (3, 2)],
                                        3: [(1, 6), (3, 5), (1, 1), (4, 2)]}
        self.transition_dict[(2, 2)] = {1: [(2, 3), (3, 2), (1, 2)], 2: [(1, 1), (4, 2), (2, 4), (3, 3)],
                                        3: [(2, 5), (4, 1), (3, 4), (2, 1), (1, 0)]}
        self.transition_dict[(2, 1)] = {1: [(2, 2)], 2: [(3, 1)], 3: [(2, 4), (3, 3), (4, 2), (1, 1)]}
        self.transition_dict[(3, 1)] = {1: [(2, 2)], 2: [(2, 3), (3, 2)], 3: [(2, 4), (3, 3), (4, 2), (1, 1)],
                                        BALANCE: PRISE_2, JUMP: [(2, 5), (5, 10), (7, 10), (8, 4), (11, 11)]}

    def init_row1(self):
        self.transition_dict[(1, 6)] = {1: [(1, 6), (1, 5)], 2: [(1, 4)], 3: [(1, 6)], ORANGE: [(1, 4)],
                                        NEED: [Certificate.PASSPORT], ENTRANCE: (1, 2)}
        self.transition_dict[(1, 5)] = {1: [(1, 4)], 2: [(1, 5)], 3: [(1, 5)], ORANGE: [(1, 4)],
                                        NEED: [Certificate.BIRTH], ENTRANCE: (1, 2)}
        self.transition_dict[(1, 4)] = {1: [(1, 3)], 2: [(1, 2)], 3: [(1, 1), (2, 2)],
                                        HAS: Certificate.ID, JUMP: [(8, 9)]}
        self.transition_dict[(1, 3)] = {1: [(1, 2)], 2: [(1, 1), (2, 2)], 3: [(2, 1), (1, 0), (3, 2)]}
        self.transition_dict[(1, 2)] = {1: [(2, 2), (1, 1)], 2: [(1, 0), (2, 1), (3, 2), (2, 3)],
                                        3: [(4, 2), (2, 4), (3, 3), (0, 0)]}
        self.transition_dict[(1, 1)] = {1: [(1, 1), (1, 0), (1, 2), (2, 1)], 2: [(1, 1), (0, 0), (2, 2)],
                                        3: [(0, 1), (3, 2), (2, 3)], ORANGE: [(0, 1)]}
        self.transition_dict[(1, 0)] = {1: [(1, 0), (0, 0), (1, 1)], 2: [(0, 1), (1, 2), (2, 1)],
                                        3: [(1, 0), (2, 2)],
                                        ORANGE: [(0, 1)]}

    def init_row0(self):
        self.transition_dict[(0, 2)] = {1: [(1, 2)], 2: [(1, 1), (2, 2)], 3: [(1, 0), (2, 1), (2, 3)]}
        self.transition_dict[(0, 1)] = {1: [(0, 2)], 2: [(1, 2)], 3: [(2, 2), (1, 1)], HAS: Certificate.TAX,
                                        JUMP: [(9, 9)]}
        self.transition_dict[(0, 0)] = {1: [(0, 1)], 2: [(0, 0)], 3: [(0, 0)], ORANGE: [(0, 1)],
                                        NEED: [Certificate.INTEGRITY], ENTRANCE: (1, 0)}