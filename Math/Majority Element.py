class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = count = 0
        for i in nums:
            if i == ans:
                count += 1
            elif count == 0:
                ans = i
                count += 1
            else:
                count -= 1
        
        return ans