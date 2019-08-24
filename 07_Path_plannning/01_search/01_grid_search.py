
# Modify the the search function so that it returns
# a shortest path as follows:
#
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]

"""
closed = list of all nodes; 0 unvisited, 1 visited
open = list of nodes that can be expanded

while not found and possible to find:
    if len(open) == 0:
        not possible
    else:
        pick node with smallest g_value
        if node == goal:
            found
        else:
            for all possible movements:
                if moved_node in grid:
                    if moved_node is not visited:
                        new_g = node + 1
                        open.append([moved_node, new_g])
                        closed[moved_node] = 1; visited

"""
grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 1, 1, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

        #first is vertical movement
        #second is horizonal movement
delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']

class Point():
    def __init__(self, g_value=0, x=0, y=0, prev_movement=0):
        self.g_value = g_value
        self.x = x
        self.y = y
        self.prev_movement = prev_movement

def search(grid, init, goal, cost):
    #store all the nodes, 0 if not visited, 1 if visited
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    #create a grid with Point objects for storing purpose
    history = [[Point for row in range(len(grid[0]))] for col in range(len(grid))]
    #create a grid to display path
    expand = [[" " for row in range(len(grid[0]))] for col in range(len(grid))]
    #efficiency, count number of expansions
    efficiency = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]

    # set the initial position to visited
    closed[init[0]][init[1]] = 1
    # set the goal to be "*" and set the obstacle to be 'X  
    expand[goal[0]][goal[1]] = "*"
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                expand[i][j] = 'X'

    x = init[0]         #initial x position
    y = init[1]         #initial y position
    g = 0               #initial g value
    open = [[g, x, y]]  #nodes that can be expanded
    history[x][y] = Point(g, x, y, -1) #set initial point
    counter = 1         #for efficiency

    found = False  # flag that is set when search is complete
    resign = False  # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0: #no nodes to expand
            resign = True
            return 'fail'
        else:
            open.sort()         #smallest g_value last
            open.reverse()      #smallest g_value first
            next = open.pop()   #get the node with smallest g_value 
            x = next[1]
            y = next[2]
            g = next[0]

            if x == goal[0] and y == goal[1]:
                found = True    
            else:
                #try all possible movements
                for i in range(len(delta)):     #delta: all possible movements
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]

                    #if the node is inside the grid
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        #if the node is not visited
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost       #cost = 1, defined above
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1  #set the node to be visited
                            history[x2][y2] = Point(g2, x2, y2, i) #record the history
                            expand[x2][y2] = '0'  #show on map that this point is visited
                            efficiency[x2][y2] = counter; counter += 1
    
    #go backwards, start from the final point
    #use history to retrive previous motion, go backwards
    #retrive again
    a_point = history[goal[0]][goal[1]]
    while a_point.prev_movement != -1: #-1 defined previously to indicate the start point
        movement = delta[a_point.prev_movement]
        prev_x = a_point.x - movement[0]
        prev_y = a_point.y - movement[1]
        expand[prev_x][prev_y] = delta_name[a_point.prev_movement]
        a_point = history[prev_x][prev_y]


    return expand, efficiency  # make sure you return the shortest path


find_path, efficiency = search(grid, init, goal, cost)
print('path')
for line in find_path:
    print(line)
print('\ncost')
for line in efficiency:
    print(line)
