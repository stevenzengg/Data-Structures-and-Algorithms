class Solution(object):
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))
    


# Time complexity: O(1), Space complexity: O(1)
# The time complexity is O(1) because the board is always 9x9
# The space complexity is O(1) because the set res is always 243 elements long