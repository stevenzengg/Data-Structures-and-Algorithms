class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque([])
        seen = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i, j))
                    seen.add((i, j))
                else:
                    mat[i][j] = "#"
        
        steps = 0
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while q:
            length = len(q)
            for _ in range(length):
                i, j = q.popleft()
                mat[i][j] = steps
                for a, b in directions:
                    x, y = a + i, b + j,
                    if 0 <= x < len(mat) and 0 <= y < len(mat[0]) and mat[x][y] == "#" and (x, y) not in seen:
                        seen.add((x, y))
                        q.append((x, y))
            steps += 1
        return mat
    
    # O(mn)