#Alpha-Beta Pruning Implementation

def alpha_beta_pruning(depth, node_index, is_maximizing_player, values, alpha, beta, max_depth):
    if depth == max_depth:
        return values[node_index]

    if is_maximizing_player:
        best = float('-inf')
        # Check left and right child
        for i in range(2):
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best

    else:
        best = float('inf')
        # Check left and right child
        for i in range(2):
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best

def main():
    print("Welcome to Alpha-Beta Pruning (Minimax with Pruning)!")
    
    depth = int(input("Enter the maximum depth of the game tree (example: 2): "))
    leaf_nodes = 2 ** depth  # Total number of leaf nodes

    print(f"\nEnter {leaf_nodes} leaf node values (space separated):")
    values = list(map(int, input().split()))
    
    if len(values) != leaf_nodes:
        print(f"Error: You must enter exactly {leaf_nodes} values!")
        return
    
    print("\nStarting Alpha-Beta Pruning calculation...\n")
    
    result = alpha_beta_pruning(0, 0, True, values, float('-inf'), float('inf'), depth)
    
    print(f"\nThe optimal value for the Maximizer is: {result}")

if __name__ == "__main__":
    main()




# # Alpha-Beta Pruning Algorithm

# # Function for Alpha-Beta Pruning
# def alpha_beta_pruning(depth, node_index, is_maximizing_player, values, alpha, beta, max_depth):
#     # Base case: if we reach the maximum depth, return the leaf node value
#     if depth == max_depth:
#         return values[node_index]

#     # If it's the maximizer's turn
#     if is_maximizing_player:
#         best = float('-inf')  # Initialize best value to negative infinity
# #Because the Maximizer is trying to find the biggest value, so we start with the smallest possible number.
# #This way, any number found in the next steps will be bigger than negative infinity and will automatically replace it.
#         # Traverse left and right child nodes
#         for i in range(2):
#             # Recursive call to the next depth, switch to minimizer
#             val = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)

#             best = max(best, val)  # Choose the maximum value
#             alpha = max(alpha, best)  # Update alpha

#             # If beta is less than or equal to alpha, prune the remaining branches
#             if beta <= alpha:
#                 break  # Prune the rest of the tree branches

#         return best  # Return the best value found

#     else:  # If it's the minimizer's turn
#         best = float('inf')  # Initialize best value to positive infinity

#         # Traverse left and right child nodes
#         for i in range(2):
#             # Recursive call to the next depth, switch to maximizer
#             val = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta, max_depth)

#             best = min(best, val)  # Choose the minimum value
#             beta = min(beta, best)  # Update beta

#             # If beta is less than or equal to alpha, prune the remaining branches
#             if beta <= alpha:
#                 break  # Prune the rest of the tree branches

#         return best  # Return the best value found


# # Main function to run the program
# def main():
#     print("Welcome to Alpha-Beta Pruning (Minimax with Pruning)!")

#     # Ask user to input the depth of the game tree
#     depth = int(input("Enter the maximum depth of the game tree (example: 2): "))
#     leaf_nodes = 2 ** depth  # Calculate total number of leaf nodes in a binary tree

#     # Ask user to input leaf node values
#     print(f"\nEnter {leaf_nodes} leaf node values (space separated):")
#     values = list(map(int, input().split()))

#     # Check if the user entered the correct number of values
#     if len(values) != leaf_nodes:
#         print(f"Error: You must enter exactly {leaf_nodes} values!")
#         return

#     # print("\nStarting Alpha-Beta Pruning calculation...\n")

#     # Call the alpha-beta pruning function starting at the root
#     result = alpha_beta_pruning(0, 0, True, values, float('-inf'), float('inf'), depth)

#     # Display the final optimal value for the maximizer
#     print(f"\nThe optimal value for the Maximizer is: {result}")


# # Execute the main function when the script runs
# if __name__ == "__main__":
#     main()
