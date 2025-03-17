class Solution:
    def firstBadVersion(self, n: int) -> int:
        def isBadVersion(n):
            if n >= 4:
                return True
            return False
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            version = isBadVersion(mid)
            if version:
                right = mid - 1
            else:
                left = mid + 1
        return left

        


if __name__ == '__main__':
    a = Solution()
    b = 5
    print(a.firstBadVersion(b))