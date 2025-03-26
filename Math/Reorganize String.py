# Steven implementation
class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = [""] * len(s)
        counts = Counter(s)
        maxLetter = max(counts, key = counts.get)
        letters = [i for i in counts if i != maxLetter]
        letters.append(maxLetter)
        if counts[maxLetter] > math.ceil(len(s) / 2):
            return ""
        for j in [0, 1]:
            for i in range(j, len(s), 2):
                ans[i] = letters[-1]
                counts[letters[-1]] -= 1
                if not counts[letters[-1]]:
                    letters.pop()
        return "".join(ans)