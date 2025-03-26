# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans - 1 if self.ans > 0 else 0

    def dfs(self, root):
        if not root:
            return 0
        
        left = self.dfs(root.left)
        if root.left and root.left.val != root.val:
            left = 0
        right = self.dfs(root.right)
        if root.right and root.right.val != root.val:
            right = 0

        self.ans = max(self.ans, 1 + left + right)
        return 1 + max(left, right)
