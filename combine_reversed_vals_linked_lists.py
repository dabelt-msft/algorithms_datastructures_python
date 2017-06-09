"""Treat the values 7-1-9 in a linked list as the 917. 
 
 Add the values of two linked lists.
 
 7->1->6 + 5->9->2 is 617 + 295 = 912"""

def combine_vals(node):
    total = 0
    mult = 1
    while node:
        val = node.data
        val *= mult
        total += val
        mult *= 10
    return total

