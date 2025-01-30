##
## Modifying Felix's solution for WS5
##
import random
import time

"""
Our field class contains if it has food, or a goal.
Adjacency here is no longer the north, west, ...  as this is not needed here.
We do not care about directions in this scenario.
"""
class Field:

    def __init__(self, food, goal, name):
        self.food = food
        self.id = name
        self.goal = goal
        self.adjacent = []

    def containsFood(self):
        return self.food

    def isGoal(self):
        return self.goal

    def getNeighbours(self):
        return self.adjacent

    def removeFood(self):
        self.food = False

"""
Our agent with decision making as described in task 4,
sensing for food, if it is adjacent or on the current field,
as well as goal state.
And a counter for consumed food (if the world granted it)
"""

class Agent:
    foodCounter = 0
    energy = 4
    action_counter = [0, 0, 0, 0, 0]

    def consumeFood(self):
        self.foodCounter += 1
        self.energy += 5

    def seeFood(self, field):
        if field.containsFood():
            return field
        return False

    def senseFood(self, field):
        for neighbour in field.getNeighbours():
            if neighbour.containsFood():
                return neighbour
        return False

    def senseGoal(self, field):
        return field.isGoal()


    def decisionMaking(self, field):
        if not self.senseGoal(field):  # First check if we want to stay here
            if not self.seeFood(field):  # Secondly, check if we can eat
                # This "if" uses a java option like feature of if in Python, utilising if Object evaluates to True
                if self.senseFood(field):  # Thirdly, check if we see something to eat
                    targetField = self.senseFood(field)
                    self.action_counter[0] += 1
                    
                else:  # Fourthly move to an adjacent
                    targetField = random.choice(field.getNeighbours())
                    self.action_counter[1] += 1
                    self.energy -= 1
                return Decision(targetField, "move")
            else:
                self.action_counter[2] += 1
                return Decision(field, "eat")
        else:
            self.action_counter[3] += 1
            Decision(field, "stay")
   
   
"""
Simply here to communicate between the agent and world 
"""
class Decision:
    def __init__(self, field, decision):
        self.field = field
        self.decision = decision


"""
Our World. Holds and agent and its current field as well as managing the movement.
Asks the agent for its decision and facilitates it (or not)
"""
class OneAgentWorld:
    def __init__(self, agentField, agent):
        self.agentField = agentField
        self.agent = agent

    def arrivedAtGoal(self):
        return self.agentField.isGoal()

    def runOneStepDeterministic(self):
        decision = self.agent.decisionMaking(self.agentField)
        if decision.decision == "eat":
            print("The agent eats")
            self.agent.consumeFood()
            print("energy= ", self.agent.energy)
            self.agentField.removeFood()
        elif decision.decision == "move":
            self.agentField = decision.field
        elif decision.decision == "stay":
            print("Agent is in the goal")    
    
    def runOneStepNondeterministic(self):
        decision = self.agent.decisionMaking(self.agentField)
        if decision.decision == "eat":
            print("The agent eats")
            self.agent.consumeFood()
            self.agentField.removeFood()
        elif decision.decision == "move":
            if random.random() < 0.5:
                self.agentField = decision.field
                print("The world moves the agent")
            else:
                print("Movement denied")
        elif decision.decision == "stay":
            print("Agent is in the goal")
   
   
"""
Adapted grid creation as we now have a 4x6 world instead of 5x5
"""
def createGrid():
    listOfFields = []
    for i in range(24):
        listOfFields.append(Field(False, False, i))

    for i in range(24):
        # Starting with all west connections
        # All nodes 0,6,12,18 do not have a neighbour to the west
        if (i % 6) != 0:  # If not 0,6,12,18
            listOfFields[i].adjacent.append(listOfFields[i - 1])  # Connecting a node to the node left/west of it
    
        # Continuing with all east connections
        # This excludes all nodes on the eastern border: 5,11,17,23
        if ((i + 1) % 6) != 0:
            listOfFields[i].adjacent.append(listOfFields[i + 1])
        # Continuing with the north, the first 6 (0-5) do not have a north
        if i > 5:
            listOfFields[i].adjacent.append(listOfFields[i - 6])
        # Continuing with the nodes south
        if i < 18:
            listOfFields[i].adjacent.append(listOfFields[i + 6])

    return listOfFields

def selectGoalAndFood(listOfFields):
    for i in range(10):
        random.choice(listOfFields).food = True

    goal = random.choice(listOfFields)
    print("The goal is in field", goal.id)
    goal.goal = True


################################
## Adding the Food and Goal
################################
def setupWorld():
    world1 = createGrid()
    selectGoalAndFood(world1)
    return world1

grid = setupWorld()

# Starting our world with the field the agent is in. This could be randomised.
world = OneAgentWorld(grid[12], Agent())
while not world.arrivedAtGoal():
    world.runOneStepDeterministic()
    print("The Agent is in Grid No. = ",world.agentField.id)
    print("Agent Energy = ", world.agent.energy) #Prints counter for agent energy at the start of every action
    print("--------------")
    time.sleep(2)
print("Goal Reached in a deterministic world")
print("The agent consumed ", world.agent.foodCounter, " food") 
print("energy= ", world.agent.energy) #Prints agent energy at the end of run
print("action_counter= ", world.agent.action_counter) #Prints the counter for actions taken during run




##while not world.arrivedAtGoal():
##    world.runOneStepNondeterministic()
##    print(world.agentField.id)
##    time.sleep(1)
##print("Goal Reached in a deterministic world")
#
