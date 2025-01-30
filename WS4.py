class Node:
    def __init__(self , name):
        self.name = str(name)
        self.adjacent = []

    def addAdjacentNode(self , neighbour, weight):
        self.adjacent.append([neighbour, weight])
        
    def getAdjacentNodes(self): 
        return self.adjacent

v1 = Node("v1")
v2 = Node("v2")
v3 = Node("v3")
v4 = Node("v4")
v5 = Node("v5")
v6 = Node("v6")

v1.addAdjacentNode(v2, 1)
v1.addAdjacentNode(v4, 3)
v2.addAdjacentNode(v3, 2)
v2.addAdjacentNode(v6, 6)
v2.addAdjacentNode(v5, 7)
v3.addAdjacentNode(v6, 4)
v4.addAdjacentNode(v1, 3)
v5.addAdjacentNode(v2, 7)
v6.addAdjacentNode(v2, 6)
v6.addAdjacentNode(v3, 4)


print(v1.getAdjacentNodes()) 
print(v2.getAdjacentNodes()) 
print(v3.getAdjacentNodes()) 
print(v4.getAdjacentNodes()) 
print(v5.getAdjacentNodes()) 
print(v6.getAdjacentNodes()) 



