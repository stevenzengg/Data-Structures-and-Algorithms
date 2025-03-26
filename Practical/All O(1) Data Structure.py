class AllOne:

    def __init__(self):
        self.head, self.tail = Node(0), Node(float('inf'))
        self.head.right, self.tail.left = self.tail, self.head
        self.map = {} # key : node

    def inc(self, key: str) -> None:
        node = self.head
        if key in self.map:
            node = self.map[key]
            node.children.remove(key)

        if node.right.freq != node.freq + 1:
            newNode = Node(node.freq + 1, None, node, node.right)
            node.right.left = newNode
            node.right = newNode

        node.right.children.add(key)
        self.map[key] = node.right
        self.cleanUp(node)


    def dec(self, key: str) -> None:
        node = self.map[key]
        node.children.remove(key)
        if node.left.freq != node.freq - 1:
            newNode = Node(node.freq - 1, None, node.left, node)
            node.left.right = newNode
            node.left = newNode
        if node.left != self.head:
            node.left.children.add(key)
            self.map[key] = node.left
        else:
            del self.map[key]
        self.cleanUp(node)
        

    def getMaxKey(self) -> str:
        return next(iter(self.tail.left.children), "") 

    def getMinKey(self) -> str:
        return next(iter(self.head.right.children), "")
    
    def cleanUp(self, node):
        if node == self.head or node == self.tail or node.children:
            return
        node.left.right, node.right.left = node.right, node.left
    
    def debugg(self):
        print("new")
        node = self.head
        while node:
            print(node, node.freq, node.children)
            node = node.right
        print(self.map)
class Node:
    def __init__(self, frequency = 0, children = None, left = None, right = None):
        self.freq = frequency
        self.children = children if children else set()
        self.left = left
        self.right = right

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()