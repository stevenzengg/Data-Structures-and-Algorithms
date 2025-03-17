from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        next_slot = {
            "0": "1",
            "1": "2",
            "2": "3",
            "3": "4",
            "4": "5",
            "5": "6",
            "6": "7",
            "7": "8",
            "8": "9",
            "9": "0",
        }
        prev_slot = {
            "0": "9",
            "1": "0",
            "2": "1",
            "3": "2",
            "4": "3",
            "5": "4",
            "6": "5",
            "7": "6",
            "8": "7",
            "9": "8",
        }
        deadends = set(deadends)
        steps = 0
        q = deque(["0000"] if "0000" not in deadends else [])
        while q:
            length = len(q)
            for _ in range(length):
                combo = q.popleft()
                if combo == target:
                    return steps
                for nextCombo in self.nextCombos(combo, prev_slot, next_slot):
                    if nextCombo not in deadends:
                        deadends.add(nextCombo)
                        q.append(nextCombo)
            steps += 1
        return -1
    
    def nextCombos(self, combo, prev_slot, next_slot):
        ans = []
        for i, v in enumerate(combo):
            left = combo[:i] if i > 0 else ""
            prev = prev_slot[v]
            nex = next_slot[v]
            right = combo[i+1:] if i + 1 < len(combo) else ""
            ans.extend([left + prev + right, left + nex + right])
        return ans
