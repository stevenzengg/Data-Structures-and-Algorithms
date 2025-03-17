class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hmap = set()

        for i in nums:
            if i in hmap:
                return True
            hmap.add(i)
        
        return False