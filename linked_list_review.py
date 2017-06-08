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

def del_middle_node(node):
    head = node
    f = node
    s = node
    tick = False
    while f.next:
        f = f.next
        if tick:
            b_s = s
            s = s.next
        tick = not tick
    if f == head.next:
        head = head.next
    else:
        b_s.next = b_s.next.next

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
# ll2.iterate()
# print(ll2.return_head())

ll3 = Linked_List()
largest_removed = remove_largest(ll2.head)
ll3.head = largest_removed

# ll3.iterate()

ll4 = Linked_List()


ll4.head = del_middle_node(ll2.head)
# ll4.iterate()

ll5 = Linked_List()
ll5.build_from_list([9,2,9,3,5,8,5,10,2,1])

def partition(node, val):
    b_n = node
    head = node
    right = False
    while node:
        if node.data < val:
            if node == head:
                node = node.next
            else:
                head = Node(node.data, head)
                b_n.next = node.next
        else:
            right = True
            if right:
                r_e = node
        b_n = node
        node = node.next
    r_e.next = None
    return head

# ll5.iterate()

ll6 = Linked_List()
ll6.head = partition(ll5.head, 5)
ll6.iterate()

