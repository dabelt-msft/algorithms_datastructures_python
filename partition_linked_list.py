"""Partition a linked list such that all items less than a value come before all items greater than or equal to the value. 
The value can come anywhere in the right side of the list.

Tested in linked_list_review"""

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