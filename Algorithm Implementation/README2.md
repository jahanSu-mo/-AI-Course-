# 🧠 Algorithm Implementation

This folder contains the implementations of various AI search algorithms, both uninformed and informed, as well as game-playing strategies. Each algorithm is accompanied by a brief explanation, its applications, complexity analysis, and input/output samples.


## 🔍 Uniformed Search Algorithms

### 1. Breadth-First Search (BFS)

- **How it works**: Explores neighbors level by level using a queue.
- **Applications**: Finding the shortest path in unweighted graphs, web crawlers, social networks.
- **Complexity**:  
  - Time: O(V + E)  
  - Space: O(V)
- **Input/Output**:
  ![BFS Input-Output](image/bfs.png)  


### 2. Depth-First Search (DFS)

- **How it works**: Explores as far as possible down each branch before backtracking.
- **Applications**: Solving puzzles, topological sort, cycle detection.
- **Complexity**:  
  - Time: O(V + E)  
  - Space: O(V)
- **Input/Output**:
  ![DFS Input-Output](image/dfs.png)  


### 3. Iterative Deepening Search (IDS)

- **How it works**: Combines DFS and BFS by doing DFS up to increasing depths.
- **Applications**: Memory-efficient optimal search in large trees.
- **Complexity**:  
  - Time: O(b^d)  
  - Space: O(bd)
- **Input/Output**:
  ![IDS Input-Output](image/IDE.png)  


### 4. Bidirectional Search

- **How it works**: Performs two simultaneous searches—one forward from the start and one backward from the goal.
- **Applications**: Faster pathfinding in graphs.
- **Complexity**:  
  - Time: O(b^(d/2))  
  - Space: O(b^(d/2))
-
  

### 5. Depth-Limited Search (DLS)

- **How it works**: DFS with a depth limit to avoid infinite depth paths.
- **Applications**: Large or infinite graphs where DFS may loop.
- **Complexity**:  
  - Time: O(b^l)  
  - Space: O(bl)


## 🤖 Informed Search Algorithms

### 6. Heuristic Search

- **How it works**: Uses domain knowledge to estimate distance to goal.
- **Applications**: Pathfinding, game AI, planning systems.
- **Complexity**: Varies depending on heuristic and method.


### 7. Best-First Search

- **How it works**: Selects node with lowest heuristic cost.
- **Applications**: Route planning, puzzle solving.
- **Complexity**:  
  - Time: O(b^m)  
  - Space: O(b^m)


### 8. A* Search

- **How it works**: Combines cost from start and heuristic (f(n) = g(n) + h(n)).
- **Applications**: Pathfinding in maps and games.
- **Complexity**:  
  - Time: O(b^d)  
  - Space: O(b^d)

### 9. AO* Algorithm

- **How it works**: Search through an AND-OR graph, solving problems with alternative and joint subgoals.
- **Applications**: Decision-making in planning, diagnostics.
- **Complexity**: Depends on graph structure and branching.


### 10. Hill Climbing

- **How it works**: Moves to neighbor with the best score until peak is reached.
- **Applications**: Optimization, scheduling, machine learning.
- **Complexity**:  
  - Time: O(n)  
  - Space: O(1)
-

### 11. Beam Search

- **How it works**: Similar to Best-First but only keeps the best k nodes at each level.
- **Applications**: Speech recognition, NLP, pathfinding.
- **Complexity**:  
  - Time: O(kb)  
  - Space: O(k)


## 🎮 Game Playing Algorithms

### 12. Minimax Algorithm

- **How it works**: Explores all possible game states to minimize possible loss.
- **Applications**: Two-player games like Chess and Tic Tac Toe.
- **Complexity**:  
  - Time: O(b^m)  
  - Space: O(m)


### 13. Alpha-Beta Pruning

- **How it works**: Improves Minimax by pruning branches that won’t affect the result.
- **Applications**: Efficient search in complex games.
- **Complexity**:  
  - Time: O(b^(m/2))  
  - Space: O(m)



