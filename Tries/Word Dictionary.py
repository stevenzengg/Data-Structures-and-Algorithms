class WordDictionary:

    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:
        # start with node
        node = self.head

        # iterate through word, adding each character to the trie
        # if the character is not in the trie, add it
        # mark the last character as a word
        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char] 
        node.isWord = True

    # use a recurserive dfs to search
    def search(self, word: str) -> bool:
        node = self.head
        return self.dfs(node, 0, word)
    
    def dfs(self, node, i, word):
        # base case
        if i == len(word):
            return node.isWord
        
        if word[i] == ".":
            # return true if dfs to any child returns true
            for child in node.children.values():
                if self.dfs(child, i + 1, word):
                    return True
            return False
        
        if word[i] in node.children: 
            return self.dfs(node.children[word[i]], i + 1, word)
        
        return False

class Node:
    def __init__(self, value = "", children = None, isWord = False):
        self.value = value
        self.children = children if children else {}
        self.isWord = isWord

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)