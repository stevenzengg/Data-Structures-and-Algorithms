from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        ans = nums[0]
        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            ans = max(ans, curSum)
        
        return ans