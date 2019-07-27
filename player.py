from dice import dice
import board
from Certificates import Certificate
import domain_create as dc

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
all_come_backs = {tile for tile in board_game if (board.NEED in board_game[tile] and (Certificate.HAT not in board_game[tile][board.NEED] or Certificate.GLASSES not in board_game[tile][board.NEED])) or board.SURPRISE in board_game[tile] or board.BALANCE in board_game[tile]}
payment_spots = {tile for tile in board_game if board.BALANCE in board_game[tile] or board.SURPRISE in board_game[tile]}

surprise_amounts = [-300, -200, -100, 100, 200, 300]
class Player:
    type = dc.OPTIMI
    money = 1500
    cell = (1,0)
    has_certificate = [False] * 13
    needs_certificate = [False] * 13
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


    def get_goals(self):
        goals = ["at_21_28", "has_%s" % Certificate.PACKAGE]
        goals.extend(dc.create_not_come_back())
        goals.extend(dc.create_not_need_pay())
        goals.extend(dc.create_not_needs_items())
        goals.extend(dc.create_not_owe())
        return goals

    def get_certificates_props(self):
        certs = []
        for i in range(len(certificates)):
            if not self.needs_certificate[i]:
                certs.append(dc.NOT_NEEDS_FORMAT % certificates[i])
            elif self.has_certificate[i]:
                certs.append(dc.CERTIFICATES_FORMAT % certificates[i])
                certs.append(dc.NOT_NEEDS_FORMAT % certificates[i])
        return certs

    def get_comeback_props(self):
        cbs = []
        for tile in self.come_back_spots:
            cbs.append(dc.COME_BACK_FORMAT % tile)
        cbs.extend([dc.NOT_COME_BACK_FORMAT % cell for cell in all_come_backs.difference(self.come_back_spots)])
        return cbs

    def get_stops(self):
        stops = []
        for i in range(1, dc.MAX_STOPS+1-self.stops_left):
            stops.append(dc.NOT_STOP_FORMAT % i)
        return stops

    def get_pays(self):
        pays = [dc.NOT_OWE % abs(d) for d in surprise_amounts if d < 0]
        pays.extend([dc.NOT_NEED_PAY_CELL % cell for cell in payment_spots.difference(self.need_pay_spots)])
        return pays


    def get_initial(self):
        initial = [dc.AT_FORMAT % self.cell,
                   dc.DICE_FORMAT % self.dice_value,
                   dc.MONEY_FORMAT % self.money]
        initial.extend(self.get_certificates_props())
        initial.extend(self.get_comeback_props())
        initial.extend(self.get_stops())
        initial.extend(self.get_pays())
        return initial




    def build_problem(self):
        agent = "optimistic"
        if self.type == dc.MEAN:
            agent = "mean"
        file_name = agent + "_" + "problem"
        domain_file = open(file_name,'w')  # use domain_file.write(str) to write to domain_file

        # write propositions to file
        domain_file.write("Initial state: ")
        inits = self.get_initial()
        domain_file.write(" ".join(inits))

        # write actions to file
        goals = self.get_goals()
        domain_file.write("Goal State: ")
        domain_file.write(" ".join(goals))
        domain_file.close()

