from graphplan.util import Pair
import copy
from graphplan.proposition_layer import PropositionLayer
from graphplan.plan_graph_level import PlanGraphLevel
from graphplan.pgparser import PgParser
from graphplan.action import Action
from graphplan.search import a_star_search


class PlanningProblem:

    def __init__(self, domain_file, problem_file, actions, propositions):
        """
        Constructor
        """
        p = PgParser(domain_file, problem_file)
        if actions is None and propositions is None:
            self.actions, self.propositions = p.parse_actions_and_propositions()

        else:
            self.actions = actions
            self.propositions = propositions
        # list of all the actions and list of all the propositions

        initial_state, goal = p.parse_problem()
        # the initial state and the goal state are lists of propositions

        self.initialState = frozenset(initial_state)
        self.goal = frozenset(goal)

        self.create_noops()
        # creates noOps that are used to propagate existing propositions from one layer to the next

        PlanGraphLevel.set_actions(self.actions)
        PlanGraphLevel.set_props(self.propositions)
        self.expanded = 0

    def get_start_state(self):
        return self.initialState

    def get_actions(self):
        return self.actions

    def get_propositions(self):
        return self.propositions

    def is_goal_state(self, state):
        """
        Hint: you might want to take a look at goal_state_not_in_prop_payer function
        """
        return not self.goal_state_not_in_prop_layer(state)

    def get_successors(self, state):
        """
        For a given state, this should return a list of triples,
        (successor, action, step_cost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'step_cost' is the incremental
        cost of expanding to that successor, 1 in our case.
        You might want to this function:
        For a list / set of propositions l and action a,
        a.all_preconds_in_list(l) returns true if the preconditions of a are in l

        Note that a state *must* be hashable!! Therefore, you might want to represent a state as a frozenset
        """
        self.expanded += 1
        successors = []
        for action in self.actions:
            if action.all_preconds_in_list(state) and not action.is_noop():
                next_state = frozenset(state.union(set(action.get_add())).difference(set(action.get_delete())))
                successors.append((next_state, action, 1))
        return successors

    @staticmethod
    def get_cost_of_actions(actions):
        return len(actions)

    def goal_state_not_in_prop_layer(self, propositions):
        """
        Helper function that returns true if all the goal propositions
        are in propositions
        """
        for goal in self.goal:
            if goal not in propositions:
                return True
        return False

    def create_noops(self):
        """
        Creates the noOps that are used to propagate propositions from one layer to the next
        """
        for prop in self.propositions:
            name = prop.name
            precon = []
            add = []
            precon.append(prop)
            add.append(prop)
            delete = []
            act = Action(name, precon, add, delete, True)
            self.actions.append(act)

    def init_new_problem(self):
        pass


def max_level(state, planning_problem):
    """
    The heuristic value is the number of layers required to expand all goal propositions.
    If the goal is not reachable from the state your heuristic should return float('inf')
    A good place to start would be:
    prop_layer_init = PropositionLayer()          #create a new proposition layer
    for prop in state:
        prop_layer_init.add_proposition(prop)        #update the proposition layer with the propositions of the state
    pg_init = PlanGraphLevel()                   #create a new plan graph level (level is the action layer and the propositions layer)
    pg_init.set_proposition_layer(prop_layer_init)   #update the new plan graph level with the the proposition layer
    """
    prop_layer_init = PropositionLayer()
    for prop in state:
        prop_layer_init.add_proposition(prop)
    pg = PlanGraphLevel()
    pg.set_proposition_layer(prop_layer_init)
    level = 0

    while not planning_problem.is_goal_state(frozenset(pg.get_proposition_layer().get_propositions())):
        level += 1
        prev_state = frozenset(pg.get_proposition_layer().get_propositions())
        pg.expand_without_mutex(pg)
        cur_state = frozenset(pg.get_proposition_layer().get_propositions())
        if len(prev_state) == len(cur_state):  # fixed state
            return float('inf')
    return level


def level_sum(state, planning_problem):
    """
    The heuristic value is the sum of sub-goals level they first appeared.
    If the goal is not reachable from the state your heuristic should return float('inf')
    """
    prop_layer_init = PropositionLayer()
    for prop in state:
        prop_layer_init.add_proposition(prop)
    pg = PlanGraphLevel()
    pg.set_proposition_layer(prop_layer_init)
    level, heuristic_cost = 0, 0
    cur_goals = set()

    while not planning_problem.is_goal_state(frozenset(pg.get_proposition_layer().get_propositions())):
        prev_state = frozenset(pg.get_proposition_layer().get_propositions())
        new_goals = prev_state.intersection(planning_problem.goal).difference(cur_goals)
        heuristic_cost += level * len(new_goals)
        cur_goals.union(new_goals)
        pg.expand_without_mutex(pg)
        cur_state = frozenset(pg.get_proposition_layer().get_propositions())
        level += 1
        if len(prev_state) == len(cur_state):  # fixed state
            return float('inf')
    return heuristic_cost + level * (len(planning_problem.goal) - len(cur_goals))


def is_fixed(graph, level):
    """
    Checks if we have reached a fixed point,
    i.e. each level we'll expand would be the same, thus no point in continuing
    """
    if level == 0:
        return False
    return len(graph[level].get_proposition_layer().get_propositions()) == len(
        graph[level - 1].get_proposition_layer().get_propositions())


def null_heuristic(*args, **kwargs):
    return 0


if __name__ == '__main__':
    import sys
    import time

    if len(sys.argv) != 1 and len(sys.argv) != 4:
        print("Usage: PlanningProblem.py domainName problemName heuristicName(max, sum or zero)")
        exit()
    domain = 'dwrDomain.txt'
    problem = 'dwrProblem.txt'
    heuristic = null_heuristic
    if len(sys.argv) == 4:
        domain = str(sys.argv[1])
        problem = str(sys.argv[2])
        if str(sys.argv[3]) == 'max':
            heuristic = max_level
        elif str(sys.argv[3]) == 'sum':
            heuristic = level_sum
        elif str(sys.argv[3]) == 'zero':
            heuristic = null_heuristic
        else:
            print("Usage: planning_problem.py domain_name problem_name heuristic_name[max, sum, zero]")
            exit()
    player = domain.split("_")[0]
    start1 = time.clock()
    prob = PlanningProblem(domain, problem)
    start = time.clock()
    plan = a_star_search(prob, heuristic)
    end = time.clock()
    extract_time = end - start
    total_time = end - start1
    if plan is not None:
        print("Plan found with %d actions in %.2f seconds" % (len(plan), extract_time))
        print("Total Runtime: %d" % total_time)
        file = open(player + "_CHECK.txt", 'w')  # use domain_file.write(str) to write to domain_file

        # write propositions to file
        file.write("Plan:\n")
        file.write("\n".join([action.name for action in plan]))
        file.write("\n")
        file.close()
    else:
        print("Could not find a plan in %.2f seconds" % extract_time)
    print("Search nodes expanded: %d" % prob.expanded)


