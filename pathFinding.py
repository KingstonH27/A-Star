import grid
import math





RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = 0
        self.h = 0
        self.connection = None

    def setG(self, g):
        self.g = g


    def setH(self, h):
        self.h = h


    def setConnection(self, other):
        self.connection = other

    @property
    def f(self):
        return self.g + self.h

    def g(self):
        return self.g
    def h(self):
        return self.h

width = 0
height = 0

start = Node(5, 5)
end = Node(10, 10)

toSearch = []
processed = []

def init(w, h):
    global width, height
    width, height = w, h
    toSearch.append(start)
    grid.text_tile(start, "s")
    grid.text_tile(end, "e")




#Algorithm
def run():
    if len(toSearch) > 0:
        focus = toSearch[0]
        neighbors = getNeighbors(focus)
        for n in neighbors:
            n.setConnection(focus)
            n.setG(focus.g + 1)
            n.setH(focus.h + h(focus, n))
            s = n.g #(str(n.g)+"-"+str(n.h))
            grid.text_tile(n,s)

        toSearch.append(bestF(neighbors))
        grid.set(focus, 2)
        toSearch.remove(focus)





def bestF(neighbors):
    best = neighbors[0].f
    node = neighbors[0]
    for n in neighbors:
        if n.f < best:
            best = n.f
            node = n
    return node







directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]


def getNeighbors(focusNode):
    neighbors = []

    for neighbor in range(4):
        x = focusNode.x + directions[neighbor][0]
        y = focusNode.y + directions[neighbor][1]

        # Out of bounds
        if x < 0 or x >= width or y < 0 or y >= height:
            continue

        # Wall
        if grid.check(Node(x, y)) == 1:
            continue

        if grid.check(Node(x, y)) == 2:
            continue

        node = Node(x, y)
        neighbors.append(node)




    return neighbors


# Heuristic
def h(n1, n2):
    return math.sqrt(
        (n2.x - n1.x) ** 2 +
        (n2.y - n1.y) ** 2
    )