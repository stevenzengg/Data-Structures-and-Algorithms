from typing import List
from collections import defaultdict

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            unico = [0] * 26
            for i in s:
                unico[ord(i) - ord('a')] += 1
            anagrams[tuple(unico)].append(s)
        
        return list(anagrams.values())


if __name__ == '__main__':
    a = Solution()
    b = ["hell", "lehj", "lehh", "hell", "lehh", "lleh"]
    print(a.groupAnagrams(b))


# Time complexity: O(n * m), Space complexity: O(n * m)
# n is the number of strings and m is the length of the longest string