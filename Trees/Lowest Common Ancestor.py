class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p, q = min(p.val, q.val), max(p.val, q.val)
        return self.dfs(root, p, q)
    
    def dfs(self, root, p, q):
        if root.val < p and root.val < q:
            return self.dfs(root.right, p, q)
        elif root.val > p and root.val > q:
            return self.dfs(root.left, p, q)
        
        return root