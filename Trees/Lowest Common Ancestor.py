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
            
# postorder version, no use of BST properties

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = 0
        self.p, self.q = p, q
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        ans = 0
        if not root:
            return ans
        ans += self.dfs(root.left)
        ans += self.dfs(root.right)
        if root == self.p or root == self.q:
            ans += 1
        if ans == 2:
            if not self.ans:
                self.ans = root
        return ans
            
# clean postorder version

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)

    def dfs(self, root, p, q):
        if not root:
            return None

        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)

        if root == p or root == q:
            return root

        if left and right:
            return root  # If p and q are found in different subtrees, root is LCA.

        return left if left else right  # Return non-null child (if exists).
