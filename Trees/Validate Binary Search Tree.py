# Definition for a binary tree node.
from typing import Optional
import math

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recurse(root, float('-inf'), float('inf'))

    
    def recurse(self, node, low, high):
        if not node:
            return True
        
        return node.val > low and node.val < high and self.recurse(node.left, low, node.val) and self.recurse(node.right, node.val, high)
            
