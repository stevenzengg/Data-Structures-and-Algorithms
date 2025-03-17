class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        self.memo = {} # (k, s)
        return self.dfs(s, t, k)
    
    def dfs(self, s, t, k):
        if (k, s) in self.memo:
            return self.memo[s]
        if k == 0:
            if s == t:
                return 1
            return 0
        ans = 0
        for i in range(1, len(s)):
            ans += self.dfs(s[i::] + s[0:i], t, k - 1)
        self.memo[(k, s)] = ans
        return ans


# DP DOES NOT WORK DUE TO K BEING LARGE AND EXCEEDING
# THE CALL STACK. THERE'S A FORMULA TO THIS ONE.