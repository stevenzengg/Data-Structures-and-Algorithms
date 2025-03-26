class StockPrice:

    def __init__(self):
        self.timestampToPrice = {}
        self.latestTime = 0
        self.maxPrices = []
        self.minPrices = []
        

    def update(self, timestamp: int, price: int) -> None:
        if timestamp > self.latestTime:
            self.latestTime = timestamp
        self.timestampToPrice[timestamp] = price
        heapq.heappush(self.minPrices, (price, timestamp))
        heapq.heappush(self.maxPrices, (-1*price, timestamp))
    def current(self) -> int:
        return self.timestampToPrice[self.latestTime]
    def maximum(self) -> int:
        price, time = heapq.heappop(self.maxPrices)
        while self.timestampToPrice[time]*-1 != price:
            price, time = heapq.heappop(self.maxPrices)
        heapq.heappush(self.maxPrices, (price, time))
        return price*-1

    def minimum(self) -> int:
        price, time = heapq.heappop(self.minPrices)
        while self.timestampToPrice[time] != price:
            price, time = heapq.heappop(self.minPrices)
        ans = price
        heapq.heappush(self.minPrices, (price, time))
        return ans


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()