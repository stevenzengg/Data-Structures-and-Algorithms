class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        operand = 0
        i = 0
        operation = '+'
        while i < len(s):
            v = s[i]
            if v.isdigit():
                operand = operand * 10 + int(v)
            elif v == ' ':
                pass
            elif operation in ['+', '-', '*', '/']:
                stack.append(self.helper(stack, operation, operand) * sign)
                sign, operand = -1 if v == '-' else 1, 0
                operation = v
            i += 1
        stack.append(self.helper(stack, operation, operand) * sign)
        return sum(stack)
    
    def helper(self, stack, operation, operand):
        if operation == '*':
            operand = stack.pop() * operand
        elif operation == '/':
            operand = int(stack.pop() / operand)
        return operand