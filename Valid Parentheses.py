from typing import List

class Solution:
    def validParantheses(self, s: str) -> bool:
        bracketMatches = {"[":"]", "{":"}", "(":")"}

        stack = []

        for i in s:
            if i in bracketMatches:
                stack.append(bracketMatches[i])
            else:
                if stack.pop() != i:
                    return False
        
        return True




if __name__ == '__main__':
    a = Solution()
    b = "{}{][]()()))("
    print(a.validParantheses(b))


# Hash map
# Stack