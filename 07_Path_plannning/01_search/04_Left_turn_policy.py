# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.

movement = [[-1,  0],  # go up
           [0, -1],  # go left
           [1,  0],  # go down
           [0,  1]]  # go right
movement_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0]  # given in the form [row,col,direction]
# direction = 0: up
#             1: left
#             2: down
#             3: right
# if action is -1, e.g. 1 -> 0, it corresponds to a right turn
# action_name[-1] = right turn

goal = [2, 0]  # given in the form [row,col]

cost = [2, 1, 20]  # cost has 3 values, corresponding to making
# a right turn, no turn, and a left turn

"""
create 4 2D value grid to store cost four different 
    for any particular position, the vehicle can have four different orientations
        the vehicle can choose to maintain current heading (stay on the same grid)
        the vehicle can choose to change heading (jump to another grid)

for all cell <- cell_prev in grid:
    for all four orientations:

        if the cell_prev is the goal:
            assign value[orientation][goal] = 0
            assign policy[orientation][goal] = '*'
        
        elif the cell_prev is not an obstacle:
            for all possible action (i.e. forward, turn left, turn right):
                cell_new = cell_prev + movement
                if cell_new on grid and not an obstacle:
                    value_new = cell_new.cost + cost of this movement
                        ##cell_new is closer to the goal hence has a lower cost

                    if value_new < cell_prev.original_cost:
                        update value[orientation][prev_cell] = value_new
                        record policy[orientation][prev_cell] = movement

"""
def optimum_policy2D(grid, init, goal, cost):

    #first dimension for each orientation, i.e. forward, left, right, back
    
    value = [[[99 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[99 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[99 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[99 for row in range(len(grid[0]))] for col in range(len(grid))]]

    policy =[[[" " for row in range(len(grid[0]))] for col in range(len(grid))],
             [[" " for row in range(len(grid[0]))] for col in range(len(grid))],
             [[" " for row in range(len(grid[0]))] for col in range(len(grid))],
             [[" " for row in range(len(grid[0]))] for col in range(len(grid))]]
    
    policy2D = [[" " for row in range(len(grid[0]))] for col in range(len(grid))]
    
    change = True
    while change:
        change = False
        #go through all grid cells and calculate values
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for orientation in range(4):     #go through all first dimension of value

                    #if goal is found
                    if goal[0] == x and goal[1] == y:
                        #set the value to be 0 and policy to be '*'
                        #initialise for all four layers (orientations)
                        if value[orientation][x][y] > 0:
                            change = True
                            value[orientation][x][y] = 0
                            policy[orientation][x][y] = '*'
                        
                    elif grid[x][y] == 0:       #grid is not an obstacle

                        #calculate three ways to propagate value
                        for action_index in range(3):
                            o2 = (orientation + action[action_index]) % 4
                            x2 = x + movement[o2][0]
                            y2 = y + movement[o2][1]
                            

                            #if the movement is within the grid and grid is not an obstacle
                            if x2>=0 and x2<len(grid) and y2>=0 and y2<len(grid[0]) and grid[x2][y2] == 0:
                                v2 = value[o2][x2][y2] + cost[action_index]
                                if v2 < value[orientation][x][y]:
                                    value[orientation][x][y] = v2
                                    policy[orientation][x][y] = action_name[action_index]
                                    change = True
                    

    # run the policy, use the inital x position
    x = init[0]
    y = init[1]
    orientation = init[2]

    policy2D[x][y] = policy[orientation][x][y]          #copy the policy from three dimension to two dimension
    while policy[orientation][x][y] != '*':             #if not the goal
        if policy[orientation][x][y] in action_name:    #check if there is an action
            action_index = action_name.index(policy[orientation][x][y])
            o2 = (orientation + action[action_index]) % 4
        x = x + movement[o2][0]
        y = y + movement[o2][1]
        orientation = o2
        policy2D[x][y] = policy[orientation][x][y]


    return policy2D, value, policy


policy2D, value, policy = optimum_policy2D(grid, init, goal, cost)
for i in policy2D:
    print(i)
print(' ')

for i in range(len(value)):
    for j in value[i]:
        print(j)
    print(' ')
print(' ')

for i in range(len(policy)):
    for j in policy[i]:
        print(j)
    print(' ')
print(' ')
