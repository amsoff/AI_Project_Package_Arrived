import numpy as np
from enum import Enum

JUMP = 'jump'
PAY = 'pay'
ONE = 1
THREE = 3
FIVE = 5


class Nodes_Types(Enum):
    EMPTY = -1
    COURT = 1
    POLICE = 2
    LOTTERY = 3
    TAXES = 4
    HOME_OFFICE = 5
    BARBERSHOP = 6
    GARDEN = 7

    ORANGE = 8
    SURPRISE = 9

    @staticmethod
    def types_dict():
        return list(map(lambda c: c.value, Nodes_Types))


class Board:

    def __init__(self, num_players, starting_point=(1, 0), end_point=(21, 27)):
        self.board_w = 23
        self.board_h = 31
        self.starting_point = starting_point
        self.num_players = num_players

        self.state = np.full((self.board_h, self.board_w), -1, np.int8)

        self.transition_matrix = np.full((self.board_h, self.board_w), -1, np.int8)

        self.transition_dict = {}
        self.init_dict()

    def init_state(self):
        pass

    def init_transition(self):
        pass

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
        self.init_row12()
        self.init_row13()
        self.init_row14()
        self.init_row15()
        self.init_row16()
        self.init_row17()
        self.init_row18()
        self.init_row19()
        self.init_row20()
        self.init_row21()
        self.init_row22()

    def init_row22(self):
        self.transition_dict[(22, 30)] = {1: [(22, 29)], 3: [(22, 29)], 5: [(22, 29)], JUMP: [(22, 28)]}
        self.transition_dict[(22, 29)] = {1: [(21, 29)], 3: [(21, 29)], 5: [(21, 29)], JUMP: [(22, 27)]},
        self.transition_dict[(22, 28)] = {1: [(22, 27), (21, 28)], 3: [(21, 26), (19, 28)],
                                          5: [(21, 24), (20, 25), (17, 28)]}
        self.transition_dict[(22, 27)] = {1: [(21, 27)], 3: [(21, 25), (20, 28)], 5: [(18, 28), (19, 25), (21, 22)]}
        self.transition_dict[(22, 26)] = {1: [(21, 26)], 3: [(21, 28), (20, 25), (21, 24), (22, 27)],
                                          5: [(19, 28), (19, 25), (21, 22)]}
        self.transition_dict[(22, 25)] = {1: [(222, 225)], 3: [(222, 225)], 5: [(222, 225)]}
        self.transition_dict[(222, 225)] = {1: [(22, 26)], 3: [(21, 27), (21, 25)],
                                            5: [(20, 28), (20, 25), (21, 23)]}  # extra cell for waiting one turn
        self.transition_dict[(22, 24)] = {1: [(22, 25)], 3: [(22, 25)], 5: [(22, 25)]}
        self.transition_dict[(22, 22)] = {1: [(21, 22)], 3: [(21, 24), (21, 20)],
                                          5: [(19, 26), (22, 19), (21, 18), (19, 20)]}
        self.transition_dict[(22, 20)] = {1: [(21, 20), (22, 19)], 3: [(21, 22), (19, 20), (21, 18)],
                                          5: [(17, 20), (21, 16), (21, 24)]}
        self.transition_dict[(22, 19)] = {1: [(21, 19), (22, 20)], 3: [(21, 21), (20, 20), (21, 17)],
                                          5: [(18, 20), (21, 15), (20, 16), (21, 23)]}
        self.transition_dict[(22, 18)] = {1: [(22, 17)], 3: [(22, 15)],
                                          5: [(21, 16), (21, 14)]}
        self.transition_dict[(22, 17)] = {1: [(22, 16)], 3: [(21, 15)],
                                          5: [(22, 14), (21, 17), (20, 16)], PAY: 120}  # BUY GLASSES
        self.transition_dict[(22, 16)] = {1: [(22, 15)], 3: [(21, 14), (21, 16)],
                                          5: [(21, 18), (19, 16)], PAY: 95}  # BUY HAT
        self.transition_dict[(22, 15)] = {1: [(21, 15)], 3: [(22, 14), (21, 17), (20, 16)],
                                          5: [(21, 19), (18, 16)]}
        self.transition_dict[(22, 14)] = {1: [(21, 14)], 3: [(21, 16)],
                                          5: [(21, 18), (19, 16)]}

    def init_row21(self):
        pass

    def init_row20(self):
        pass

    def init_row19(self):
        pass

    def init_row18(self):
        pass

    def init_row17(self):
        pass

    def init_row16(self):
        pass

    def init_row15(self):
        pass

    def init_row14(self):
        pass

    def init_row13(self):
        pass

    def init_row12(self):
        pass

    def init_row11(self):
        correction = {
            (11, 30): {1: [(10, 30), (11, 30)], 3: [(8, 30), (12, 28)], 5: [(6, 30), (10, 28), (12, 26)], 'jump': []},
            (11, 28): {1: [(10, 28), (12, 28)], 3: [(13, 27), (12, 26)], 5: [(6, 28), (15, 27), (12, 24)], 'jump': []},
            (11, 25): {1: [(10, 25), (12, 25)], 3: [(12, 27), (8, 25), (12, 23), (13, 24)],
                       5: [(6, 25), (7, 24), (12, 29), (11, 28), (14, 27), (14, 23), (15, 24), (12, 21)], 'jump': []},
            (11, 21): {1: [(10, 22), (12, 23)], 3: [(8, 21), (12, 22), (12, 19), (13, 20)],
                       5: [(7, 22), (7, 20), (12, 25), (13, 24), (13, 18), (12, 17), (15, 20)], 'jump': []},
            (11, 20): {1: [(11, 19)], 3: [(12, 18)], 5: [(12, 20), (11, 17), (14, 18)], 'jump': []},
            (11, 19): {1: [(11, 18)], 3: [(12, 19), (12, 17), (13, 18)],
                       5: [(15, 18), (12, 21), (13, 20), (10, 17), (11, 16)], 'jump': []},
            (11, 18): {1: [(12, 18)], 3: [(12, 20), (14, 18), (11, 17)],
                       5: [(14, 20), (12, 22), (11, 21), (15, 17), (10, 16), (11, 15), (9, 17)], 'jump': []},
            (11, 17): {1: [(12, 17), (10, 17), (11, 16)], 3: [(12, 19), (13, 18), (10, 15), (12, 15), (8, 17), (9, 16)],
                       5: [(15, 18), (13, 20), (12, 21), (7, 18), (7, 16), (12, 14), (12, 15), (10, 15), (9, 16)],
                       'jump': []},
            (11, 16): {1: [(11, 17), (11, 15), (10, 16)], 3: [(12, 18), (12, 14), (10, 16), (9, 17), (8, 16)],
                       5: [(14, 18), (12, 20), (7, 17), (7, 15), (8, 16)], 'jump': []},
            (11, 15): {1: [(12, 17), (10, 15), (11, 16)], 3: [(12, 13), (12, 17), (11, 17), (10, 17), (9, 16)],
                       5: [(14, 13), (12, 11), (11, 12), (13, 18), (12, 20), (7, 16), (8, 17), (9, 16)], 'jump': []},
            (11, 12): {1: [(12, 12), (10, 12)], 3: [(12, 14), (12, 10)], 5: [(11, 15), (15, 13), (11, 9), (12, 8)],
                       'jump': []},
            (11, 9): {1: [(4, 29)], 3: [(4, 29)], 5: [(4, 29)], 'jump': [(4, 29)]},
            (11, 8): {1: [(11, 9), (12, 8), (10, 8)], 3: [(8, 8), (9, 13), (12, 10), (12, 6), (9, 9)],
                      5: [(6, 8), (7, 9), (7, 7), (8, 10), (16, 8), (15, 7), (12, 12), (12, 4)], 'jump': []}}

        self.transition_dict.update(correction)
        self.transition_dict[(11, 4)] = {1: [(12,4),(10,4)], 3: [(12,6), (14,4), (12,2),(8,4),(10,2)], 5: [(6,4),(7,5),(7,3),(10,0),(12,0),(12,8),(13,7),(16,4)], JUMP: []}
        self.transition_dict[(11, 0)] = {1: [(12,0),(10,0)], 3: [(14,0),(12,2),(10,2)], 5: [(10,4),(12,4),(16,0)], JUMP: []}

    def init_row10(self):
        self.transition_dict[(10, 30)] = {1: [(11, 30), (9, 30)], 3: [(7, 30), (12, 29)],
                                          5: [(5, 30), (11, 28), (12, 27)], JUMP: []}
        self.transition_dict[(10, 28)] = {1: [(11,28),(9,28)], 3:[(7,28), (12,29),(12,27)], 5:[(5,28),(6,27),(11,30),(12,25),(14,27)], JUMP:[]}
        self.transition_dict[(10, 25)] = {1: [(11,25),(9,25)], 3:[(7,25), (12,26),(12,24)], 5:[(5,25),(7,23),(6,26),(14,24),(12,22)], JUMP:[]}
        self.transition_dict[(10, 21)] = {1: [(11,21),(9,21)], 3:[(12,20), (12,22),(8,20),(7,21)], 5:[(7,23),(7,19),(14,20),(12,18),(12,24)], JUMP:[]}
        # todo fine constraind?
        self.transition_dict[(10, 20)] = {1: [(11,20)], 3:[(11,18)], 5:[(12,19),(12,17),(13,18)], JUMP:[]}
        self.transition_dict[(10, 17)] = {1: [(10,17),(10,16),(9,17)], 3:[(12,18),(7,17),(11,15),(8,16)], 5:[(12,20),(14,18),(12,14),(7,19),(7,15)], JUMP:[]}
        self.transition_dict[(10, 16)] = {1: [(10,17),(9,16),(11,16),(10,15)], 3:[(12,15),(8,17),(7,16),(12,17)], 5:[(7,18),(7,14),(7,16),(12,13),(12,19),(13,18)], JUMP:[]}
        self.transition_dict[(10, 15)] = {1: [(11,15),(10,16)], 3:[(12,14),(11,17),(8,16),(9,17)], 5:[(13,13),(12,12),(12,19),(13,18),(7,18),(6,16),(7,15)], JUMP:[]}
        self.transition_dict[(10, 12)] = {1: [(9,12),(11,12)], 3:[(12,13),(12,11)], 5:[(12,9),(13,14),(12,15)], JUMP:[]}
        self.transition_dict[(10, 9)] = {1: [(10,8),(9,9),(11,9)], 3:[(12,10),(12,8),(7,9),(8,8)], 5:[(7,11),(7,7),(6,8),(12,12),(12,5),(14,8),(13,7)], JUMP:[]}
        self.transition_dict[(10, 8)] = {1: [(10,9),(11,8),(9,8)], 3:[(8,9),(13,8),(12,7),(7,8),(12,9)], 5:[(5,8),(7,6),(7,10),(15,8),(12,11),(12,5),(14,7)], JUMP:[]}
        self.transition_dict[(10, 4)] = {1: [(11,4),(10,3),(9,4)], 3:[(7,4),(10,1),(12,5),(12,3)], 5:[(7,6),(7,2),(11,0),(12,7),(12,1)], JUMP:[]}
        self.transition_dict[(10, 3)] = {1: [(10,4),(10,2)], 3:[(8,4),(12,4),(10,0)], 5:[(14,4),(12,0),(12,2),(12,6),(7,5),(6,4),(7,3)], JUMP:[]}
        self.transition_dict[(10, 2)] = {1: [(10,3),(10,1)], 3:[(11,0),(9,4),(11,4)], 5:[(12,1),(13,0),(8,3),(7,4),(12,5),(13,4),(12,3)], JUMP:[]}
        self.transition_dict[(10, 1)] = {1: [(10,0),(10,2)], 3:[(12,0),(10,4)], 5:[(12,2),(14,0),(8,4),(12,4)], JUMP:[]}
        self.transition_dict[(10, 0)] = {1: [(10,1),(11,0)], 3:[(12,1),(13,0),(10,3)], 5:[(15,0),(12,3),(9,4),(11,4)], JUMP:[]}



    def init_row9(self):
        self.transition_dict[(9, 30)] = {1: [(10, 30), (11, 30)], 3: [(12, 30), (6, 30)], 5: [(5, 29), (12, 28)],
                                         JUMP: []}
        self.transition_dict[(9, 28)] = {1: [(10,28),(8,28)], 3:[(12,28),(6,28)], 5:[(12,29),(12,27),(6,27),(5,28)], JUMP:[]}
        self.transition_dict[(9, 27)] = {1: [(9,28)], 3:[(11,28),(7,28)], 5:[(12,29),(12,27),(6,27),(5,28)], JUMP:[]}
        self.transition_dict[(9, 26)] = {1: [(9,27)], 3:[(10,28),(8,28)], 5:[(6,28),(12,28)], JUMP:[]}
        self.transition_dict[(9, 25)] = {1: [(9,26),(10,25),(8,25)], 3:[(6,25),(12,25),(9,28)], 5:[(7,22),(6,27),(9,28),(12,23),(12,27),(4,25)], JUMP:[]}
        self.transition_dict[(9, 21)] = {1: [(10,21),(8,21)], 3:[(7,22),(7,20),(12,21)], 5:[(13,20),(12,19),(12,23),(7,24),(18,7)], JUMP:[]}
        self.transition_dict[(9, 21)] = {1: [(10,21),(8,21)], 3:[(7,22),(7,20),(12,21)], 5:[(13,20),(12,19),(12,23),(7,24),(18,7)], JUMP:[]}
        self.transition_dict[(9, 20)] = {1: [(9,19)], 3:[(9,19)], 5:[(9,19)], JUMP:[]}
        self.transition_dict[(9, 19)] = {1: [(9,18)], 3:[(9,18)], 5:[(9,18)], JUMP:[]}
        self.transition_dict[(9, 18)] = {1: [(10,20)], 3:[(11,19)], 5:[(12,18)], JUMP:[]}
        self.transition_dict[(9, 17)] = {1: [(10,17)], 3:[(8,17),(10,17),(9,16)], 5:[(7,20),(5,18),(7,14),(12,19),(12,15)], JUMP:[]}
        self.transition_dict[(9, 16)] = {1: [(10,16),(8,16),(9,17)], 3:[(11,15),(11,17),(7,17),(7,15)], 5:[(12,14),(12,18),(7,13),(7,19),(6,18)], JUMP:[]}
        self.transition_dict[(9, 12)] = {1: [(10,12)], 3:[(12,12)], 5:[(12,10),(12,14),(13,13)], JUMP:[]}
        self.transition_dict[(9, 9)] = {1: [(10,9),(9,8),(8,9)], 3:[(12,9),(7,8),(7,10),(11,8)], 5:[(7,12),(6,11),(5,8),(7,6),(12,11),(12,7),(13,8)], JUMP:[]}
        self.transition_dict[(9, 8)] = {1: [(10,8),(8,8),(9,9)], 3:[(12,8),(11,9),(6,8),(7,7),(7,9)], 5:[(4,8),(7,11),(7,5),(14,8),(13,7),(12,10),(11,9),(12,6)], JUMP:[]}
        self.transition_dict[(9, 7)] = {1: [(9,6)], 3:[(9,6)], 5:[(9,6)], JUMP:[]}
        self.transition_dict[(9, 6)] = {1: [(9,5)], 3:[(9,5)], 5:[(9,5)], JUMP:[]}
        self.transition_dict[(9, 5)] = {1: [(9,4)], 3:[(11,4),(7,4),(10,3)], 5:[(5,4),(7,6),(7,2),(10,3),(11,4)], JUMP:[]}
        self.transition_dict[(9, 4)] = {1: [(8,4),(10,4)], 3:[(6,4),(7,5),(7,3),(10,2),(12,4)], 5:[(7,7),(7,1),(4,4),(10,0),(12,6),(12,2)], JUMP:[]}
        self.transition_dict[(9, 3)] = {1: [(10,3)], 3:[(10,1),(11,4),(7,4)], 5:[(11,0),(12,5),(13,4),(12,3),(7,6),(7,2),(5,4)], JUMP:[]}

    def init_row8(self):
        self.transition_dict[(8, 30)] = {1: [(9, 30), (7, 30)], 3: [(12, 30), (6, 30)], 5: [(5, 29), (12, 28)],
                                         JUMP: []}
        self.transition_dict[(8, 28)] = {1: [(9,28),(7,28)], 3:[(5,28),(11,28),(6,27)], 5:[(6,25),(5,30),(3,28),(12,29),(12,27)], JUMP:[]}
        self.transition_dict[(8, 25)] = {1: [(9,25),(7,25)], 3:[(11,25),(7,24),(5,25),(6,26)], 5:[(6,28),(7,21),(3,25),(12,27),(12,24)], JUMP:[]}
        self.transition_dict[(8, 21)] = {1: [(8,20)], 3:[(8,20)], 5:[(8,20)], JUMP:[]}
        self.transition_dict[(8, 20)] = {1: [(9,20)], 3:[(11,20)], 5:[(11,18)], JUMP:[]}
        self.transition_dict[(8, 17)] = {1: [(9,17),(8,16),(7,17)], 3:[(11,17),(7,15),(6,18),(6,16)], 5:[(12,18),(7,13),(6,20),(7,21),(11,15)], JUMP:[]}
        self.transition_dict[(8, 16)] = {1: [(8,17),(7,16),(9,16)], 3:[(11,16),(10,17),(7,14),(7,18),(5,16)], 5:[(12,15),(12,17),(7,20),(5,18),(8,13)], JUMP:[]}
        self.transition_dict[(8, 13)] = {1: [(7,13)], 3:[(7,11),(7,15)], 5:[(8,16),(6,16),(5,11),(8,10),(7,9)], JUMP:[]}
        self.transition_dict[(8, 10)] = {1: [(7,10),(8,9)], 3:[(8,7),(7,8),(9,8),(10,9),(6,11)], 5:[(7,14),(8,13),(4,11),(5,8),(7,6),(11,8),(12,9)], JUMP:[]}
        self.transition_dict[(8, 9)] = {1: [(8,10),(8,8),(9,9),(7,9)], 3:[(7,11),(6,8),(7,7),(11,9),(10,8)], 5:[(5,11),(7,13),(8,6),(7,5),(12,10),(12,8)], JUMP:[]}
        self.transition_dict[(8, 8)] = {1: [(8,9),(9,8),(7,8),(7,8)], 3:[(9,7),(7,10),(11,8),(7,6)], 5:[(9,5),(12,7),(7,4),(6,11),(7,12),(12,9)], JUMP:[]}
        self.transition_dict[(8, 7)] = {1: [(8,6)], 3:[(9,6)], 5:[(9,5)], JUMP:[]}
        self.transition_dict[(8, 6)] = {1: [(9,7)], 3:[(9,5)], 5:[(10,4),(8,4)], JUMP:[]}
        self.transition_dict[(8, 4)] = {1: [(8,3),(9,4),(7,4)], 3:[(10,3),(5,4),(7,6),(7,2)], 5:[(10,4),(12,5),(12,3),(10,1),(3,4),(7,8)], JUMP:[]}
        self.transition_dict[(8, 3)] = {1: [(9,3)], 3:[(10,4),(10,2)], 5:[(8,4),(12,4),(10,0)], JUMP:[]}

    def init_row7(self):
        self.transition_dict[(7, 30)] = {1: [(6, 30),(8,30)], 3: [(10,30), (5,29)], 5: [(4,28), (6,28), (12, 30)], JUMP: []}
        self.transition_dict[(7, 28)] = {1: [(8, 28),(6,28)], 3: [(10,28), (5,29),(4,28),(6,26)], 5: [(6,30), (7,25), (5, 25),(3,28),(12,28)], JUMP: []}
        self.transition_dict[(7, 25)] = {1: [(8, 25),(6,25), (7,24)], 3: [(7,22), (10,25),(4,25),(6,27)], 5: [(8,21), (7,20), (7, 28),(5,28),(12,25)], JUMP: []}
        self.transition_dict[(7, 24)] = {1: [(7, 25),(7,23)], 3: [(7,21), (9,25),(5,25),(6,26)], 5: [(8,20), (9,21), (7,19) ,(6,20),(11,25),(6,28),(3,25)], JUMP: []}
        self.transition_dict[(7, 23)] = {1: [(7, 24),(7,22)], 3: [(8,21), (7,20),(8,25),(6,25)], 5: [(10,25), (6,27), (4,25) ,(10,21),(8,20),(7,18),(5,20)], JUMP: []}
        self.transition_dict[(7, 22)] = {1: [(7, 23),(7,21)], 3: [(7,25), (8,20),(9,21),(7,19),(6,20)], 5: [(9,25), (6,26), (5,25) ,(4,20),(6,18),(11,21),(5,20)], JUMP: []}
        self.transition_dict[(7, 21)] = {1: [(7, 22),(7,20),(8,21)], 3: [(7,24), (10,21),(7,18),(5,20),(8,20)], 5: [(8,20), (8,25), (6,25) ,(12,21),(5,18),(3,20)], JUMP: []}
        self.transition_dict[(7, 20)] = {1: [(7, 21),(7,19),(6,20)], 3: [(6,18), (4,20),(8,20),(7,23),(7,17)], 5: [(7,25), (2,20), (4,18) ,(8,20),(11,21),(6,16),(17,15),(9,17)], JUMP: []}
        self.transition_dict[(7, 19)] = {1: [(7, 20),(7,18)], 3: [(5,18), (5,20),(7,22),(8,21),(7,16)], 5: [(7,24), (8,20), (10,21) ,(3,20),(3,18),(10,17),(9,16),(5,16),(7,14)], JUMP: []}
        self.transition_dict[(7, 18)] = {1: [(7, 19),(7,17),(6,18)], 3: [(7,21), (6,20),(4,18),(7,15),(9,17),(8,16)], 5: [(8,20), (7,23), (4,20),(9,21),(3,17),(11,17),(10,16),(7,13),(5,16)], JUMP: []}
        self.transition_dict[(7, 17)] = {1: [(7, 18),(7,16),(8,17)], 3: [(7,20), (5,18),(5,16),(7,14),(10,17),(10,16)], 5: [(8,13), (8,12), (3,16),(7,22),(8,21),(5,20),(3,18),(3,16),(7,12)], JUMP: []}
        self.transition_dict[(7, 16)] = {1: [(7, 17),(7,15),(8,16),(6,16)], 3: [(7,19), (10,16),(7,13),(4,16),(6,18),(8,17)], 5: [(7,21), (3,17), (3,14),(7,11),(11,16),(11,15)], JUMP: []}
        self.transition_dict[(7, 15)] = {1: [(7, 16),(7,14)], 3: [(7,12), (8,13),(9,16),(8,17),(7,18),(5,16)], 5: [(10,17), (11,16), (7,20),(3,16),(7,10)], JUMP: []}
        self.transition_dict[(7, 14)] = {1: [(7, 15),(7,13)], 3: [(8,16), (6,16),(7,17),(7,11)], 5: [(10,16), (9,17), (7,19),(4,16),(7,9)], JUMP: []}
        self.transition_dict[(7, 13)] = {1: [(7, 14),(7,12),(8,13)], 3: [(7,16), (7,10)], 5: [(8,9), (7,18), (5,16),(4,11)], JUMP: []}
        self.transition_dict[(7, 12)] = {1: [(7, 13),(7,11)], 3: [(7,9), (8,10),(7,15)], 5: [(7,17), (8,16), (6,16),(7,7),(8,8),(6,8),(9,9)], JUMP: []}
        self.transition_dict[(7, 11)] = {1: [(7, 12),(7,10),(6,11)], 3: [(7,13), (4,11),(7,8),(8,9),(5,13)], 5: [(7,16), (2,11),(5,13),(3,10),(8,8),(7,6)], JUMP: []}
        self.transition_dict[(7, 10)] = {1: [(7, 11),(8,10),(7,9)], 3: [(7,13), (5,11),(7,7),(6,8),(9,9)], 5: [(7,15), (5,13),(3,11),(7,5),(8,8),(9,9),(10,8)], JUMP: []}
        self.transition_dict[(7, 9)] = {1: [(8,9),(7,10),(7,8)], 3: [(10,9), (8,7),(7,12),(7,6),(5,8)], 5: [(12,9), (9,6),(8,13),(7,14),(3,8)], JUMP: []}
        self.transition_dict[(7, 8)] = {1: [(7,9),(8,8),(6,8),(7,7)], 3: [(8,10), (7,11),(4,8),(7,5),(10,8)], 5: [(7,13), (11,9),(12,8),(9,5),(8,4),(7,3),(6,4),(3,9),(2,8),(3,7)], JUMP: []}
        self.transition_dict[(7, 7)] = {1: [(7,8),(7,6)], 3: [(8,7), (7,4),(7,10),(9,8),(5,8),(8,9)], 5: [(8,3), (7,2),(9,4),(5,4),(3,8),(7,12),(10,8),(10,9)], JUMP: []}
        self.transition_dict[(7, 6)] = {1: [(7,7),(7,5)], 3: [(8,8), (7,9),(6,8),(8,4),(7,3),(6,4)], 5: [(10,8), (7,11),(4,8),(10,4),(4,4),(7,1),(9,3)], JUMP: []}
        self.transition_dict[(7, 5)] = {1: [(7,6),(7,4)], 3: [(7,8), (7,2),(8,3),(9,4),(5,4)], 5: [(8,7), (6,8),(7,9),(8,8),(11,4),(3,4),(7,0)], JUMP: []}
        self.transition_dict[(7, 4)] = {1: [(7,5),(7,3),(6,4),(8,4)], 3: [(10,4), (7,1),(4,4),(7,7),(9,3)], 5: [(7,9), (2,4),(12,4),(10,2)], JUMP: []}
        self.transition_dict[(7, 3)] = {1: [(7,4),(7,2)], 3: [(9,4), (7,0),(7,6),(5,4)], 5: [(11,4), (10,3),(3,4)], JUMP: []}
        self.transition_dict[(7, 2)] = {1: [(7,1),(7,3)], 3: [(7,5), (6,4),(8,4)], 5: [(10,4), (4,4),(7,7),(9,3)], JUMP: []}
        self.transition_dict[(7, 1)] = {1: [(7,0),(7,2)], 3: [(7,4)], 5: [(9,4), (5,4),(7,6),(8,3)], JUMP: []}
        self.transition_dict[(7, 0)] = {1: [(7,1)], 3: [(7,3)], 5: [(8,3), (7,5),(6,4)], JUMP: []}

    def init_row6(self):
        self.transition_dict[(6, 30)] = {1: [(7, 30),(5,30)], 3: [(5, 28),(9,30)], 5: [(3, 28), (11, 30), (7, 28),(6,27)], JUMP: []}
        self.transition_dict[(6, 28)] = {1: [(7, 28),(5,28),(6,27)], 3: [(3, 28),(6,25),(5,30),(9,28)], 5: [(7, 30), (2,28), (11, 28),(8,25),(7,24),(4,25)], JUMP: []}
        self.transition_dict[(6, 27)] = {1: [(6, 28),(6,26)], 3: [(8, 28),(4,28),(5,29),(7,25),(5,25)], 5: [(9, 25), (10,28), (3, 25),(6,30),(4,28)], JUMP: []}
        self.transition_dict[(6, 26)] = {1: [(6, 27),(6,25)], 3: [(5, 28),(7,28),(7,24),(8,25),(4,25)], 5: [(9, 28), (5,30), (2, 25),(3,28),(7,22),(10,25)], JUMP: []}
        self.transition_dict[(6, 25)] = {1: [(6, 26),(5,25),(7,25)], 3: [(3, 25),(6,28),(9,25),(7,23)], 5: [(8, 28), (5,29), (4, 28),(1,25),(7,21),(11,25)], JUMP: []}
        self.transition_dict[(6, 24)] = {1: [(5, 24)], 3: [(5, 22)], 5: [(5, 22)], JUMP: []}
        self.transition_dict[(6, 23)] = {1: [(6, 24)], 3: [(5, 23)], 5: [(5, 22)], JUMP: [], PAY: 50}
        self.transition_dict[(6, 22)] = {1: [(6, 21)], 3: [(6, 21)], 5: [(6, 21)], JUMP: []}
        self.transition_dict[(6, 21)] = {1: [(6, 23)], 3: [(5, 24)], 5: [(5, 22)], JUMP: []}
        self.transition_dict[(6, 20)] = {1: [(5, 20),(7,20)], 3: [(7,22),(3,22),(7,18),(8,21)], 5: [(3, 18),(1,20),(5,18),(8,20),(10,21),(7,24)], JUMP: []}
        self.transition_dict[(6, 18)] = {1: [(7, 18),(5,18)], 3: [(7,20),(8,17),(7,16),(3,18)], 5: [(7, 22),(8,21),(5,20),(3,20),(3,16),(9,17),(7,14),(10,17),(9,16)], JUMP: []}
        self.transition_dict[(6, 17)] = {1: [(5, 17),(7,16)], 3: [(3,16),(7,18),(7,14),(9,16),(8,17)], 5: [(7, 22),(8,21),(5,20),(3,20),(3,16),(9,17),(7,14),(10,17),(9,16)], JUMP: []}
        self.transition_dict[(6, 14)] = {1: [(5, 14)], 3: [(3,14)], 5: [(3, 16),(3,12)], JUMP: []}
        self.transition_dict[(6, 13)] = {1: [(6, 14)], 3: [(4,14)], 5: [(3, 15),(3,13)], JUMP: []}
        self.transition_dict[(6, 11)] = {1: [(7, 11),(5,11)], 3: [(3,11),(5,13),(7,13),(7,9),(8,10)], 5: [(3, 13),(3,9),(1,11),(7,15),(8,8),(7,7),(9,9)], JUMP: []}
        self.transition_dict[(6, 8)] = {1: [(7, 8),(5,8)], 3: [(3,8),(7,10),(7,6),(9,8),(8,9)], 5: [(7, 12),(9,7),(1,8),(3,10),(3,6),(8,8),(7,4),(11,8)], JUMP: []}
        self.transition_dict[(6, 4)] = {1: [(7, 4),(5,4)], 3: [(4,4),(7,6),(7,2),(8,3),(9,4)], 5: [(8, 7),(7,8),(3,6),(1,4),(7,0),(11,4),(10,3)], JUMP: []}

    def init_row5(self):
        self.transition_dict[(5, 30)] = {1: [(6, 30),(5,29)], 3: [(4,28),(6,28),(8,30)], 5: [(10, 30),(2,28),(8,28),(6,26)], JUMP: []}
        self.transition_dict[(5, 29)] = {1: [(5, 30),(5,28)], 3: [(7,30),(7,28),(3,28),(6,27)], 5: [(9,30),(9,28),(6,25)], JUMP: []}
        self.transition_dict[(5, 28)] = {1: [(5, 29),(4,28),(6,28)], 3: [(6,30),(8,28),(6,26),(2,28)], 5: [(9,30),(9,28),(6,25)], JUMP: []}
        self.transition_dict[(5, 27)] = {1: [(5, 28)], 3: [(5,30),(7,28),(3,28),(6,27)], 5: [(7,30),(9,28),(6,25)], JUMP: []}
        self.transition_dict[(5, 25)] = {1: [(6, 25), (4,25)], 3: [(6,28),(2,25),(8,25),(7,24)], 5: [(5,28),(7,28),(10,25),(7,22),(0,25),(3,26)], JUMP: []}
        self.transition_dict[(5, 24)] = {1: [(5,23)], 3: [(5,22)], 5: [(5,22)], JUMP: []}
        self.transition_dict[(5, 23)] = {1: [(5,22)], 3: [(5,22)], 5: [(5,22)], JUMP: []}
        self.transition_dict[(5, 22)] = {1: [(5,21)], 3: [(6,20),(4,20)], 5: [(7,21),(7,19),(2,20),(3,19),(1,20)], JUMP: []}
        self.transition_dict[(5, 21)] = {1: [(5,20)], 3: [(7,20),(3,20)], 5: [(7,18),(7,22),(8,21),(3,18),(1,20)], JUMP: []}
        self.transition_dict[(5, 20)] = {1: [(6,20),(4,20)], 3: [(7,21),(7,19),(2,20),(3,19)], 5: [(9,21),(7,23),(6,18),(4,18),(3,17),(0,20)], JUMP: []}
        self.transition_dict[(5, 18)] = {1: [(6,18),(4,18)], 3: [(7,19),(3,19),(3,17)], 5: [(6,20),(7,21),(6,18),(4,20),(4,16),(3,15),(2,20)], JUMP: []}
        self.transition_dict[(5, 17)] = {1: [(4,17)], 3: [(5,18),(3,18)], 5: [(7,18),(3,20),(3,16)], JUMP: []}
        self.transition_dict[(5, 16)] = {1: [(4,16),(6,16),(5,17)], 3: [(3,17),(3,15),(7,16)], 5: [(6,18),(3,19),(3,18),(3,13),(7,19),(6,18),(7,13)], JUMP: []}
        self.transition_dict[(5, 15)] = {1: [(5,14)], 3: [(3,14)], 5: [(3,16),(3,12)], JUMP: []}
        self.transition_dict[(5, 14)] = {1: [(4,14)], 3: [(3,15),(3,13)], 5: [(3,17),(4,16),(3,11)], JUMP: []}
        self.transition_dict[(5, 13)] = {1: [(6,13)], 3: [(5,14)], 5: [(3,14)], JUMP: []}
        self.transition_dict[(5, 12)] = {1: [(5,13)], 3: [(5,13)], 5: [(5,13)], JUMP: []}
        self.transition_dict[(5, 11)] = {1: [(5,12),(4,11),(6,11)], 3: [(5,13),(3,12),(2,11),(3,10),(7,12),(7,10)], 5: [(5,13),(7,14),(3,14),(11,0),(3,8),(7,8),(8,9)], JUMP: []}
        self.transition_dict[(5, 8)] = {1: [(6,8),(4,8)], 3: [(4,6),(3,9),(3,7),(2,8),(8,8),(7,9),(7,7)], 5: [(3,11),(0,8),(4,5),(3,5),(7,5),(7,11),(8,6),(10,8)], JUMP: []}
        self.transition_dict[(5, 4)] = {1: [(5,6),(4,4)], 3: [(8,4),(7,5),(7,3),(2,4),(3,5)], 5: [(0,4),(3,7),(9,3),(7,1),(7,7),(10,4)], JUMP: []}

    def init_row4(self):
        pass

    def init_row3(self):
        pass

    def init_row2(self):
        pass

    def init_row1(self):
        pass

    def init_row0(self):
        pass
