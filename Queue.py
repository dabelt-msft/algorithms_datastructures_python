from collections import deque
class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.appendleft(item)

    def peek(self):
        return self.items[-1]


items = Queue()
items.enqueue(1)
items.enqueue(2)

print(items.peek())