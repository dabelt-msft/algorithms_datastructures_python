from math import inf

class Largest_in_Stack:

    def __init__(self):
        self.largest_l = []
        self.all_nums = []
        self.largest = -inf


    def push(self, num):
        self.all_nums.append(num)
        if num > self.largest:
            self.largest = num
            self.largest_l.append(num)

    def pop(self):
        item = self.all_nums.pop()
        if item == self.largest:
            self.largest_l.pop()
            self.largest = self.largest_l[-1]
        return item

    def largest_item(self):
        return self.largest


largest_items = Largest_in_Stack()

largest_items.push(1)
# print(largest_items.pop())
# largest_items.push(1)
# largest_items.push(2)
# print(largest_items.largest())
# print(largest_items.pop())
# largest_items.push(5)
# print(largest_items.largest)
# print(largest_items.pop())




