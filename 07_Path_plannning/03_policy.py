# ----------
# User Instructions:
#
# Write a function optimum_policy that returns
# a grid which shows the optimum policy for robot
# motion. This means there should be an optimum
# direction associated with each navigable cell from
# which the goal can be reached.
#
# Unnavigable cells as well as cells from which
# the goal cannot be reached should have a string
# containing a single space (' '), as shown in the
# previous video. The goal cell should have '*'.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']

"""
create a value grid same size as actual grid, initialise with big number
create a policy grid to display optimal action
create a change switch to indicate if there is anything cell that has been changed

for all cells in grid:
    check if it is the goal:
        set value[goal cell]  = 0
        set policy[goal cell] = '*'
    elif the cell <- cell_prev is not an obstacle:
        for all movements:
            if cell_new is within the grid and not an obstacle:
                value_new = cell_new.cost + cost of this movement
                    ##cell_new is closer to the goal hence has a lower cost
                    
                if value_new < cell_prev.original_cost:
                    update value[prev_cell] = value_new
                    record policy[prev_cell] = movement

effectively this first find the goal cell and set its value to 0
    for all other cells:
        with initial value of 99, with movement, new cost will be 100
        not updated
then it will update around goal cell:
    #because all other cell with value of 99 will not be updated
    for a_cell next to the goal cell, movement to goal cell:
        new_value = goal_cell.value + cost

        because new_value < a_cell.original_value:
            value[a_cell] = new_value
            policy[a_cell] = movement_to_goal_cell
"""
def optimum_policy(grid, goal, cost):
    # 99 for unreachable place
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    # map tp display the optimum path
    policy = [[" " for row in range(len(grid[0]))] for col in range(len(grid))]

    # a switch for the program, only runs if it is true
    # when there is nothing to be changed, it will be set to false
    change = True

    while change:
        # During running, it will be set to false, it will only be true if something changed
        change = False

        #iterate over all grid cells, call it cell_prev
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                #check if it is the goal cell
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        policy[x][y] = '*'          #set the goal cell to be star
                        change = True

                elif grid[x][y] == 0:               #if the cell_prev is not an obstacle
                    for a in range(len(delta)):     #try all possble movements
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]

                        #if the movement is within the grid and grid is not an obstacle
                        if x2>=0 and x2<len(grid) and y2>=0 and y2<len(grid[0]) and grid[x2][y2]==0:
                            v2 = value[x2][y2] + cost

                            #if this value is better, assign it to the cell_prev
                            if v2 < value[x][y]:
                                change = True       #something has been changed
                                value[x][y] = v2    #update the new value to cell_prev
                                #memorize the action, display on the cell_prev
                                policy[x][y] = delta_name[a] 
                                
    return value, policy

value, policy = optimum_policy(grid, goal, cost)
for i in value:
    print (i)
for i in policy:
    print(i)
