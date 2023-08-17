from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i in strs:
            unicodeRep = 26* [0]
            for j in i:
                unicodeRep[ord(j) - ord('a')] += 1
            
            tupleUnicode = tuple(unicodeRep)
            anagrams[tupleUnicode].append(i)
            
        
        return list(anagrams.values())


if __name__ == '__main__':
    a = Solution()
    b = ["hell", "lehj", "lehh", "hell", "lehh", "lleh"]
    print(a.groupAnagrams(b))


# Easy
# Hashmap
# Two Pointer (sort and low high)