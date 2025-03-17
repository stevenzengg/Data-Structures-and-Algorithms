from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i[-1].isnumeric():
                stack.append(i)
                continue
            b = int(stack.pop())
            a = int(stack.pop())
            if i == "*":
                stack.append(str(a*b))
            elif i == "/":
                stack.append(str(int(a/b)))
            elif i == "+":
                stack.append(str(a+b))
            elif i == "-":
                stack.append(str(a-b))
        
        return int(stack[-1])



if __name__ == '__main__':
    a = Solution()
    b = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(a.evalRPN(b))


