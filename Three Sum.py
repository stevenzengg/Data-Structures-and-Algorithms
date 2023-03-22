from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(nums, ans, i+1)
        
        return ans
    
    
    def twoSum(self, nums: List[int], ans: List[List[int]], i: int) -> None:
        target = -nums[i-1]
        seen = {} # third value: second value
        while i < len(nums):
            if nums[i] in seen:
                ans.append([-target, nums[i], seen[nums[i]]])
                while i < len(nums) - 1 and nums[i] == nums[i+1]:
                    i +=1
            
            seen[target - nums[i]] = nums[i]
            i += 1
            
            
            
            
        
                
               



if __name__ == '__main__':
    a = Solution()
    b = [1,2,3,4,5]
    c = 3
    print(a.threeSum(b,c))


# Easy
# Hashmap
# Two Pointer (sort and low high)