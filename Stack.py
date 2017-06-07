class Stack:
    def __init__(self):
        self.length = 0
        self.storage = list()

    def push(self, item):
        self.storage.append(item)

    def pop(self):
        item = self.storage[-1]
        del self.storage[-1]
        self.length -= 1
        return item

    def is_empty(self):
        return len(self.storage) == 0


items = []

opening = ["{", "(", "["]
closing = ["}",")","]"]

def both_found(opening, closing):
    return opening and closing

def is_matched(string):
    left_count = {}
    right_count = {}
    left = []
    opening_found = False
    closing_found = False
    # both_found = opening_found and closing_found

    if len(string) % 2 != 0:
        return False
    for chr in string:
        try:
            if chr in opening:
                opening_found = True
                left.append(chr)
            else:
                closing_found = True
                item = left.pop()
                if opening.index(item) != closing.index(chr):
                    return False
        except:
            return False
    return both_found(opening_found, closing_found) and len(left) == 0

# print(is_matched("{{}("))


def reverse(items, temp=None):
    if temp is None:
        temp = Stack()
    if items.is_empty():
        return temp
    else:
        temp.push(items.pop())
        return reverse(items, temp)

def print_s(stack):
    for i in range(len(stack.storage)-1, -1, -1):
        print(stack.pop(), " {}".format(i))

items = Stack()
items.push(1)
items.push(2)
items.push(3)
items.push(4)
# print(items.pop())


# print(items.is_empty())
#
# newStack = reverse(items)
# print(newStack.pop())
# print(newStack.pop())
# print(newStack.pop())
# print(newStack.pop())

print_s(items)
