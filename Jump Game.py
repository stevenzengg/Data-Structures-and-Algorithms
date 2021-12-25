from typing import List
from collections import defaultdict

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return nums

        lastSafeElement = len(nums)-1

        for i in range(reversed(len(nums))):
            if lastSafeElement > i + nums[i]:
                return False
            
            lastSafeElement = i
        
        return True


if __name__ == '__main__':
    a = Solution()
    b = [1,2,6,2,2,6,0,1]
    print(a.canJump(b))


# Easy
# Hashmap
# Two Pointer (sort and low high)