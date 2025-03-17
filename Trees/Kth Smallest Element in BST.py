from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = self.inorder(root)
        return nodes[k-1]
    
    def inorder(self, node):
        if not node:
            return []
        return self.inorder(node.left) + [node.val] + self.inorder(node.right)
            


if __name__ == '__main__':
    a = Solution()
    b = TreeNode(val = 2, left = TreeNode(val = 1))
    print(a.kthSmallest(b, 2))
