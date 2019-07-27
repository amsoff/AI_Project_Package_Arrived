from dice import dice
import board
from Certificates import Certificate

GRANDMA = 0
INTEGRITY = 1
BIRTH = 2
ID = 3
RABIES = 4
PASSPORT = 5
MILITARY = 6
TAX = 7
PORT = 8
GLASSES = 9
HAT = 10
HAIRCUT = 11
PACKAGE = 12
certificates = [Certificate.GRANDMA,
                Certificate.INTEGRITY,
                Certificate.BIRTH,
                Certificate.ID,
                Certificate.RABIES,
                Certificate.PASSPORT,
                Certificate.MILITARY,
                Certificate.TAX,
                Certificate.PORT,
                Certificate.GLASSES,
                Certificate.HAT,
                Certificate.HAIRCUT,
                Certificate.PACKAGE]


board_game = board.Board(1).transition_dict
come_back_spots = [tile for tile in board_game if (board.NEED in board_game[tile] and (Certificate.HAT not in board_game[tile][board.NEED] or Certificate.GLASSES not in board_game[tile][board.NEED])) or board.SURPRISE in board_game[tile] or board.BALANCE in board_game[tile]]
payment_spots = [tile for tile in board_game if board.BALANCE in board_game[tile] or board.SURPRISE in board_game[tile]]

surprise_amounts = [-300, -200, -100, 100, 200, 300]
class Player:
    money = 1500
    cell = (1,0)
    has = [False] * 13
    needs = []
    dice_value = 0
    come_back_spots = []
    need_pay_spots = []
    stops_left = 0
    package_cost = 0
    dice = dice()
    owe = []


    def pay(self, amount):
        if self.money >= amount:
            self.money -= amount
        else:
            self.owe.append(amount)

    def build_problem(self):
        pass
