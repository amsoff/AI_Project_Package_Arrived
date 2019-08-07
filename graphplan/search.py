"""
In search.py, you will implement generic search algorithms
"""

import graphplan.util as util
COUNTER = 0
CURR_NODE = 0
SUCCESSOR = 0
ACTION = 1
COST = 2
PARENT_NODE = 3
first_plan = dict()

class PQItem:
    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def get_node(self):
        return self.data[CURR_NODE]

    def get_action(self):
        return self.data[ACTION]

    def get_cost(self):
        return self.data[COST]

    def get_parent(self):
        return self.data[PARENT_NODE]


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def is_goal_state(self, state):
        """
        state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def get_path(curr_node):
    """

    :param curr_node:
    :return:
    """
    path = []
    curr = curr_node
    first_path = False
    if len(first_plan) == 0:
        first_path = True
    while curr.get_parent():
        path.append(curr.get_action())
        curr = curr.get_parent()
        if first_path:
            build_first_plan_dict(curr, path[::-1])
    return path[::-1]


def get_past_path(cur_node):
    path = []
    curr = cur_node
    while curr.get_parent():
        path.append(curr.get_action())
        curr = curr.get_parent()

    return path[::-1] + first_plan[cur_node.get_node()]


def is_visited_by_plan(curr_get_node: frozenset):
    return curr_get_node in first_plan


def build_first_plan_dict(curr_node: PQItem, path):
    first_plan[curr_node.get_node()] = path


def sort_successors(successors):
    ret = []
    jump = []
    goto = []
    move = []
    pay = []
    stop = []
    for successor in successors:
        if "jump" in successor[1].name:
            jump.append(successor)
        elif "Goto" in successor[1].name:
            goto.append(successor)
        elif "pay" in successor[1].name:
            pay.append(successor)
        elif "Move" in successor[1].name:
            move.append(successor)
        elif "Stop" in successor[1].name:
            stop.append(successor)
        else:
            print("##### in search forgot " + successor[1].name + " ###########")
    ret.extend(stop)
    ret.extend(jump)
    ret.extend(move)
    ret.extend(goto)
    ret.extend(pay)

    return ret




def general_search(problem, fringe):
    """
    general graph search algorithm from tirgul
    :param problem:
    :param fringe:
    :return:
    """

    fringe.push(PQItem((problem.get_start_state(), None, 0, None)))  # curr_node, action, cost, parent
    closed = set()
    while not fringe.isEmpty():
        i = 1
        curr = fringe.pop()

        if problem.is_goal_state(curr.get_node()):
            return get_path(curr)

        # elif is_visited_by_plan(curr.get_node()):
        #     print("VISITED!")
        #     return get_past_path(curr)

        elif curr.get_node() not in closed:
            successors = problem.get_successors(curr.get_node())
            successors = sort_successors(successors)
            for i in range(len(successors)):
                fringe.push(PQItem((successors[i][0], successors[i][1], successors[i][2] + curr.get_cost(), curr)))
            closed.add(curr.get_node())
        i += 1
    return "failed"


def depth_first_search(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches
    the goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem.txt that is being passed in:
    """
    fringe = util.Stack()
    return general_search(problem, fringe)


def breadth_first_search(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    fringe = util.Queue()
    return general_search(problem, fringe)


def uniform_cost_search(problem):
    """
    Search the node of least total cost first.
    """
    fringe = util.PriorityQueueWithFunction(lambda x: x.get_cost())
    return general_search(problem, fringe)


def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def a_star_search(problem, heuristic=null_heuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    print("reached aStar")
    fringe = util.PriorityQueueWithFunction(lambda x: x.get_cost() + heuristic(x.get_node(), problem))
    return general_search(problem, fringe)




# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
astar = a_star_search
ucs = uniform_cost_search
