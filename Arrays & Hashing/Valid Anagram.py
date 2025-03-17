from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sC, tC = Counter(s), Counter(t)

        return sC == tC
        