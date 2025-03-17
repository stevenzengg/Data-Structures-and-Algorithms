from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums or len(nums) <= 1:
            return nums

        left = right = ans = 1
        while right < len(nums):
            if nums[right] != nums[right -1]:
                nums[left] = nums[right]
                left += 1
                ans += 1

            right += 1
        
        return ans







if __name__ == '__main__':
    a = Solution()
    b = [1,2,3,4,5]
    print(a.removeDuplicates(b))