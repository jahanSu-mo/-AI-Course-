import heapq  

def best_first_search(graph, heuristics, start, goal):
    visited = set()  
    priority_queue = []  
    heapq.heappush(priority_queue, (heuristics[start], start))  

    while priority_queue:  
        _, current = heapq.heappop(priority_queue)  

        print(f"Visiting Node {current}") 

        if current == goal: 
            print(f"Goal node {goal} found!")
            return True  

        if current not in visited:  
            visited.add(current)  

            for neighbor, cost in graph.get(current, []):  
                if neighbor not in visited:  
                    heapq.heappush(priority_queue, (heuristics[neighbor], neighbor))  

    print("Goal node not found.")  
    return False  

def main():
    graph = {}  
    heuristics = {}  

    n = int(input("Enter number of nodes: "))
    print("Enter node names (as integers, e.g., 0, 1, 2):")
    nodes = [int(input(f"Node {i + 1}: ")) for i in range(n)]  
    # Input number of edges
    e = int(input("Enter number of edges: "))
    print("Enter edges in format 'u v cost' (e.g., 0 1 4):")
    for _ in range(e):
        u, v, cost = map(int, input().split())  
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, cost)) 
        graph[v].append((u, cost))  

    print("Enter heuristic values for each node:")
    for node in nodes:
        heuristics[node] = int(input(f"Heuristic for node {node}: "))  # Read heuristic

    start = int(input("Enter start node: "))
    goal = int(input("Enter goal node: "))

    print("\nGraph structure:")
    for node in graph:
        print(f"{node} --> {graph[node]}")

    print("\nHeuristics:")
    for node in heuristics:
        print(f"Node {node}: {heuristics[node]}")

    print(f"\nRunning Best-First Search from {start} to {goal}:\n")

    # Run the best-first search
    result = best_first_search(graph, heuristics, start, goal)
    if not result:
        print("Path to goal was not found.")

if __name__ == "__main__":
    main()



# # Import the heapq module to use a priority queue (min-heap)
# import heapq  

# # Best-First Search (Greedy) algorithm implementation
# def best_first_search(graph, heuristics, start, goal):
#     # visited: A set to keep track of already visited nodes
#     visited = set()  
#     # priority_queue: A min-heap to prioritize nodes with the lowest heuristic value
#     priority_queue = []  
#     # Push the start node into the priority queue with its heuristic value
#     heapq.heappush(priority_queue, (heuristics[start], start))  

#     # Continue until the priority queue is empty
#     while priority_queue:  
#         # Pop the node with the smallest heuristic value
#         _, current = heapq.heappop(priority_queue)  

#         # Print the current node being visited (for debugging/tracking)
#         print(f"Visiting Node {current}") 

#         # If the current node is the goal, return success
#         if current == goal: 
#             print(f"Goal node {goal} found!")
#             return True  

#         # If the node hasn't been visited yet, process it
#         if current not in visited:  
#             visited.add(current)  # Mark as visited

#             # Explore all neighbors of the current node
#             for neighbor, cost in graph.get(current, []):  
#                 # If the neighbor hasn't been visited, add it to the priority queue
#                 if neighbor not in visited:  
#                     heapq.heappush(priority_queue, (heuristics[neighbor], neighbor))  

#     # If the queue is empty and the goal wasn't found, return failure
#     print("Goal node not found.")  
#     return False  

# # Main function to handle user input and execute Best-First Search
# def main():
#     # graph: Adjacency list representation of the graph (dictionary)
#     graph = {}  
#     # heuristics: Dictionary storing heuristic values for each node
#     heuristics = {}  

#     # Input the number of nodes
#     n = int(input("Enter number of nodes: "))
#     # Input node names (as integers)
#     print("Enter node names (as integers, e.g., 0, 1, 2):")
#     nodes = [int(input(f"Node {i + 1}: ")) for i in range(n)]  

#     # Input the number of edges
#     e = int(input("Enter number of edges: "))
#     # Input edges in the format 'u v cost' (undirected graph)
#     print("Enter edges in format 'u v cost' (e.g., 0 1 4):")
#     for _ in range(e):
#         u, v, cost = map(int, input().split())  
#         # Initialize adjacency lists for nodes if they don't exist
#         if u not in graph:
#             graph[u] = []
#         if v not in graph:
#             graph[v] = []
#         # Add edges (undirected, so both directions are stored)
#         graph[u].append((v, cost)) 
#         graph[v].append((u, cost))  

#     # Input heuristic values for each node
#     print("Enter heuristic values for each node:")
#     for node in nodes:
#         heuristics[node] = int(input(f"Heuristic for node {node}: "))  

#     # Input start and goal nodes
#     start = int(input("Enter start node: "))
#     goal = int(input("Enter goal node: "))

#     # Print the graph structure for verification
#     print("\nGraph structure:")
#     for node in graph:
#         print(f"{node} --> {graph[node]}")

#     # Print heuristic values for verification
#     print("\nHeuristics:")
#     for node in heuristics:
#         print(f"Node {node}: {heuristics[node]}")

#     # Execute Best-First Search and print progress
#     print(f"\nRunning Best-First Search from {start} to {goal}:\n")
#     result = best_first_search(graph, heuristics, start, goal)
#     if not result:
#         print("Path to goal was not found.")

# # Entry point of the program
# if __name__ == "__main__":
#     main()