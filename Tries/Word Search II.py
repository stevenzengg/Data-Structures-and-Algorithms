from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        head = Node()
        for word in words:
            node = head
            for char in word:
                if char not in node.children:
                    node.children[char] = Node(char)
                node = node.children[char]
            node.word = word

        self.ans = set()
        self.directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in head.children:
                    self.dfs(i, j, set([(i, j)]), board, head.children[board[i][j]], head)
        
        return list(self.ans)

    def dfs(self, i, j, visited, board, node, parent):
        if node.word:
            self.ans.add(node.word)
        
        for a, b in self.directions:
            x, y = a + i, b + j
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and (x, y) not in visited and board[x][y] in node.children:
                visited.add((x, y))
                self.dfs(x, y, visited, board, node.children[board[x][y]], node)
                visited.remove((x, y))
        if not node.children:
            del parent.children[node.char]


class Node:
    def __init__(self, char = "", children = None, word = ""):
        self.char = char
        self.children = children if children else {}
        self.word = word
        