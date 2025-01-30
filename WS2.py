# Grid.printGrid() to print and intitialize the grid
# Grid.moveObstacle("E") to move East with the leaf as the obstacle
# Grid.moveObstacle("W") to move West with the leaf as the obstacle
# Grid.moveObstacle("N") to move North with the leaf as the obstacle
# Grid.moveObstacle("S") to move South with the leaf as the obstacle

# Grid.movePassable("E") to move East and pass over the leaf
# Grid.movePassable("W") to move West and pass over the leaf
# Grid.movePassable("N") to move North and pass over the leaf
# Grid.movePassable("S") to move South and pass over the leaf


# Agent class with self postion and (x,y) as parameters


class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getPosition(self):
        return (self.x, self.y)

    def setPosition(self,x,y):
        self.x = x
        self.y = y

class Leaf:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getPosition(self):
        return (self.x, self.y)
    
    def setPosition(self,x,y):
        self.x = x
        self.y = y

class World:
    def __init__(self):
        self.agent = Agent(2,2)
        self.leaf = Leaf(2,3)
        self.possible_coordinates = [
        (0,0) ,
        (0,1) ,
        (0,2) ,
        (0,3) ,
        (0,4) ,
        (1,0) ,
        (1,1) ,
        (1,2) ,
        (1,3) ,
        (1,4) ,
        (2,0) ,
        (2,1) ,
        (2,2) ,
        (2,3) ,
        (2,4) ,
        (3,0) ,
        (3,1) ,
        (3,2) ,
        (3,3) ,
        (3,4) ,
        (4,0) ,
        (4,1) ,
        (4,2) ,
        (4,3) ,
        (4,4) ,
        ]
        self.coordinate_labels = dict.fromkeys(self.possible_coordinates , '.')

        self.coordinate_labels[(self.agent.x,self.agent.y)] = "m"
        self.coordinate_labels[(self.leaf.x,self.leaf.y)] = "l"

    #prints the grid

    def printGrid(self): 
        current_count = 0 
        for coordinate in self.coordinate_labels.keys():
            if current_count == 4:
                print(self.coordinate_labels[coordinate])
                current_count = 0
                continue
            
            print(self.coordinate_labels[coordinate] , end = "     ")
            current_count = current_count + 1

    #checks if co-ordinate is on the grid

    def isInGrid(self,location):
        if location in self.possible_coordinates:
            return True 
        else:
            return False


    # Assigns the value of the the next co-ordinate over to new_pos and increments/decrement the value of the column/row one more time to
    # determine what the new value of the agent would be
    # this is again followed by a check to see if the co-ordinate exists on the grid

    def movePassable(self, direction):
        if direction == "N":
            curr_pos = self.agent.getPosition()
            new_pos = (curr_pos[0]-1,curr_pos[1])
            if new_pos == self.leaf.getPosition():
                new_pos = (new_pos[0]-1,new_pos[1])
            if self.isInGrid(new_pos):
                self.coordinate_labels[(self.agent.x,self.agent.y)] = "."
                self.agent.setPosition(new_pos[0],new_pos[1])
                self.coordinate_labels[(self.agent.x,self.agent.y)] = "m"
            else:
                return
        elif direction == "S":
            curr_pos = self.agent.getPosition()
            new_pos = (curr_pos[0]+1,curr_pos[1])
            if new_pos == self.leaf.getPosition():
                new_pos = (new_pos[0]+1,new_pos[1])
            if self.isInGrid(new_pos):
                self.coordinate_labels[(self.agent.x,self.agent.y)] = "."
                self.agent.setPosition(new_pos[0],new_pos[1])
                self.coordinate_labels[(self.agent.x,self.agent.y)] = "m"
            else:
                return
        elif direction == "E":
            curr_pos = self.agent.getPosition()
            new_pos = (curr_pos[0],curr_pos[1]+1)
            if new_pos == self.leaf.getPosition():
                new_pos = (new_pos[0],new_pos[1]+1)
            if self.isInGrid(new_pos):
                self.coordinate_labels[(self.agent.x,self.agent.y)] = "."
                self.agent.setPosition(new_pos[0],new_pos[1])
                self.coordinate_labels[(self.agent.x,self.agent.y)] = "m"
            else:
                return
        elif direction == "W":
            curr_pos = self.agent.getPosition()
            new_pos = (curr_pos[0],curr_pos[1]-1)
            if new_pos == self.leaf.getPosition():
                new_pos = (new_pos[0],new_pos[1]-1)
            if self.isInGrid(new_pos):
                self.coordinate_labels[(self.agent.x,self.agent.y)] = "."
                self.agent.setPosition(new_pos[0],new_pos[1])
                self.coordinate_labels[(self.agent.x,self.agent.y)] = "m"
            else:
                return
            
    # This works similarly to movePassable() except it checks if the new position of the agent is the same as the current postion
    # of the leaf. If new_pos_leaf = new_pos and the new position of the leaf is not on the grid, it just changes the value of the leaf
    # without the bouncy border implementation and the leaf is no longer on the grid.
    # If the new_pos_leaf is a valid on the grid, is uses the isInGrid() check to see if this is true and just moves the leaf one cell over


    def moveObstacle(self, direction):
        if direction == "N":
            curr_pos = self.agent.getPosition()
            new_pos = (curr_pos[0]-1,curr_pos[1])
            new_pos_leaf = self.leaf.getPosition()
            if new_pos == self.leaf.getPosition():
                new_pos = (new_pos[0],new_pos[1])
                new_pos_leaf = (new_pos[0]-1,new_pos[1])
            if self.isInGrid(new_pos):
                self.coordinate_labels[(self.agent.x,self.agent.y)] = "."
                self.agent.setPosition(new_pos[0],new_pos[1])
                self.leaf.setPosition(new_pos_leaf[0],new_pos_leaf[1])
                self.coordinate_labels[(self.agent.x,self.agent.y)] = "m"
                self.coordinate_labels[(self.leaf.x,self.leaf.y)] = "l"
            else:
                return
        elif direction == "S":
            curr_pos = self.agent.getPosition()
            new_pos = (curr_pos[0]+1,curr_pos[1])
            new_pos_leaf = self.leaf.getPosition()
            if new_pos == self.leaf.getPosition():
                new_pos = (new_pos[0],new_pos[1])
                new_pos_leaf = (new_pos[0]+1,new_pos[1])
            if self.isInGrid(new_pos):
                self.coordinate_labels[(self.agent.x,self.agent.y)] = "."
                self.agent.setPosition(new_pos[0],new_pos[1])
                self.leaf.setPosition(new_pos_leaf[0],new_pos_leaf[1])
                self.coordinate_labels[(self.agent.x,self.agent.y)] = "m"
                self.coordinate_labels[(self.leaf.x,self.leaf.y)] = "l"
            else:
                return
        elif direction == "E":
            curr_pos = self.agent.getPosition()
            new_pos = (curr_pos[0],curr_pos[1]+1)
            new_pos_leaf = self.leaf.getPosition()
            if new_pos == self.leaf.getPosition():
                new_pos = (new_pos[0],new_pos[1])
                new_pos_leaf = (new_pos[0],new_pos[1]+1)
            if self.isInGrid(new_pos):
                self.coordinate_labels[(self.agent.x,self.agent.y)] = "."
                self.agent.setPosition(new_pos[0],new_pos[1])
                self.leaf.setPosition(new_pos_leaf[0],new_pos_leaf[1])
                self.coordinate_labels[(self.agent.x,self.agent.y)] = "m"
                self.coordinate_labels[(self.leaf.x,self.leaf.y)] = "l"
            else:
                return
        elif direction == "W":
            curr_pos = self.agent.getPosition()
            new_pos = (curr_pos[0],curr_pos[1]-1)
            new_pos_leaf = self.leaf.getPosition()
            if new_pos == self.leaf.getPosition():
                new_pos = (new_pos[0],new_pos[1])
                new_pos_leaf = (new_pos[0],new_pos[1]-1)
            if self.isInGrid(new_pos):
                self.coordinate_labels[(self.agent.x,self.agent.y)] = "."
                self.agent.setPosition(new_pos[0],new_pos[1])
                self.leaf.setPosition(new_pos_leaf[0],new_pos_leaf[1])
                self.coordinate_labels[(self.agent.x,self.agent.y)] = "m"
                self.coordinate_labels[(self.leaf.x,self.leaf.y)] = "l"
            else:
                return





Grid = World()
Grid.printGrid()

# Grid.moveObstacle("E")

# print()
# Grid.printGrid()

# Grid.moveObstacle("E")

# print()
# Grid.printGrid()

# Grid.moveObstacle("S")
# Grid.moveObstacle("E")
# Grid.moveObstacle("N")
# Grid.moveObstacle("N")
# Grid.moveObstacle("N")






