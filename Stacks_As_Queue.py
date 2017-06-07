class Queue:

    def __init__(self):
        self.r_order = []
        self.ordered = []

    def enqueue(self, item):
        self.r_order.append(item)

    def dequeue(self):
        if not self.ordered:
            while self.r_order:
                self.ordered.append(self.r_order.pop())
        return self.ordered.pop()


    def peek(self):
        if len(self.ordered) <= 0:
            self.arrange()
        return self.ordered[-1]

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.dequeue()
