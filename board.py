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
PAIS = 1000
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
        self.transition_dict[(11,0)] = {1: [(11,0), (11,1),(10,0)],
                                        2: [(11,0), (11,2), (9,0)],
                                        3:[(8,0),(9,1),(11,3)],
                                        ORANGE:[(11,3)],
                                        MESSAGE: "You entered the Hospital!"}

        self.transition_dict[(11,1)] = {1: [(11,1), (11,2)],
                                        2: [(11,3)],
                                        3:[(11,1),(11,4)],
                                        ORANGE: [(11,3)],
                                        NEED: Certificate.GRANDMA,
                                        JUMP: [(11,5)]}

        self.transition_dict[(11,2)] = {1: [(11,3)],
                                        2:[(11,2)],
                                        3:[(11,2)],
                                        ORANGE:[(11,3)],
                                        WAIT: 2}

        self.transition_dict[(11,3)] = {1: [(11,4)],
                                        2: [(11,5)],
                                        3:[(10,5)],
                                        HAS: Certificate.BIRTH,
                                        JUMP: [(9,11), (1,5)]}
        self.transition_dict[(11,4)] = {1: [(11,5)],
                                        2:[(10,5)],
                                        3:[(9,5)],}

        self.transition_dict[(11,5)] = {1: [(10,5)],
                                        2:[(9,5)],
                                        3:[(9,6),(8,5), (9,4)]}

        self.transition_dict[(11,8)] = {1: [(10,8)],
                                        2: [(10,7), (9,8)],
                                        3:[(8,8),(10,6),(9,7)]}

        self.transition_dict[(11,10)] = {1: [(11,9)],
                                         2: [(11,10)],
                                         3:[(11,10)],
                                         ORANGE:[(11,9)]}

        self.transition_dict[(11,11)] = {1: [(11,10)],
                                         2:[(11,11)],
                                         3:[(11,11)],
                                         BALANCE: PACKAGE_COST,
                                         JUMP: [(11,8)]}

    def init_row10(self):
        self.transition_dict[(10, 0)] = {1: [(9, 0)],
                                         2: [(11, 1), (8, 0), (9, 1)],
                                         3: [(10, 2), (8, 1), (9, 2)]}

        self.transition_dict[(10, 5)] = {1: [(11, 5), (9, 5)],
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
                                         BALANCE: PAIS,  # POSITIVE
                                         JUMP: []}  # TODO BIG JUMP

        self.transition_dict[(10, 8)] = {1: [(9, 8)],
                                         2: [(9, 7), (8, 8)],
                                         3: [(7, 8), (9, 6)]}

        self.transition_dict[(10, 11)] = {1: [(11, 11)],
                                          2: [(10, 11)],
                                          3: [(10, 11)],
                                          NEED: Certificate.GRANDMA,
                                          JUMP: (11, 8)}

    def init_row9(self):
        self.transition_dict[(9, 0)] = {1: [(8, 0), (9,1)],
                                        2: [(8, 1), (9, 2)],
                                        3: [(7,1), (8, 2), (9, 3)]}

        self.transition_dict[(9,1)] = {1: [(8,1), (9, 0), (9,2)],
                                       2: [(10,0), (8,0), (8,2), (9,3)],
                                       3: [(11,0), (6,1), (8,3), (9,4)]}

        self.transition_dict[(9,2)] = {1: [(8,2), (9, 1), (9,3), (9,2)],
                                       2: [(8,1), (9,0), (8,3), (9,4), (9,2)],
                                       3: [(10,0), (7,1), (8,4), (9,5)],
                                       ORANGE: [(8,4)]}

        self.transition_dict[(9,3)] = {1: [(9, 4), (9,2)],
                                       2: [(9,1), (8,2), (9,5)],
                                       3: [(10,5), (9,6), (8,5), (8,1), (8,3), (9,0)]}

        self.transition_dict[(9,4)] = {1: [(9, 3), (9,5)],
                                       2: [(10,5), (8,5), (9,2), (9,6)],
                                       3: [(7,5), (9,1), (8,2), (9,7)]}

        self.transition_dict[(9,5)] = {1: [(9,4), (8,5), (9,6)],
                                       2: [(10,7), (7,5), (9,3)],
                                       3: [(7,6), (9,8), (10,2), (6,5)],
                                       SURPRISE: True}

        self.transition_dict[(9, 6)] = {1: [(9, 7), (9,5)],
                                        2: [(8,5), (9,4), (9,8)],
                                        3: [(10,8), (7,5), (9,3)]}

        self.transition_dict[(9, 7)] = {1: [(9, 8), (9,6)],
                                        2: [(8,8), (9,5), (10,8)],
                                        3: [(10,7), (7,8), (8,5), (9,4)]}

        self.transition_dict[(9, 8)] = {1: [(9, 7), (10,8), (8,8)],
                                        2: [(10,7), (9,6), (7,8)],
                                        3: [(6,8), (9,5)],
                                        WAIT: 4,
                                        MESSAGE: "That was stupid. You are in Prison"} #Prison

        self.transition_dict[(9, 9)] = {1: [(9, 10)],
                                        2: [(9,11)],
                                        3: [(10,11)],
                                        NEED: Certificate.TAX,
                                        JUMP: [(11,8)]}

        self.transition_dict[(9, 10)] = {1: [(9,11)],
                                         2: [(10,11)],
                                         3: [(11,11)]}

        self.transition_dict[(9, 11)] = {1: [(10,11), (9,11)],
                                         2: [(11,11)],
                                         3: [(9,11)],
                                         ORANGE: [(11,11)],
                                         NEED: Certificate.BIRTH,
                                         JUMP: [(11,8)]}


    def init_row8(self):
        self.transition_dict[(8, 0)] = {1: [(8, 1)],
                                        2: [(9, 1), (7,1)],
                                        3: [(9,0), (6,1), (9, 2)],
                                        HAS: Certificate.GRANDMA,
                                        JUMP: [(11,1), (10,11)]}

        self.transition_dict[(8,1)] = {1: [(9,1), (7,1)],
                                       2: [(9,2), (6,1)],
                                       3: [(8,0), (5,1), (8,2)]}

        self.transition_dict[(8,2)] = {1: [(8,3), (8,2)],
                                       2: [(8,4)],
                                       3: [(8,2)],
                                       ORANGE: [(8,4)],
                                       MESSAGE: "You entered the Photography studio."}

        self.transition_dict[(8,3)] = {1: [(8, 4)],
                                       2: [(8,3)],
                                       3: [(8,3)],
                                       ORANGE: [(8,4)]}

        self.transition_dict[(8,4)] = {1: [(8,5)],
                                       2: [(9,5), (7,5)],
                                       3: [(7,6), (9,6), (9,4)],
                                       BALANCE: PACKAGE_COST,  # negative
                                       JUMP: [(8,5), (11,11)],
                                       HAS: Certificate.PASSPORT}

        self.transition_dict[(8,5)] = {1: [(7, 5), (9, 5), (8, 5)],
                                       2: [(7, 6), (6, 5), (9, 6), (8, 5)],
                                       3: [(6, 6), (6, 4), (9, 7), (9, 3)],
                                       ORANGE: [(6, 4)]}

        self.transition_dict[(8, 8)] = {1: [(9, 8), (7, 8)],
                                        2: [(6, 8), (10, 8), (9, 7)],
                                        3: [(5, 8), (10, 7), (9, 6)]}

        self.transition_dict[(8, 9)] = {1: [(9, 9)],
                                        2: [(9, 10)],
                                        3: [(9, 11)],
                                        NEED: Certificate.ID,
                                        JUMP: [(11,8)]}
