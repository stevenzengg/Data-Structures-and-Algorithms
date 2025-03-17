class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = []
        for i, v in enumerate(intervals):
            # if new interval ends before current interval starts
            if newInterval[1] < v[0]:
                return newIntervals + [newInterval] + intervals[i:]
            # if new interval starts after current interval ends
            elif newInterval[0] > v[1]:
                newIntervals.append(v)
            # some overlap
            else:
                newInterval = [min(newInterval[0], v[0]), max(newInterval[1], v[1])]
        newIntervals.append(newInterval)
        return newIntervals
                