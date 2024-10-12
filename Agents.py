from  game import Agent
from game import Directions
import random

class DumbAgent(Agent) :
    def getAction(self, state):
        print("Location: ", state.getPacmanPosition())
        print("Actions available: ", state.getLegalPacmanActions())
        if Directions.EAST in state.getLegalPacmanActions():
            print("Going East.")
            return Directions.EAST
        else:
            print("Stopping.")
            return Directions.STOP
class RandomAgent(Agent):
    def getAction(self, state):     
        legal_actions = state.getLegalPacmanActions()
        for a in state.getLegalActions(self.index):  random_action = random.choice(legal_actions)
        return random_action
class BetterRandomAgent(Agent):
    def getAction(self, state):
        legal_actions = state.getLegalPacmanActions()
        legal_actions.remove(Directions.STOP)  # Remove STOP from legal actions
        random_action = random.choice(legal_actions)
        return random_action
class ReflexAgent(Agent):
    def getAction(self, state):
        legal_actions = state.getLegalPacmanActions()
        for action in legal_actions:
            next_pacman_position = state.generatePacmanSuccessor(action)
            next_pacman_pos = next_pacman_position.getPacmanState().getPosition()
            if state.hasFood(next_pacman_pos[0], next_pacman_pos[1]):
                return action
            else: 
                legal_actions = state.getLegalPacmanActions()
                legal_actions.remove(Directions.STOP)  # Remove STOP from legal actions
                random_action = random.choice(legal_actions)
                return random_action
            
        
        







