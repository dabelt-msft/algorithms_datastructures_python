class Node:

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Linked_List:

    def __init__(self):
        self.node = None
        self.head = None
        self.next = None

    def create_from_list(self, nums):
        self.nums = nums
        index = len(nums) - 1
        self.node = None
        while index >= 0:
            self.node = Node(nums[index], self.node)
            index -= 1
        self.head = self.node

    def insert(self, value):
        self.node = Node(value, self.node)
        self.head = self.node

    def iterate(self):
        while self.node:
            print(self.node.val)
            self.node = self.node.next


nums = [1,2,3]

linked_list = Linked_List()
linked_list.create_from_list([1,2,3,4,5])
# print(linked_list.iterate())


#Regular Linked List
linked = None
linked = Node(3, linked)
linked = Node(2, linked)

#linked list with loop
first = None
second = Node(5, first)
third = Node(4, second)
fourth = Node(3, third)
second.next = fourth
fifth = Node(2, fourth)

def find_repeat(head):
    node = head
    uniq = set()
    while node:
        if node not in uniq:
            uniq.add(node)
        else:
            return node
        node = node.next
    return uniq


# print(find_repeat(fifth))
# print(find_repeat(linked))


def run_all(linked):
    while linked:
        print(linked.val)
        linked = linked.next

# print(run_all(linked))

def find_middle_node(linked):
    tick = False
    half = linked
    while linked:
        linked = linked.next
        if tick:
            half = half.next
        tick = not tick
    return half.val

print(find_middle_node(linked))

