class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Linked_List:
    def __init__(self):
        self.node = None
        self.head = self.node

    def insert_front(self, data):
        temp = Node(data)
        temp.next = self.head
        self.node = temp
        self.head = self.node

    def create_from_list(self, items):
        self.node = None
        for i in range(len(items)-1, -1, -1):
            self.node = Node(items[i], self.node)
        self.head = self.node


def check_linked_list_for_palindrome(items):
    rev = list()
    count = 0
    e = items
    m = items
    s = items
    tick = False

    while e.next is not None:
        count += 1
        e = e.next
        if tick:
            m = m.next
        tick = not tick

    if count % 2 == 0:
        if m.val != m.next.val:
            return False
        else:
            item = m.next.next
    else:
        item = m.next

    while item is not None:
        rev.append(item.val)
        item = item.next

    while rev:
        if rev.pop() != s.val:
            return False
        else:
            s = s.next
    return True


ll = Linked_List()
ll.create_from_list(["a","b","c","f","b","a"])

print(check_linked_list_for_palindrome(ll.head))

