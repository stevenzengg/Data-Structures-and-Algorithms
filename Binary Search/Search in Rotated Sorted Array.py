from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1 

        while start <= end:
            mid = (start + end) // 2

            if target == nums[mid]:
                return mid
            
            # Determine which half is sorted
            if nums[mid] >= nums[start]:  
                # Left half is sorted (nums[start] to nums[mid])
                if target >= nums[start] and target < nums[mid]:  
                    # Target is in the left sorted half
                    end = mid - 1  
                else:
                    # Target is in the right half (unsorted part)
                    start = mid + 1  
            else:
                # Right half is sorted (nums[mid] to nums[end])
                if target > nums[mid] and target <= nums[end]:  
                    # Target is in the right sorted half
                    start = mid + 1  
                else:
                    # Target is in the left half (unsorted part)
                    end = mid - 1  

        return -1  # Target not found
    

# Time complexity: O(log(n)), Space complexity: O(1)