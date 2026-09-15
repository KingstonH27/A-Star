import grid
import math

def run():
    # Write your pathfinding algorithm here
    # grid.gridData[row][col] gives you the tile

    # Example:
    start = Node(0, 0)
    end = Node(10, 10)

    neighbors = getNeighbors(start)
    #for i in range(4):
        #grid.color_tile(neighbors[i],(255,0,0))


    # YOUR ALGORITHM GOES HERE

openList = []
gCost = []


directions = [
    (0,1),
    (1,0),
    (0,-1),
    (-1,0)
]
def getNeighbors(focusNode):
    neighbors = []
    for neighbor in range(4):
        x = focusNode.x + directions[neighbor][0]
        y = focusNode.y + directions[neighbor][1]
        openList.append(Node(x,y))
    return neighbors

#heuristic
def h(n1,n2,b):
    return math.sqrt((n2.x-n1.x)**2 + (n2.y-n1.y)**2)


class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y