from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # For this problem, if a List is in descending order, it has no next permutation (hence reverse).
        iterator = len(nums) - 1
        
        # Find first element that breaks the descending order from the right.
        while iterator > 0:
            if nums[iterator -1] < nums[iterator]:
                break
            
            iterator -= 1
        # Reverse list if entire list is in descending order
        if iterator == 0:
            nums.reverse()
            return
        
        iterator -= 1
        nextBiggest = len(nums) - 1
        
        # From right to left, find the first element that is strictly greater than previous first element.
        while nums[iterator] >= nums[nextBiggest]:
            nextBiggest -= 1
        # Swap them
        nums[nextBiggest], nums[iterator] = nums[iterator], nums[nextBiggest]
        
        iterator += 1
        reverser = len(nums) - 1
        
        # Reverse the list to the right of previous first element index.
        while iterator < reverser:
            nums[iterator], nums[reverser] = nums[reverser], nums[iterator]
            iterator += 1
            reverser -= 1
        
if __name__ == '__main__':
    a = Solution()
    b = [1,5,1]
    a.nextPermutation(b)