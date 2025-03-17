from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = (0, (0, 0))
        for i in range(len(s)):
            ans = max(ans, self.palindrome(i, i, s), self.palindrome(i, i + 1, s) if i + 1 < len(s) else ans)
        return s[ans[1][0]:ans[1][1]]

    def palindrome(self, i, j, s):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        
        return (j - i + 1, (i + 1, j))




if __name__ == '__main__':
    a = Solution()
    b = "askdjfipiasj"
    print(a.longestPalindrome(b))


# 