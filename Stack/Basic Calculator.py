class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        sign = 1

        i = 0
        while i < len(s):
            v = s[i]
            if v.isdigit():
                operand = operand * 10 + int(v)
            elif v == '(':
                stack.append(sign)
                stack.append(v)
                sign = 1
            elif v == ' ':
                pass
            else:
                stack.append(operand * sign)
                if v == ')':
                    self.helper(stack)
                sign = -1 if v == '-' else 1
                operand = 0
            i += 1
        return sum(stack) + operand * sign
        
    def helper(self, stack):
        operand = 0
        while stack[-1] != '(':
            operand += stack.pop()
        stack.pop()
        stack.append(operand*stack.pop())

# Backtracking Solution

class Solution:
    def calculate(self, s: str) -> int:
        return self.recurse(s, 0)[0]
    
    def recurse(self, s, i):
        ans = 0
        sign = 1
        while i < len(s):
            v = s[i]
            if v == ")":
                break
            elif v == "(":
                add, i = self.recurse(s, i + 1)
                ans += sign*add
                sign = 1
            elif v.isalnum():
                i, add = self.number(s, i)
                ans += sign * int(add)
                sign = 1
            elif v == "-":
                sign = -1
            i += 1
        return (sign*ans, i)

    def number(self, s, i):
        num = []
        while i < len(s) and s[i].isalnum():
            num.append(s[i])
            i += 1
        return (i - 1, int("".join(num)))
