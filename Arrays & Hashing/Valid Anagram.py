from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sC, tC = Counter(s), Counter(t)

        return sC == tC
        


# Time complexity: O(s + t), Space complexity: O(s + t)
# s is the length of the string s and t is the length of the string t
# The time complexity is O(s + t) because we count the characters in both strings