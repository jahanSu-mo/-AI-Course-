import heapq

def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic[start], 0, start, [start]))  # (f_score, g_score, current_node, path)

    closed_set = set()

    while open_list:
        f_score, g_score, current, path = heapq.heappop(open_list)

        if current == goal:
            print("\nGoal found!")
            return path

        closed_set.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor not in closed_set:
                new_g_score = g_score + cost
                new_f_score = new_g_score + heuristic[neighbor]
                heapq.heappush(open_list, (new_f_score, new_g_score, neighbor, path + [neighbor]))

    return None

def main():
    graph = {}
    heuristic = {}

    n = int(input("Enter number of nodes: "))
    print("Enter node names:")

    nodes = []
    for _ in range(n):
        node = input().strip()
        nodes.append(node)

    e = int(input("Enter number of edges: "))
    print("Enter edges in format 'u v cost' (e.g., A B 4):")

    for _ in range(e):
        u, v, cost = input().split()
        cost = int(cost)
        if u not in graph:
            graph[u] = []
        graph[u].append((v, cost))
        

    print("Enter heuristic values for each node (estimated cost to goal):")
    for node in nodes:
        h = int(input(f"Heuristic value for {node}: "))
        heuristic[node] = h

    start = input("Enter start node: ").strip()
    goal = input("Enter goal node: ").strip()

    path = a_star(graph, start, goal, heuristic)

    if path:
        print("Final Path:", " -> ".join(path))
    else:
        print("Goal not reachable.")

if __name__ == "__main__":
    main()




# import heapq  # Import the heapq module for priority queue operations

# def a_star(graph, start, goal, heuristic):
    
#     # Initialize the open list (priority queue) with the start node
#     # Elements in open_list are tuples: (f_score, g_score, current_node, path)
#     open_list = []
#     # Push the start node with f_score = g_score + heuristic, g_score = 0, and initial path
#     heapq.heappush(open_list, (0 + heuristic[start], 0, start, [start]))

#     closed_set = set()  # Set to keep track of already explored nodes

#     while open_list:  # While there are nodes to explore
#         # Pop the node with the lowest f_score from the priority queue
#         f_score, g_score, current, path = heapq.heappop(open_list)

#         if current == goal:  # If we've reached the goal
#             print("\nGoal found!")
#             return path  # Return the path taken

#         closed_set.add(current)  # Add current node to explored set

#         # Explore all neighbors of the current node
#         for neighbor, cost in graph.get(current, []):
#             if neighbor not in closed_set:  # Only consider unexplored neighbors
#                 new_g_score = g_score + cost  # Calculate new path cost
#                 new_f_score = new_g_score + heuristic[neighbor]  # f(n) = g(n) + h(n)
#                 # Add neighbor to the open list with updated scores and path
#                 heapq.heappush(open_list, (new_f_score, new_g_score, neighbor, path + [neighbor]))

#     return None  # Return None if goal is not reachable

# def main():
#     """Main function to handle user input and execute A* search."""
#     graph = {}  # Dictionary to store the graph structure
#     heuristic = {}  # Dictionary to store heuristic values

#     # Get number of nodes from user
#     n = int(input("Enter number of nodes: "))
#     print("Enter node names:")
    
#     nodes = []  # List to store all node names
#     for _ in range(n):
#         node = input().strip()  # Get node name from user
#         nodes.append(node)

#     # Get number of edges from user
#     e = int(input("Enter number of edges: "))
#     print("Enter edges in format 'u v cost' (e.g., A B 4):")

#     for _ in range(e):
#         u, v, cost = input().split()  # Get edge information
#         cost = int(cost)  # Convert cost to integer
#         if u not in graph:
#             graph[u] = []  # Initialize adjacency list for node u if not exists
#         graph[u].append((v, cost))  # Add edge to the graph
#         # Note: This implementation assumes a directed graph. For undirected, 
#         # you would need to add the reverse edge as well.

#     # Get heuristic values from user
#     print("Enter heuristic values for each node (estimated cost to goal):")
#     for node in nodes:
#         h = int(input(f"Heuristic value for {node}: "))  # Get heuristic value
#         heuristic[node] = h  # Store in heuristic dictionary

#     # Get start and goal nodes from user
#     start = input("Enter start node: ").strip()
#     goal = input("Enter goal node: ").strip()

#     # Run A* algorithm
#     path = a_star(graph, start, goal, heuristic)

#     # Display results
#     if path:
#         print("Final Path:", " -> ".join(path))
#     else:
#         print("Goal not reachable.")

# if __name__ == "__main__":
#     main()  # Execute the program