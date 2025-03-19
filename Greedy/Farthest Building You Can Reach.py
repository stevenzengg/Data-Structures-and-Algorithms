class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxJumps = []
        i = 1
        while i < len(heights):
            jump = heights[i] - heights[i-1]

            if jump < 0:
                i += 1
                continue
            heapq.heappush(maxJumps, -1*jump)
            if bricks >= jump:
                bricks -= jump
            elif ladders:
                ladders -= 1
                bricks -= heapq.heappop(maxJumps)
                bricks -= jump
            else:
                break
            i += 1
        return i - 1
            