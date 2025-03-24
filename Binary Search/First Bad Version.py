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

# Note here we return left, because we want the first bad version, and left will be the first bad version after the loop ends.        
# In binary search, the leftover left will be the bigger value,
# and the leftover right will be the smaller value if target is not found.

# Time complexity: O(log(n)), Space complexity: O(1)

if __name__ == '__main__':
    a = Solution()
    b = 5
    print(a.firstBadVersion(b))