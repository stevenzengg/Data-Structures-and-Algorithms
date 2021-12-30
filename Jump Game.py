from typing import List
from collections import defaultdict

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return nums

        lastSafeElement = len(nums)-1

        for i in reversed(range(len(nums))):
            if lastSafeElement < i + nums[i]:
                lastSafeElement = i
        
        return lastSafeElement == 0


if __name__ == '__main__':
    a = Solution()
    b = [10,0,0,0,0,0,0,0,1]
    print(a.canJump(b))


# Easy
# Hashmap
# Two Pointer (sort and low high)