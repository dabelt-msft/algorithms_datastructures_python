"""Delete the middle item from a linked list.

Takes a head node and returns the head node with the middle item deleted. 
"""

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