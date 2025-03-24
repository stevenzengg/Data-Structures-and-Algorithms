from typing import List

class Solution:
    def TwoSum(nums: List[int], target: int) -> List[int]:
        seen = {} # value:index
        for i,v in enumerate(nums):
            if target - v in seen:
                return [seen[target-v], i]
            seen[v] = i
        
        return []




if __name__ == '__main__':
    a = Solution()
    b = [1,2,3,4,5]
    c = 3
    print(a.TwoSum(b,c))


# Time Complexity: O(n)
# Space Complexity: O(n)
# The time complexity is O(n) because we loop through the list once
# The space complexity is O(n) because we store the output in a dictionary of size n