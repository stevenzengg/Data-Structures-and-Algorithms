class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r, m = Counter(ransomNote), Counter(magazine)

        return all([True if m[i] >= r[i] else False for i in r.keys()])