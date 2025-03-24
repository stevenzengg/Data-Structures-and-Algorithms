class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        self.memo = {} # (tuple(nums), k) : minimized
        self.nums = nums
        return self.helper(0, k - 1, 0)

    @cache
    def helper(self, idx, k, minimized):
        if idx == len(self.nums) - 1 and k:
            return float('inf')
        if not k:
            return max(minimized, sum(self.nums[idx:]))
        summ = self.nums[idx]
        ans = float('inf')
        for i in range(idx + 1, len(self.nums)):
            ans = min(self.helper(i, k - 1, max(minimized, summ)), ans)
            summ += self.nums[i]
        return ans
    

# Time complexity is way too slow here. There are other