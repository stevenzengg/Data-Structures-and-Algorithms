from typing import List

class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        elementIndex = {}

        left = right = ans = 0

        while right < len(s):
            if s[right] in elementIndex:
                left = elementIndex[s[right]] + 1
            
            elementIndex[s[right]] = right
            ans = max(ans, right - left + 1)
            right += 1
        
        return ans




if __name__ == '__main__':
    a = Solution()
    b = "askdjfipiasj"
    print(a.lengthOfLongestSubstring(b))


# Easy
# Hashmap
# Sliding Window