"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hmap = {node: Node(node.val, [])} # oldNode: newNode
        self.dfs(node, hmap)
        return hmap[node]
    
    def dfs(self, node, hmap):
        # potentially check here if node has been created or is in seen
        for neighbor in node.neighbors:
            if neighbor not in hmap:
                newNeighbor = Node(neighbor.val, [])
                hmap[neighbor] = newNeighbor
                self.dfs(neighbor, hmap)
            hmap[node].neighbors.append(hmap[neighbor])
        

# O(n + m) where n is the number of nodes and m is the number of edges
# O(n) space complexity