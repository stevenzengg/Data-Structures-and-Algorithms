from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        last = False
        ans = 0
        for i in flowerbed:
            if i == 1:
                last = True
                continue
            if last:
                last = False
                continue
            ans += 1
            last = True
        return ans >= n