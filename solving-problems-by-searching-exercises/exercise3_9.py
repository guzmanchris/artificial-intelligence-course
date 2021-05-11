"""
 CIIC 5015: Artificial Intelligence
 Prof. J. Fernando Vega Riveros
 Programming Assignment 2
 Date: March 26, 2021
 Author: Christian D. Guzmán Torres

 Project is based on Russell, S. and Norvig P. Artificial Intelligence: A Modern Approach, 3rd Edition
 Exercise 3.9
"""

# Import code from the aima repo using the import script.
from import_script import *


# =======================================================================================================================
#                                            Define the problem
# =======================================================================================================================
class MissionariesAndCannibalsProblem(Problem):
    """
        This problem class implements the problem defined in Exercise 3.9. Please refer to
        "Missionaries and Cannibals Diagram.png" for a diagram of the complete state space and a legend of the
        abbreviations used to describe each state.

        In this implementation the states are tuples with the number of missionaries and cannibals at each side
        and the position of the boat. (ML, CL, MR, CR, B). E.g. In state (3, 3, 0, 0, 'L') all missionaries and
        cannibals, and the boat are on the left.
    """

    def __init__(self, initial=None, goal=None):
        super(MissionariesAndCannibalsProblem, self).__init__(initial, goal)
        # If no initial state is provided, use the default (All missionaries and cannibals on left side)
        if self.initial is None:
            self.initial = (3, 3, 0, 0, 'L')
        # If no goal is specified, use the default goal (All missionaries and cannibals on right side).
        if self.goal is None:
            self.goal = (0, 0, 3, 3, 'R')

    def actions(self, state):
        possible_actions = []
        # Only add actions that lead to valid states.
        for action in ('Move 1M', 'Move 2M', 'Move 1C', 'Move 2C', 'Move 1M 1C'):
            ML, CL, MR, CR, B = self.result(state, action)
            # Condition checks if mathematically possible to execute action.
            positive_values = ML >= 0 and CL >= 0 and MR >= 0 and CR >= 0
            # Conditions check if missionaries outnumber cannibals at both sides
            ml_gte_cl = not ML or ML >= CL
            mr_gte_cr = not MR or MR >= CR
            if positive_values and ml_gte_cl and mr_gte_cr:
                possible_actions.append(action)
            # This method does not check if repeated state. Search algorithm should take that in consideration.
        return possible_actions

    def result(self, state, action):
        ML, CL, MR, CR, B = state
        # Update locations of missionaries and cannibals appropriately
        if action == 'Move 1M':
            if B == 'L':
                ML -= 1
                MR += 1
            elif B == 'R':
                MR -= 1
                ML += 1
        elif action == 'Move 2M':
            if B == 'L':
                ML -= 2
                MR += 2
            elif B == 'R':
                MR -= 2
                ML += 2
        elif action == 'Move 1C':
            if B == 'L':
                CL -= 1
                CR += 1
            elif B == 'R':
                CR -= 1
                CL += 1
        elif action == 'Move 2C':
            if B == 'L':
                CL -= 2
                CR += 2
            elif B == 'R':
                CR -= 2
                CL += 2
        elif action == 'Move 1M 1C':
            if B == 'L':
                ML -= 1
                CL -= 1
                MR += 1
                CR += 1
            elif B == 'R':
                MR -= 1
                CR -= 1
                ML += 1
                CL += 1

        # Update location of boat
        B = 'L' if B == 'R' else 'R'

        return ML, CL, MR, CR, B

    def value(self, state):
        # Return NotImplementedException. This function is not needed in this case.
        return super(MissionariesAndCannibalsProblem, self).value(state)


# =======================================================================================================================
#                                Use search algorithms to find optimal solution
# =======================================================================================================================
problem = MissionariesAndCannibalsProblem()  # Initialize problem


# Get the path from the result node. Return a list with the path taken.
def get_path(node):
    path = [node.state]
    while node.parent:
        path.append(node.parent.state)
        node = node.parent
    return path[-1::-1]


# Perform Breadth-First search algorithm. Display info.
print("Performing Breadth-First search algorithm")
result = breadth_first_tree_search(problem)
print('The resulting path of the search was:')
for state in get_path(result):
    print(state)
print("With a path cost of:", result.path_cost, 'boat rides')


# The following lines of code show why it is important to check for repeated states. Uncomment to see what happens!

# print("Performing Depth-First search algorithm")
# print("This case illustrates an infinite loop because of repeated states")
# result = depth_first_tree_search(problem)
# # This part of the code will never be reached
# print('The resulting path of the search was:')
# for state in get_path(result):
#     print(state)
# print("With a path cost of:", result.path_cost, 'boat rides')
