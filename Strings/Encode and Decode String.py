class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for word in strs:
            for letter in word:
                if letter == "/":
                    ans.append("/")
                ans.append(letter)
            ans.append("/n")
        return "".join(ans)

                
    def decode(self, s: str) -> List[str]:
        ans, placeholder = [], []
        i = 0
        while i < len(s):
            v = s[i]
            if v == "/" and i < len(s) - 1:
                if s[i + 1] == "n":
                    ans.append("".join(placeholder))
                    placeholder = []
                else:
                    placeholder.append(v)
                i += 2
                continue
            placeholder.append(v)
            i += 1
        return ans
            