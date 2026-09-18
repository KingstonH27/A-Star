Chatgpt was used for assistance:

https://chatgpt.com/share/6aac8a67-6394-83ea-bfa1-39d02fb2ba0f

https://chatgpt.com/share/6aa97ead-7fac-83ea-906d-ab4d3b7776a7


This repo is a visual representation of the A* path finding algorithm. It is programmed in python and uses pygame for graphics.
This project is for 4 directional A* and can be used with Manhattan or Euclidean heuristics.

A* works by calculating the total path distance between a node and the start node, g; and from the node to the end node, h.
It starts at the start node and checks the f value of all neighbors. The f value is the sum of the g and h values.
It then adds those neighbors to a list and the next node to check is the one from that list with the lowest f value to prioritize the most promising path.
Once the end is reached, it retraces its steps back to the start based on the connections each node saves to its previous node.

Optimization:
 - Originally I had done the previous node's g value + h(focus,n) to find the new nodes g value, but calculating the distance is unnecessary since each movement cost is 1 in 4 directional movement. I instead just add 1 to the previous node's g value.
 - The Manhattan is optimal for this setup because it uses a 4 directional grid and diagonal motion is not allowed. This means no square roots or squares need to be calculated which reduces calculations and therefore increases speed.
 - 
Files:
- main.py - Calls all other files, includes UI
- pathFinding.py - A* Algorithm
- controls.py - Global settings
- grid.py - Sets up the grid

To use:
- Run the **main.py** file
- On the grid, S is the start and the E is the end. The end switches to F once the end has been found.

- Click(or click and drag) on the grid to create walls, A* will go around walls

- The UI contains buttons for
  - Start - Auto steps the algorithm
  - Step - Manually move the algorithm one step forward in the process
  - Manhattan/Euclidean - Changes the heuristic type
  - Paths - Shows paths to each explored node when enabled and only the shortest otherwise
  - Restart - restarts the program to rerun the algorithm
- The UI contains labels for
  - Step - How many steps into the algorithm
  - No Path - Reads true if the end is unreachable
  - Path Length - How long the path is
