class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, 1)

    
    def dfs(self, root, level):
        if not root:
            return level
        
        left = self.dfs(root.left, level + 1)
        right = self.dfs(root.right, level + 1)

        if not left or not right or abs(left - right) > 1:
            return False

        return max(left, right)