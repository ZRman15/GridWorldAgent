import random

directionLabels = ["west", "east", "north", "south"] #adding a list of directions
goalLabels = ["goal"] #adding a list of goals

#MiniController for the agent to detect the label in the grid and move agent according to the label
class MiniController:
    def __init__(self, agent):
        self.agent = agent
        self.world = [["goal", "west", "north", "east", "east"],
                ["west", "north", "west", "east", "north"],
                ["west", "north", "north", "east", "east"],
                ["west", "south", "south", "east", "east"],
                ["west", "south", "south", "east", "east"]]

    def run(self):
        prettyPrint()
        while True:
            label = self.agent.perceiveLabel(self.world)
            if label in goalLabels:
                print(">> Reached goal!")
                break
            elif label in directionLabels:
                moveAgent(label)
                prettyPrint()


    def reset(self):
        self.agent.setPosition([2, 2])

#MiniController that moves the agent randomly
class MiniControllerRandom:
    def __init__(self, agent):
        self.agent = agent
        self.world = [["goal", "west", "north", "east", "east"],
                ["west", "north", "west", "east", "north"],
                ["west", "north", "north", "east", "east"],
                ["west", "south", "south", "east", "east"],
                ["west", "south", "south", "east", "east"]]


    def run(self):
        prettyPrint()
        while True:
            label = self.agent.perceiveLabel(self.world)
            if label in goalLabels:
                print(">> Reached goal!")

                break
            elif label != "G":
                direction = random.choice(directionLabels)
                moveAgent(direction)

                prettyPrint()
        self.reset()

    def reset(self):
        self.agent.setPosition([2, 2])



#Agent class to intitialize the agent
class Agent:

    def __init__(self, position):
        self.position = position

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def perceiveLabel(self, world): #adding a fucntion to perceive the label
        x, y = self.position
        return world[x][y]
#the code below is the same as the code provided by the teacher in the last worksheet solution
#in only modified the prettyPrint function to print the world with directions and added a function to print the random world
class Leaf:

    def __init__(self, position):
        self.position = position

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position



agent = Agent([2, 2])


leaf = Leaf([2, 3])
listOfThings = [agent, leaf]



#Function prints out the grid 
def prettyPrint():
    worldcopy = [["goal", "west", "north", "east", "east"],
                ["west", "north", "west", "east", "north"],
                ["west", "north", "north", "east", "east"],
                ["west", "south", "south", "east", "east"],
                ["west", "south", "south", "east", "east"]]

    for thing in listOfThings:
        if outOfBounds(thing.getPosition()):
            continue
        x = thing.getPosition()[0]
        y = thing.getPosition()[1]
        field = worldcopy[x][y]
        if type(thing) is Leaf:
            symbol = "L"
        elif type(thing) is Agent:
            symbol = "A"

        if field != "0":
            field = field + symbol
        if field == "0":
            field = symbol
        worldcopy[x][y] = field
    for row in worldcopy:
        print(*row)
    print("--------------------")


##Helper function to detect out of bounds 
##This will be used for movement of different objects 
def outOfBounds(position):
    if min(position) == -1:
        return True
    if max(position) == 5:
        return True
    return False


    # Helper function to calculate a move
    # Takes an object and a change array and computes how the new position would look like.
def calculateNewPosition(thing, change):
    return [x1 + x2 for x1, x2 in zip(thing.getPosition(), change)]


    #Translation function from labels to relative coordinates
def moveAgent(direction):
    if direction == "west":
        passableLeaf([0, -1])
    if direction == "east":
        passableLeaf([0, 1])
    if direction == "north":
        passableLeaf([-1, 0])
    if direction == "south":
        passableLeaf([1, 0])



def passableLeaf(change):
    wouldBeNewPosition = calculateNewPosition(agent, change)
    if outOfBounds(wouldBeNewPosition):
        return
    agent.setPosition(wouldBeNewPosition)


#Function for Agent pushing the leaf


def moveAgentpushing(direction):
    if direction == "west":
        pushLeaf([0, -1])
    if direction == "east":
        pushLeaf([0, 1])
    if direction == "north":
        pushLeaf([-1, 0])
    if direction == "south":
        pushLeaf([1, 0])



def pushLeaf(change):
    wouldBeNewPosition = calculateNewPosition(agent, change)
    if outOfBounds(wouldBeNewPosition):
        return
    if wouldBeNewPosition == leaf.getPosition():
        newLeafPosition = calculateNewPosition(leaf, change)
        leaf.setPosition(newLeafPosition)
    agent.setPosition(wouldBeNewPosition)

 #resetting the agent to the starting position

controller = MiniControllerRandom(agent)
controller.run()
controller.reset()
