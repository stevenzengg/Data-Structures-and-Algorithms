class Solution:
    def firstBadVersion(self, n: int) -> int:
        def isBadVersion(n):
            if n >= 4:
                return True
            return False

        left, right = 1, n
        while left <= right:
            guess = (right + left) // 2
            version = isBadVersion(guess)
            beforeVersion = isBadVersion(guess-1)
            if version == True and beforeVersion == False:
                return guess
            elif version == True:
                right = guess - 1
            else:
                left = guess + 1
        


if __name__ == '__main__':
    a = Solution()
    b = 5
    print(a.firstBadVersion(b))