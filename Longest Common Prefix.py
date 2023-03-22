from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minimum = min(strs)
        maximum = max(strs)
        ans = 0
        for a,b in zip(minimum, maximum):
            if a != b:
                break
            ans += 1

        return minimum[0:ans]