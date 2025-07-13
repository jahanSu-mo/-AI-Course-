def beam_search(graph, heuristics, start, goal, beam_width):
    frontier = [(start, [start])]  # (current_node, path_so_far)

    while frontier:
        frontier.sort(key=lambda x: heuristics.get(x[0], float('inf')))
        frontier = frontier[:beam_width]

        new_frontier = []

        for node, path in frontier:
            print(f"Visiting: {node}, Path: {' -> '.join(path)}")

            if node == goal:
                print("\nGoal reached!")
                return path

            for neighbor in graph.get(node, []):
                new_path = path + [neighbor]
                new_frontier.append((neighbor, new_path))

        frontier = new_frontier

    print("Goal not found.")
    return None

def main():
    graph = {}
    heuristics = {}

    n = int(input("Enter number of nodes: "))
    print("Enter node names:")
    nodes = [input().strip() for _ in range(n)]

    e = int(input("Enter number of edges: "))
    print("Enter edges in format 'u v' (e.g., A B):")
    for _ in range(e):
        u, v = input().strip().split()
        if u not in graph:
            graph[u] = []
        graph[u].append(v)

    print("Enter heuristic values for each node:")
    for node in nodes:
        heuristics[node] = int(input(f"Heuristic for {node}: "))

    start = input("Enter start node: ").strip()
    goal = input("Enter goal node: ").strip()
    beam_width = int(input("Enter beam width: "))

    result_path = beam_search(graph, heuristics, start, goal, beam_width)
    if result_path:
        print("Final Path:", " -> ".join(result_path))

if __name__ == "__main__":
    main()





# # Define the beam search function
# def beam_search(graph, heuristics, start, goal, beam_width):
#     frontier = [(start, [start])]  # Initialize the frontier with the start node and path

#     # Continue searching until the frontier is empty
#     while frontier:
#         # Sort the frontier based on heuristic values (lower is better)
#         frontier.sort(key=lambda x: heuristics.get(x[0], float('inf')))

#         # Keep only the best `beam_width` nodes in the frontier
#         frontier = frontier[:beam_width]

#         new_frontier = []  # Temporary list to store next level of nodes

#         # Explore each node in the current frontier
#         for node, path in frontier:
#             print(f"Visiting: {node}, Path: {' -> '.join(path)}")  # Display current node and path

#             # Check if we have reached the goal
#             if node == goal:
#                 print("\nGoal reached!")  # Announce success
#                 return path  # Return the successful path

#             # Explore all neighbors of the current node
#             for neighbor in graph.get(node, []):
#                 new_path = path + [neighbor]  # Extend the path to the neighbor
#                 new_frontier.append((neighbor, new_path))  # Add to the new frontier

#         frontier = new_frontier  # Move to the next level

#     print("Goal not found.")  # If we exit the loop, the goal was not found
#     return None  # Return None to indicate failure

# # Define the main function to take user input and run the algorithm
# def main():
#     graph = {}        # Dictionary to store the graph
#     heuristics = {}   # Dictionary to store heuristic values

#     # Get number of nodes from user
#     n = int(input("Enter number of nodes: "))
#     print("Enter node names:")
#     nodes = [input().strip() for _ in range(n)]  # Read node names

#     # Get number of edges from user
#     e = int(input("Enter number of edges: "))
#     print("Enter edges in format 'u v' (e.g., A B):")
#     for _ in range(e):
#         u, v = input().strip().split()  # Read each edge
#         if u not in graph:
#             graph[u] = []  # Initialize list if not already in graph
#         graph[u].append(v)  # Add edge from u to v

#     # Get heuristic values from user
#     print("Enter heuristic values for each node:")
#     for node in nodes:
#         heuristics[node] = int(input(f"Heuristic for {node}: "))  # Input heuristic for each node

#     # Get start and goal nodes
#     start = input("Enter start node: ").strip()
#     goal = input("Enter goal node: ").strip()

#     # Get beam width from user
#     beam_width = int(input("Enter beam width: "))

#     # Run the beam search algorithm
#     result_path = beam_search(graph, heuristics, start, goal, beam_width)

#     # Print the result if path was found
#     if result_path:
#         print("Final Path:", " -> ".join(result_path))

# # Run the main function if the script is executed directly
# if __name__ == "__main__":
#     main()
