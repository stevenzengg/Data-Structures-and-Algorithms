"""
Design a logger system that receives a stream of messages along with their timestamps. 
Each unique message should only be printed at most every 10 seconds 

(i.e. a message printed at timestamp t will prevent other identical
messages from being printed until timestamp t + 10).

All messages will come in chronological order. Several messages may arrive at the same timestamp.

Implement the Logger class:

Logger() Initializes the logger object.

bool shouldPrintMessage(int timestamp, string message) 
Returns true if the message should be printed in the given timestamp, otherwise returns false.

"""
class Logger:

    def __init__(self):
        self.seen = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.seen and timestamp < self.seen[message] + 10:
            return False
        self.seen[message] = timestamp
        return True



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)