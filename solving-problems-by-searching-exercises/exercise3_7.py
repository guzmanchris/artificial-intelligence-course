"""
 CIIC 5015: Artificial Intelligence
 Prof. J. Fernando Vega Riveros
 Programming Assignment 2
 Date: March 26, 2021
 Author: Christian D. Guzmán Torres

 Project is based on Russell, S. and Norvig P. Artificial Intelligence: A Modern Approach, 3rd Edition
 Exercise 3.7
"""

# Import code from the aima repo using the import script.
from import_script import *


#=======================================================================================================================
#                                            Define the problem
#=======================================================================================================================
class PolygonalObjectsProblem(Problem):
    """
    This problem class implements the problem defined in Exercise 3.7. Points adjacent to each of the vertices of the
    polygon obstacles are used as the state space. Please refer to "Figure3_31_numbered.png" for clarifying the
    vertex identifiers used in the vertices dictionary. The vertex coordinates were found using paint and are
    the (x, y) pixel coordinates in the image.
    """
    S = (86, 185)  # Point S (initial state)
    G = (448, 15)  # Point G (goal state)

    def __init__(self, initial=S, goal=G):
        super(PolygonalObjectsProblem, self).__init__(initial, goal)
        # The following dictionary stores the adjacent points to each of the vertices of the polygon objects.
        self.vertices = {
            1: (98, 153), 2: (98, 213), 3: (271, 153), 4: (271, 213),  # Rectangle 1
            5: (90, 122), 6: (79, 61), 7: (144, 3), 8: (188, 61), 9: (152, 135),  # Pentagon
            10: (181, 139), 11: (235, 139), 12: (207, 45),  # Triangle 1
            13: (231, 85), 14: (231, 9), 15: (276, 3), 16: (310, 28),  # Trapezoid
            17: (273, 102), 18: (333, 150), 19: (292, 188),  # Triangle 2
            20: (311, 128), 21: (388, 127), 22: (388, 10), 23: (311, 10),  # Rectangle 2
            24: (351, 151), 25: (350, 195), 26: (388, 216), 27: (426, 197), 28: (426, 152), 29: (392, 124),  # Hexagon
            30: (430, 142), 31: (443, 32), 32: (419, 7), 33: (389, 25)  # Polygon
        }
        # Specify the heuristic function. Returns straight line distance from state to goal.
        self.h = lambda node: self.v_magnitude(self.straight_line_vector(node.state, goal))

    def actions(self, state):
        # Maps each vertex to the vertices that can be reached from a given state.
        v = self.vertices
        if state == self.initial:
            vertices = (v[1], v[2], v[5], v[6])
        elif state == v[1]:
            vertices = (v[2], v[5], v[6], v[9], v[10], v[11], v[3], self.initial)
        elif state == v[2]:
            vertices = (v[1], v[4], v[5], v[6], self.initial)
        elif state == v[3]:
            vertices = (v[1], v[4], v[19], v[17], v[13], v[12], v[11], v[10], v[9], v[5])
        elif state == v[4]:
            vertices = (v[2], v[3], v[17], v[19], v[18], v[21], v[24], v[25], v[26])
        elif state == v[5]:
            vertices = (v[1], v[2], self.initial, v[9], v[10], v[3], v[6])
        elif state == v[6]:
            vertices = (v[2], self.initial, v[1], v[5], v[7])
        elif state == v[7]:
            vertices = (v[6], v[8], v[12], v[14], v[15])
        elif state == v[8]:
            vertices = (v[7], v[9], v[10], v[12], v[14])
        elif state == v[9]:
            vertices = (v[1], v[3], v[5], v[8], v[10], v[11], v[12])
        elif state == v[10]:
            vertices = (v[1], v[3], v[5], v[8], v[9], v[11], v[12])
        elif state == v[11]:
            vertices = (v[1], v[3], v[9], v[10], v[12], v[12], v[14], v[16], v[17])
        elif state == v[12]:
            vertices = (v[7], v[8], v[9], v[10], v[11], v[13], v[14])
        elif state == v[13]:
            vertices = (v[3], v[11], v[12], v[14], v[16], v[17], v[19])
        elif state == v[14]:
            vertices = (v[7], v[8], v[11], v[12], v[13], v[15])
        elif state == v[15]:
            vertices = (v[7], v[14], v[16], v[22], v[23], v[32])
        elif state == v[16]:
            vertices = (v[11], v[13], v[15], v[17], v[20], v[23])
        elif state == v[17]:
            vertices = (v[3], v[4], v[11], v[13], v[16], v[18], v[19], v[20], v[24])
        elif state == v[18]:
            vertices = (v[4], v[17], v[19], v[20], v[21], v[24], v[25], v[29])
        elif state == v[19]:
            vertices = (v[3], v[4], v[13], v[17], v[18], v[21], v[24], v[25], v[26])
        elif state == v[20]:
            vertices = (v[16], v[17], v[18], v[21], v[23], v[24], v[29])
        elif state == v[21]:
            vertices = (v[4], v[18], v[19], v[20], v[22], v[24], v[29], v[33])
        elif state == v[22]:
            vertices = (v[15], v[21], v[23], v[29], v[32], v[33])
        elif state == v[23]:
            vertices = (v[15], v[16], v[20], v[22], v[32])
        elif state == v[24]:
            vertices = (v[4], v[17], v[18], v[19], v[20], v[21], v[25], v[29])
        elif state == v[25]:
            vertices = (v[4], v[18], v[19], v[24], v[26])
        elif state == v[26]:
            vertices = (v[2], v[4], v[19], v[25], v[27])
        elif state == v[27]:
            vertices = (v[26], v[28], v[30], v[31], self.goal)
        elif state == v[28]:
            vertices = (v[27], v[29], v[30], v[33])
        elif state == v[29]:
            vertices = (v[18], v[20], v[21], v[22], v[24], v[28], v[30], v[33])
        elif state == v[30]:
            vertices = (v[27], v[28], v[29], v[31], self.goal)
        elif state == v[31]:
            vertices = (v[27], v[30], v[32], self.goal)
        elif state == v[32]:
            vertices = (v[15], v[22], v[23], v[31], v[33], self.goal)
        elif state == v[33]:
            vertices = (v[21], v[22], v[28], v[29], v[30], v[32])
        elif state == self.goal:
            return tuple()  # No actions required. Already at goal.
        else:
            raise Exception("Invalid state provided.")

        # Return a tuple of the straight-line vectors to all reachable vertices.
        return tuple([self.straight_line_vector(state, vertex) for vertex in vertices])

    def result(self, state, action):
        # Add the straight-line vector to the current vertex to arrive at the next vertex.
        x1, y1 = state
        dx, dy = action
        return x1 + dx, y1 + dy

    def path_cost(self, c, state1, action, state2):
        # Add to the current cost, the magnitude of the action vector (straight-line distance).
        return c + self.v_magnitude(action)

    def value(self, state):
        # Returns not implemented exception. Function not needed.
        return super(PolygonalObjectsProblem, self).value(state)

    @staticmethod
    def straight_line_vector(v1, v2):
        # Returns a new vector that points from v1 to v2
        x1, y1 = v1
        x2, y2 = v2
        return x2 - x1, y2 - y1

    @staticmethod
    def v_magnitude(vector):
        """ Returns the magnitude of the vector. If the vector is the straight-line vector, it gives the straight-line
        distance """
        x, y = vector
        return np.sqrt(x**2 + y**2)


#=======================================================================================================================
#                                Use search algorithms to find optimal solution
#=======================================================================================================================
problem = PolygonalObjectsProblem()  # Initialize the problem.

# Invert vertex mapping. Map the (x,y) coordinate of the vertex to it's identifier.
vertex_mapping = {v: k for k, v in problem.vertices.items()}
vertex_mapping.update({(86, 185): 'S', (448, 15): 'G'})


# Get the path from the result node. Return a list with the path taken.
def get_path(node):
    path = [vertex_mapping[node.state]]
    while node.parent:
        path.append(vertex_mapping[node.parent.state])
        node = node.parent

    return path[-1::-1]


print("Using Informed Search Strategies")

# Perform a* search algorithm. Display info.
# Print the path taken.
# Please refer to 'astar_path_chosen.png' for a visual representation of the path.
print("\nPerforming A* search algorithm")
result = astar_search(problem, problem.h, display=True)
print('The resulting path of the search was:', *get_path(result))
print("With a path cost of:", result.path_cost, 'pixels traveled from the 536x218 pixels plane')


# Perform greedy best-first search algorithm.
# Print the path taken.
# Please refer to 'greedy_path_chosen.png' for a visual representation of the path.
print("\nPerforming Greedy Best-First Search algorithm")
result = greedy_best_first_graph_search(problem, problem.h, display=True)
print('The resulting path of the search was:', *get_path(result))
print("With a path cost of:", result.path_cost, 'pixels traveled from the 536x218 pixels plane')

print("\nUsing an Uninformed Search Strategy")
# Perform uniform cost search algorithm.
# Print the path taken. The same path as a* search is found.
print("Performing Uniform Cost Search algorithm")
result = uniform_cost_search(problem, display=True)
print('The resulting path of the search was:', *get_path(result))
print("With a path cost of:", result.path_cost, 'pixels traveled from the 536x218 pixels plane')
