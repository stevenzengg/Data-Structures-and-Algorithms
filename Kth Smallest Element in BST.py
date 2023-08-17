from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = None
        stack = []
        if root:
            stack.append(root)
        for _ in range(k):
            root = stack[-1]
            while root.left:
                stack.append(root.left)
                root.left, root = None, root.left

            ans = stack.pop().val
            if root.right:
                stack.append(root.right)
        return ans
            


if __name__ == '__main__':
    a = Solution()
    b = TreeNode(val = 2, left = TreeNode(val = 1))
    print(a.kthSmallest(b, 2))
