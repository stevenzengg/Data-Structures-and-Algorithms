class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = list(reversed([(b, a) for a, b in food]))
        self.directions = {"R": (1, 0), "L": (-1, 0), "D": (0, 1), "U": (0, -1)}
        self.snakeQ = deque([(0, 0)])
        self.snakeS = set([(0, 0)])
        self.score = 0

    def move(self, direction: str) -> int:
        x, y = self.directions[direction]
        x, y = x + self.snakeQ[-1][0], y + self.snakeQ[-1][1]
        if x < 0 or x == self.width or y < 0 or y == self.height:
            return -1
        if self.food and (x, y) == self.food[-1]:
            self.food.pop()
            self.score += 1
        else:
            tail = self.snakeQ.popleft()
            self.snakeS.remove(tail)

        if (x, y) in self.snakeS:
            return -1

        self.snakeQ.append((x, y))
        self.snakeS.add((x, y))
        
        return self.score
        
        

        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)