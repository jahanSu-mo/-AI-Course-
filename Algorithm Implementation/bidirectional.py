from collections import deque

def bfs_bidirectional(graph, start, goal):
    if start == goal:
        print(f"Start and goal are the same: {start}")
        return

    n = len(graph)
    visited_start = [False] * n
    visited_goal = [False] * n

    parent_start = [-1] * n
    parent_goal = [-1] * n

    queue_start = deque([start])
    queue_goal = deque([goal])

    visited_start[start] = True
    visited_goal[goal] = True

    while queue_start and queue_goal:
        # Step from start side
        if bfs_step(graph, queue_start, visited_start, visited_goal, parent_start, direction="Start"):
            meeting_node = find_meeting_node(visited_start, visited_goal)
            print_path(parent_start, parent_goal, meeting_node, start, goal)
            return

        # Step from goal side
        if bfs_step(graph, queue_goal, visited_goal, visited_start, parent_goal, direction="Goal"):
            meeting_node = find_meeting_node(visited_start, visited_goal)
            print_path(parent_start, parent_goal, meeting_node, start, goal)
            return

    print("No path found between start and goal.")

def bfs_step(graph, queue, visited_this, visited_other, parent, direction):
    current = queue.popleft()
    for neighbor in graph[current]:
        if not visited_this[neighbor]:
            visited_this[neighbor] = True
            parent[neighbor] = current
            queue.append(neighbor)

            if visited_other[neighbor]:
                return True
    return False

def find_meeting_node(visited_start, visited_goal):
    for i in range(len(visited_start)):
        if visited_start[i] and visited_goal[i]:
            return i
    return -1

def print_path(parent_start, parent_goal, meeting_node, start, goal):
    path = []

    node = meeting_node
    while node != -1:
        path.append(node)
        node = parent_start[node]
    path.reverse()

    node = parent_goal[meeting_node]
    while node != -1:
        path.append(node)
        node = parent_goal[node]

    print("Path from", start, "to", goal, ": ", end='')
    print(" -> ".join(map(str, path)))

def main():
    n = int(input("Enter number of nodes: "))
    graph = [[] for _ in range(n)]

    e = int(input("Enter number of edges: "))
    print("Enter each edge in the format 'u v' (0-based index):")
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)  # undirected

    start = int(input("Enter starting node: "))
    goal = int(input("Enter goal node: "))

    bfs_bidirectional(graph, start, goal)


main()









# from collections import deque

# def bfs_bidirectional(graph, start, goal):
#     # Check if start and goal are the same node
#     if start == goal:
#         print(f"Start and goal are the same: {start}")
#         return

#     n = len(graph)
#     # Visited lists for BFS from start and from goal
#     visited_start = [False] * n
#     visited_goal = [False] * n

#     # Parent pointers to reconstruct paths
#     parent_start = [-1] * n  # Tracks path from start
#     parent_goal = [-1] * n   # Tracks path from goal

#     # Queues for BFS from both directions
#     queue_start = deque([start])
#     queue_goal = deque([goal])

#     # Mark start and goal as visited in their respective searches
#     visited_start[start] = True
#     visited_goal[goal] = True

#     # Continue while both queues have nodes to process
#     while queue_start and queue_goal:
#         # Perform one step of BFS from the start side
#         if bfs_step(graph, queue_start, visited_start, visited_goal, parent_start, direction="Start"):
#             # If the searches meet, find the meeting node
#             meeting_node = find_meeting_node(visited_start, visited_goal)
#             # Print the complete path
#             print_path(parent_start, parent_goal, meeting_node, start, goal)
#             return

#         # Perform one step of BFS from the goal side
#         if bfs_step(graph, queue_goal, visited_goal, visited_start, parent_goal, direction="Goal"):
#             # If the searches meet, find the meeting node
#             meeting_node = find_meeting_node(visited_start, visited_goal)
#             # Print the complete path
#             print_path(parent_start, parent_goal, meeting_node, start, goal)
#             return

#     # If we get here, no path was found
#     print("No path found between start and goal.")

# def bfs_step(graph, queue, visited_this, visited_other, parent, direction):
#     # Get the next node from the queue
#     current = queue.popleft()
    
#     # Explore all neighbors of the current node
#     for neighbor in graph[current]:
#         if not visited_this[neighbor]:
#             # Mark as visited and record parent
#             visited_this[neighbor] = True
#             parent[neighbor] = current
#             queue.append(neighbor)

#             # Check if this node has been visited by the other search
#             if visited_other[neighbor]:
#                 return True  # The searches have met
#     return False  # No meeting found in this step

# def find_meeting_node(visited_start, visited_goal):
#     # Find the first node that was visited by both searches
#     for i in range(len(visited_start)):
#         if visited_start[i] and visited_goal[i]:
#             return i
#     return -1  # No meeting node found

# def print_path(parent_start, parent_goal, meeting_node, start, goal):
#     path = []

#     # Reconstruct path from start to meeting node
#     node = meeting_node
#     while node != -1:
#         path.append(node)
#         node = parent_start[node]
#     path.reverse()  # Reverse to get start -> meeting node order

#     # Reconstruct path from meeting node to goal (excluding meeting node)
#     node = parent_goal[meeting_node]
#     while node != -1:
#         path.append(node)
#         node = parent_goal[node]

#     # Print the complete path
#     print("Path from", start, "to", goal, ": ", end='')
#     print(" -> ".join(map(str, path)))

# def main():
#     # Get graph information from user
#     n = int(input("Enter number of nodes: "))
#     graph = [[] for _ in range(n)]

#     e = int(input("Enter number of edges: "))
#     print("Enter each edge in the format 'u v' (0-based index):")
#     for _ in range(e):
#         u, v = map(int, input().split())
#         graph[u].append(v)
#         graph[v].append(u)  # undirected

#     # Get start and goal nodes
#     start = int(input("Enter starting node: "))
#     goal = int(input("Enter goal node: "))

#     # Run bidirectional BFS
#     bfs_bidirectional(graph, start, goal)

# main()