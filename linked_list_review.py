class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None

    def iterate(self, node=None):
        if node == None:
            node = self.head
        while node:
            print(node.data)
            node = node.next

    def build_from_list(self, items):
        node = None
        for i in range(len(items)-1, -1, -1):
            node = Node(items[i], node)
        self.head = node

    def return_head(self):
        return self.head

def remove_largest(node):
    head = node
    largest_node = node
    before_l = node
    largest = node.data
    if node is None:
        return None
    while node.next:
        if node.next.data > largest:
            largest = node.next.data
            largest_node = node.next
            before_l = node
        node = node.next
    if largest_node == head:
        head = head.next
    else:
        before_l.next = before_l.next.next  
    return head


f = Node(1)
s = Node(2)
t = Node(3)

f.next = s
s.next = t

ll = Linked_List()
ll.head = f

# ll.iterate()

nums = [9, 7, 5]

ll2 = Linked_List()
ll2.build_from_list(nums)
#  ll2.iterate()
# print(ll2.return_head())

ll3 = Linked_List()
largest_removed = remove_largest(ll2.head)
ll3.head = largest_removed

ll3.iterate()
