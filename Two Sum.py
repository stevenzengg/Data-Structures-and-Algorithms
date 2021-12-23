from typing import List

class Solution:
    def TwoSum(nums: List[int], target: int) -> List[int]:
        elementIndex = {}

        if not nums:
            return None

        for i, v in enumerate(nums):
            complement = target - i
            if complement in elementIndex:
                return [elementIndex[complement], i]
            elementIndex[v] = i
        
        return None




if __name__ == '__main__':
    a = Solution()
    b = [1,2,3,4,5]
    c = 3
    print(a.TwoSum(b,c))


# Easy
# Hashmap
# Two Pointer (sort and low high)