# ============================================ Exercise 2.11 ==========================================================

# Already implemented code from the online repository will be used. The following code imports all from agents.py
import httpimport
import random
with httpimport.github_repo('aimacode', 'aima-python', ['utils', 'agents'], 'master'):
    from agents import *


def MyRandomVacuumAgent():

    def program(percept):
        if percept == 'Dirty':
            return 'Suck'
        elif percept == 'Clean':
            return random.choice(('Left', 'Right', 'Up', 'Down'))

    return Agent(program)


class EnvironmentA(Environment):

    def __init__(self):
        super().__init__()
        # Add walls around perimeter
        self.add_thing(Wall(), (-1, -1))
        self.add_thing(Wall(), (-1, 0))
        self.add_thing(Wall(), (-1, 1))
        self.add_thing(Wall(), (-1, 2))
        self.add_thing(Wall(), (-1, 3))
        self.add_thing(Wall(), (0, 3))
        self.add_thing(Wall(), (1, 3))
        self.add_thing(Wall(), (1, 2))
        self.add_thing(Wall(), (1, 1))
        self.add_thing(Wall(), (1, 0))
        self.add_thing(Wall(), (1, -1))
        self.add_thing(Wall(), (0, -1))

        #randomly add dirt at locations
        self.status = {
            (0, 0): random.choice(['Clean', 'Dirty']),
            (0, 1): random.choice(['Clean', 'Dirty']),
            (0, 2): random.choice(['Clean', 'Dirty'])
        }

    def thing_classes(self):
        return [Wall, Dirt, MyRandomVacuumAgent]

    def percept(self, agent):
        return self.status[agent.location]

    def execute_action(self, agent, action):

        if action == 'Suck':
            self.status[agent.location] = 'Clean'
            agent.performance += 10
        elif action == 'Left' and not super().some_things_at((agent.location[0]-1, agent.location[1]), tclass=Wall):
            agent.location = (agent.location[0]-1, agent.location[1])
            agent.performance -= 1
        elif action == 'Right' and not super().some_things_at((agent.location[0]+1, agent.location[1]), tclass=Wall):
            agent.location = (agent.location[0]+1, agent.location[1])
            agent.performance -= 1
        elif action == 'Up' and not super().some_things_at((agent.location[0], agent.location[1]+1), tclass=Wall):
            agent.location = (agent.location[0], agent.location[1]+1)
            agent.performance -= 1
        elif action == 'Down' and not super().some_things_at((agent.location[0], agent.location[1]-1), tclass=Wall):
            agent.location = (agent.location[0], agent.location[1]-1)
            agent.performance -= 1

    def default_location(self, thing):
        return random.choice(((0, 0), (0, 1), (0, 2)))


class EnvironmentB(EnvironmentA):
    def __init__(self):
        super(EnvironmentA, self).__init__()
        # Add walls around perimeter
        for x in range(-2, 3):
            self.add_thing(Wall(), (x, -1))
            self.add_thing(Wall(), (x, 3))

        for y in range(-1, 4):
            self.add_thing(Wall(), (-2, y))
            self.add_thing(Wall(), (2, y))
        self.add_thing(Wall(), (-1, 0))
        self.add_thing(Wall(), (1, 0))
        self.add_thing(Wall(), (-1, 2))
        self.add_thing(Wall(), (1, 2))

        # randomly add dirt at locations
        self.status = {
            (0, 0): random.choice(['Clean', 'Dirty']),
            (0, 1): random.choice(['Clean', 'Dirty']),
            (0, 2): random.choice(['Clean', 'Dirty']),
            (-1, 1): random.choice(['Clean', 'Dirty']),
            (1, 1): random.choice(['Clean', 'Dirty'])
        }

    def default_location(self, thing):
        return random.choice(((0, 0), (0, 1), (0, 2), (-1, 1), (1, 1)))


def run_simulation(agent, environment):
    """
    Receives a single agent and runs a simulation on a given environment.
    :param agent: class which generally describes the sensors, actuators. To customize, you can make your own.
    :param environment: class which defines the environment, percepts, effects of actions and updates performance.
    To customize, you can make your own.
    :return The performance measure of the agent after all steps completed.

    """
    environment.add_thing(agent)
    environment.run(steps=20)
    return agent.performance


print("%3s %10s %10s" % ('n', 'environment a', 'environment b'))
for n in range(20):
    print("%3d %10d %10d" % (n, run_simulation(MyRandomVacuumAgent(), EnvironmentA()),
                        run_simulation(MyRandomVacuumAgent(), EnvironmentB())))





