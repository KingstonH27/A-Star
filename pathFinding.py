import grid
import math
import controls



# --- Color presets ---
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)



# --- Classes ---
class Path:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

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

    # The f value is the sum of the g and h
    @property
    def f(self):
        return self.g + self.h

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# --- Variables ---
heuristic = "Manhattan"
start = Node(2, 2)
end = Node(controls.width-3, controls.height-3)
toSearch = []
processed = []

directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]


# --- Initialization ---
def init(w, h):
    global width, height
    width, height = w, h
    toSearch.append(start)
    grid.text_tile(start, "s")
    grid.text_tile(end, "e")




# --- Main Algorithm ---
def run():
    if len(toSearch) == 0:
        controls.pathNotFound = True
        controls.started = False
        return

    if controls.started == False:
        return

    # Sets the node with the best F value as the current node to prioritize more likely optimal paths
    focus = bestF(toSearch)

    # Checks if the end has been reached
    if focus == end:
        controls.started = False
        grid.text_tile(focus, "f")
        reconstructPath(focus)

        if controls.showAllPaths:
            for n in processed:
                reconstructPath(n)
            return

    # Gets neighbors of the current node, these are the options of where the path can go
    neighbors = getNeighbors(focus)

    # For each neighbor calculate the heuristic(h), g, and f values. If the node is not already in toSearch aka the queue of nodes to check, then its added to toSearch. The connection to the previous node is saved so that the path can be retraced if it is the best.
    for n in neighbors:
        #The g value is the path distance from a node to the start
        #Originally I had done the previous node's g value + h(focus,n), but calculating the distance is unnecessary since each movement cost is 1 in 4 directional movement.
        newG = focus.g + 1


        if n not in toSearch:
            n.setConnection(focus)
            n.setG(newG)
            n.setH(h(n, end))
            toSearch.append(n)
            grid.set(n, 3)


        else:
            # If a better path is found(better g value) through already explored nodes, they will be updated
            existing = toSearch[toSearch.index(n)]

            if newG < existing.g:
                existing.setConnection(focus)

                existing.setG(newG)

    grid.set(focus, 2)
    toSearch.remove(focus)
    processed.append(focus)


# --- Retraces path back to the start from n node ---
def reconstructPath(n):
    while n != start:
        grid.color_tile(n, GREEN)
        n2 = n
        n = n.connection
        controls.pathLength += 1
        grid.drawPaths(Path(n,n2))




# --- BestF returns the nodes with the lowest F value ---
def bestF(neighbors):
    best = neighbors[0].f
    node = neighbors[0]
    for n in neighbors:
        if n.f < best:
            best = n.f
            node = n
    return node



# --- Returns neighboring nodes(4 directions) around a focus node ---
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

        if Node(x, y) in processed:
            continue

        node = Node(x, y)
        neighbors.append(node)
    return neighbors


# --- Calculates the heuristic, Manhattan or Euclidean ---
# This project works on a 4 directional grid(no diagonal movement) and so Manhattan is more optimized because it can avoid calculating diagonals since the path traveled will be the same length as Manhattan movement
# The heuristic(h) is the distance from one node to the end
def h(n1, n2):
    if heuristic == "Manhattan":
        return abs(n2.x - n1.x) + abs(n2.y - n1.y)

    return math.sqrt((n2.x - n1.x)**2 + (n2.y - n1.y)**2)