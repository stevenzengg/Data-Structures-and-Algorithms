class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        return self.recurse(n, seen)

    

    def recurse(self, n, seen):
        if n in seen:
            return False
        if n == 1:
            return True
        seen.add(n)
        digits = []
        while n:
            n, mod = divmod(n, 10)
            digits.append(mod)
        
        return self.recurse(sum([i*i for i in digits]), seen)
