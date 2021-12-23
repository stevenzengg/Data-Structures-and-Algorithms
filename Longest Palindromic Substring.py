from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        record = 0
        startEnd = (0, 0)

        for i in range(len(s)-1):
            ans1 = self.expandFromCenter(i, i)
            ans2 = self.expandFromCenter(i, i+1)
            record1 = ans1[1] - ans1[0]
            record2 = ans2[1] - ans2[0]
            if max(record1, record2, record) != record:
                if record1 > record2:
                    record = record1
                    startEnd = ans1
                else:
                    record = record2
                    startEnd = ans2
        
        return s[startEnd[0]:startEnd[1]]

    
    def expandFromCenter(self, s: str, index1: int, index2: int) -> tuple:
        while index1 >= 0 and index2 < len(s) and s[index1] == s[index2]:
            index1 -= 1
            index2 -= 1
        
        return (index1 + 1, index2)




if __name__ == '__main__':
    a = Solution()
    b = "askdjfipiasj"
    print(a.longestPalindrome(b))


# 