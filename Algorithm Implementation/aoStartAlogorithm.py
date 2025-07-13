class Graph:
    def __init__(self):
        self.graph = {} 
        self.heuristic = {}  

    def add_node(self, node, heuristic_value):
        self.heuristic[node] = heuristic_value
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, parent, children_set):
        self.graph[parent].append(children_set)

    def get_neighbors(self, node):
        return self.graph.get(node, [])


class AOStar:
    def _init_(self, graph, start_node):
        self.graph = graph
        self.start_node = start_node
        self.solution = {}

    def ao_star(self, node):
        if node not in self.graph.graph or not self.graph.graph[node]:
            return self.graph.heuristic[node]

        min_cost = float('inf')
        best_children = None

        for children in self.graph.get_neighbors(node):
            cost = 0
            for child, edge_cost in children:
                cost += edge_cost + self.graph.heuristic[child]
            if cost < min_cost:
                min_cost = cost
                best_children = children

        self.solution[node] = [child for child, _ in best_children]

        for child, _ in best_children:
            self.ao_star(child)

        self.graph.heuristic[node] = min_cost
        return self.graph.heuristic[node]

    def print_solution(self, node=None, level=0):
        if node is None:
            node = self.start_node
        print("  " * level + node)
        if node in self.solution:
            for child in self.solution[node]:
                self.print_solution(child, level + 1)


def main():
    graph = Graph()  # Create a Graph object

    num_nodes = int(input("Enter the number of nodes: "))  

    print("\nEnter node names and heuristic values:")
    for _ in range(num_nodes):
        node = input("Node name: ")                            
        heuristic = int(input(f"Heuristic value of {node}: ")) 
        graph.add_node(node, heuristic)                        

    print("\nFor each parent node, you can add multiple OR options (each OR option can have one or more children).")
    print("Example input for one OR option: B 9 (meaning B is a child with edge cost 9).")
    print("Enter 'done' as parent node when you want to stop adding edges.\n")

    while True:
        parent = input("\nEnter parent node (or type 'done' to stop adding edges): ")  
        if parent.lower() == 'done':
            break

        while True:
            option = input(f"Enter child set for {parent} (separate multiple children like 'B 9, C 5') or 'done' to stop: ")
            if option.lower() == 'done':  # Stop adding OR options for this parent
                break

            children_set = []  
            child_entries = option.split(',')  
            for entry in child_entries:
                child, cost = entry.strip().split()  
                children_set.append((child, int(cost)))  
            graph.add_edge(parent, children_set)  

    start_node = input("\nEnter the start node: ")  

    ao_star_solver = AOStar(graph, start_node)  
    ao_star_solver.ao_star(start_node)  

    print("\nFinal Solution Graph:")  
    ao_star_solver.print_solution()

if __name__ == "__main__":
    main()  # Run the main function









# Define a class to represent the AND-OR graph structure
class Graph:
    # Initialize the graph with empty dictionaries for nodes/edges and heuristics
    def __init__(self):
        self.graph = {}  # Dictionary to store nodes and their child sets
        self.heuristic = {}  # Dictionary to store heuristic values for nodes

    # Method to add a node to the graph with its heuristic value
    def add_node(self, node, heuristic_value):
        # Store the heuristic value for this node
        self.heuristic[node] = heuristic_value
        # Initialize empty list for child sets if node doesn't exist
        if node not in self.graph:
            self.graph[node] = []

    # Method to add an edge from parent to a set of children (AND nodes)
    def add_edge(self, parent, children_set):
        # Add this set of children as an OR option for the parent
        self.graph[parent].append(children_set)

    # Method to get all neighbor sets (OR options) of a node
    def get_neighbors(self, node):
        # Return empty list if node doesn't exist, otherwise return its child sets
        return self.graph.get(node, [])


# Define the AO* search algorithm class
class AOStar:
    # Initialize the AO* solver with graph and start node
    def _init_(self, graph, start_node):
        # Store the graph object
        self.graph = graph
        # Store the starting node for the search
        self.start_node = start_node
        # Dictionary to store the solution path (node -> chosen children)
        self.solution = {}

    # The main AO* algorithm implementation (recursive)
    def ao_star(self, node):
        # Base case: if node is terminal (no children), return its heuristic
        if node not in self.graph.graph or not self.graph.graph[node]:
            return self.graph.heuristic[node]

        # Initialize minimum cost to infinity
        min_cost = float('inf')
        # Variable to store the best child set found
        best_children = None

        # Evaluate all OR options (child sets) of the current node
        for children in self.graph.get_neighbors(node):
            # Calculate total cost for this OR option
            cost = 0
            # Sum edge costs and child heuristics for all AND children in this set
            for child, edge_cost in children:
                cost += edge_cost + self.graph.heuristic[child]
            # Update best solution if this path is cheaper
            if cost < min_cost:
                min_cost = cost
                best_children = children

        # Store the chosen children in the solution
        self.solution[node] = [child for child, _ in best_children]

        # Recursively process each child in the best solution
        for child, _ in best_children:
            self.ao_star(child)

        # Update the node's heuristic with the new minimum cost
        self.graph.heuristic[node] = min_cost
        return self.graph.heuristic[node]

    # Method to print the solution tree (recursive with indentation)
    def print_solution(self, node=None, level=0):
        # Start from root if no node specified
        if node is None:
            node = self.start_node
        # Print node with indentation based on depth level
        print("  " * level + node)
        # Recursively print all children in the solution
        if node in self.solution:
            for child in self.solution[node]:
                self.print_solution(child, level + 1)


# Main function with interactive input for graph construction
def main():
    graph = Graph()  # Create a Graph object

    num_nodes = int(input("Enter the number of nodes: "))  # Ask user how many nodes in the graph

    print("\nEnter node names and heuristic values:")
    for _ in range(num_nodes):
        node = input("Node name: ")                            # Take node name from user
        heuristic = int(input(f"Heuristic value of {node}: ")) # Take heuristic value from user
        graph.add_node(node, heuristic)                        # Add the node to the graph

    print("\nFor each parent node, you can add multiple OR options (each OR option can have one or more children).")
    print("Example input for one OR option: B 9 (meaning B is a child with edge cost 9).")
    print("Enter 'done' as parent node when you want to stop adding edges.\n")

    while True:
        parent = input("\nEnter parent node (or type 'done' to stop adding edges): ")  # Take parent node from user
        if parent.lower() == 'done':
            break

        while True:
            option = input(f"Enter child set for {parent} (separate multiple children like 'B 9, C 5') or 'done' to stop: ")
            if option.lower() == 'done':  # Stop adding OR options for this parent
                break

            children_set = []  # Initialize a list to store one OR option
            child_entries = option.split(',')  # Separate multiple children
            for entry in child_entries:
                child, cost = entry.strip().split()  # Get child name and edge cost
                children_set.append((child, int(cost)))  # Add child and cost to the list
            graph.add_edge(parent, children_set)  # Add this OR option to the graph

    start_node = input("\nEnter the start node: ")  # Take the start node from user

    ao_star_solver = AOStar(graph, start_node)  # Create AOStar solver object
    ao_star_solver.ao_star(start_node)  # Run the AO* algorithm starting from the start node

    print("\nFinal Solution Graph:")  # Print the final solution path
    ao_star_solver.print_solution()

if __name__ == "__main__":
    main()  # Run the main function
