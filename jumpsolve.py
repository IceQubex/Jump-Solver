#main function receiving data about the puzzle
def main():
    y = int(input("What is the length of the puzzle? "))
    x = int(input("What is the breadth of the puzzle? "))
    x1 = int(input("What is the x position of the start tile? "))
    y1 = int(input("What is the y position of the start tile? "))
    xG = int(input("What is the x position of the goal tile? "))
    yG = int(input("What is the y position of the goal tile? "))
    start = (x1,y1)
    goal = (xG,yG)
    board = list()
    for i in range(x):
        row = list()
        for j in range(y):
            temp = int(input("What is the value at the (" + str(i) + ", " + str(j) + ") tile? "))
            row.append(temp)
        board.append(row)
    astar_solution = jumpsolve_astar(start, goal, board)
    print("This is the A* Solution: ")
    print(astar_solution)
    bfs_solution = jumpsolve_bfs(start, goal, board)
    print("This is the BFS Solution:")
    print(bfs_solution)
    ids_solution = jumpsolve_ids(start, goal, board)
    print("This is the IDS Solution: ")
    print(ids_solution)

#astar search implementation
def jumpsolve_astar(start, goal, board):
    astar_queue_list = list()
    current = start
    current_path = list()
    current_path.append(start)
    while (1):
        print(current)
        if ((current[1]-board[current[0]][current[1]]) >= 0) and board[current[0]][current[1]] != 0:
            temp_option = (current[0],(current[1]-board[current[0]][current[1]]))
            current_path.append(temp_option)
            if goal in current_path:
                break
            temp_list = current_path[:]
            astar_queue_list.append(temp_list)
            current_path.pop()
        if ((current[0]-board[current[0]][current[1]]) >= 0) and board[current[0]][current[1]] != 0:
            temp_option = ((current[0]-board[current[0]][current[1]]),current[1])
            current_path.append(temp_option)
            if goal in current_path:
                break
            temp_list = current_path[:]
            astar_queue_list.append(temp_list)
            current_path.pop()
        if ((current[1]+board[current[0]][current[1]]) < len(board[0])) and board[current[0]][current[1]] != 0:
            temp_option = (current[0], (current[1] + board[current[0]][current[1]]))
            current_path.append(temp_option)
            if goal in current_path:
                break
            temp_list = current_path[:]
            astar_queue_list.append(temp_list)
            current_path.pop()
        if ((current[0]+board[current[0]][current[1]]) < len(board)) and board[current[0]][current[1]] != 0:
            temp_option = ((current[0]+board[current[0]][current[1]]),current[1])
            current_path.append(temp_option)
            if goal in current_path:
                break
            temp_list = current_path[:]
            astar_queue_list.append(temp_list)
            current_path.pop()
        print(astar_queue_list)
        options_rating = list()
        for i in range(len(astar_queue_list)):
            options_rating.append(f_n(astar_queue_list[i],goal,board))
        print(options_rating)
        min_rating = min(options_rating)
        choice = options_rating.index(min_rating)
        current_path = astar_queue_list.pop(choice)
        current = current_path[-1]
    return current_path

#heuristic function for astar search
def h_n(option, goal, board):
    return ((max(option[0],goal[0]) - min(option[0],goal[0])) + (max(option[1],goal[1]) - min(option[1],goal[1])))/(len(board))

#calculating path cost for astar search
def g_n(option_path):
    return (len(option_path)-1)

#calculating the sum of heuristic function and path cost
def f_n(option_path,goal,board):
    return g_n(option_path) + h_n(option_path[-1],goal,board)

#implementation of breadth-first search
def jumpsolve_bfs(start, goal, board):
    bfs_queue_list = list()
    current = start
    current_path = list()
    current_path.append(start)
    while (1):
        if ((current[1]-board[current[0]][current[1]]) >= 0) and board[current[0]][current[1]] != 0:
            temp_option = (current[0],(current[1]-board[current[0]][current[1]]))
            current_path.append(temp_option)
            if goal in current_path:
                break
            temp_list = current_path[:]
            bfs_queue_list.append(temp_list)
            current_path.pop()
        if ((current[0]-board[current[0]][current[1]]) >= 0) and board[current[0]][current[1]] != 0:
            temp_option = ((current[0]-board[current[0]][current[1]]),current[1])
            current_path.append(temp_option)
            if goal in current_path:
                break
            temp_list = current_path[:]
            bfs_queue_list.append(temp_list)
            current_path.pop()
        if ((current[1]+board[current[0]][current[1]]) < len(board[0])) and board[current[0]][current[1]] != 0:
            temp_option = (current[0], (current[1] + board[current[0]][current[1]]))
            current_path.append(temp_option)
            if goal in current_path:
                break
            temp_list = current_path[:]
            bfs_queue_list.append(temp_list)
            current_path.pop()
        if ((current[0]+board[current[0]][current[1]]) < len(board)) and board[current[0]][current[1]] != 0:
            temp_option = ((current[0]+board[current[0]][current[1]]),current[1])
            current_path.append(temp_option)
            if goal in current_path:
                break
            temp_list = current_path[:]
            bfs_queue_list.append(temp_list)
            current_path.pop()
        current_path = bfs_queue_list.pop(0)
        current = current_path[-1]
    return current_path

#implementation of iterative depth search, starting with limit = 1
def jumpsolve_ids(start, goal, board):
    ids_queue_list = list()
    current = start
    current_path = list()
    current_path.append(start)
    limit = 1
    while (1):
        if ((current[1] - board[current[0]][current[1]]) >= 0) and board[current[0]][current[1]] != 0:
            temp_option = (current[0], (current[1] - board[current[0]][current[1]]))
            current_path.append(temp_option)
            if goal in current_path:
                break
            temp_list = current_path[:]
            if len(temp_list)<=(limit+1):
                ids_queue_list.append(temp_list)
            current_path.pop()
        if ((current[0] - board[current[0]][current[1]]) >= 0) and board[current[0]][current[1]] != 0:
            temp_option = ((current[0] - board[current[0]][current[1]]), current[1])
            current_path.append(temp_option)
            if goal in current_path:
                break
            temp_list = current_path[:]
            if len(temp_list)<=(limit+1):
                ids_queue_list.append(temp_list)
            current_path.pop()
        if ((current[1] + board[current[0]][current[1]]) < len(board[0])) and board[current[0]][current[1]] != 0:
            temp_option = (current[0], (current[1] + board[current[0]][current[1]]))
            current_path.append(temp_option)
            if goal in current_path:
                break
            temp_list = current_path[:]
            if len(temp_list)<=(limit+1):
                ids_queue_list.append(temp_list)
            current_path.pop()
        if ((current[0] + board[current[0]][current[1]]) < len(board)) and board[current[0]][current[1]] != 0:
            temp_option = ((current[0] + board[current[0]][current[1]]), current[1])
            current_path.append(temp_option)
            if goal in current_path:
                break
            temp_list = current_path[:]
            if len(temp_list)<=(limit+1):
                ids_queue_list.append(temp_list)
            current_path.pop()
        if(len(ids_queue_list)==0):
            limit+=1
            current = start
            current_path = []
            current_path.append(start)
        else:
            current_path = ids_queue_list.pop()
            current = current_path[-1]
    return current_path

#calling the main function to activate program
main()
