# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

# [[0,0,1], 
#  [0,0,0], 
#  [0,1,1]] -> answer is 2

# [[1,0,1], 
#  [1,1,1], 
#  [0,1,1]] -> 7

# [[0,0,0], 
#  [0,0,0], 
#  [0,0,0]] -> 0

def maxAreaOfIsland(grid) -> int:
  ans = 0
  seen = set()
  #iterate over every element double for
  for i, v1 in enumerate(grid):
    for j, v2 in enumerate(v1):
      if v2 == 0 or (i, j) in seen:
        continue
      islandSize = dfs((i, j), seen, grid)
      ans = max(ans, islandSize)
  
  return ans

def dfs(node, seen, grid) -> None:
  if validElement(node, seen, grid):
    seen.add(node)
    return 1 + dfs((node[0]+ 1, node[1]), seen, grid) + dfs((node[0], node[1] + 1), seen, grid) + dfs((node[0] - 1, node[1]), seen, grid) + dfs((node[0], node[1] - 1), seen, grid)
  return 0


def validElement(tuple1, seen, grid):
  if 0 <= tuple1[0] < len(grid) and 0 <= tuple1[1] < len(grid[0]) and tuple1 not in seen and grid[tuple1[0]][tuple1[1]] == 1:
    return True
  return False 

if __name__ == '__main__':
  print(maxAreaOfIsland([[0,0,0], [0,0,0], [0,0,0]]))
  
