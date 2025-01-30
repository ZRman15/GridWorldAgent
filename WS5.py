import random

class GridWorld:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for i in range(cols)] for j in range(rows)]

class Agent:
    def __init__(self):
        self.x = None
        self.y = None

class Food:
    def __init__(self):
        self.x = None
        self.y = None

# Create the GridWorld
gridWorld = GridWorld(6,4)

# Create the Agent and position it in a random field
agent = Agent()
agent.x = random.randint(0, 5)
agent.y = random.randint(0, 3)

# Place the 10 food pieces randomly in the grid
for i in range(10):
    food = Food()
    food.x = random.randint(0, 5)
    food.y = random.randint(0, 3)

# Set a random field as the goal state
goal_x = random



class Goal:
    def __init__(self):
        self.x = None
        self.y = None

def print_grid(gridWorld, agent, food, goal):
    for i in range(gridWorld.rows):
        for j in range(gridWorld.cols):
            if i == agent.x and j == agent.y:
                print(' A ', end='')
            elif i == goal.x and j == goal.y:
                print(' G ', end='')
            elif (i == food[0].x and j == food[0].y) or (i == food[1].x and j == food[1].y) or (i == food[2].x and j == food[2].y) or (i == food[3].x and j == food[3].y) or (i == food[4].x and j == food[4].y) or (i == food[5].x and j == food[5].y) or (i == food[6].x and j == food[6].y) or (i == food[7].x and j == food[7].y) or (i == food[8].x and j == food[8].y) or (i == food[9].x and j == food[9].y):
                print(' F ', end='')
            else:
                print(' x ', end='')
        print()
    print()

# create a list containing the 10 food objects
food_list = []
for i in range(10):
    food = Food()
    food.x = random.randint(0, 5)
    food.y = random.randint(0, 3)
    food_list.append(food)

# Create the goal
goal = Goal()
goal.x = random.randint(0, 5)
goal.y = random.randint(0, 3)

# Make sure there are 10 food pieces
while len(food_list) < 10:
    food = Food()
    food.x = random.randint(0, 5)
    food.y = random.randint(0, 3)
    food_list.append(food)

print_grid(gridWorld, agent, food_list, goal)
