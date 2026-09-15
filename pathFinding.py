import grid
import math


RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
ORANGE = (255,165,0)



openList = []
gCost = []



def run():
    # Write your pathfinding algorithm here
    # grid.gridData[row][col] gives you the tile

    # Example:
    start = Node(5, 5)
    end = Node(10, 10)

    grid.text_tile(start, "S")
    grid.text_tile(end, "E")

    grid.color_tile(Node(13,13), (255, 0, 0))
    grid.text_tile(Node(13,13), "Test")

    neighbors = getNeighbors(start)
    openList.extend(neighbors)
    for n in openList:
        grid.text_tile(n, "N")
        grid.color_tile(n, ORANGE)

    neighbors = getNeighbors(start)
    #for i in range(4):
        #grid.color_tile(neighbors[i],(255,0,0))


    # YOUR ALGORITHM GOES HERE




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
        if(Node(x,y) != )
        neighbors.append(Node(x,y))
    return neighbors

#heuristic
def h(n1,n2,b):
    return math.sqrt((n2.x-n1.x)**2 + (n2.y-n1.y)**2)


class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y