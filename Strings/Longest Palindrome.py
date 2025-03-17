class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        ans = 0
        for v in count.values():
            if not v % 2:
                ans += v
            else:
                ans += v - 1
                if not ans % 2:
                    ans += 1
        return ans