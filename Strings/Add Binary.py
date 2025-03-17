class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        i = j = carry = 0
        ans = []
        while i < len(a) or j < len(b):
            aVal = 0 if i >= len(a) else int(a[i])
            bVal = 0 if j >= len(b) else int(b[i])
            carry, add = divmod(aVal + bVal + carry, 2)
            ans.append(str(add))
            i += 1
            j += 1
        
        if carry == 1:
            ans.append("1")

        
        return "".join(reversed(ans))
            

        
                