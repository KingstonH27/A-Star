import grid
import math


class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y


RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
ORANGE = (255,165,0)



openList = []
gCost = []


start = Node(5, 5)
end = Node(10, 10)

def init():
    openList.append(start)


def run():
    # Write your pathfinding algorithm here
    # grid.gridData[row][col] gives you the tile

    # Example:


    grid.text_tile(start, "S")
    grid.text_tile(end, "E")

    grid.color_tile(Node(13,13), (255, 0, 0))
    grid.text_tile(Node(13,13), "Test")


    neighbors = getNeighbors(openList[0])
    openList.extend(neighbors)
    for n in openList:
        grid.set(n,2)
        openList.remove(n)



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
        if grid.check(Node(x,y)) != 1:
            neighbors.append(Node(x,y))
    return neighbors

#heuristic
def h(n1,n2,b):
    return math.sqrt((n2.x-n1.x)**2 + (n2.y-n1.y)**2)




