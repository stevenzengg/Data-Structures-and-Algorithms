from typing import List

class Solution(object):
    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return matrix
        
        length = len(matrix)

        def transpose() -> None:
            for i in range(length):
                for j in range(i+1, length):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        def reverse() -> None:
            for i in range(length):
                matrix[i].reverse()
        
        transpose()
        reverse()

        print(matrix)

            


if __name__ == '__main__':
    a = Solution()
    b = [[1,2,3],[4,5,6],[7,8,9]]
    print(a.rotate(b))
