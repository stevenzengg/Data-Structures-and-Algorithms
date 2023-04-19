from typing import List
from collections import defaultdict

class Solution:
    def mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            v = intervals[i]
            last = ans[-1]
            if v[0] <= last[1]:
                ans[-1][1] = max(last[-1], v[1])
            else:
                ans.append(v)
        
        return ans
            
            




if __name__ == '__main__':
    a = Solution()
    b = [[1,3],[2,6],[8,10],[15,18]]
    print(a.mergeIntervals(b))


# Easy
# Hashmap
# Two Pointer (sort and low high)