class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hmap = set()

        for i in nums:
            if i in hmap:
                return True
            hmap.add(i)
        
        return False
    
    # Time complexity: O(n), Space complexity: O(n)
    # Runs through the list once (O(n)) and stores each element in a set (O(1)).