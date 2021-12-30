from typing import List

class Solution:
    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        if len(nums) < 3:
            return None

        def twoSum(self, nums: List[int], target: int) -> None:
            if len(nums) < 2:
                return

            diffs = {}

            for i in nums:
                if i in diffs:
                    ans.append([v, diffs[i], i])
                else:
                    diffs[target-i] = i
            

        for i, v in enumerate(set(nums)):
            twoSum(nums[i+1:], target - v)

        return ans
    


            



if __name__ == '__main__':
    a = Solution()
    b = [1,2,3,4,5]
    c = 3
    print(a.threeSum(b,c))


# Easy
# Hashmap
# Two Pointer (sort and low high)