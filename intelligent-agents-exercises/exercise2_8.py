# ================================================= Exercise 2.8 =======================================================

# Already implemented code from the online repository will be used. The following code imports all from agents.py
import httpimport
with httpimport.github_repo('aimacode', 'aima-python', ['utils', 'agents'], 'master'):
    from agents import *


class CleanlinessPMEnv(TrivialVacuumEnvironment):
    """
    Implements the environment referenced in the exercise and uses performance measure 1(described in ProjectReport.pdf)
    """

    def step(self):
        if not self.is_done():
            # It is assumed that only one vacuum is present in the environment. Said vacuum is
            # awarded one performance point for each clean square at each time step.
            vacuum = self.agents[0]
            for square in self.status.values():
                if square == 'Clean':
                    vacuum.performance += 1
            super().step()

    def execute_action(self, agent, action):
        """ Executes the appropriate action. No performance points are added nor subtracted when performing action"""
        if action == 'Right':
            agent.location = loc_B
        elif action == 'Left':
            agent.location = loc_A
        elif action == 'Suck':
            self.status[agent.location] = 'Clean'


class CleanlinessAndMovementPMEnv(CleanlinessPMEnv):
    """
    Implements the environment referenced in the exercise and uses performance measure 1(described in ProjectReport.pdf)
    """

    def execute_action(self, agent, action):
        """ Executes the appropriate action. In this case, a performance point is deducted for each movement."""
        if action == 'Right':
            agent.location = loc_B
            agent.performance -= 1
        elif action == 'Left':
            agent.location = loc_A
            agent.performance -= 1
        elif action == 'Suck':
            self.status[agent.location] = 'Clean'


def SimpleAgentActionProgram(action_map):
    """
    My own implementation where the agent acts only based on the current percept (which is mapped to an action in
    the action_map parameter).
    """

    def program(percept):
        return action_map.get(percept)

    return program


def SimpleAgent():
    """
    My own implementation in which I map the possible percepts the agent could receive at a given time (Ignoring past
    percepts).
    :return: An Agent object with its appropriate agent program.
    """
    action_map = {
        (loc_A, 'Clean'): 'Right',
        (loc_A, 'Dirty'): 'Suck',
        (loc_B, 'Clean'): 'Left',
        (loc_B, 'Dirty'): 'Suck'
    }
    return Agent(SimpleAgentActionProgram(action_map))


def run_simulation(agent, environment):
    """
    Receives a single agent and runs a simulation on a given environment.
    :param agent: class which generally describes the sensors, actuators. To customize, you can make your own.
    :param environment: class which defines the environment, percepts, effects of actions and updates performance.
    To customize, you can make your own.
    :return The performance measure of the agent after all steps completed.

    """
    environment.add_thing(agent)
    environment.run()
    return agent.performance


# Runs the simulation 10 times and prints a table with the performance results with each approach.
# See ProjectReport.pdf for explanation of cases.
print("%3s %10s %10s %10s" % ("n", "Case 1", "Case 2", "Case 3"))
for n in range(10):
    print("%3d %10d %10d %10d" % (n, run_simulation(SimpleAgent(), CleanlinessPMEnv()),
                             run_simulation(SimpleAgent(), CleanlinessAndMovementPMEnv()),
                             run_simulation(TableDrivenVacuumAgent(), CleanlinessAndMovementPMEnv())))
