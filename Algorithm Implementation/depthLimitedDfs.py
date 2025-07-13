def depth_limited_dfs(graph, node, visited, depth):
    if depth < 0:
        return
    visited[node] = True
    print(node, end=' ')
    for neighbor in graph[node]:
        if not visited[neighbor]:
            depth_limited_dfs(graph, neighbor, visited, depth - 1)

def iterative_deepening_dfs(graph, start, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nDepth Limit = {depth} =>", end=' ')
        visited = [False] * len(graph)
        depth_limited_dfs(graph, start, visited, depth)

def main():
    n = int(input("Enter number of nodes: "))
    graph = [[] for _ in range(n + 1)]  # +1 because nodes are 1-indexed

    e = int(input("Enter number of edges: "))
    print("Enter each edge in the format 'u v' (1-based index):")

    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)  # If undirected graph

    start = int(input("Enter starting node for IDS: "))
    max_depth = int(input("Enter maximum depth to search: "))

    print("\nIterative Deepening DFS Traversal:")
    iterative_deepening_dfs(graph, start, max_depth)

main()





# # Depth-Limited Depth First Search (DFS) function
# def depth_limited_dfs(graph, node, visited, depth):
#     # Base case: if we've exceeded our depth limit, return
#     if depth < 0:
#         return
    
#     # Mark the current node as visited
#     visited[node] = True
#     # Print the current node (traversal order)
#     print(node, end=' ')
    
#     # Explore all neighbors of the current node
#     for neighbor in graph[node]:
#         # If the neighbor hasn't been visited, recursively explore it
#         if not visited[neighbor]:
#             depth_limited_dfs(graph, neighbor, visited, depth - 1)  # Decrease depth by 1

# # Iterative Deepening DFS function
# def iterative_deepening_dfs(graph, start, max_depth):
#     # Try all depth limits from 0 up to max_depth
#     for depth in range(max_depth + 1):
#         print(f"\nDepth Limit = {depth} =>", end=' ')
#         # Initialize visited array for each new depth limit
#         visited = [False] * len(graph)

#         # Perform DFS with the current depth limit
#         depth_limited_dfs(graph, start, visited, depth)

# # Main function to handle user input and execution
# def main():
#     # Get number of nodes from user
#     n = int(input("Enter number of nodes: "))
#     # Initialize adjacency list for graph (using 1-based indexing)
#     graph = [[] for _ in range(n + 1)]  # +1 because nodes are 1-indexed

#     # Get number of edges from user
#     e = int(input("Enter number of edges: "))
#     print("Enter each edge in the format 'u v' (1-based index):")

#     # Read all edges and build the graph
#     for _ in range(e):
#         u, v = map(int, input().split())
#         # Add edge in both directions for undirected graph
#         graph[u].append(v)
#         graph[v].append(u)  # If undirected graph

#     # Get starting node and maximum depth from user
#     start = int(input("Enter starting node for IDS: "))
#     max_depth = int(input("Enter maximum depth to search: "))

#     # Execute and print the Iterative Deepening DFS traversal
#     print("\nIterative Deepening DFS Traversal:")
#     iterative_deepening_dfs(graph, start, max_depth)

# # Entry point of the program
# main()