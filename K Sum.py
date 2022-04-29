from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans, before = [], []
        nums.sort()
        self.kSum(nums, target, 4, ans, 0, [])
        return ans
        
        
        
    
    
    def kSum(self, nums: List[int], target: int, k: int, ans: List[List[int]], i: int, before: List[int]) -> None:
        if k == 2:
            self.twoSum(nums, target, ans, i, before)
            return

        limit = len(nums) - k + 1
        for j in range(i, len(nums) - k + 2):
            if j == i or nums[j] != nums[j-1]:
                newbefore = before.copy()
                newbefore.append(nums[j])
                self.kSum(nums, target - nums[j], k - 1, ans, j+1, newbefore)
            
    
    def twoSum(self, nums: List[int], target: int, ans: List[List[int]], i: int, before: List[int]) -> None:
        left, right = i, len(nums) - 1
        while left < right:
            add = nums[left] + nums[right]
            if add < target:
                left += 1
            elif add > target:
                right -= 1
            else:
                ans.append([nums[left], nums[right]] + before)
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                left += 1
                
        
        


if __name__ == '__main__':
    a = Solution()
    b = [1,0,-1,0,-2,2]
    c = 0
    d = 4
    ans = []
    print(a.fourSum(b, c))
    


# Easy
# Hashmap
# Two Pointer (sort and low high)