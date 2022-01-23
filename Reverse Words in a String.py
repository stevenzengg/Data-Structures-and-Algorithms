class Solution:
    def reverseWords(self, s: str) -> str:
        right = len(s) - 1
        ans = []
        stack = []
        while right >= 0:
            if s[right] == " ":
                right -= 1
                if stack:
                    ans.append("".join(reversed(stack)))
                stack.clear()
                continue
            stack.append(s[right])
            right -= 1
        
        if stack:
            ans.append("".join(reversed(stack)))
        
        return " ".join(ans)
            
            

if __name__ == '__main__':
    a = Solution()
    b = "  hello world  "
    print(a.reverseWords(b))