"""
Clone Graph
------------

Given a reference of a node in a connected undirected graph,
return a deep copy (clone) of the graph.

Each node in the graph contains:
    - an integer value `val`
    - a list of its neighbors `neighbors`

The Node class for reference:
    class Node:
        def __init__(self, val: int = 0, neighbors: List['Node'] = None):
            self.val = val
            self.neighbors = neighbors if neighbors is not None else []

Test Case Format
----------------
For simplicity, each node's value is the same as its index (1-indexed).
For example, the first node has val == 1, the second has val == 2, and so on.

The graph is represented as an adjacency list, where each element of the list
describes the set of neighbors for a node in the graph.

The given node will always be the first node with val = 1.
You must return the reference to the cloned node corresponding to this node.

Examples
--------
Example 1:
    Input:  adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    Output: [[2, 4], [1, 3], [2, 4], [1, 3]]
    Explanation:
        There are 4 nodes in the graph:
        Node 1 -> [2, 4]
        Node 2 -> [1, 3]
        Node 3 -> [2, 4]
        Node 4 -> [1, 3]

Example 2:
    Input:  adjList = [[]]
    Output: [[]]
    Explanation:
        The graph contains a single node with val = 1 and no neighbors.

Example 3:
    Input:  adjList = []
    Output: []
    Explanation:
        The graph is empty and contains no nodes.

Constraints
-----------
- The number of nodes is in the range [0, 100].
- 1 <= Node.val <= 100
- Node.val is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The graph is connected, and all nodes can be visited starting from the given node.

Implementation Notes
--------------------
You can use either DFS or BFS to traverse and clone the graph.
Make sure to maintain a mapping between original nodes and cloned nodes
to prevent duplications and ensure correct neighbor connections.
"""


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)
            old_to_new[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None




