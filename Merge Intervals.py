from typing import List
from collections import defaultdict

class Solution:
    def mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:

        if not (all(len(i) == 2 and (all(isinstance(j, int) for j in i)) for i in intervals) or intervals):
            return intervals

        ans, curr = [], intervals[0]

        for i in range(1, len(intervals)):
            currEnd = intervals[i][1]
            currStart = intervals[i][0]
            lastEnd = intervals[i-1][1]
            if currStart < lastEnd:
                curr[1] = max(curr[1], currEnd)
            else:
                ans.append(curr)
                curr = intervals[i]
        
        ans.append(curr)

        return ans
            




if __name__ == '__main__':
    a = Solution()
    b = [[1,3],[2,6],[8,10],[15,18]]
    print(a.mergeIntervals(b))


# Easy
# Hashmap
# Two Pointer (sort and low high)