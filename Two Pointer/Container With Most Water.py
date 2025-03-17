from typing import List

class Solution:
    def maxArea(height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1

        while left < right:
            if height[left] < height[right]:
                tempAns = (right - left) * height[right]
                left += 1
            else:
                tempAns = (right - left) * height[left]
                right -= 1
                
            ans = max(tempAns, ans)
        
        return ans



if __name__ == '__main__':
    a = Solution()
    b = [1,2,3,4,5]
    print(a.maxArea(b))


# Two Pointer (sort and low high)