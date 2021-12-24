from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return nums

        left = right = ans = 0
        
        while right < len(nums):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
                ans += 1
            
            right += 1
        
if __name__ == '__main__':
    a = Solution()
    b = [1,2,3,4,5]
    c = 3
    print(a.removeElement(b, c))


# Easy
# Hashmap
# Two Pointer (sort and low high)