from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in nums:
            length = len(ans)
            for j in range(length):
                ans.append(ans[j] + [i])
        
        return ans

# Recursive solution, backtracking.

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, temp = [], []
        self.recurse(0, nums, temp, ans)
        return ans

    def recurse(self, idx, nums, temp, ans):
        ans.append(temp)
        for i in range(idx, len(nums)):
            self.recurse(i + 1, nums, temp + [nums[i]], ans)

if __name__ == '__main__':
    a = Solution()
    b = [1,2,3]
    a.subsets(b)

# Time complexity: O(n*2^n), Space complexity: O(n*2^n)
# Recurrence relation: T(n) = 2T(n-1) + O(n)
# Basically, each decision creates two subproblems, at a depth of n
# When looking at a tree, there are *2 more nodes each level down
# a height of n. Therefore, there are 2^n nodes at the bottom level.
#

# When analyzing recurrence relations, up the operation. + becomes *,
# * becomes ^. 