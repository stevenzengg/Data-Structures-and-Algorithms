# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.lcaNode = None
        self.lca(root, startValue, destValue)

        left = self.findPath(self.lcaNode, startValue, [])
        if not left:
            left = ""
        right = self.findPath(self.lcaNode, destValue, [])
        if not right:
            right = ""

        return len(left) * "U" + "".join(right)

    def lca(self, root, start, dest):
        if not root:
            return 0
        
        ans = 0
        if root.val == start or root.val == dest:
            ans += 1
        
        ans += self.lca(root.left, start, dest) + self.lca(root.right, start, dest)
        if ans == 2:
            if not self.lcaNode:
                self.lcaNode = root
            return 0
        return ans
    
    def findPath(self, root, target, builder):
        if not root:
            return
        if root.val == target:
            return builder
        
        builder.append("L")
        if self.findPath(root.left, target, builder):
            return builder
        
        builder.pop()
        builder.append("R")
        if self.findPath(root.right, target, builder):
            return builder
        builder.pop()
