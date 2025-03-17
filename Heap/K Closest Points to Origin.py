class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for i in points:
            x, y = i[0], i[1]
            distances.append((sqrt(x**2 + y**2), [x, y]))


        heapq.heapify(distances)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(distances)[1])

        return ans