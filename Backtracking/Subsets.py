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