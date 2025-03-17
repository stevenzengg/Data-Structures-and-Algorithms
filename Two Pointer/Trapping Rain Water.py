from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        
        length = len(height)
        left = length*[0]
        right = length*[0]

        max = 0

        for i, v in enumerate(height):
            if v > max:
                max = v
            else:
                left[i] = max
        max = 0

        for i, v in enumerate(reversed(height)):
            if v > max:
                max = v
            else:
                left[len(height) - 1 - i] = max
        
        ans = 0

        for a, b in zip(left, right):
            ans += min(a, b)
        
        return ans







if __name__ == '__main__':
    a = Solution()
    b = [1,2,3,4,5]
    print(a.trap(b))


# Easy
# Hashmap
# Two Pointer (sort and low high)