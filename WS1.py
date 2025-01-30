##moveAgentWestBouncy() to move West
##moveNorthAroundTheWorld() to move Up
##printGrid() to print grid
## Have fun <3





possible_coordinates = [
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


coordinate_labels = dict.fromkeys(possible_coordinates , '.')

coordinate_labels[(2,2)] = "X"

def printGrid(): 
    current_count = 0 
    for coordinate in coordinate_labels.keys():
        if current_count == 4:
            print(coordinate_labels[coordinate])
            current_count = 0
            continue
        
        print(coordinate_labels[coordinate] , end = "     ")
        current_count = current_count + 1

def location():
    return [k for k, v in coordinate_labels.items() if v == 'X'][0]

def moveAgentWest():
    currLoc = location()
    newLoc = (currLoc[0],currLoc[1]-1)

    if isInGrid(newLoc):
        coordinate_labels[currLoc] = "."
        coordinate_labels[newLoc] = "X" 
    else:
        return
    
def moveNorthAroundTheWorld():
    currLoc = location()
    newLoc = (currLoc[0] -1 ,currLoc[1])

    if isInGrid(newLoc):
        coordinate_labels[currLoc] = "."
        coordinate_labels[newLoc] = "X" 
    else:
        coordinate_labels[currLoc] = "."
        coordinate_labels[(currLoc[0] + 4, currLoc[1])] = "X"
        

def isInGrid(location):
    if location in possible_coordinates:
        return True
    else:
        False

#Test
# # coordinate_labels
# printGrid()

# moveAgentWest()
# moveAgentWest()
# moveAgentWest()

# moveUp()
# moveUp()
# moveUp()
# moveUp()


# # coordinate_labels


# # %%
# printGrid()
