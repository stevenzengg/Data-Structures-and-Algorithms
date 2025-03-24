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
        
        if not root:
            return None
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root

        if left:
            return left
        elif right:
            return right
        return None
        