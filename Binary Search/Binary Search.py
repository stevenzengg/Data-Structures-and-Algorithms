from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            guess = nums[middle]
            if target == guess:
                return middle
            elif target < guess:
                right = middle - 1
            else:
                left = middle + 1
            
        return -1



if __name__ == '__main__':
    a = Solution()
    b = [1,2,3,4,5,6]
    print(a.search(b, 4))
