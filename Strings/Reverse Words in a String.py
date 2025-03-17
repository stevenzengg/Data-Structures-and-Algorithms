class Solution:
    def reverseWords(self, s: str) -> str:
        s = " ".join(reversed([i for i in s.strip().split(" ") if i != ""]))
        return s
            
            

if __name__ == '__main__':
    a = Solution()
    b = "  hello world  "
    print(a.reverseWords(b))