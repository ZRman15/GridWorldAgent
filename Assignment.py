class Gridworld:
    def __init__(self, width=8, height=8):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        
    def addWall(self, x, y):
        self.grid[y][x] = 1
        
    def isWall(self, x, y):
        return self.grid[y][x] == 1
    
    def addInterrupt(self, x, y):
        self.grid[y][x] = 2

    def isInterrupt(self, x, y):
        return self.grid[y][x] == 2
    

class Agent:
    def __init__(self, gridworld):
        self.gridworld = gridworld
        self.x = 0
        self.y = 0

    def move(self, dx, dy):
        if not self.gridworld.isWall(self.x + dx, self.y + dy):
            self.x += dx
            self.y += dy

    #adding an automatic move function
    def autoMove(self, dx, dy):
        if not self.gridworld.isWall(self.x + dx, self.y + dy):
            self.x += dx
            self.y += dy
        else:
            self.x += 0
            self.y += 0

            











class GridLabels:
    def __init__(self, gridworld):
        self.gridworld = gridworld
        self.labels = [['path' for _ in range(gridworld.width)] for _ in range(gridworld.height)]
        
    def setLabel(self, x, y, label):
        self.labels[y][x] = label
        
    def getLabel(self, x, y):
        return self.labels[y][x]


    
gw = Gridworld()

# adding walls at the edges
for x in range(gw.width):
    gw.addWall(x, 0)
    gw.addWall(x, gw.height-1)
for y in range(gw.height):
    gw.addWall(0, y)
    gw.addWall(gw.width-1, y)

# adding walls in the second row
gw.addWall(1, 1)
gw.addWall(2, 1)
gw.addWall(3, 1)
gw.addWall(4, 1)
gw.addWall(5, 1)
gw.addWall(6, 1)

# adding walls at (3,2), (4,2), (5,2)
gw.addWall(3, 2)
gw.addWall(4, 2)
gw.addWall(5, 2)

#adding walls at (3,3), (4,3), (5,3)
gw.addWall(3, 3)
gw.addWall(4, 3)
gw.addWall(5, 3)

#adding interrupt at (4,4)
gw.addInterrupt(4, 4)

#labelling the walls as 'wall'
gl = GridLabels(gw)
for x in range(gw.width):
    gl.setLabel(x, 0, 'wall')
    gl.setLabel(x, gw.height-1, 'wall')
for y in range(gw.height):
    gl.setLabel(0, y, 'wall')
    gl.setLabel(gw.width-1, y, 'wall')  

# fucntion to print the grid
def printGrid(gridworld, gridlabels): 
    for y in range(gridworld.height):
        for x in range(gridworld.width):
            if gridworld.isWall(x, y):
                print('W', end=' ')
            elif gridworld.isInterrupt(x, y):
                print('I', end=' ')
            else:
                print(gridlabels.getLabel(x, y), end=' ')
        print()

#adding a pretty print function so a wall is printed as a square and a path is printed as a dot and an interrupt is printed as a capital I

def printGridPretty(gridworld, gridlabels):
    for y in range(gridworld.height):
        for x in range(gridworld.width):
            if gridworld.isWall(x, y):
                print('■', end=' ')
            elif gridworld.isInterrupt(x, y):
                print('I', end=' ')
            else:
                print('·', end=' ')
        print()
printGridPretty(gw, None)

































