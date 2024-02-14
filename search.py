# Latif Ahmed
# Project 1
# Python version 3.12.2
import random
from queue import Queue
from queue import PriorityQueue
from collections import deque
import time

def copy_maze(maze):
    new_maze = [[0 for i in range(collumns)] for j in range(rows)]
    for j in range(rows):
        for i in range(collumns):
            new_maze[j][i] = maze[j][i]
    return new_maze

def print_maze(maze):
    length = len(str(rows - 1))
    top_and_bottom_row = " " * length
    for i in range(collumns):
        top_and_bottom_row = top_and_bottom_row + " " + str(i)
    print(top_and_bottom_row)
    for j in range(rows):
        row = " " * (length - len(str(j))) + str(j)
        for i in range(collumns):
            row = row + " " + maze[j][i] + " " * (len(str(i)) - 1)
        row = row + " " + str(j) 
        print(row)
    print(top_and_bottom_row)
            
def generate_maze():
    start_set = False
    goal_set = False
     
    global start_row
    global start_col
    global goal_row
    global goal_col
    
    goal_row = 0
    goal_col = 0
    
    # in percent, so 4 = 4%
    chance_of_setting_start_or_goal = 4
    
    maze = []
    for j in range(rows):
        row = []
        for i in range(collumns):
            # start of setting start and goal state
            if (not start_set and not goal_set):
                state_to_set = 'S' if random.randint(0,1) == 0 else 'G'
                if random.randint(0, 99) < chance_of_setting_start_or_goal:
                    row.append(state_to_set)
                    if (state_to_set == 'S'):
                        start_row = j
                        start_col = i
                        start_set = True
                    else:
                        goal_row = j
                        goal_col = i
                        goal_set = True
                    continue
            elif (not start_set):
                if (abs(j - goal_row) + abs(i - goal_col) < 10):
                    # in tenths of a percent, so chance_of_setting_start = 5 -> .5%
                    chance_of_setting_start = 5
                else:
                    chance_of_setting_start = 10
                if (random.randint(0,999) < chance_of_setting_start):
                    row.append('S')
                    start_row = j
                    start_col = i
                    start_set = True
                    continue
            elif (not goal_set):
                if (abs(j - start_row) + abs(i - start_col) < 10):
                    # in tenths of a percent, so chance_of_setting_start = 5 -> .5%
                    chance_of_setting_start = 5
                else:
                    chance_of_setting_start = 10
                if (random.randint(0,999) < chance_of_setting_start):
                    row.append('G')
                    goal_row = j
                    goal_col = i
                    goal_set = True
                    continue
            # end of setting start and goal state
            if (random.randint(0,99) < density):
                row.append('X')
            else:
                row.append('.')
        maze.append(row)
    # retry to assign start and/or goal state
    while (not start_set or not goal_set):
        for j in range(rows):
            if (start_set and goal_set):
                break
            for i in range(collumns):
                if (not start_set and not goal_set):
                    state_to_set = 'S' if random.randint(0,1) == 0 else 'G'
                    if random.randint(0, 99) < chance_of_setting_start_or_goal:
                        maze[j][i] = state_to_set
                        if (state_to_set == 'S'):
                            start_row = j
                            start_col = i
                            start_set = True
                        else:
                            goal_row = j
                            goal_col = i
                            goal_set = True
                elif (not start_set and maze[j][i] != 'G'):
                    if (abs(j - goal_row) + abs(i - goal_col) < 10):
                        # in tenths of a percent, so chance_of_setting_start = 5 -> .5%
                        chance_of_setting_start = 5
                    else:
                        chance_of_setting_start = 10
                    if (random.randint(0,999) < chance_of_setting_start):
                        maze[j][i] = 'S'
                        start_row = j
                        start_col = i
                        start_set = True
                        break  
                elif (not goal_set and maze[j][i] != 'S'):
                    if (abs(j - start_row) + abs(i - start_col) < 10):
                        # in tenths of a percent, so chance_of_setting_start = 5 -> .5%
                        chance_of_setting_start = 5
                    else:
                        chance_of_setting_start = 10
                    if (random.randint(0,999) < chance_of_setting_start):
                        maze[j][i] = 'G'
                        goal_row = j
                        goal_col = i
                        goal_set = True
                        break
    return maze
     
def dfs_search(maze):
    print("Depth first search on maze")
    
    # to calculate Execution Time
    start_time = time.time()
    user_time = 0
    temp_time = 0
    
    stack = deque()
    stack.append((start_row, start_col))
    
    path_exists = False
    
    print("Start state. Nodes expanded: 0")
    print_maze(maze)
    
    # used to link child with parent
    parent_dictionary = {}
    nodes_expanded_count = 0
    while len(stack) != 0:
        # state[0] is row, state[1] is col
        state = stack.pop()
        
        if maze[state[0]][state[1]] == 'o':
            continue
        
        if maze[state[0]][state[1]] == '.':
            maze[state[0]][state[1]] = 'o'
        
        temp_time = time.time()
        input("Press enter to continue.")
        user_time += time.time() - temp_time
        nodes_expanded_count = nodes_expanded_count + 1 
        print("Node expanded -> (" + str(state[0]) + "," + str(state[1]) + ")")
        print("Total Nodes expanded: " + str(nodes_expanded_count))
        print_maze(maze)
            
        
        if maze[state[0]][state[1]] == 'G':
            temp_time = time.time()
            input("Solution found. Press enter to continue.")
            user_time += time.time() - temp_time
            path_exists = True
            solution = []
            solution.append((state[0],state[1]))
            state = (state[0],state[1])
            while (state != (start_row, start_col)):
                state = parent_dictionary[state]
                solution.append(state)
            solution.reverse()
            
            print("Start state -> (" + str(start_row) + "," + str(start_col) + ")")
            print("Solution Path Length Count: 0")
            print_maze(maze)
            
            for i in range(len(solution) - 1):
                temp_time = time.time()
                input("Press enter to continue.")
                user_time += time.time() - temp_time
                
                if (i == len(solution) - 2):
                    print("Goal reached -> (" + str(solution[i+1][0]) + "," + str(solution[i+1][1]) + ")")
                    print("Total Nodes Expanded: " + str(nodes_expanded_count))
                    print("Total Solution Path Length: " + str(len(solution) - 1))
                else:
                    maze[solution[i+1][0]][solution[i+1][1]] = '|' if (solution[i][0] != solution[i+1][0]) else '-'
                    print("Node -> (" + str(solution[i+1][0]) + "," + str(solution[i+1][1]) + ")")
                    print("Solution Path Length Count: " + str(i+1))
                print_maze(maze)
            print("Solution: ", end = "")
            print(solution)
            break
        
        # add left
        if (state[1] - 1) >= 0 and (maze[state[0]][state[1] - 1] == '.' or maze[state[0]][state[1] - 1] == 'G') :
            stack.append((state[0], state[1] - 1))
            parent_dictionary[(state[0], state[1] - 1)] = (state[0], state[1])
        
        # add down
        if (state[0] + 1) < rows and (maze[state[0] + 1][state[1]] == '.' or maze[state[0] + 1][state[1]] == 'G'):
            stack.append((state[0] + 1, state[1]))
            parent_dictionary[(state[0] + 1, state[1])] = (state[0], state[1])

        # add right
        if (state[1] + 1) < collumns and (maze[state[0]][state[1] + 1] == '.' or maze[state[0]][state[1] + 1] == 'G'):
            stack.append((state[0], state[1] + 1))
            parent_dictionary[(state[0], state[1] + 1)] = (state[0], state[1])
 
        # add up
        if (state[0] - 1) >= 0 and (maze[state[0] - 1][state[1]] == '.' or maze[state[0] - 1][state[1]] == 'G'):
            stack.append((state[0] - 1, state[1]))
            parent_dictionary[(state[0] - 1, state[1])] = (state[0], state[1])
    
    if (not path_exists):
        print("No path was found.")
    print("Execution Time: " + str(time.time() - start_time - user_time) + " seconds")
    print("Depth first search completed.")


def bfs_search(maze):
    print("Breadth first search on maze")
    
    # to calculate Execution Time
    start_time = time.time()
    user_time = 0
    temp_time = 0
    
    queue = Queue(maxsize=0)
    queue.put((start_row,start_col))

    path_exists = False
    
    print("Start state. Nodes expanded: 0")
    print_maze(maze)
    
    # used to link child with parent
    parent_dictionary = {}
    nodes_expanded_count = 0
    while queue.qsize() != 0:
        # state[0] is row, state[1] is col
        state = queue.get()
        
        if maze[state[0]][state[1]] == 'o':
            continue
        
        if maze[state[0]][state[1]] == '.':
            maze[state[0]][state[1]] = 'o'
            
        temp_time = time.time()
        input("Press enter to continue.")
        user_time += time.time() - temp_time
        
        nodes_expanded_count = nodes_expanded_count + 1 
        print("Node expanded -> (" + str(state[0]) + "," + str(state[1]) + ")")
        print("Total Nodes expanded: " + str(nodes_expanded_count))
        print_maze(maze)
            
        
        if maze[state[0]][state[1]] == 'G':
            temp_time = time.time()
            input("Solution found. Press enter to continue.")
            user_time += time.time() - temp_time
            
            path_exists = True
            solution = []
            solution.append((state[0],state[1]))
            state = (state[0],state[1])
            while (state != (start_row, start_col)):
                state = parent_dictionary[state]
                solution.append(state)
            solution.reverse()
            
            print("Start state -> (" + str(start_row) + "," + str(start_col) + ")")
            print("Solution Path Length Count: 0")
            print_maze(maze)
            
            for i in range(len(solution) - 1):
                temp_time = time.time()
                input("Press enter to continue.")
                user_time += time.time() - temp_time
                
                if (i == len(solution) - 2):
                    print("Goal reached -> (" + str(solution[i+1][0]) + "," + str(solution[i+1][1]) + ")")
                    print("Total Nodes Expanded: " + str(nodes_expanded_count))
                    print("Total Solution Path Length: " + str(len(solution) - 1))
                else:
                    maze[solution[i+1][0]][solution[i+1][1]] = '|' if (solution[i][0] != solution[i+1][0]) else '-'
                    print("Node -> (" + str(solution[i+1][0]) + "," + str(solution[i+1][1]) + ")")
                    print("Solution Path Length Count: " + str(i+1))
                print_maze(maze)
            print("Solution: ", end = "")
            print(solution)
            break

        # add up
        if (state[0] - 1, state[1]) not in parent_dictionary and state[0] - 1 >= 0 and (maze[state[0] - 1][state[1]] == '.' or maze[state[0] - 1][state[1]] == 'G'):
            queue.put((state[0] - 1, state[1]))
            parent_dictionary[(state[0] - 1, state[1])] = (state[0], state[1])

        # add right
        if (state[0], state[1] + 1) not in parent_dictionary and state[1] + 1 < collumns and (maze[state[0]][state[1] + 1] == '.' or maze[state[0]][state[1] + 1] == 'G'):
            queue.put((state[0], state[1] + 1))
            parent_dictionary[(state[0], state[1] + 1)] = (state[0], state[1])
        
        # add down
        if (state[0] + 1, state[1]) not in parent_dictionary and state[0] + 1 < rows and (maze[state[0] + 1][state[1]] == '.' or maze[state[0] + 1][state[1]] == 'G'):
            queue.put((state[0] + 1, state[1]))
            parent_dictionary[(state[0] + 1, state[1])] = (state[0], state[1])

        # add left
        if (state[0], state[1] - 1) not in parent_dictionary and state[1] - 1 >= 0 and (maze[state[0]][state[1] - 1] == '.' or maze[state[0]][state[1] - 1] == 'G') :
            queue.put((state[0], state[1] - 1))
            parent_dictionary[(state[0], state[1] - 1)] = (state[0], state[1])
 
    if (not path_exists):
        print("No path was found.")
    print("Execution Time: " + str(time.time() - start_time - user_time) + " seconds")
    print("Breadth first search completed.")
    
def a_star_search(maze):
    print("A* search on maze.")
    
    # to calculate Execution Time
    start_time = time.time()
    user_time = 0
    temp_time = 0
    
    priority_queue = PriorityQueue()
    
    # priority number is g(n) + h(n) where g(n) is number of nodes to reach a given node 
    # and h(n) is the manhatten distance to the goal
    # data is node coordinates and g(n) in the form ((row,collumn),g(n))
    priority_queue.put((0 + abs(start_row - goal_row) + abs(start_col - goal_col) , ((start_row, start_col), 0)))
    path_exists = False
    
    print("Start state. Nodes expanded: 0")
    print_maze(maze)
    
    # used to link child with parent
    parent_dictionary = {}
    nodes_expanded_count = 0
    while priority_queue.qsize() != 0:
        # state[0] is estimate total cost of solution, state[1] is data
        # state[1][0] is (row, collumn) tuple where state[1][0][0] is row and state[1][0][1] is collumn
        # state[1][1] is g(n), the steps to reach 
        state = priority_queue.get()
        possible_length = state[0]
        node = (state[1][0][0],state[1][0][1])
        steps = state[1][1]

        if maze[node[0]][node[1]] == 'o':
            continue
        
        if maze[node[0]][node[1]] == '.':
            maze[node[0]][node[1]] = 'o'
            
        temp_time = time.time()
        input("Press enter to continue.")
        user_time += time.time() - temp_time
        
        nodes_expanded_count = nodes_expanded_count + 1 
        print("Node expanded -> (" + str(node[0]) + "," + str(node[1]) + ")")
        print("Possible Solution Length: " + str(possible_length))
        print("Steps from start: " + str(steps))
        print("Total Nodes expanded: " + str(nodes_expanded_count))
        print_maze(maze)
            
        
        if maze[node[0]][node[1]] == 'G':
            temp_time = time.time()
            input("Solution found. Press enter to continue.")
            user_time += time.time() - temp_time
            
            path_exists = True
            solution = []
            solution.append((node[0],node[1]))
            state = (node[0],node[1])
            while (state != (start_row, start_col)):
                state = parent_dictionary[state]
                solution.append(state)
            solution.reverse()
            
            print("Start state -> (" + str(start_row) + "," + str(start_col) + ")")
            print("Solution Path Length Count: 0")
            print_maze(maze)
            
            for i in range(len(solution) - 1):
                temp_time = time.time()
                input("Press enter to continue.")
                user_time += time.time() - temp_time
                
                if (i == len(solution) - 2):
                    print("Goal reached -> (" + str(solution[i+1][0]) + "," + str(solution[i+1][1]) + ")")
                    print("Total Nodes Expanded: " + str(nodes_expanded_count))
                    print("Total Solution Path Length: " + str(len(solution) - 1))
                else:
                    maze[solution[i+1][0]][solution[i+1][1]] = '|' if (solution[i][0] != solution[i+1][0]) else '-'
                    print("Node -> (" + str(solution[i+1][0]) + "," + str(solution[i+1][1]) + ")")
                    print("Solution Path Length Count: " + str(i+1))
                print_maze(maze)
            print("Solution: ", end = "")
            print(solution)
            break

        # add up
        if (node[0] - 1, node[1]) not in parent_dictionary and node[0] - 1 >= 0 and (maze[node[0] - 1][node[1]] == '.' or maze[node[0] - 1][node[1]] == 'G'):
            estimate_length = steps + 1 + abs(node[0] - 1 - goal_row) + abs(node[1] - goal_col)
            priority_queue.put((estimate_length, ((node[0] - 1, node[1]) , steps + 1)))
            parent_dictionary[(node[0] - 1, node[1])] = (node[0], node[1])

        # add right
        if (node[0], node[1] + 1) not in parent_dictionary and node[1] + 1 < collumns and (maze[node[0]][node[1] + 1] == '.' or maze[node[0]][node[1] + 1] == 'G'):
            estimate_length = steps + 1 + abs(node[0] - goal_row) + abs(node[1] + 1 - goal_col)
            priority_queue.put((estimate_length, ((node[0], node[1] + 1) , steps + 1)))
            parent_dictionary[(node[0], node[1] + 1)] = (node[0], node[1])
        
        # add down
        if (node[0] + 1, node[1]) not in parent_dictionary and node[0] + 1 < rows and (maze[node[0] + 1][node[1]] == '.' or maze[node[0] + 1][node[1]] == 'G'):
            estimate_length = steps + 1 + abs(node[0] + 1 - goal_row) + abs(node[1] - goal_col)
            priority_queue.put((estimate_length, ((node[0] + 1, node[1]) , steps + 1)))
            parent_dictionary[(node[0] + 1, node[1])] = (node[0], node[1])

        # add left
        if (node[0], node[1] - 1) not in parent_dictionary and node[1] - 1 >= 0 and (maze[node[0]][node[1] - 1] == '.' or maze[node[0]][node[1] - 1] == 'G') :
            estimate_length = steps + 1 + abs(node[0] - goal_row) + abs(node[1] - 1 - goal_col)
            priority_queue.put((estimate_length, ((node[0] , node[1] - 1) , steps + 1)))
            parent_dictionary[(node[0], node[1] - 1)] = (node[0], node[1])
 
    if (not path_exists):
        print("No path was found.")
    print("Execution Time: " + str(time.time() - start_time - user_time) + " seconds")
    print("A* search completed.*")


print("Maze generation.")
collumns = int(input("Enter number of collumns: "))
rows = int(input("Enter number of rows: "))
density = int(input("Enter obstacle density (as a whole number percent): "))

maze = generate_maze()
print_maze(maze)

selection = input("Accept maze (Enter yes or no): ")
while (selection != "yes"):
    if (selection == "no"):
        print("New maze")
        maze = generate_maze()
        print_maze(maze)
        selection = input("Accept maze (Enter yes or no): ")
    else:
        print("Invalid input")
        print_maze(maze)
        print("Accept maze (Enter yes or no): ")

dfs_search(copy_maze(maze))

input("Press enter to start bfs search.")
bfs_search(copy_maze(maze))
        
input("Press enter to start a* search.")
a_star_search(copy_maze(maze))
