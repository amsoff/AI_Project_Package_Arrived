"""
In search.py, you will implement generic search algorithms
"""

import graphplan.util as util
from tkinter import *

COUNTER = 0
CURR_NODE = 0
SUCCESSOR = 0
ACTION = 1
COST = 2
PARENT_NODE = 3


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
    while curr.get_parent():
        path.append(curr.get_action())
        curr = curr.get_parent()

    return path[::-1]


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
        curr = fringe.pop()

        if problem.is_goal_state(curr.get_node()):
            return get_path(curr)

        elif curr.get_node() not in closed:
            successors = problem.get_successors(curr.get_node())
            for i in range(len(successors)):
                fringe.push(PQItem((successors[i][0], successors[i][1], successors[i][2] + curr.get_cost(), curr)))
            closed.add(curr.get_node())
    return []


def depth_first_search(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches
    the goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
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
