# O(n) time and space complexity version due to use of pointers

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.dfs(preorder, inorder, 0, len(preorder), 0, len(inorder))
    def dfs(self, preorder, inorder, l1, r1, l2, r2):
        if l1 >= r1 or l2 >= r2:
            return None
        node = TreeNode(preorder[l1])
        mid = inorder.index(preorder[l1])
        left_size = mid - l2
        
        node.left = self.dfs(preorder, inorder, l1 + 1, l1 + 1 + left_size, l2, mid)
        node.right = self.dfs(preorder, inorder, l1 + 1 + left_size, r1, mid + 1, r2)
        return node
    
# O(n^2) time and space complexity version due to list concats.

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.dfs(preorder, inorder)
    def dfs(self, preorder, inorder):
        if not preorder:
            return None
        node = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        node.left = self.dfs(preorder[1:mid + 1], inorder[:mid + 1])
        node.right = self.dfs(preorder[mid + 1:], inorder[mid + 1:])
        return node