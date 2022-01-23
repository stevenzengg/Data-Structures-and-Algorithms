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
        
        def recurse(root, low = -math.inf, big = math.inf):
            if not root:
                return True
            if root.val >= big or root.val <= low:
                return False
            return True and recurse(root.left, low, root.val) and recurse(root.right, root.val, big)
        
        return recurse(root)
        
