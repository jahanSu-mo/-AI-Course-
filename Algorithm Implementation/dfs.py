def dfs ( graph, start , visited):
    visited[start]= True
    print(start, end=' ')

    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph,neighbor,visited)
def main():
    n =int(input("enter number of nodes : "))
    graph=[[] for _ in range(n)]

    e= int(input("Enter number of edges : "))
    print("Enter each edge in the format 'u v' (0-based index):")      

    for _ in range(e):
        u ,v =map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    start = int(input("enter starting node of dfs :"))
    visited =[False]*n 
    print("DFS traversal starting from node", start, ":")
    dfs(graph, start, visited)
main()    


# enter number of nodes: 5  
# Enter number of edges: 4  
# Enter each edge in the format 'u v' (0-based index):  
# 0 1  
# 0 2  
# 1 3  
# 3 4  
# enter starting node for bfs: 0  

# Depth-First Search (DFS) function that takes a graph, starting node, and visited list as input
# def dfs(graph, start, visited):
#     # Mark the current node as visited
#     visited[start] = True
#     # Print the current node (with space separator, no newline)
#     print(start, end=' ')

#     # Explore all neighbors of the current node
#     for neighbor in graph[start]:
#         # If the neighbor hasn't been visited yet
#         if not visited[neighbor]:
#             # Recursively call DFS on the unvisited neighbor
#             dfs(graph, neighbor, visited)

# # Main function to handle input and initiate DFS
# def main():
#     # Get number of nodes in the graph
#     n = int(input("Enter number of nodes: "))
#     # Initialize adjacency list for the graph (empty list for each node)
#     graph = [[] for _ in range(n)]

#     # Get number of edges in the graph
#     e = int(input("Enter number of edges: "))
#     # Prompt user for edge input format
#     print("Enter each edge in the format 'u v' (0-based index):")      

#     # Process each edge
#     for _ in range(e):
#         # Read edge (two space-separated integers)
#         u, v = map(int, input().split())
#         # Add edge in both directions (since it's an undirected graph)
#         graph[u].append(v)
#         graph[v].append(u)
    
#     # Get starting node for DFS
#     start = int(input("Enter starting node of DFS : "))
#     # Initialize visited list (all nodes unvisited initially)
#     visited = [False] * n 
    
#     # Print header for DFS traversal
#     print("DFS traversal starting from node", start, ":")
#     # Call DFS function with the constructed graph, starting node, and visited list
#     dfs(graph, start, visited)

# # Entry point of the program
# main()

