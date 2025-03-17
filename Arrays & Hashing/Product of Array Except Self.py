from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = [1] * len(nums)
        product = 1
        for i, v in enumerate(nums):
            ans[i] = ans[i]*product
            product = product*v
        product = 1
        for i in reversed(range(len(nums))):
            ans[i] = ans[i]*product
            product = product*nums[i]

        return ans