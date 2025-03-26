#STEVEN
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        ans = []  
        i = 0
        while i < len(words):
            temp, i = self.helper(words, i, maxWidth)
            ans.append(temp)
        
        lastLine = " ".join(ans[-1].split())
        ans[-1] = lastLine + (maxWidth - len(lastLine)) * " "
        return ans
    
    def helper(self, words, i, maxWidth):
        ans = []
        length = 0
        while i < len(words):
            word = words[i]
            if length + len(word) + len(ans) > maxWidth:
                break
            ans.append(word)
            length += len(word)
            i += 1
        spaces, carry = divmod(maxWidth - length, len(ans) - 1) if len(ans) > 1 else (maxWidth - length, 0)
        for idx, word in enumerate(ans):
            if idx == len(ans) - 1 and len(ans) != 1:
                break
            space = spaces
            if carry:
                space += 1
                carry -= 1
            ans[idx] = word + " " * (space) 
        return "".join(ans), i
