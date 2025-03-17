from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small = float('inf')
        big = ans = 0

        for i in prices:
            if i < small:
                small = i
                big = i
            big = max(big, i)
            ans = max(ans, big - small)
        
        return ans