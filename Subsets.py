from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in nums:
            length = len(ans)
            for j in range(length):
                ans.append(j + [i])
        
        return ans

if __name__ == '__main__':
    a = Solution()
    b = [1,2,3]
    a.subsets(b)