class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if num1 == '0' or num2 == '0':
            return '0'
        
        ans = [0]*(len(num1) + len(num2))
        
        num1, num2 = num1[::-1], num2[::-1]
        
        for digit1, number1 in enumerate(num1):
            for digit2, number2 in enumerate(num2):
                numZeroes = digit1 + digit2
                carry = ans[numZeroes]
                lumpSum = carry + int(number1) * int(number2)
                
                carry, ans[numZeroes] = divmod(lumpSum, 10)
                ans[numZeroes + 1] += carry
        
        while ans[-1] == 0:
            ans.pop()
        
        return "".join([str(i) for i in reversed(ans)])

if __name__ == '__main__':
    a = Solution()
    b = "12354"
    c = "6632"
    a.multiply(b, c)