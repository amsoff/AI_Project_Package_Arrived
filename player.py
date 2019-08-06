import board
from Certificates import Certificate
from Constants import Types
import Constants
import domain_create as dc
certificates = Certificate.list()

board_game = board.Board().transition_dict
all_come_backs = {tile for tile in board_game if (board.NEED in board_game[tile]) or (board.BALANCE in board_game[tile] and board_game[tile][board.BALANCE] < 0)}
payment_spots = {tile for tile in board_game if board.BALANCE in board_game[tile] or board.SURPRISE in board_game[tile]}

class Player:
    type = Types.AVERAGE.value
    money = Constants.PLAYER_STARTING_MONEY
    cell = Constants.START
    has_certificates = []
    dice_value = 0
    come_back_spots = []
    need_pay_spots = []
    goal = Constants.GOAL
    start = Constants.START
    # package_cost = 0

    def __init__(self, player_type, goal=Constants.GOAL, start = Constants.START, money = Constants.PLAYER_STARTING_MONEY):
        self.type = player_type
        self.goal = goal
        self.cell = start
        self.money = money


    def set_type(self, player_type):
        self.type = player_type



    def get_goals(self):
        goals = [dc.AT_FORMAT % self.goal]
        goals.extend(dc.create_not_come_back_props())
        goals.extend(dc.create_not_need_pay_props())
        # goals.extend(dc.create_not_needs_items())
        return goals

    def get_certificates_props(self):
        certs = []
        for cert in self.has_certificates:
            certs.append(dc.CERTIFICATES_FORMAT % cert)
            # certs.append(dc.NOT_NEEDS_FORMAT % certificates[i])
        return certs

    def get_comeback_props(self):
        cbs = []
        for tile in self.come_back_spots:
            cbs.append(dc.COME_BACK_FORMAT % tile)
        cbs.extend([dc.NOT_COME_BACK_FORMAT % cell for cell in all_come_backs.difference(self.come_back_spots)])
        return cbs

    def get_stops(self):
        stops = []
        for i in range(1, Constants.MAX_STOPS + 1):
            stops.append(Constants.NOT_STOP_FORMAT % i)
        return stops


    def get_pays(self):
        pays = [dc.NOT_NEED_PAY_CELL % cell for cell in payment_spots.difference(self.need_pay_spots)]
        return pays



    def get_initial(self):
        initial = [dc.AT_FORMAT % self.cell,
                   dc.DICE_FORMAT % self.dice_value,
                   dc.MONEY_FORMAT % self.money]
        initial.extend(self.get_certificates_props())
        initial.extend(self.get_comeback_props())
        initial.extend(self.get_stops())
        initial.extend(self.get_pays())
        # initial.extend(self.get_owes())
        # initial.extend(self.get_not_owes())
        return initial
    
    def set_goal(self,cell):
        self.goal = cell

    def build_problem(self):
        agent = Types.OPTIMISTIC.name.lower()
        if self.type == Types.AVERAGE.value:
            agent = Types.AVERAGE.name.lower()
        file_name = agent + "_" + "problem.txt"
        problem_file = open(file_name, 'w')  # use problem_file.write(str) to write to problem_file

        # write propositions to file
        problem_file.write("Initial state: ")
        inits = self.get_initial()
        problem_file.write(" ".join(inits))

        # write actions to file
        goals = self.get_goals()
        problem_file.write("\nGoal state: ")
        problem_file.write(" ".join(goals))
        problem_file.write("\n")
        problem_file.close()


pla = Player(Constants.GOAL)
pla.build_problem()