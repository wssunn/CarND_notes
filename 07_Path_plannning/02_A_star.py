grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

# to turn off a* and use grid search
# heuristic = [[0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right
delta_name = ['^', '<', 'v', '>']

"""
closed = list of all nodes; 0 unvisited, 1 visited
    initialise start node as visited (set to 1)
open = list of nodes that can be expanded
expand


while not found and possible to find:
    if len(open) == 0:
        not possible to find; algorithm fail
    else:
        pick node with smallest g_value
        if node == goal:
            found
        else:
            for all possible movements:
                if moved_node in grid:
                    if moved_node is not visited:
                        new_g = old_node.g + cost
                        heuristic = moved_node.heuristic
                        new_f = new_g + heuristic
                        open.append([moved_node, new_f])
                        closed[moved_node] = 1; visited

"""
def search(grid, init, goal, cost, heuristic):

    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[init[0]][init[1]] = 1

    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0
    h = heuristic[x][y]
    f = g + h

    open = [[f, g, h, x, y]]

    found = False  # flag that is set when search is complete
    resign = False  # flag set if we can't find expand
    count = 0

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return "Fail"
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[3]
            y = next[4]
            g = next[1]
            expand[x][y] = count
            count += 1

            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            h2 = heuristic[x2][y2]
                            f2 = g2 + h2
                            open.append([f2, g2, h2, x2, y2])
                            closed[x2][y2] = 1

    return expand


expand = search(grid, init, goal, cost, heuristic)
for line in expand:
    print(line)
