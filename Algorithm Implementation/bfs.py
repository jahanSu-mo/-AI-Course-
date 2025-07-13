from collections import deque

def bfs(graph, start):
    visited=[False]*len(graph)
    queue = deque()
    visited[start]=True
    queue.append(start)

    while queue:
        current =queue.popleft()
        print(current, end=' ')


        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor]=True
                queue.append(neighbor)

def main():
    n =int(input("enter number of nodes: "))
    graph=[[] for _ in  range(n)]

    e=int(input("Enter number of edges: "))
    print("Enter each edge in the format 'u v' (0-based index):")

    for _ in range(e):
        u, v=map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    start = int(input("enter starting node for bfs: "))
    print("BFS traversal starting from node", start,":")
    bfs(graph, start)

main()

# enter number of nodes: 5  
# Enter number of edges: 4  
# Enter each edge in the format 'u v' (0-based index):  
# 0 1  
# 0 2  
# 1 3  
# 3 4  
# enter starting node for bfs: 0  
# BFS traversal starting from node 0 : 0 1 2 3 4

# from collections import deque

# def bfs(graph, start):
#     visited = [False] * len(graph)  # Keeps track of visited nodes
#     queue = deque()  # Initialize a queue
#     visited[start] = True  # Mark the start node as visited
#     queue.append(start)  # Add the start node to the queue

#     while queue:
#         current = queue.popleft()  # Dequeue a node
#         print(current, end=' ')  # Process the current node

#         for neighbor in graph[current]:  # Visit all adjacent nodes
#             if not visited[neighbor]:  # If not visited
#                 visited[neighbor] = True  # Mark as visited
#                 queue.append(neighbor)  # Enqueue the neighbor

# def main():
#     n = int(input("enter number of nodes: "))  # Read number of nodes
#     graph = [[] for _ in range(n)]  # Initialize adjacency list

#     e = int(input("Enter number of edges: "))  # Read number of edges
#     print("Enter each edge in the format 'u v' (0-based index):")

#     for _ in range(e):  # Read all edges
#         u, v = map(int, input().split())  # Read edge
#         graph[u].append(v)  # Add edge u -> v
#         graph[v].append(u)  # Add edge v -> u (undirected)

#     start = int(input("enter starting node for bfs: "))  # Starting node
#     print("BFS traversal starting from node", start, ":")
#     bfs(graph, start)  # Perform BFS

# main()  # Run the main function
