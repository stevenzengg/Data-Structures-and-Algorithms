class Trie:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        node = self.head
        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.head
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        node = self.head
        print(node.children)
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
class Node:
    def __init__(self, value = "", children=None, isWord = False):
        self.value = value
        self.children = {} if children is None else children
        self.isWord = isWord

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)