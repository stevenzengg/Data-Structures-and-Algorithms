from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        queue = deque()
        seen = set(deadends)
        ans = 0
        queue.append("0000")

        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if node == target:
                    return ans
                
                for i in self.children(seen, node):
                    queue.append(i)

            ans += 1
        
        return -1
    
    def children(seen: set, node: str) -> List[str]:
        ans = []
        for i in range(4):
            INT
