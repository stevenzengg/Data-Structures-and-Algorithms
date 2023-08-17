from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans
    
    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.ans = max(left + right, self.ans)
        return max(left, right) + 1
    


if __name__ == '__main__':
    a = Solution()
    b = TreeNode(val=1, left = TreeNode(val=2, left = TreeNode(4), right = TreeNode(5)), right = TreeNode(3))
    print(a.diameterOfBinaryTree(b))